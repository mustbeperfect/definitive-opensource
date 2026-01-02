package cli

import (
	"bufio"
	"fmt"

	"definitive-opencore/data"
)

func selectPlatforms(scanner *bufio.Scanner) ([]string, error) {
	platforms, err := data.LoadPlatforms()
	if err != nil {
		return nil, err
	}

	selected := []string{}

	for {
		fmt.Println("Select platforms (0 to finish):")
		for i, p := range platforms {
			fmt.Printf("%d) %s\n", i+1, p.Name)
		}

		var idx int
		fmt.Scanln(&idx)
		if idx == 0 {
			break
		}
		if idx > 0 && idx <= len(platforms) {
			selected = append(selected, platforms[idx-1].ID)
		}
	}

	return selected, nil
}
