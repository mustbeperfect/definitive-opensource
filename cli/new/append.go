package data

import (
	"encoding/json"
	"os"

	"definitive-opensource/models"
)

func AppendApplication(app models.Application) error {
	file, err := os.ReadFile("applications.json")
	if err != nil {
		return err
	}

	var apps []models.Application
	if err := json.Unmarshal(file, &apps); err != nil {
		return err
	}

	apps = append(apps, app)

	out, err := json.MarshalIndent(apps, "", " ")
	if err != nil {
		return err
	}

	return os.WriteFile("applications.json", out, 0644)
}
