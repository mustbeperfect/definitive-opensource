package cli

import "fmt"

func Run() error {
	fmt.Println("Definitive Open Source CLI")
	fmt.Println("1) Add new project")

	var choice int
	fmt.Print("Select an option: ")
	fmt.Scanln(&choice)

	switch choice {
	case 1:
		return AddProject()
	default:
		fmt.Println("Invalid option")
	}

	return nil
}
