package data

import (
	"encoding/json"
	"os"

	"definitive-opensource/models"
)

func LoadSubcategories() ([]models.Subcategory, error) {
	file, err := os.ReadFile("categories.json")
	if err != nil {
		return nil, err
	}

	var wrapper struct {
		Subcategories []models.Subcategory `json:"subcategories"`
	}

	err = json.Unmarshal(file, &wrapper)
	return wrapper.Subcategories, err
}

func LoadPlatforms() ([]models.Platform, error) {
	file, err := os.ReadFile("platforms.json")
	if err != nil {
		return nil, err
	}

	var wrapper struct {
		Platforms []models.Platform `json:"platforms"`
	}

	err = json.Unmarshal(file, &wrapper)
	return wrapper.Platforms, err
}

func LoadTags() ([]models.Tag, error) {
	file, err := os.ReadFile("tags.json")
	if err != nil {
		return nil, err
	}

	var wrapper struct {
		Properties []models.Tag `json:"properties"`
	}

	err = json.Unmarshal(file, &wrapper)
	return wrapper.Properties, err
}
