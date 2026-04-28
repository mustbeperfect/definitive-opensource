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

// UTILS
// 1. Sanitize HTML to prevent XSS
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

// 2. Debounce function to limit rapid-fire function calls
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
  // Use map and join to avoid DOM thrashing (innerHTML += in a loop)
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

  // Rebuild options efficiently
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
  // Add a 300ms debounce to the search input so it doesn't fire on every single keystroke
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

  // PERFORMANCE: Pre-calculate valid subcategories OUTSIDE the loop
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

  // Use map and join instead of appending elements in a loop to improve render time
  appContainer.innerHTML = filteredApps
    .map(
      (app) => `
    <div class="app-card">
        <div class="app-title">
            <a href="${escapeHTML(app.homepage_url)}" target="_blank" rel="noopener noreferrer">${escapeHTML(app.name)}</a>
        </div>
        <div class="app-property"><strong>Description:</strong> ${escapeHTML(app.description)}</div>
        <div class="app-property"><strong>Category:</strong> ${escapeHTML(app.category)}</div>
        <div class="app-property"><strong>Repository:</strong> <a href="${escapeHTML(app.repo_url)}" target="_blank">${escapeHTML(app.repo_url)}</a></div>
        <div class="app-property"><strong>Language:</strong> ${escapeHTML(app.language)}</div>
        <div class="app-property"><strong>Stars:</strong> ${escapeHTML(app.stars)}</div>
        <div class="app-property"><strong>License:</strong> ${escapeHTML(app.license)}</div>
        <div class="app-property"><strong>Last Commit:</strong> ${escapeHTML(app.last_commit)}</div>
        <div class="app-property"><strong>Platforms:</strong> ${escapeHTML(app.platforms.join(", "))}</div>
        <div class="app-property"><strong>Tags:</strong> ${escapeHTML(app.tags.join(", "))}</div>
    </div>
  `,
    )
    .join("");
}

init();
