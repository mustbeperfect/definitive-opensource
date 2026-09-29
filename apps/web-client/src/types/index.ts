
export interface Application {
  name: string
  description: string
  repo_url: string
  tags: string[]
  platforms: string[]
  category: string
  flags: string[]
  license: string
  stars: number
  language: string
  homepage_url: string
  last_commit: string
  archived?: boolean
  github_full_name?: string
}
