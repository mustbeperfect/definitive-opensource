const endpoints = {
  applications:
    "https://raw.githubusercontent.com/mustbeperfect/definitive-opensource/main/core/data/dynamic/applications.json",
  categories:
    "https://raw.githubusercontent.com/mustbeperfect/definitive-opensource/main/core/data/static/categories.json",
  platforms:
    "https://raw.githubusercontent.com/mustbeperfect/definitive-opensource/main/core/data/static/platforms.json",
  tags: "https://raw.githubusercontent.com/mustbeperfect/definitive-opensource/main/core/data/static/tags.json",
};

let db = {
  apps: [],
  categories: [],
  subcategories: [],
  platforms: [],
  tags: [],
};

const appContainer = document.getElementById("appContainer");
const searchInput = document.getElementById("search");
const categoryFilter = document.getElementById("categoryFilter");
const subcategoryFilter = document.getElementById("subcategoryFilter");
const platformFilter = document.getElementById("platformFilter");
const tagFilter = document.getElementById("tagFilter");

const escapeHTML = (str) => {
  if (!str) return "";
  return String(str).replace(
    /[&<>'"]/g,
    (tag) =>
      ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        "'": "&#39;",
        '"': "&quot;",
      })[tag],
  );
};

const debounce = (func, delay) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
};

async function init() {
  try {
    const [appRes, catRes, platRes, tagRes] = await Promise.all([
      fetch(endpoints.applications),
      fetch(endpoints.categories),
      fetch(endpoints.platforms),
      fetch(endpoints.tags),
    ]);

    const [appData, catData, platData, tagData] = await Promise.all([
      appRes.json(),
      catRes.json(),
      platRes.json(),
      tagRes.json(),
    ]);

    db.apps = appData.applications || [];
    db.categories = catData.categories || [];
    db.subcategories = catData.subcategories || [];
    db.platforms = platData.platforms || [];
    db.tags = tagData.properties || [];

    populateFilters();
    renderApps();
    setupEventListeners();
  } catch (error) {
    appContainer.innerHTML = `<strong>Error loading data:</strong> ${escapeHTML(error.message)}`;
    console.error(error);
  }
}

function populateFilters() {
  const catHTML = db.categories
    .map(
      (cat) =>
        `<option value="${escapeHTML(cat.id)}">${escapeHTML(cat.name)}</option>`,
    )
    .join("");
  categoryFilter.insertAdjacentHTML("beforeend", catHTML);

  const platHTML = db.platforms
    .map(
      (plat) =>
        `<option value="${escapeHTML(plat.id)}">${escapeHTML(plat.name)}</option>`,
    )
    .join("");
  platformFilter.insertAdjacentHTML("beforeend", platHTML);

  const tagHTML = db.tags
    .map(
      (tag) =>
        `<option value="${escapeHTML(tag.id)}">${escapeHTML(tag.name)}</option>`,
    )
    .join("");
  tagFilter.insertAdjacentHTML("beforeend", tagHTML);

  updateSubcategoryDropdown();
}

function updateSubcategoryDropdown() {
  const selectedCategory = categoryFilter.value;

  const filteredSubcategories =
    selectedCategory === ""
      ? db.subcategories
      : db.subcategories.filter((sub) => sub.parent === selectedCategory);

  const subHTML =
    '<option value="">All Subcategories</option>' +
    filteredSubcategories
      .map(
        (sub) =>
          `<option value="${escapeHTML(sub.id)}">${escapeHTML(sub.name)}</option>`,
      )
      .join("");

  subcategoryFilter.innerHTML = subHTML;
}

function setupEventListeners() {
  searchInput.addEventListener("input", debounce(renderApps, 300));

  categoryFilter.addEventListener("change", () => {
    updateSubcategoryDropdown();
    renderApps();
  });

  subcategoryFilter.addEventListener("change", renderApps);
  platformFilter.addEventListener("change", renderApps);
  tagFilter.addEventListener("change", renderApps);
}

function renderApps() {
  const searchTerm = searchInput.value.toLowerCase();
  const selectedCategory = categoryFilter.value;
  const selectedSubcategory = subcategoryFilter.value;
  const selectedPlatform = platformFilter.value;
  const selectedTag = tagFilter.value;

  let validSubcategoryIds = null;
  if (selectedCategory !== "") {
    validSubcategoryIds = db.subcategories
      .filter((sub) => sub.parent === selectedCategory)
      .map((sub) => sub.id);
  }

  const filteredApps = db.apps.filter((app) => {
    const matchesSearch =
      app.name.toLowerCase().includes(searchTerm) ||
      app.description.toLowerCase().includes(searchTerm);

    let matchesCategory = true;
    if (validSubcategoryIds) {
      matchesCategory = validSubcategoryIds.includes(app.category);
    }

    const matchesSubcategory =
      selectedSubcategory === "" || app.category === selectedSubcategory;
    const matchesPlatform =
      selectedPlatform === "" || app.platforms.includes(selectedPlatform);
    const matchesTag = selectedTag === "" || app.tags.includes(selectedTag);

    return (
      matchesSearch &&
      matchesCategory &&
      matchesSubcategory &&
      matchesPlatform &&
      matchesTag
    );
  });

  if (filteredApps.length === 0) {
    appContainer.innerHTML =
      "<div>No applications match your current filters.</div>";
    return;
  }

  appContainer.innerHTML = filteredApps
    .map(
      (app) => `
    <div class="app-card">
        <div class="app-header">
            <div class="app-title" target="_blank" rel="noopener noreferrer">${escapeHTML(app.name)}</div>
            <div class="item-group">
              <div class="app-tag">${escapeHTML(app.tags.join(", "))}</div>
              <a href="${escapeHTML(app.homepage_url)}">
                <img src="../../assets/icon/box-arrow-up-right.svg" alt="Description of my SVG" width="15" height="15">
              </a>
              <a href="${escapeHTML(app.repo_url)}">
                <img src="../../assets/icon/github.svg" alt="Description of my SVG" width="15" height="15">
              </a>
            </div>
        </div>
        <div class="app-description">${escapeHTML(app.description)}</div>

        <div class="app-header">
          <div class=""><strong>Category:</strong> ${escapeHTML(app.category)}</div>
          <div class="">${escapeHTML(app.platforms.join(", "))}</div>
        </div>

        <div class="line-x"></div>

        <div class="app-bottom">
          <div class="app-property">${escapeHTML(app.language)}</div>
          <div style="text-align: center" class="app-property">${escapeHTML(app.stars)}</div>
          <div style="text-align: right" class="app-property">${escapeHTML(app.license)}</div>
        </div>

    </div>
  `,
    )
    .join("");
}

init();
