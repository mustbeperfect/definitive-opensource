package models

type Subcategory struct {
	Name string `json:"name"`
	ID   string `json:"id"`
}

type Platform struct {
	Name string `json:"name"`
	ID   string `json:"id"`
}

type Tag struct {
	Name string `json:"name"`
	ID   string `json:"id"`
}

type Application struct {
	Name      string   `json:"name"`
	RepoURL   string   `json:"repo_url"`
	Tags      []string `json:"tags,omitempty"`
	Platforms []string `json:"platforms,omitempty"`
	Category  string   `json:"category"`
}
