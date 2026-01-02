package main

import (
	"fmt"
	"os"

	"github.com/definitive-opensource/cli"
)

func main() {
	if err := cli.Run(); err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}
}
