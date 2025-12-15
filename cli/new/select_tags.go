package cli

import (
	"bufio"
	"fmt"

	"definitive-opensource/data"
)

func selectTags(scanner *bufio.Scanner) ([]string, error) {
	tags, err := data.LoadTags()
	if err != nil {
		return nil, err
	}

	selected := []string{}

	for {
		fmt.Println("Select tags (0 to finish):")
		for i, t := range tags {
			fmt.Printf("%d) %s\n", i+1, t.Name)
		}

		var idx int
		fmt.Scanln(&idx)
		if idx == 0 {
			break
		}
		if idx > 0 && idx <= len(tags) {
			selected = append(selected, tags[idx-1].ID)
		}
	}

	return selected, nil
}
