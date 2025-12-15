package cli

import (
	"bufio"
	"fmt"
	"strings"

	"definitive-opensource/data"
)

func selectCategory(scanner *bufio.Scanner) (string, error) {
	subs, err := data.LoadSubcategories()
	if err != nil {
		return "", err
	}

	for {
		fmt.Print("Search category: ")
		scanner.Scan()
		query := strings.ToLower(scanner.Text())

		filtered := []string{}
		for _, s := range subs {
			if strings.Contains(strings.ToLower(s.Name), query) {
				filtered = append(filtered, fmt.Sprintf("%s (%s)", s.Name, s.ID))
			}
		}

		for i, f := range filtered {
			fmt.Printf("%d) %s\n", i+1, f)
		}

		fmt.Print("Select category number: ")
		var idx int
		fmt.Scanln(&idx)
		if idx > 0 && idx <= len(filtered) {
			return subs[idx-1].ID, nil
		}

		fmt.Println("Invalid selection, try again")
	}
}
