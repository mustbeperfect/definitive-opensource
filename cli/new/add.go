package cli

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"definitive-opensource/data"
	"definitive-opensource/models"
)

func AddProject() error {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("GitHub repo URL: ")
	scanner.Scan()
	repo := strings.TrimSpace(scanner.Text())

	fmt.Print("Project name: ")
	scanner.Scan()
	name := strings.TrimSpace(scanner.Text())

	category, err := selectCategory(scanner)
	if err != nil {
		return err
	}

	platforms, err := selectPlatforms(scanner)
	if err != nil {
		return err
	}

	tags, err := selectTags(scanner)
	if err != nil {
		return err
	}

	entry := models.Application{
		Name:      name,
		RepoURL:   repo,
		Category:  category,
		Platforms: platforms,
		Tags:      tags,
	}

	return data.AppendApplication(entry)
}
