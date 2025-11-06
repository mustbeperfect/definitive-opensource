
<table align="center">
    <tr>
    <td>🌍 v0.6.3-beta</td>
    </tr>
</table>

<h1 align="center">[ definitive-opensource ] </h1>
<p align="center">The definitive list of the best of everything open source</p>

<p align="center"><code>Status: Active</code> - <code>Projects: 697</code></p>

> [!TIP]
> This list is EXCLUSIVELY for apps that you use directly such as desktop apps, selfhosted apps, and command line utilities. Developer facing tools like languages, frameworks, and libraries are excluded. 

> [!NOTE]
> Please visit the [portal](resources/PORTAL.md) for quick access to the foundations of this project. Please read contributing documents before submitting a PR as this list is edited from a JSON file, not the README!

##

<h4 align="center">
  <a href="https://github.com/mustbeperfect/definitive-opensource/blob/main/readmes/windows.md">Windows</a>
  <span> · </span>
  <a href="https://github.com/mustbeperfect/definitive-opensource/blob/main/readmes/macos.md">MacOS</a>
  <span> · </span>
  <a href="https://github.com/mustbeperfect/definitive-opensource/blob/main/readmes/linux.md">Linux</a>
  <span> · </span>
  <a href="https://github.com/mustbeperfect/definitive-opensource/blob/main/readmes/selfhost.md">SelfHosted</a>
</h4>

##

**Our Goal -** There's plenty of awesome lists on GitHub, many focusing on open source specifically. However I've found them including many long-deprecated apps, cluttered with smaller projects on the verge of extinction, or missing a lot of modern open source projects. 

This list aims to serve as a single centralized location for the best of open source, characterized by a solid user base, solid set of contributors, visible long term growth, and overall product quality. 

<details>
  <summary><b>More Information</b></summary><br />
  Definitive-opensource aims to consolidate only the best open source projects. Our guidelines include strict minimum requirements and additional research for vetting. For a project to pass it's likely popular enough to survive far into the future, however we continously monitor projects on the list and remove anything that no longer fits the criteria. 
  <p>&nbsp;</p>
  It is a fundamental goal for this list to be as neutral as possible and simply present options, not persuade or redact, regardless of the maintainer's opinion. Projects that fit the criteria, which by passing will inherently be used by thousands to millions, are put on the list. This list is "curated" - not relative to opinion but statistics and facts.
  <p>&nbsp;</p>
  Although the list is called definitive, in this context it doesn't quite mean the implied dictionary definition of finality. This project can only survive and thrive through continuous contributions by the community, as this list is, in itself, open source. 
</details>

<details>
  <summary><b>How The List Works</b></summary><br />

  Definitive-opensource was initially a single markdown file that was edited directly. However, as the list scaled, this manual approach proved cumbersome and limited. Additionally, as popularity increased, we recieved many requests for README's of individual platforms - something that would be not be realistic to do manually.
  <p>&nbsp;</p>
  As of v0.6.2-beta, the project was fundamentally re-made. Categories and applications were put in categories.json and applications.json, respectively. Python scripts were made to generate one main list and more platform-specific lists. This was paired with GitHub actions to run the scripts when any changes were made. This opened up a world of possibilies, making refactoring the list format far easier whilst eliminating typos. 
  <p>&nbsp;</p>
  This list aims to stand in the middle ground between human input and automation. Mostly automated websites exist for finding open source projects, but statistics alone fails to encompass the complete picture. This list has scripts to automate markdown formatting, updating stats, and finding potentially abandoned projects. However, the actual processes of choosing which projects make it onto the list, which ones should be removed, and what tags to assign are controlled entirely by humans. 
</details>

## Project Status
```css
Active - Active Development
```
```
Incremental - Minor Updates
```
```
Maintenence - Critical Fixes
```
```
Idle - Temporarily Paused
```
```
Abandoned - Development Halted
```

## Tags

### Alerts
`🟡` `🟠` `🔴` `⭕` - Security incident **(Minor, Moderate, Major, Critical)**

`🚫` - Potentially abandoned

`🔒` - Potentially closed source

`🛑` - Development paused

`⏳` - Development slowed

`⚠️` - Restrictive license

`🏦` - Corporate influence

`💰` - Commercial

`🧪` - Experimental (Pre-Alpha)

`🚧` - Critically unstable/buggy

`❌` - On watch for removal

### Highlights
`💥` - Disruptive

`🌍` - Influential

`🌟` - Pioneering

`💡` - Innovative

### Awards (At 10k Stars)
`🏆` - Crown of open source

`🥈` - Second

`🥉` - Third

### Platforms
`Cross` - Cross-platform (MacOS, Windows, Linux)

`Mobile` - Android and IOS

`Windows`, `MacOS`, `Linux`, `Android`, `IOS`, `SelfHost`, `Web (Cloud)`, `VSCode`, `JetBrains`, `Chromium`, `Firefox`,  `N/A`

### Properties
`CLI+` - CLI in addition to GUI

`TUI` - Terminal user interface

`Manual` - Installation with pip, npm, cargo, building from source

`CLI`, `Plugin`, `Extension`, `Web UI`

> [!NOTE]
> Cross, MacOS, Linux, and Windows tags, by default, imply that the app ships as a binary (EX: exe, dmg) unless they are accompanied by the `manual` tag that indicates another runtime or installation method. The same goes for `SelfHost`, which by default, implies the app can be installed via Docker.
## Table of Contents

<details>
  <summary><b>Alphabetical</b></summary> <br />

- [AD Blocker](#ad-blocker)
- [Agent](#agent)
- [AI Image GUI](#ai-image-gui)
- [AI Utilities](#ai-utilities)
- [All In One](#all-in-one)
- [Antivirus](#antivirus)
- [API Client](#api-client)
- [Arr](#arr)
- [Assistant](#assistant)
- [Audio Editor](#audio-editor)
- [Audio Player](#audio-player)
- [Authentication](#authentication)
- [Automation](#automation)
- [Autonomy](#autonomy)
- [Backup](#backup)
- [Bookmark Manager](#bookmark-manager)
- [Browser](#browser)
- [Browser Extensions](#browser-extensions)
- [Calendar](#calendar)
- [Canvas](#canvas)
- [Chat](#chat)
- [Cleaner](#cleaner)
- [Clipboard Manager](#clipboard-manager)
- [Code Assistant](#code-assistant)
- [Code Editor](#code-editor)
- [Collaboration](#collaboration)
- [Container Management](#container-management)
- [Containers](#containers)
- [Context](#context)
- [Control](#control)
- [Dashboard](#dashboard)
- [Dev Tools](#dev-tools)
- [Diagrams](#diagrams)
- [Document Editor](#document-editor)
- [Document Management](#document-management)
- [Document Modifier](#document-modifier)
- [Dotfiles Manager](#dotfiles-manager)
- [Download Manager](#download-manager)
- [EMACS Packages](#emacs-packages)
- [Engineering](#engineering)
- [File Manager](#file-manager)
- [File Sharing](#file-sharing)
- [Finance](#finance)
- [Firewall](#firewall)
- [Firmware](#firmware)
- [Game Engine](#game-engine)
- [Game Launcher](#game-launcher)
- [Games](#games)
- [Git Client](#git-client)
- [Git Hosting](#git-hosting)
- [Graphics](#graphics)
- [Home Automation](#home-automation)
- [Home Server](#home-server)
- [IDE](#ide)
- [Image Editing](#image-editing)
- [Image Processing](#image-processing)
- [Information Processing](#information-processing)
- [Keyboard Manager](#keyboard-manager)
- [Knowledge Base](#knowledge-base)
- [Language Package Manager](#language-package-manager)
- [Launcher](#launcher)
- [Linux](#linux)
- [LLM GUI](#llm-gui)
- [MacOS](#macos)
- [Mail](#mail)
- [Manager](#manager)
- [Markdown Editor](#markdown-editor)
- [Media Downloader](#media-downloader)
- [Media Management](#media-management)
- [Model Tools](#model-tools)
- [Neovim Extensions](#neovim-extensions)
- [Network](#network)
- [Note Taking](#note-taking)
- [Office Suite](#office-suite)
- [Operating System](#operating-system)
- [Other](#other)
- [Package Manager](#package-manager)
- [Password Manager](#password-manager)
- [Project Management](#project-management)
- [Prompt](#prompt)
- [Proofreading](#proofreading)
- [RAG](#rag)
- [Remote Desktop](#remote-desktop)
- [Research](#research)
- [Robotics](#robotics)
- [Rocketry](#rocketry)
- [Screen Recording](#screen-recording)
- [Search Engine](#search-engine)
- [Server Management](#server-management)
- [Shell](#shell)
- [Simulation](#simulation)
- [Social Network](#social-network)
- [Spreadsheet](#spreadsheet)
- [Storage](#storage)
- [Surveillance](#surveillance)
- [Sync](#sync)
- [System](#system)
- [System Monitoring](#system-monitoring)
- [Task Management](#task-management)
- [Terminal Emulator](#terminal-emulator)
- [Terminal Multiplexer](#terminal-multiplexer)
- [Terminal Utilities](#terminal-utilities)
- [Text Editor](#text-editor)
- [Time Management](#time-management)
- [Tools](#tools)
- [Transcription](#transcription)
- [Uncategorized](#uncategorized)
- [Version Manager](#version-manager)
- [Video Conference](#video-conference)
- [Video Editing](#video-editing)
- [Video Player](#video-player)
- [Video Transcoder](#video-transcoder)
- [Virtual Machine](#virtual-machine)
- [VPN](#vpn)
- [Wiki](#wiki)
- [Window Management](#window-management)
- [Windows](#windows)

</details>

<details open>
  <summary><b>Categorized</b></summary> <br />
  
- Artificial Intelligence (AI)
    - [Agent](#agent)
    - [AI Image GUI](#ai-image-gui)
    - [AI Utilities](#ai-utilities)
    - [All In One](#all-in-one)
    - [Assistant](#assistant)
    - [Context](#context)
    - [Information Processing](#information-processing)
    - [LLM GUI](#llm-gui)
    - [Manager](#manager)
    - [Model Tools](#model-tools)
    - [RAG](#rag)
    - [Research](#research)
- Communication
    - [Chat](#chat)
    - [Collaboration](#collaboration)
    - [Mail](#mail)
    - [Video Conference](#video-conference)
- Data
    - [Backup](#backup)
    - [Storage](#storage)
    - [Sync](#sync)
- Development
    - [API Client](#api-client)
    - [Code Assistant](#code-assistant)
    - [Code Editor](#code-editor)
    - [Dev Tools](#dev-tools)
    - [Game Engine](#game-engine)
    - [Git Client](#git-client)
    - [Git Hosting](#git-hosting)
    - [IDE](#ide)
    - [Language Package Manager](#language-package-manager)
- Entertainment
    - [Game Launcher](#game-launcher)
    - [Games](#games)
- Extensions
    - [Browser Extensions](#browser-extensions)
    - [EMACS Packages](#emacs-packages)
    - [Neovim Extensions](#neovim-extensions)
- Internet
    - [Browser](#browser)
    - [Download Manager](#download-manager)
    - [Network](#network)
    - [Search Engine](#search-engine)
    - [Social Network](#social-network)
- Media
    - [Audio Editor](#audio-editor)
    - [Audio Player](#audio-player)
    - [Canvas](#canvas)
    - [Diagrams](#diagrams)
    - [Graphics](#graphics)
    - [Image Editing](#image-editing)
    - [Image Processing](#image-processing)
    - [Media Downloader](#media-downloader)
    - [Screen Recording](#screen-recording)
    - [Video Editing](#video-editing)
    - [Video Player](#video-player)
    - [Video Transcoder](#video-transcoder)
- Operating System
    - [Linux](#linux)
    - [MacOS](#macos)
    - [Operating System](#operating-system)
    - [Windows](#windows)
- Organization
    - [Bookmark Manager](#bookmark-manager)
    - [Document Management](#document-management)
- Productivity
    - [Calendar](#calendar)
    - [Document Modifier](#document-modifier)
    - [Finance](#finance)
    - [Knowledge Base](#knowledge-base)
    - [Project Management](#project-management)
    - [Task Management](#task-management)
    - [Time Management](#time-management)
- Security/Privacy
    - [AD Blocker](#ad-blocker)
    - [Antivirus](#antivirus)
    - [Authentication](#authentication)
    - [Firewall](#firewall)
    - [Password Manager](#password-manager)
    - [VPN](#vpn)
- Server
    - [Arr](#arr)
    - [Dashboard](#dashboard)
    - [Home Automation](#home-automation)
    - [Home Server](#home-server)
    - [Media Management](#media-management)
    - [Server Management](#server-management)
    - [Surveillance](#surveillance)
- STEM
    - [Autonomy](#autonomy)
    - [Control](#control)
    - [Engineering](#engineering)
    - [Firmware](#firmware)
    - [Robotics](#robotics)
    - [Rocketry](#rocketry)
    - [Simulation](#simulation)
- Terminal
    - [Prompt](#prompt)
    - [Shell](#shell)
    - [Terminal Emulator](#terminal-emulator)
    - [Terminal Multiplexer](#terminal-multiplexer)
    - [Terminal Utilities](#terminal-utilities)
- Text
    - [Document Editor](#document-editor)
    - [Markdown Editor](#markdown-editor)
    - [Note Taking](#note-taking)
    - [Office Suite](#office-suite)
    - [Proofreading](#proofreading)
    - [Spreadsheet](#spreadsheet)
    - [Text Editor](#text-editor)
    - [Wiki](#wiki)
- Utilities
    - [Automation](#automation)
    - [Cleaner](#cleaner)
    - [Clipboard Manager](#clipboard-manager)
    - [Container Management](#container-management)
    - [Containers](#containers)
    - [Dotfiles Manager](#dotfiles-manager)
    - [File Manager](#file-manager)
    - [File Sharing](#file-sharing)
    - [Keyboard Manager](#keyboard-manager)
    - [Launcher](#launcher)
    - [Package Manager](#package-manager)
    - [Remote Desktop](#remote-desktop)
    - [System](#system)
    - [System Monitoring](#system-monitoring)
    - [Tools](#tools)
    - [Transcription](#transcription)
    - [Version Manager](#version-manager)
    - [Virtual Machine](#virtual-machine)
    - [Window Management](#window-management)
- Other
    - [Other](#other)
    - [Uncategorized](#uncategorized)
- [Removed Projects](#removed-projects)
- [FAQ](#faq)
- [Honorable Mentions of Closed-Source Software](#honorable-mentions-of-closed-source-software)
</details>

# Artificial Intelligence (AI) - [Go to top](#table-of-contents)

### Agent

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [AgentGPT](https://github.com/reworkd/AgentGPT) | 🤖 Assemble, configure, and deploy autonomous AI Agents in your browser. | `SelfHost` | **35.2k** |
| [AgenticSeek](https://github.com/Fosowl/agenticSeek) `Manual` | Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. 🔔 Official updates only via twitter @Martin993886460 (Beware of fake account) | `Cross` | **23.4k** |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters. | `SelfHost` | **179.5k** |
| [Browser Use](https://github.com/browser-use/browser-use) `Manual` | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. | `Cross` | **72.2k** |
| [c/ua](https://github.com/trycua/cua) `Manual` | Open-source infrastructure for Computer-Use Agents. Sandboxes, SDKs, and benchmarks to train and evaluate AI agents that can control full desktops (macOS, Linux, Windows). | `Cross` | **11.2k** |
| [Claudia](https://github.com/getAsterisk/claudia) | A powerful GUI app and Toolkit for Claude Code - Create custom agents, manage interactive Claude Code sessions, run secure background agents, and more. | `Cross` | **18.6k** |
| [Crush](https://github.com/charmbracelet/crush) `TUI` | The glamourous AI coding agent for your favourite terminal 💘 | `Cross` | **14.6k** |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) `TUI` `Manual` | An open-source AI agent that brings the power of Gemini directly into your terminal. | `Cross` | **81.6k** |
| [gptme](https://github.com/gptme/gptme) `CLI` `Manual` | Your agent in your terminal, equipped with local tools: writes code, uses the terminal, browses the web, vision. | `Cross` | **4.1k** |
| [Huginn](https://github.com/huginn/huginn) | Create agents that monitor and act on your behalf.  Your agents are standing by! | `SelfHost` | **47.9k** |
| [Nanobrowser](https://github.com/nanobrowser/nanobrowser) | Open-Source Chrome extension for AI-powered web automation. Run multi-agent workflows using your own LLM API key. Alternative to OpenAI Operator. | `Chromium` | **11.2k** |
| [Open Intepreter](https://github.com/OpenInterpreter/open-interpreter) `Manual` | A natural language interface for computers | `Cross` | **60.8k** |
| [opencode](https://github.com/sst/opencode) `TUI` | The AI coding agent built for the terminal. | `Cross` | **31.7k** |
| [Refact](https://github.com/smallcloudai/refact) | AI Agent that handles engineering tasks end-to-end: integrates with developers’ tools, plans, executes, and iterates until it achieves a successful result. | `VSCode` | **3.4k** |
| [Telegraf](https://github.com/influxdata/telegraf) `CLI+` | Agent for collecting, processing, aggregating, and writing metrics, logs, and other arbitrary data. | `Cross` `SelfHost` | **16.4k** |
| [TEN Agent](https://github.com/TEN-framework/TEN-Agent) |  Open-source framework for conversational voice AI agents | `SelfHost` | **8.5k** |
| [UI-TARS](https://github.com/bytedance/UI-TARS-desktop) | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra | `Cross` | **19.4k** |
| [WrenAI](https://github.com/Canner/WrenAI) | ⚡️ GenBI (Generative BI) queries any database in natural language, generates accurate SQL (Text-to-SQL), charts (Text-to-Chart), and AI-powered business intelligence in seconds. | `Web (Cloud)` `SelfHost` | **12.9k** |

### AI Image GUI

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Auto1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | Stable Diffusion web UI | `SelfHost` | **157.9k** |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. | `SelfHost` | **92.8k** |
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Focus on prompting and generating | `SelfHost` | **47k** |
| [InvokeAI](https://github.com/invoke-ai/InvokeAI) | Invoke is a leading creative engine for Stable Diffusion models, empowering professionals, artists, and enthusiasts to generate and create visual media using the latest AI-driven technologies. The solution offers an industry leading WebUI, and serves as the foundation for multiple commercial products. | `Cross` `SelfHost` | **26.2k** |
| [SD.Next](https://github.com/vladmandic/sdnext) | SD.Next: All-in-one WebUI for AI generative image and video creation | `SelfHost` | **6.7k** |
| [SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI) `Manual` | SwarmUI (formerly StableSwarmUI), A Modular Stable Diffusion Web-User-Interface, with an emphasis on making powertools easily accessible, high performance, and extensibility. | `Cross` | **3.3k** |
| [WebUI Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) | Stable Diffusion WebUI Forge is a platform on top of Stable Diffusion WebUI (based on Gradio ) to make development easier, optimize resource management, speed up inference, and study experimental features. | `SelfHost` | **11.8k** |

### AI Utilities

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Airweave](https://github.com/airweave-ai/airweave) `Manual` `Web UI` | Context retrieval for AI agents across apps and databases | `Cross` | **4.4k** |
| [mem0](https://github.com/mem0ai/mem0) `Manual` | Universal memory layer for AI Agents; Announcing OpenMemory MCP - local and secure memory management. | `SelfHost` | **42.7k** |
| [Netron](https://github.com/lutzroeder/netron) | Visualizer for neural network, deep learning and machine learning models | `Cross` | **31.7k** |

### All In One

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [AIChat](https://github.com/sigoden/aichat) `CLI` | All-in-one LLM CLI tool featuring Shell Assistant, Chat-REPL, RAG, AI Tools & Agents, with access to OpenAI, Claude, Gemini, Ollama, Groq, and more. | `Cross` | **8.5k** |
| [ClaraVerse](https://github.com/badboysm890/ClaraVerse) | ClaraVerse is a privacy-first, fully local AI workspace featuring a Local LLM chat powered by LLama.cpp, along with support for any provider, tool calling, agent building, Stable Diffusion, and n8n-style automation. It requires no backend or API keys—just your stack and machine. | `Cross` `SelfHost` | **3.5k** |
| [Khoj AI](https://github.com/khoj-ai/khoj) | Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free. | `Web (Cloud)` `SelfHost` | **31.5k** |
| [Lobe Chat](https://github.com/lobehub/lobe-chat) | 🤯 LobeHub - an open-source, modern design AI Agent Workspace. Supports multiple AI providers (OpenAI / Claude 4 / Gemini / DeepSeek / Ollama / Qwen), Knowledge Base (file upload / RAG ), one click install MCP Marketplace and Artifacts / Thinking. One-click FREE deployment of your private AI Agent application. | `Web (Cloud)` `SelfHost` | **67.5k** |

### Assistant

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Glass](https://github.com/pickle-com/glass) | Digital Mind Extension | `MacOS` `Windows` | **6.9k** |
| [Leon](https://github.com/leon-ai/leon) | 🧠 Leon is your open-source personal assistant. | `SelfHost` | **16.8k** |
| [Meetily](https://github.com/Zackriya-Solutions/meeting-minutes) | A free and open source, self hosted Ai based live meeting note taker and minutes summary generator that can completely run in your Local device (Mac OS and windows OS Support added. Working on adding linux support soon) https://meetily.ai/ is meetly ai | `Windows` `MacOS` | **8.1k** |

### Context

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [omi](https://github.com/BasedHardware/omi) | AI wearables. Put it on, speak, transcribe, automatically | `Mobile` | **7.2k** |
| [screenpipe](https://github.com/mediar-ai/screenpipe) 💰 💥 | AI app store powered by 24/7 desktop history.  open source - 100% local - dev friendly - 24/7 screen, mic recording | `MacOS` `Windows` | **15.9k** |

### Information Processing

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Code2prompt](https://github.com/mufeedvh/code2prompt) `CLI` | A CLI tool to convert your codebase into a single LLM prompt with source tree, prompt templating, and token counting. | `Cross` | **6.7k** |
| [Docling](https://github.com/DS4SD/docling) `CLI` `Manual` | Get your documents ready for gen AI | `Cross` | **43.1k** |
| [Firecrawl](https://github.com/mendableai/firecrawl) | 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data | `Web (Cloud)` `SelfHost` | **66.5k** |
| [Gitingest](https://github.com/cyclotruc/gitingest) `Manual` | Replace 'hub' with 'ingest' in any GitHub URL to get a prompt-friendly extract of a codebase  | `Web (Cloud)` `Chromium` `Firefox` | **13k** |
| [GPT crawler](https://github.com/BuilderIO/gpt-crawler) | Crawl a site to generate knowledge files to create your own custom GPT from a URL | `SelfHost` | **22k** |
| [olmOCR](https://github.com/allenai/olmocr) `Manual` | Toolkit for linearizing PDFs for LLM datasets/training | `Cross` | **15.8k** |
| [Repomix](https://github.com/yamadashy/repomix) `CLI` `Manual` | 📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more. | `Web (Cloud)` | **20.1k** |
| [Unstract](https://github.com/Zipstack/unstract) | No-code LLM Platform to launch APIs and ETL Pipelines to structure unstructured documents | `MacOS` `Linux` `SelfHost` | **5.9k** |

### LLM GUI

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [5ire](https://github.com/nanbingxyz/5ire) | 5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers . | `Cross` | **4.7k** |
| [Chatbox](https://github.com/Bin-Huang/chatbox) | User-friendly Desktop Client App for AI Models/LLMs (GPT, Claude, Gemini, Ollama...) | `Cross` | **37.3k** |
| [Cherry Studio](https://github.com/CherryHQ/cherry-studio) | 🍒 Cherry Studio is a desktop client that supports for multiple LLM providers. | `Cross` | **35.1k** |
| [DeepChat](https://github.com/ThinkInAIXYZ/deepchat) | 🐬DeepChat - A smart assistant that connects powerful AI to your personal world | `Cross` | **4.9k** |
| [fullmoon](https://github.com/mainframecomputer/fullmoon-ios) | chat with private and local large language models | `IOS` | **2.1k** |
| [GPT4ALL](https://github.com/nomic-ai/gpt4all) | GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use. | `Cross` | **76.9k** |
| [h2oGPT](https://github.com/h2oai/h2ogpt) | Private chat with local GPT with document, images, video, etc. 100% private, Apache 2.0. Supports oLLaMa, Mixtral, llama.cpp, and more. Demo: https://gpt.h2o.ai/ https://gpt-docs.h2o.ai/ | `SelfHost` | **11.9k** |
| [Jan](https://github.com/janhq/jan) | Jan is an open source alternative to ChatGPT that runs 100% offline on your computer. | `Cross` | **39.1k** |
| [LibreChat](https://github.com/danny-avila/LibreChat) | Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active. | `SelfHost` | **31.4k** |
| [NextChat](https://github.com/ChatGPTNextWeb/NextChat) `CLI+` | ✨ Light and Fast AI Assistant. Support: Web - iOS - MacOS - Android -  Linux - Windows | `Cross` `Web (Cloud)` | **86.3k** |
| [Onyx](https://github.com/onyx-dot-app/onyx) | Open Source AI Platform - AI Chat with advanced features that works with every LLM | `SelfHost` | **15.7k** |
| [Open WebUI](https://github.com/open-webui/open-webui) | User-friendly AI Interface (Supports Ollama, OpenAI API, ...) | `SelfHost` | **114.3k** |
| [SillyTavern](https://github.com/SillyTavern/SillyTavern) | LLM Frontend for Power Users. | `SelfHost` | **19.7k** |
| [SurfSense](https://github.com/MODSetter/SurfSense) | Open Source Alternative to NotebookLM / Perplexity, connected to external sources such as Search Engines, Slack, Linear, Jira, ClickUp, Confluence, Notion, YouTube, GitHub, Discord and more. Join our discord: https://discord.gg/ejRNvftDp9 | `SelfHost` | **10.4k** |
| [Text generation webUI](https://github.com/oobabooga/text-generation-webui) | The definitive Web UI for local AI, with powerful features and easy setup. | `SelfHost` | **45.3k** |

### Manager

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [KoboldCpp](https://github.com/LostRuins/koboldcpp) | Run GGUF models easily with a KoboldAI UI. One File. Zero Install. | `Cross` `SelfHost` | **8.8k** |
| [Ollama](https://github.com/ollama/ollama) 🌍`CLI` | Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemma 3 and other models. | `Cross` `SelfHost` | **155.4k** |
| [StabilityMatrix](https://github.com/LykosAI/StabilityMatrix) | Multi-Platform Package Manager for Stable Diffusion | `Cross` | **6.8k** |

### Model Tools

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Agno](https://github.com/agno-agi/agno) `CLI` `Manual` | Multi-agent framework, runtime and control plane. Built for speed, privacy, and scale. | `Cross` | **34.9k** |
| [GPT-SoVITS-WebUI](https://github.com/RVC-Boss/GPT-SoVITS) `Manual` | 1 min voice data can also be used to train a good TTS model! (few shot voice cloning) | `Cross` `SelfHost` | **52.1k** |
| [Kiln](https://github.com/Kiln-AI/Kiln) | The easiest tool for fine-tuning LLM models, synthetic data generation, and collaborating on datasets. | `Cross` | **4.4k** |
| [LLaMa-Factory](https://github.com/hiyouga/LLaMA-Factory) `CLI+` `Manual` | Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024) | `SelfHost` | **61.9k** |
| [Ludwig](https://github.com/ludwig-ai/ludwig) `Manual` | Low-code framework for building custom LLMs, neural networks, and other AI models | `Cross` | **11.6k** |
| [Opik](https://github.com/comet-ml/opik) | Debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tracing, automated evaluations, and production-ready dashboards. | `SelfHost` `Web (Cloud)` | **15.5k** |
| [PyTorch Lightning](https://github.com/Lightning-AI/pytorch-lightning) `CLI` `Manual` | Pretrain, finetune ANY AI model of ANY size on 1 or 10,000+ GPUs with zero code changes. | `Cross` | **30.4k** |
| [Second Me](https://github.com/mindverse/Second-Me) | Train your AI self, amplify you, bridge the world | `SelfHost` `Web (Cloud)` | **14.5k** |

### RAG

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more. | `Cross` | **50.7k** |
| [AutoFlow](https://github.com/pingcap/autoflow) | pingcap/autoflow is a Graph RAG based and conversational knowledge base tool built with TiDB Serverless Vector Storage. Demo: https://tidb.ai | `SelfHost` | **2.7k** |
| [DocsGPT](https://github.com/arc53/DocsGPT) | Private AI platform for agents, assistants and enterprise search. Built-in Agent Builder, Deep research, Document analysis, Multi-model support, and API connectivity for agents. | `Cross` `SelfHost` | **17.3k** |
| [kotaemon](https://github.com/Cinnamon/kotaemon) | An open-source RAG-based tool for chatting with your documents. | `SelfHost` | **24.6k** |
| [PaperQA2](https://github.com/Future-House/paper-qa) `CLI` `Manual` | High accuracy RAG for answering questions from scientific documents with citations | `Cross` | **7.8k** |
| [R2R](https://github.com/SciPhi-AI/R2R) `CLI` | SoTA production-ready AI retrieval system. Agentic Retrieval-Augmented Generation (RAG) with a RESTful API. | `Web (Cloud)` `SelfHost` | **7.4k** |
| [RAGFlow](https://github.com/infiniflow/ragflow) | RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs | `SelfHost` | **67.1k** |
| [Verba](https://github.com/weaviate/Verba) | Retrieval Augmented Generation (RAG) chatbot powered by Weaviate | `SelfHost` | **7.4k** |

### Research

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [DeepSearcher](https://github.com/zilliztech/deep-searcher) `CLI` | Open Source Deep Research Alternative to Reason and Search on Private Data. Written in Python. | `Cross` | **7.1k** |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) `CLI+` | An LLM agent that conducts deep research (local and web) on any given topic and generates a long report with citations. | `Cross` `SelfHost` | **24k** |
| [STORM](https://github.com/stanford-oval/storm) `Manual` | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. | `Cross` | **27.6k** |

# Communication - [Go to top](#table-of-contents)

### Chat

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [bitchat](https://github.com/permissionlesstech/bitchat?tab=readme-ov-file) | bluetooth mesh chat, IRC vibes | `Mobile` | **23.2k** |
| [Legcord](https://github.com/Legcord/Legcord) | Legcord is a custom client designed to enhance your Discord experience while keeping everything lightweight. | `Cross` | **2.7k** |
| [Signal](https://github.com/signalapp/Signal-Android) | A private messenger for Android. | `Cross` | **27.9k** |
| [SimpleX](https://github.com/simplex-chat/simplex-chat) `CLI+` | SimpleX - the first messaging network operating without user identifiers of any kind - 100% private by design! iOS, Android and desktop apps 📱! | `Cross` | **9.8k** |
| [Telegram Desktop](https://github.com/telegramdesktop/tdesktop) | Telegram Desktop messaging app | `Cross` | **29k** |

### Collaboration

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Mattermost](https://github.com/mattermost/mattermost) | Mattermost is an open source platform for secure collaboration across the entire software development lifecycle.. | `SelfHost` | **34.3k** |
| [Rocket.Chat](https://github.com/RocketChat/Rocket.Chat) | The communications platform that puts data protection first. | `SelfHost` `Web (Cloud)` | **43.8k** |
| [Zulip](https://github.com/zulip/zulip) | Zulip server and web application. Open-source team chat that helps teams stay productive and focused. | `SelfHost` `Web (Cloud)` | **23.7k** |

### Mail

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Himalaya](https://github.com/pimalaya/himalaya) `TUI` | CLI to manage emails | `Cross` | **5k** |
| [Inbox Zero](https://github.com/elie222/inbox-zero) | The world's best AI personal assistant for email. Open source app to help you reach inbox zero fast. | `Web (Cloud)` `SelfHost` | **9.3k** |
| [Mailspring](https://github.com/Foundry376/Mailspring) | :love_letter: A beautiful, fast and fully open source mail client for Mac, Windows and Linux. | `Cross` | **16.8k** |
| [ProtonMail](https://github.com/ProtonMail/WebClients) | Monorepo hosting the proton web clients | `Cross` `Mobile` | **5.1k** |
| [Thunderbird](https://github.com/thunderbird/thunderbird-android) | Meet Thunderbird, the email and productivity app that maximizes your freedoms. | `Cross` | **12.7k** |
| [Tuta Mail](https://github.com/tutao/tutanota) | Tuta is an email service with a strong focus on security and privacy that lets you encrypt emails, contacts and calendar entries on all your devices. | `Android` | **7k** |

### Video Conference

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Element](https://github.com/element-hq/element-web) `CLI+` | A glossy Matrix collaboration client for the web. | `Web (Cloud)` | **12.3k** |
| [Jitsi Meet](https://github.com/jitsi/jitsi-meet) `CLI+` | Jitsi Meet - Secure, Simple and Scalable Video Conferences that you use as a standalone app or embed in your web application. | `Web (Cloud)` | **27.5k** |

# Data - [Go to top](#table-of-contents)

### Backup

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Backrest](https://github.com/garethgeorge/backrest) | Backrest is a web UI and orchestrator for restic backup. | `Cross` `SelfHost` | **4.3k** |
| [Borg](https://github.com/borgbackup/borg) `CLI` | Deduplicating archiver with compression and authenticated encryption. | `Cross` | **12.5k** |
| [Cryptomator](https://github.com/cryptomator/cryptomator) | Cryptomator for Windows, macOS, and Linux: Secure client-side encryption for your cloud storage, ensuring privacy and control over your data. | `Cross` `Mobile` | **13.9k** |
| [Duplicacy](https://github.com/gilbertchen/duplicacy) `CLI` | A new generation cloud backup tool  | `Cross` | **5.5k** |
| [Duplicati](https://github.com/duplicati/duplicati) | Store securely encrypted backups in the cloud! | `Cross` | **13.4k** |
| [Kopia](https://github.com/kopia/kopia) `CLI` | Cross-platform backup tool for Windows, macOS & Linux with fast, incremental backups, client-side end-to-end encryption, compression and data deduplication. CLI and GUI included. | `Cross` | **11.4k** |
| [Rclone](https://github.com/rclone/rclone) `CLI` | "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files | `Cross` | **53.4k** |
| [Restic](https://github.com/restic/restic) `CLI` | Fast, secure, efficient backup program | `Cross` | **30.7k** |
| [rustic](https://github.com/rustic-rs/rustic) `CLI` | rustic - fast, encrypted, and deduplicated backups powered by Rust | `Cross` | **2.7k** |
| [Timeshift](https://github.com/linuxmint/timeshift) | System restore tool for Linux. Creates filesystem snapshots using rsync+hardlinks, or BTRFS snapshots. Supports scheduled snapshots, multiple backup levels, and exclude filters. Snapshots can be restored while system is running or from Live CD/USB. | `Linux` | **3.6k** |
| [Vorta](https://github.com/borgbase/vorta) | Desktop Backup Client for Borg Backup | `Cross` | **2.3k** |

### Storage

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Ceph](https://github.com/ceph/ceph) | Ceph is a distributed object, block, and file storage platform  | `SelfHost` | **15.7k** |
| [myDrive](https://github.com/subnub/myDrive) | Node.js and mongoDB Google Drive Clone | `SelfHost` | **4.1k** |
| [Nextcloud](https://github.com/nextcloud/server) | ☁️ Nextcloud server, a safe home for all your data | `Cross` `SelfHost` | **33.3k** |
| [ownCloud](https://github.com/owncloud/core) | :cloud: ownCloud web server core (Files, DAV, etc.) | `SelfHost` | **8.7k** |
| [Seafile](https://github.com/haiwen/seafile) `CLI+` | Beyond file syncing and sharing, a new way to organize your files with extensible file properties and flexible views | `Cross` `SelfHost` | **13.9k** |

### Sync

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Rsync](https://github.com/RsyncProject/rsync) `CLI` | An open source utility that provides fast incremental file transfer. It also has useful features for backup and restore operations among many other use cases. | `Cross` | **3.9k** |
| [Syncthing](https://github.com/syncthing/syncthing) `CLI+` | Open Source Continuous File Synchronization | `Cross` | **77.4k** |
| [Syncthing Tray](https://github.com/Martchus/syncthingtray) | Tray application and Dolphin/Plasma integration for Syncthing | `Windows` `Linux` | **2.5k** |
| [syncthing-macos](https://github.com/syncthing/syncthing-macos) `CLI+` | Official frugal and native macOS Syncthing application bundle | `MacOS` | **3.3k** |

# Development - [Go to top](#table-of-contents)

### API Client

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Hoppscotch](https://github.com/hoppscotch/hoppscotch) `CLI+` | Open-Source API Development Ecosystem • https://hoppscotch.io • Offline, On-Prem & Cloud • Web, Desktop & CLI • Open-Source Alternative to Postman, Insomnia | `Cross` `Web (Cloud)` | **76.8k** |
| [HTTPie CLI](https://github.com/httpie/cli) `CLI` | 🥧 HTTPie CLI  — modern, user-friendly command-line HTTP client for the API era. JSON support, colors, sessions, downloads, plugins & more. | `Cross` | **36.9k** |
| [HTTPie Desktop](https://github.com/httpie/desktop) | 🚀 HTTPie Desktop — cross-platform API testing client for humans. Painlessly test REST, GraphQL, and HTTP APIs. | `Cross` | **3.7k** |
| [Insomnia](https://github.com/Kong/insomnia) | The open-source, cross-platform API client for GraphQL, REST, WebSockets, SSE and gRPC. With Cloud, Local and Git storage. | `Cross` | **37.5k** |
| [Requestly](https://github.com/requestly/requestly) | Free and open-source API Client & Interceptor. | `Cross` | **4.7k** |
| [Restfox](https://github.com/flawiddsouza/Restfox) | Offline-First Minimalistic HTTP & Socket Testing Client for the Web & Desktop | `Cross` | **2.5k** |
| [Yaak](https://github.com/mountain-loop/yaak) | The most intuitive desktop API client. Organize and execute REST, GraphQL, WebSockets, Server Sent Events, and gRPC 🦬 | `Cross` | **15.1k** |

### Code Assistant

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Aider](https://github.com/Aider-AI/aider) `CLI` | aider is AI pair programming in your terminal | `Cross` | **38.2k** |
| [Cline](https://github.com/cline/cline) | Autonomous coding agent right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way. | `VSCode` | **52.1k** |
| [Codex](https://github.com/openai/codex) `CLI` `Manual` | Lightweight coding agent that runs in your terminal | `Cross` | **49.9k** |
| [Cody](https://github.com/sourcegraph/cody) | Type less, code more: Cody is an AI code assistant that uses advanced search and codebase context to help you write and fix code. | `VSCode` `JetBrains` | **3.8k** |
| [Continue](https://github.com/continuedev/continue) | ⏩ Ship faster with Continuous AI. Open-source CLI that can be used in TUI mode as a coding agent or Headless mode to run background agents | `VSCode` `JetBrains` | **29.7k** |
| [Goose](https://github.com/block/goose) `CLI+` | an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM | `Cross` | **21.9k** |
| [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot) `CLI` | The first real AI developer | `Cross` | **33.6k** |
| [MetaGPT](https://github.com/geekan/MetaGPT) | 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming | `SelfHost` `Web (Cloud)` | **59.2k** |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 🙌 OpenHands: Code Less, Make More | `Cross` `SelfHost` | **64.7k** |
| [Plandex](https://github.com/plandex-ai/plandex) `CLI` | Open source AI coding agent. Designed for large projects and real world tasks. | `Cross` | **14.6k** |
| [Roo Code](https://github.com/RooVetGit/Roo-Code) | Roo Code gives you a whole dev team of AI agents in your code editor. | `VSCode` | **20.6k** |
| [Tabby](https://github.com/TabbyML/tabby) | Self-hosted AI coding assistant | `SelfHost` `VSCode` `JetBrains` | **32.4k** |
| [windsurf.vim](https://github.com/Exafunction/windsurf.vim) | Free, ultrafast Copilot alternative for Vim and Neovim | `N/A` | **5.1k** |

### Code Editor

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [code-server](https://github.com/coder/code-server) | VS Code in the browser | `SelfHost` | **74.5k** |
| [CodeEdit](https://github.com/CodeEditApp/CodeEdit) | 📝 CodeEdit App for macOS – Elevate your code editing experience. Open source, free forever. | `MacOS` | **22.3k** |
| [Helix](https://github.com/helix-editor/helix) `CLI` | A post-modern modal text editor. | `Cross` | **41.1k** |
| [Lapce](https://github.com/lapce/lapce) | Lightning-fast and Powerful Code Editor written in Rust | `Cross` | **37.6k** |
| [LazyVim](https://github.com/LazyVim/LazyVim) `CLI` | Neovim config for the lazy | `Cross` | **23.8k** |
| [neovim](https://github.com/neovim/neovim) `CLI` | Vim-fork focused on extensibility and usability | `Cross` | **94k** |
| [NvChad](https://github.com/NvChad/NvChad) `CLI` | Blazing fast Neovim framework providing solid defaults and a beautiful UI, enhancing your neovim experience. | `Cross` | **27.4k** |
| [Onlook](https://github.com/onlook-dev/onlook) | The Cursor for Designers • An Open-Source AI-First Design tool • Visually build, style, and edit your React App with AI | `Cross` | **23.2k** |
| [Vim](https://github.com/vim/vim) 🌍`CLI` | The official Vim repository | `Cross` | **39.2k** |
| [Void](https://github.com/voideditor/void) | Void is the open-source Cursor alternative. | `Windows` `MacOS` | **27.4k** |
| [VS Code](https://github.com/microsoft/vscode) | Visual Studio Code | `Cross` | **178.2k** |
| [VSCodium](https://github.com/VSCodium/vscodium) | binary releases of VS Code without MS branding/telemetry/licensing | `Cross` | **29k** |
| [Zed](https://github.com/zed-industries/zed) 🏦 | Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter. | `MacOS` `Linux` | **69.2k** |

### Dev Tools

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [act](https://github.com/nektos/act) | Run your GitHub Actions locally 🚀 | `SelfHost` | **66.8k** |
| [Backlog.md](https://github.com/MrLesk/Backlog.md) | Backlog.md - A tool for managing project collaboration between humans and AI Agents in a git ecosystem | `Cross` | **3.9k** |
| [bat](https://github.com/sharkdp/bat) `CLI` | A cat(1) clone with wings. | `Cross` | **55.7k** |
| [ByteStash](https://github.com/jordan-dalby/ByteStash) | A code snippet storage solution written in React & node.js | `SelfHost` | **1.8k** |
| [DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser) | Official home of the DB Browser for SQLite (DB4S) project. Previously known as "SQLite Database Browser" and "Database Browser for SQLite". Website at:  | `Cross` | **23.2k** |
| [DevToys](https://github.com/DevToys-app/DevToys) | A Swiss Army knife for developers. | `Cross` | **30.3k** |
| [jj](https://github.com/jj-vcs/jj) | A Git-compatible VCS that is both simple and powerful | `Cross` | **21.9k** |
| [JSON Crack](https://github.com/AykutSarac/jsoncrack.com) `Manual` | ✨ Innovative and open-source visualization application that transforms various data formats, such as JSON, YAML, XML, CSV and more, into interactive graphs. | `Cross` `Web (Cloud)` | **42.4k** |
| [Jujutsu](https://github.com/jj-vcs/jj) `CLI` | A Git-compatible VCS that is both simple and powerful | `Cross` | **21.9k** |
| [massCode](https://github.com/massCodeIO/massCode) | A free and open source code snippet manager for developers | `Cross` | **6.5k** |
| [Onefetch](https://github.com/o2sh/onefetch) `TUI` | Command-line Git information tool | `Cross` | **11.3k** |
| [typos](https://github.com/crate-ci/typos) `CLI` | Source code spell checker | `Cross` | **3.6k** |
| [Watchexec](https://github.com/watchexec/watchexec) `CLI` | Executes commands in response to file modifications | `Cross` | **6.5k** |

### Game Engine

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [GDevelop](https://github.com/4ian/GDevelop) | 🎮 Open-source, cross-platform 2D/3D/multiplayer game engine designed for everyone. | `Cross` | **17.4k** |
| [Godot](https://github.com/godotengine/godot) | Godot Engine – Multi-platform 2D and 3D game engine | `Cross` | **102.9k** |

### Git Client

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [gh-dash](https://github.com/dlvhdr/gh-dash) `TUI` `Manual` | A rich terminal UI for GitHub that doesn't break your flow. | `Cross` | **9.2k** |
| [GitBucket](https://github.com/gitbucket/gitbucket) `Manual` | A Git platform powered by Scala with easy installation, high extensibility & GitHub API compatibility | `Cross` | **9.3k** |
| [GitButler](https://github.com/gitbutlerapp/gitbutler) | The GitButler version control client, backed by Git, powered by Tauri/Rust/Svelte | `Cross` | **17k** |
| [GitHub Desktop](https://github.com/desktop/desktop) | Focus on what matters instead of fighting with Git. | `Cross` | **20.9k** |
| [GitHub Desktop - The Linux Fork](https://github.com/shiftkey/desktop) | Fork of GitHub Desktop to support various Linux distributions | `Linux` | **7.6k** |
| [GitUI](https://github.com/gitui-org/gitui) `TUI` | Blazing 💥 fast terminal-ui for git written in rust 🦀 | `Cross` | **20.8k** |
| [Lazygit](https://github.com/jesseduffield/lazygit) `TUI` | simple terminal UI for git commands | `Cross` | **67.3k** |

### Git Hosting

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Gitea](https://github.com/go-gitea/gitea) | Git with a cup of tea! Painless self-hosted all-in-one software development service, including Git hosting, code review, team collaboration, package registry and CI/CD | `SelfHost` | **51.8k** |
| [GitLab](https://github.com/gitlabhq/gitlabhq) | GitLab CE Mirror - Please open new issues in our issue tracker on GitLab.com | `SelfHost` `Web (Cloud)` | **24.2k** |
| [Gogs](https://github.com/gogs/gogs) | Gogs is a painless self-hosted Git service | `SelfHost` | **47.2k** |
| [Soft Serve](https://github.com/charmbracelet/soft-serve) `TUI` | The mighty, self-hostable Git server for the command line🍦 | `Cross` | **6.3k** |

### IDE

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Bruno](https://github.com/usebruno/bruno) | Opensource IDE For Exploring and Testing API's (lightweight alternative to Postman/Insomnia) | `Cross` | **38.3k** |
| [IntelliJ IDEA](https://github.com/JetBrains/intellij-community) | IntelliJ IDEA & IntelliJ Platform | `Cross` | **19.1k** |
| [Neovide](https://github.com/neovide/neovide) | No Nonsense Neovim Client in Rust | `Cross` | **14.5k** |
| [Qt Creator](https://github.com/qt-creator/qt-creator) | A cross-platform Qt IDE | `Cross` | **2.9k** |

### Language Package Manager

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Bun](https://github.com/oven-sh/bun) `CLI` | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one | `Cross` | **82k** |
| [PNPM](https://github.com/pnpm/pnpm) `CLI` | Fast, disk space efficient package manager | `Cross` | **33.1k** |
| [uv](https://github.com/astral-sh/uv) `CLI` | An extremely fast Python package and project manager, written in Rust. | `Cross` | **72k** |
| [Yarn](https://github.com/yarnpkg/berry) `CLI` | 📦🐈 Active development trunk for Yarn ⚒ | `Cross` | **7.9k** |

# Entertainment - [Go to top](#table-of-contents)

### Game Launcher

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Heroic Games Launcher](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher) | A games launcher for GOG, Amazon and Epic Games for Linux, Windows and macOS. | `Cross` | **10k** |
| [Hydra](https://github.com/hydralauncher/hydra) | Hydra Launcher is an open-source gaming platform created to be the single tool that you need | `Cross` | **14.6k** |
| [Lutris](https://github.com/lutris/lutris) | Lutris desktop client | `Linux` | **9.2k** |
| [Moonlight](https://github.com/moonlight-stream/moonlight-qt) | GameStream client for PCs (Windows, Mac, Linux, and Steam Link) | `Cross` | **15k** |
| [Pelican Panel](https://github.com/pelican-dev/panel) | Pelican Panel is an open-source, web-based application designed for easy management of game servers. | `SelfHost` | **1.7k** |
| [Playnite](https://github.com/JosefNemec/Playnite) | Video game library manager with support for wide range of 3rd party libraries and game emulation support, providing one unified interface for your games. | `Windows` | **11.7k** |
| [RomM](https://github.com/rommapp/romm) | A beautiful, powerful, self-hosted rom manager and player. | `SelfHost` | **6.8k** |

### Games

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Cataclysm DDA](https://github.com/CleverRaven/Cataclysm-DDA) | Cataclysm - Dark Days Ahead. A turn-based survival game set in a post-apocalyptic world. | `Cross` | **11.7k** |
| [Endless Sky](https://github.com/endless-sky/endless-sky) | Space exploration, trading, and combat game. | `Cross` | **6.9k** |
| [lichess](https://github.com/lichess-org/lila) | ♞ lichess.org: the forever free, adless and open source chess server ♞ | `Web (Cloud)` | **17.3k** |
| [Mindustry](https://github.com/Anuken/Mindustry) | The automation tower defense RTS | `Cross` `Mobile` | **25.6k** |
| [OpenRA](https://github.com/OpenRA/OpenRA) | Open Source real-time strategy game engine for early Westwood games such as Command & Conquer: Red Alert written in C# using SDL and OpenGL. Runs on Windows, Linux, *BSD and Mac OS X. | `Cross` | **16.1k** |
| [Thrive](https://github.com/Revolutionary-Games/Thrive) | The main repository for the development of the evolution game Thrive.  | `Cross` | **3.3k** |
| [Unciv](https://github.com/yairm210/Unciv) | Open-source Android/Desktop remake of Civ V | `Cross` `Android` | **9.7k** |
| [Veloren](https://github.com/veloren/veloren) | [mirror of https://gitlab.com/veloren/veloren] An open world, open source voxel RPG inspired by Dwarf Fortress and Cube World. This repository is a mirror. Please submit all PRs and issues on our GitLab page. | `Cross` | **6.9k** |
| [Wesnoth](https://github.com/wesnoth/wesnoth) | An open source, turn-based strategy game with a high fantasy theme. | `Cross` | **6.3k** |

# Extensions - [Go to top](#table-of-contents)

### Browser Extensions

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Dark Reader](https://github.com/darkreader/darkreader) | Dark Reader Chrome and Firefox extension | `Chromium` `Firefox` | **21.3k** |
| [Page Assist](https://github.com/n4ze3m/page-assist) | Use your locally running AI models to assist you in your web browsing | `Chromium` `Firefox` | **7.3k** |
| [Refined GitHub](https://github.com/refined-github/refined-github) | :octocat: Browser extension that simplifies the GitHub interface and adds useful features | `Chromium` `Firefox` | **29.6k** |
| [uBlock Origin](https://github.com/gorhill/uBlock) | uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean. | `Chromium` `Firefox` | **59.6k** |
| [Web Clipper](https://github.com/webclipper/web-clipper) | For Notion,OneNote,Bear,Yuque,Joplin。Clip anything to anywhere | `Chromium` `Firefox` | **6.6k** |

### EMACS Packages

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |

### Neovim Extensions

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Coq](https://github.com/ms-jpq/coq_nvim) | Fast as FUCK nvim completion. SQLite, concurrent scheduler, hundreds of hours of optimization. | `N/A` | **3.7k** |
| [lazy.nvim](https://github.com/folke/lazy.nvim) | 💤 A modern plugin manager for Neovim | `N/A` | **19.3k** |
| [mason.nvim](https://github.com/mason-org/mason.nvim) `TUI` | Portable package manager for Neovim that runs everywhere Neovim runs. Easily install and manage LSP servers, DAP servers, linters, and formatters. | `N/A` | **9.7k** |
| [Neorg](https://github.com/nvim-neorg/neorg) | Modernity meets insane extensibility. The future of organizing your life in Neovim. | `N/A` | **7.1k** |
| [nvim-dap](https://github.com/mfussenegger/nvim-dap) | Debug Adapter Protocol client implementation for Neovim | `N/A` | **6.7k** |
| [VimWiki](https://github.com/vimwiki/vimwiki) | Personal Wiki for Vim | `N/A` | **9.3k** |

# Internet - [Go to top](#table-of-contents)

### Browser

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Brave](https://github.com/brave/brave-browser) | Brave browser for Android, iOS, Linux, macOS, Windows. | `Cross` | **20.6k** |
| [Firefox](https://github.com/mozilla-firefox/firefox) | Fast, reliable and private — for peace of mind online. | `Cross` `Mobile` | **10.4k** |
| [Floorp](https://github.com/Floorp-Projects/Floorp) | All of source code of version 10 or later of Floorp Browser, the most Advanced and Fastest Firefox derivative 🦊 | `Cross` | **7.7k** |
| [Helium](https://github.com/imputnet/helium) | Private, fast, and honest web browser | `Cross` | **6.5k** |
| [Min](https://github.com/minbrowser/min) | A fast, minimal browser that protects your privacy | `Cross` | **8.7k** |
| [Neko](https://github.com/m1k1o/neko) | A self hosted virtual browser that runs in docker and uses WebRTC. | `SelfHost` | **15.8k** |
| [Noi](https://github.com/lencx/Noi) | 🚀 Power Your World with AI - Explore, Extend, Empower. | `Cross` | **8.1k** |
| [Zen](https://github.com/zen-browser/desktop) | Welcome to a calmer internet | `Cross` | **37.6k** |

### Download Manager

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [AB](https://github.com/amir1376/ab-download-manager) | A Download Manager that speeds up your downloads | `Cross` | **11.3k** |
| [File Centipede](https://github.com/filecxx/FileCentipede) | Cross-platform internet upload/download manager for HTTP(S), FTP(S), SSH, magnet-link, BitTorrent, m3u8, ed2k, and online videos.  WebDAV client, FTP client, SSH client. | `SelfHost` | **10.6k** |
| [GoPeed](https://github.com/GopeedLab/gopeed) | A modern download manager that supports all platforms.  Built with Golang and Flutter. | `Cross` | **21.2k** |
| [Persepolis](https://github.com/persepolisdm/persepolis) | Persepolis is a download manager written in Python. | `Cross` | **7k** |
| [qBittorrent](https://github.com/qbittorrent/qBittorrent) | qBittorrent BitTorrent client | `Cross` | **33.8k** |
| [Transmission](https://github.com/transmission/transmission) | Official Transmission BitTorrent client repository | `Cross` | **13.7k** |

### Network

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Sniffnet](https://github.com/GyulyVGC/sniffnet) | Comfortably monitor your Internet traffic 🕵️‍♂️ | `Cross` | **31.6k** |
| [Wireshark](https://github.com/wireshark/wireshark) | Wireshark lets you dive deep into your network traffic - free and open source. | `Cross` | **8.6k** |

### Search Engine

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Morphic](https://github.com/miurla/morphic) | An AI-powered search engine with a generative UI | `SelfHost` `Web (Cloud)` | **8.3k** |
| [Perplexica](https://github.com/ItzCrazyKns/Perplexica) | Perplexica is an AI-powered answering engine. It is an Open source alternative to Perplexity AI | `SelfHost` | **27.1k** |
| [Scira](https://github.com/zaidmukaddam/scira) | Scira (Formerly MiniPerplx) is a minimalistic AI-powered search engine that helps you find information on the internet and cites it too. Powered by Vercel AI SDK! Open Source perplexity alternative. | `SelfHost` `Web (Cloud)` | **10.9k** |
| [SearXNG](https://github.com/searxng/searxng) | SearXNG is a free internet metasearch engine which aggregates results from various search services and databases. Users are neither tracked nor profiled. | `SelfHost` | **23k** |
| [Spyglass](https://github.com/spyglass-search/spyglass) | A personal search engine:  Create a searchable library from your personal documents, interests, and more! | `Cross` | **2.7k** |
| [YaCy](https://github.com/yacy/yacy_search_server) | Distributed Peer-to-Peer Web Search Engine and Intranet Search Appliance | `SelfHost` | **3.7k** |

### Social Network

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Folo](https://github.com/RSSNext/Folo) | 🧡 Folo is the AI Reader | `Cross` `Mobile` `Web (Cloud)` | **35.6k** |
| [IceCubesApp](https://github.com/Dimillian/IceCubesApp) | A SwiftUI Mastodon client | `MacOS` `IOS` | **6.7k** |
| [Mastodon](https://github.com/mastodon/mastodon) | Your self-hosted, globally interconnected microblogging community | `web` `Mobile` | **49.2k** |
| [Pixelfed](https://github.com/pixelfed/pixelfed) | Photo Sharing. For Everyone. | `Mobile` | **6.8k** |
| [Toot](https://github.com/ihabunek/toot) `TUI` | toot - Mastodon CLI & TUI | `Cross` | **1.3k** |

# Media - [Go to top](#table-of-contents)

### Audio Editor

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Audacity](https://github.com/audacity/audacity) | Audio Editor                                      | `Cross` | **15.9k** |
| [MuseScore](https://github.com/musescore/MuseScore) | MuseScore is an open source and free music notation software. For support, contribution, bug reports, visit MuseScore.org. Fork and make pull requests! | `Cross` | **13.9k** |
| [OpenUtau](https://github.com/stakira/OpenUtau) | Open singing synthesis platform / Open source UTAU successor | `Cross` | **3.3k** |

### Audio Player

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Feishin](https://github.com/jeffvli/feishin) | A modern self-hosted music player. | `Cross` `SelfHost` | **5.3k** |
| [Navidrome](https://github.com/navidrome/navidrome) | 🎧☁️ Your Personal Streaming Service | `Cross` `SelfHost` | **17.2k** |
| [spotify_player](https://github.com/aome510/spotify-player) `TUI` | A Spotify player in the terminal with full feature parity | `Cross` | **5.6k** |
| [Spotube](https://github.com/KRTirtho/spotube) | 🎧 Open source music client! Available for both desktop & mobile! | `Cross` | **42.2k** |
| [Supersonic](https://github.com/dweymouth/supersonic) | A lightweight and full-featured cross-platform desktop client for self-hosted music servers | `Cross` | **1.7k** |
| [Youtube Music](https://github.com/th-ch/youtube-music) | Pear 🍐 is extension for music player | `Cross` | **29k** |

### Canvas

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Agora Flat](https://github.com/netless-io/flat) | Project flat is the Web, Windows and macOS client of Agora Flat open source classroom. | `Windows` `MacOS` `SelfHost` | **6.3k** |
| [Excalidraw](https://github.com/excalidraw/excalidraw) | Virtual whiteboard for sketching hand-drawn like diagrams | `SelfHost` `VSCode` | **109.7k** |

### Diagrams

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [drawDB](https://github.com/drawdb-io/drawdb) `Manual` | Free, simple, and intuitive online database diagram editor and SQL generator. | `Cross` `SelfHost` `Web (Cloud)` | **34.7k** |
| [Liam ERD](https://github.com/liam-hq/liam) `Manual` | Automatically generates beautiful and easy-to-read ER diagrams from your database. | `Web (Cloud)` `SelfHost` | **4.4k** |

### Graphics

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Blender](https://github.com/blender/blender) | Official mirror of Blender | `Cross` | **16.7k** |
| [CAD Sketcher](https://github.com/hlorus/CAD_Sketcher) | Constraint-based geometry sketcher for blender | `N/A` | **3.1k** |
| [CadQuery](https://github.com/CadQuery/cadquery) | A python parametric CAD scripting framework based on OCCT | `Cross` | **4.1k** |
| [FreeCAD](https://github.com/FreeCAD/FreeCAD) | Official source code of FreeCAD, a free and opensource multiplatform 3D parametric modeler. | `Cross` | **26.9k** |
| [Gaphor](https://github.com/gaphor/gaphor) | Gaphor is the simple modeling tool | `Cross` | **2.1k** |
| [Graphite](https://github.com/GraphiteEditor/Graphite) | An open source graphics editor for 2025: comprehensive 2D content creation tool suite for graphic design, digital art, and interactive real-time motion graphics — featuring node-based procedural editing | `Web (Cloud)` | **22.6k** |
| [Krita](https://github.com/KDE/krita) | Krita is a free and open source cross-platform application that offers an end-to-end solution for creating digital art files from scratch built on the KDE and Qt frameworks. | `Cross` | **9k** |
| [OpenSCAD](https://github.com/openscad/openscad) | OpenSCAD - The Programmers Solid 3D CAD Modeller   | `Cross` | **8.4k** |
| [PAINT BOARD](https://github.com/LHRUN/paint-board) | 🎨  A powerful multi-end drawing board that brings together a lot of creative brushes to experience a whole new range of drawing effects! | `SelfHost` | **2.6k** |
| [Penpot](https://github.com/penpot/penpot) | Penpot: The open-source design tool for design and code collaboration | `Web (Cloud)` | **41k** |
| [PixiEditor](https://github.com/PixiEditor/PixiEditor) | PixiEditor is a Universal Editor for all your 2D needs | `Cross` | **6.8k** |

### Image Editing

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [darktable](https://github.com/darktable-org/darktable) | darktable is an open source photography workflow application and raw developer | `Cross` | **11.6k** |
| [ImageMagick](https://github.com/ImageMagick/ImageMagick) | ImageMagick is a free, open-source software suite for creating, editing, converting, and displaying images. It supports 200+ formats and offers powerful command-line tools and APIs for automation, scripting, and integration across platforms. | `Cross` | **14.8k** |
| [PhotoDemon](https://github.com/tannerhelland/PhotoDemon) | A free portable photo editor focused on pro-grade features, high performance, and maximum usability. | `Windows` | **1.9k** |
| [RapidRAW](https://github.com/CyberTimon/RapidRAW) | A beautiful, non-destructive, and GPU-accelerated RAW image editor built with performance in mind. | `Cross` | **3.4k** |
| [RawTherapee](https://github.com/RawTherapee/RawTherapee) | A powerful cross-platform raw photo processing program | `Cross` | **3.6k** |

### Image Processing

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [chaiNNer](https://github.com/chaiNNer-org/chaiNNer) | A node-based image processing GUI aimed at making chaining image processing tasks easy and customizable. Born as an AI upscaling application, chaiNNer has grown into an extremely flexible and powerful programmatic image processing application. | `Cross` | **5.4k** |
| [Upscayl](https://github.com/upscayl/upscayl) | 🆙 Upscayl - #1 Free and Open Source AI Image Upscaler for Linux, MacOS and Windows. | `Cross` | **41k** |

### Media Downloader

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Cobalt](https://github.com/imputnet/cobalt) | best way to save what you love | `Web (Cloud)` | **37.1k** |
| [MeTube](https://github.com/alexta69/metube) | Self-hosted YouTube downloader (web UI for youtube-dl / yt-dlp) | `SelfHost` | **10.6k** |
| [Parabolic](https://github.com/NickvisionApps/Parabolic) | Download web video and audio | `Windows` `Linux` | **4.2k** |
| [Pinchflat](https://github.com/kieraneglin/pinchflat) | Your next YouTube media manager | `SelfHost` | **4.1k** |
| [Seal](https://github.com/JunkFood02/Seal) | 🦭 Video/Audio Downloader for Android, based on yt-dlp | `Android` | **22.7k** |
| [YoutubeDownloader](https://github.com/Tyrrrz/YoutubeDownloader) | Downloads videos and playlists from YouTube | `Cross` | **13.2k** |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) `CLI` | A feature-rich command-line audio/video downloader | `Cross` | **133.9k** |
| [YTDLnis](https://github.com/deniscerri/YTDLnis) | Full-featured audio/video downloader for Android using yt-dlp | `Android` | **6.6k** |

### Screen Recording

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Cap](https://github.com/CapSoftware/Cap) | Open source Loom alternative. Beautiful, shareable screen recordings. | `Cross` | **14.4k** |
| [Flameshot](https://github.com/flameshot-org/flameshot) | Powerful yet simple to use screenshot software :desktop_computer: :camera_flash: | `Cross` | **28.2k** |
| [OBS Studio](https://github.com/obsproject/obs-studio) | OBS Studio - Free and open source software for live streaming and screen recording | `Cross` | **67.9k** |
| [ShareX](https://github.com/ShareX/ShareX) | ShareX is a free and open-source application that enables users to capture or record any area of their screen with a single keystroke. It also supports uploading images, text, and various file types to a wide range of destinations. | `Windows` | **34.3k** |

### Video Editing

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Gyroflow](https://github.com/gyroflow/gyroflow) | Video stabilization using gyroscope data | `Cross` | **7.9k** |
| [Kdenlive](https://github.com/KDE/kdenlive) | Free and open source video editor, based on MLT Framework and KDE Frameworks | `Cross` | **4.2k** |
| [LossletCut](https://github.com/mifi/lossless-cut) | The swiss army knife of lossless video/audio editing | `Cross` | **34.5k** |
| [Natron](https://github.com/NatronGitHub/Natron) | Open-source video compositing software. Node-graph based. Similar in functionalities to Adobe After Effects and Nuke by The Foundry. | `Cross` | **5.1k** |
| [Olive](https://github.com/olive-editor/olive) | Free open-source non-linear video editor | `Cross` | **8.8k** |
| [OpenCut](https://github.com/OpenCut-app/OpenCut) | The open-source CapCut alternative | `Web (Cloud)` | **43.3k** |
| [Shotcut](https://github.com/mltframework/shotcut) | cross-platform (Qt), open-source (GPLv3) video editor | `Cross` | **12.9k** |

### Video Player

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [IINA](https://github.com/iina/iina) | The modern video player for macOS. | `MacOS` | **42.5k** |
| [Jellyfin Media Player](https://github.com/jellyfin/jellyfin-media-player) | Jellyfin Desktop Client | `Cross` | **4.3k** |
| [mpv](https://github.com/mpv-player/mpv) | 🎥 Command line media player | `Cross` | **32.6k** |
| [VLC](https://github.com/videolan/vlc) | VLC media player - All pull requests are ignored, please use MRs on https://code.videolan.org/videolan/vlc | `Cross` | **16.7k** |

### Video Transcoder

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [HandBrake](https://github.com/HandBrake/HandBrake) | HandBrake's development repository  | `Cross` | **21.2k** |

# Operating System - [Go to top](#table-of-contents)

### Linux

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Extension Manager](https://github.com/mjakeman/extension-manager) | A utility for browsing and installing GNOME Shell Extensions. | `Linux` | **1.2k** |
| [Flatseal](https://github.com/tchx84/Flatseal) | Manage Flatpak permissions | `Linux` | **1.5k** |
| [WinBoat](https://github.com/TibixDev/winboat) | Run Windows apps on 🐧 Linux with ✨ seamless integration | `Linux` | **14.9k** |

### MacOS

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [AltTab](https://github.com/lwouis/alt-tab-macos) | Windows alt-tab on macOS  | `MacOS` | **13.6k** |
| [AppLite](https://github.com/milanvarady/Applite) | User-friendly GUI macOS application for Homebrew Casks | `Cross` | **5.8k** |
| [battery](https://github.com/actuallymentor/battery) `CLI+` | CLI/GUI for managing the battery charging status for Apple silicon (M1, M2, M3) Macs | `MacOS` | **6.1k** |
| [Battery Toolkit](https://github.com/mhaeuser/Battery-Toolkit) | Control the platform power state of your Apple Silicon Mac. | `MacOS` | **2k** |
| [Calendr](https://github.com/pakerwreah/Calendr) | Menu bar calendar for macOS - MVVM - RxSwift - AppKit - SwiftUI | `MacOS` | **1.9k** |
| [Cork](https://github.com/buresdv/Cork) | A fast GUI for Homebrew written in SwiftUI | `MacOS` | **3.8k** |
| [DockDoor](https://github.com/ejbills/DockDoor) | Window peeking & alt-tab for macOS | `MacOS` | **3.1k** |
| [Ice](https://github.com/jordanbaird/Ice) ⏳ | Powerful menu bar manager for macOS | `MacOS` | **23.9k** |
| [Itsycal](https://github.com/sfsam/Itsycal) | Itsycal is a tiny calendar for your Mac's menu bar. http://www.mowglii.com/itsycal | `MacOS` | **3.7k** |
| [KeepingYouAwake](https://github.com/newmarcel/KeepingYouAwake) | Prevents your Mac from going to sleep. | `MacOS` | **6.1k** |
| [LinearMouse](https://github.com/linearmouse/linearmouse) | The mouse and trackpad utility for Mac. | `MacOS` | **5.1k** |
| [Lunar](https://github.com/alin23/Lunar) | Intelligent adaptive brightness for your external monitors | `MacOS` | **5.3k** |
| [MeetingBar](https://github.com/leits/MeetingBar) | 🇺🇦 Your meetings at your fingertips in the macOS menu bar  | `MacOS` | **5k** |
| [OnlySwitch](https://github.com/jacklandrin/OnlySwitch) | ⚙️ All-in-One menu bar app, hide 💻MacBook Pro's notch, dark mode, AirPods, Shortcuts | `MacOS` | **5.2k** |
| [Pika](https://github.com/superhighfives/pika) | An open-source colour picker app for macOS | `MacOS` | **2.2k** |
| [Plash](https://github.com/sindresorhus/Plash) | 💦 Make any website your Mac desktop wallpaper | `MacOS` | **3.9k** |
| [Reminders MenuBar](https://github.com/DamascenoRafael/reminders-menubar?tab=readme-ov-file) | Simple macOS menu bar application to view and interact with reminders. Developed with SwiftUI and using Apple Reminders as a source. | `MacOS` | **3.5k** |
| [SketchyBar](https://github.com/FelixKratz/SketchyBar) | A highly customizable macOS status bar replacement | `MacOS` | **10.4k** |
| [Sloth](https://github.com/sveinbjornt/Sloth) | Mac app that shows all open files, directories, sockets, pipes and devices in use by all running processes. Nice GUI for lsof. | `MacOS` | **8.6k** |
| [SwiftBar](https://github.com/swiftbar/SwiftBar) | Powerful macOS menu bar customization tool | `MacOS` | **3.5k** |
| [TheBoringNotch](https://github.com/TheBoredTeam/boring.notch) | TheBoringNotch: Not so boring notch That Rocks 🎸🎶 | `MacOS` | **5.3k** |
| [WWDC](https://github.com/insidegui/WWDC) | The unofficial WWDC app for macOS | `MacOS` | **8.7k** |

### Operating System

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Omarchy](https://github.com/basecamp/omarchy) | Beautiful, Modern & Opinionated Linux | `N/A` | **16.5k** |
| [openmediavault](https://github.com/openmediavault/openmediavault) | openmediavault is the next generation network attached storage (NAS) solution based on Debian Linux. Thanks to the modular design of the framework it can be enhanced via plugins. openmediavault is primarily designed to be used in home environments or small home offices. | `N/A` | **6.1k** |
| [Puter](https://github.com/HeyPuter/puter) | 🌐 The Internet Computer! Free, Open-Source, and Self-Hostable. | `N/A` | **37.1k** |
| [SerenityOS](https://github.com/SerenityOS/serenity) | The Serenity Operating System 🐞 | `N/A` | **32.6k** |
| [umbrelOS](https://github.com/getumbrel/umbrel) | A beautiful home server OS for self-hosting with an app store. Buy a pre-built Umbrel Home with umbrelOS, or install on a Raspberry Pi or any x86 system. | `N/A` | **9.6k** |
| [YunoHost](https://github.com/YunoHost/yunohost) | YunoHost is an operating system aiming to simplify as much as possible the administration of a server. This repository corresponds to the core code, written mostly in Python and Bash. | `N/A` | **2.7k** |

### Windows

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [PowerToys](https://github.com/microsoft/PowerToys) | Microsoft PowerToys is a collection of utilities that help you customize Windows and streamline everyday tasks | `Windows` | **125.5k** |
| [Rainmeter](https://github.com/rainmeter/rainmeter) | Desktop customization tool for Windows | `Windows` | **5.5k** |
| [UniGetUI](https://github.com/marticliment/UniGetUI) | UniGetUI: The Graphical Interface for your package managers. Could be terribly described as a package manager manager to manage your package managers | `Windows` | **19.1k** |
| [Win11Debloat](https://github.com/Raphire/Win11Debloat) `CLI` | A simple, lightweight PowerShell script to remove pre-installed apps, disable telemetry, as well as perform various other changes to customize, declutter and improve your Windows experience. Win11Debloat works for both Windows 10 and Windows 11. | `Windows` | **32.2k** |
| [WinUtil](https://github.com/ChrisTitusTech/winutil) | Chris Titus Tech's Windows Utility - Install Programs, Tweaks, Fixes, and Updates | `Windows` | **42.4k** |

# Organization - [Go to top](#table-of-contents)

### Bookmark Manager

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [buku](https://github.com/jarun/buku) `CLI+` | :bookmark: Personal mini-web in text | `Cross` | **6.9k** |
| [Karakeep](https://github.com/karakeep-app/karakeep) | A self-hostable bookmark-everything app (links, notes and images) with AI-based automatic tagging and full text search | `SelfHost` | **20.8k** |
| [LinkAce](https://github.com/Kovah/LinkAce) | LinkAce is a self-hosted archive to collect links of your favorite websites. | `SelfHost` | **3.1k** |
| [linkding](https://github.com/sissbruecker/linkding) | Self-hosted bookmark manager that is designed be to be minimal, fast, and easy to set up using Docker. | `SelfHost` | **9.5k** |
| [Linkwarden](https://github.com/linkwarden/linkwarden) | ⚡️⚡️⚡️ Self-hosted collaborative bookmark manager to collect, read, annotate, and fully preserve what matters, all in one place. | `SelfHost` | **15.4k** |
| [Shiori](https://github.com/go-shiori/shiori) | Simple bookmark manager built with Go | `SelfHost` | **11k** |
| [wallabag](https://github.com/wallabag/wallabag) | wallabag is a self hostable application for saving web pages: Save and classify articles. Read them later. Freely. | `SelfHost` | **12.2k** |

### Document Management

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Docspell](https://github.com/eikek/docspell) `CLI+` | Assist in organizing your piles of documents, resulting from scanners, e-mails and other sources with miminal effort. | `SelfHost` `Android` | **1.9k** |
| [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | A community-supported supercharged document management system: scan, index and archive all your documents | `SelfHost` | **34.1k** |
| [Papermerge DMS](https://github.com/ciur/papermerge) | Open Source Document Management System for Digital Archives (Scanned Documents) | `SelfHost` | **2.8k** |
| [TagSpaces](https://github.com/tagspaces/tagspaces) | TagSpaces is an offline, open source, document manager with tagging support | `SelfHost` | **4.6k** |

# Productivity - [Go to top](#table-of-contents)

### Calendar

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Cal](https://github.com/calcom/cal.com) | Scheduling infrastructure for absolutely everyone. | `SelfHost` | **38.7k** |

### Document Modifier

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Documenso](https://github.com/documenso/documenso) | The Open Source DocuSign Alternative. | `SelfHost` `Web (Cloud)` | **11.8k** |
| [DocuSeal](https://github.com/docusealco/docuseal) | Open source DocuSign alternative. Create, fill, and sign digital documents ✍️ | `SelfHost` | **10.8k** |
| [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) `CLI` | OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched | `Cross` | **31.7k** |
| [OpenSign](https://github.com/OpenSignLabs/OpenSign) | 🔥 The free & Open Source DocuSign alternative | `SelfHost` `Web (Cloud)` | **5.4k** |
| [Stirling PDF](https://github.com/Stirling-Tools/Stirling-PDF) | #1 Locally hosted web application that allows you to perform various operations on PDF files | `MacOS` `Windows` `SelfHost` | **69.5k** |

### Finance

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Actual](https://github.com/actualbudget/actual) | A local-first personal finance app | `SelfHost` `Cross` | **23k** |
| [ezBookkeeping](https://github.com/mayswind/ezbookkeeping) | A lightweight, self-hosted personal finance app with a user-friendly interface and powerful bookkeeping features. | `SelfHost` | **2.8k** |
| [Firefly III](https://github.com/firefly-iii/firefly-iii) | Firefly III: a personal finances manager | `SelfHost` | **21.4k** |
| [Ghostfolio](https://github.com/ghostfolio/ghostfolio) | Open Source Wealth Management Software. Angular + NestJS + Prisma + Nx + TypeScript 🤍 | `SelfHost` | **6.9k** |
| [Maybe](https://github.com/maybe-finance/maybe) | The personal finance app for everyone | `SelfHost` | **53.3k** |
| [Midday](https://github.com/midday-ai/midday) | Invoicing, Time tracking, File reconciliation, Storage, Financial Overview & your own Assistant made for Freelancers | `Web (Cloud)` | **12.8k** |
| [Ticker](https://github.com/achannarasappa/ticker) `TUI` | Track stocks, crypto, and derivatives prices and positions in real time from your terminal | `Cross` | **5.6k** |
| [Wallos](https://github.com/ellite/Wallos) | Wallos: Open-Source Personal Subscription Tracker | `SelfHost` | **6.5k** |
| [Wealthfolio](https://github.com/afadil/wealthfolio) | A Beautiful Private and Secure Desktop Investment Tracking Application | `Cross` | **5.6k** |

### Knowledge Base

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Affine](https://github.com/toeverything/AFFiNE) | There can be more than Notion and Miro. AFFiNE(pronounced [ə‘fain]) is a next-gen knowledge base that brings planning, sorting and creating all together. Privacy first, open-source, customizable and ready to use.  | `Cross` | **59.2k** |
| [Anytype](https://github.com/anyproto/anytype-ts) | Official Anytype client for MacOS, Linux, and Windows | `Cross` | **6.4k** |
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) 💰 | Bring projects, wikis, and teams together with AI. AppFlowy is the AI collaborative workspace where you achieve more without losing control of your data. The leading open source Notion alternative. | `Cross` | **66.3k** |
| [FastGPT](https://github.com/labring/FastGPT) | FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration. | `Cross` | **26.2k** |
| [Foam](https://github.com/foambubble/foam) | A personal knowledge management and sharing system for VSCode | `VSCode` | **16.5k** |
| [Freeplane](https://github.com/freeplane/freeplane) | Application for Mind Mapping, Knowledge Management, Project Management. Develop, organize and communicate your ideas and knowledge in the most effective way. | `Cross` | **3.6k** |
| [Logseq](https://github.com/logseq/logseq) | A privacy-first, open-source platform for knowledge management and collaboration. Download link:  http://github.com/logseq/logseq/releases. roadmap: http://trello.com/b/8txSM12G/roadmap | `Cross` | **39.3k** |
| [Outline](https://github.com/outline/outline) | The fastest knowledge base for growing teams. Beautiful, realtime collaborative, feature packed, and markdown compatible. | `Cross` | **35.7k** |
| [Siyuan](https://github.com/siyuan-note/siyuan) | A privacy-first, self-hosted, fully open source personal knowledge management software, written in typescript and golang. | `Cross` | **38.8k** |

### Project Management

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Focalboard](https://github.com/mattermost-community/focalboard) | Focalboard is an open source, self-hosted alternative to Trello, Notion, and Asana. | `Cross` `SelfHost` | **25.4k** |
| [Huly](https://github.com/hcengineering/platform) | Huly — All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion) | `SelfHost` `Web (Cloud)` | **23.6k** |
| [Leantime](https://github.com/Leantime/leantime) | Leantime is a goals focused project management system for non-project managers. Building with ADHD, Autism, and dyslexia in mind. | `SelfHost` | **8.6k** |
| [OpenProject](https://github.com/opf/openproject) | OpenProject is the leading open source project management software. | `SelfHost` | **13.1k** |
| [Plane](https://github.com/makeplane/plane) | 🔥 🔥 🔥 Open Source JIRA, Linear, Monday, and Asana Alternative. Plane helps you track your issues, epics, and cycles the easiest way on the planet. | `SelfHost` `Web (Cloud)` | **39.7k** |
| [Worklenz](https://github.com/Worklenz/worklenz) | All in one project management tool for efficient teams | `Web (Cloud)` `SelfHost` | **2.9k** |

### Task Management

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Planka](https://github.com/plankanban/planka) `CLI+` | PLANKA is the kanban-style project mastering tool for everyone. | `SelfHost` | **10.9k** |
| [Super Productivity](https://github.com/johannesjo/super-productivity) | Super Productivity is an advanced todo list app with integrated Timeboxing and time tracking capabilities. It also comes with integrations for Jira, GitLab, GitHub and Open Project. | `Cross` | **15.9k** |

### Time Management

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [ActivityWatch](https://github.com/ActivityWatch/activitywatch) | The best free and open-source automated time tracker. Cross-platform, extensible, privacy-focused. | `Cross` `Android` | **15.7k** |
| [solidtime](https://github.com/solidtime-io/solidtime) | Modern open-source time-tracking app | `SelfHost` `Web (Cloud)` | **7.5k** |

# Security/Privacy - [Go to top](#table-of-contents)

### AD Blocker

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [AdGuard](https://github.com/AdguardTeam/AdGuardHome) `CLI+` | Network-wide ads & trackers blocking DNS server | `SelfHost` `Chromium` `Firefox` | **30.8k** |
| [Blocky](https://github.com/0xERR0R/blocky) | Fast and lightweight DNS proxy as ad-blocker for local network with many features | `SelfHost` | **5.7k** |
| [Pi-hole](https://github.com/pi-hole/pi-hole) | A black hole for Internet advertisements | `SelfHost` | **54.1k** |

### Antivirus

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [ClamAV](https://github.com/Cisco-Talos/clamav) | ClamAV - Documentation is here: https://docs.clamav.net | `Cross` `SelfHost` | **5.8k** |

### Authentication

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [2FAuth](https://github.com/Bubka/2FAuth) | A Web app to manage your Two-Factor Authentication (2FA) accounts and generate their security codes | `SelfHost` | **3.5k** |
| [Aegis](https://github.com/beemdevelopment/Aegis) | A free, secure and open source app for Android to manage your 2-step verification tokens. | `Android` | **11.3k** |
| [authelia](https://github.com/authelia/authelia) | The Single Sign-On Multi-Factor portal for web apps, now OpenID Certified™ | `SelfHost` | **25.7k** |

### Firewall

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [BunkerWeb](https://github.com/bunkerity/bunkerweb) | 🛡️ Open-source and next-generation Web Application Firewall (WAF) | `SelfHost` | **9.3k** |
| [LuLu](https://github.com/objective-see/LuLu) | LuLu is the free open-source macOS firewall | `MacOS` | **11.5k** |
| [SafeLine](https://github.com/chaitin/SafeLine) | SafeLine is a self-hosted WAF(Web Application Firewall) / reverse proxy to protect your web apps from attacks and exploits. | `SelfHost` | **19k** |

### Password Manager

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Bitwarden](https://github.com/bitwarden/server) `CLI+` | Open source security solutions for individuals, teams, and business organizations. Explore Password Manager, Secrets Manager, and passkey innovations. | `Cross` `Mobile` `Chromium` `Firefox` | **17.4k** |
| [Infiscal](https://github.com/Infisical/infisical) `Manual` `Web UI` | Infisical is the open-source platform for secrets, certificates, and privileged access management. | `Cross` `Web (Cloud)` `SelfHost` | **23.5k** |
| [KeePass](https://github.com/keepassxreboot/keepassxc) | KeePassXC is a cross-platform community-driven port of the Windows application “KeePass Password Safe”. | `Cross` | **24.7k** |
| [LessPass](https://github.com/lesspass/lesspass) `CLI` `CLI+` | :key: stateless open source password manager | `Cross` `Chromium` `Firefox` | **5.9k** |
| [Passbolt](https://github.com/passbolt/passbolt_api) `CLI+` | Passbolt Community Edition (CE) API. The JSON API for the open source password manager for teams! | `Cross` `SelfHost` `Chromium` `Firefox` | **5.4k** |
| [Vaultwarden](https://github.com/dani-garcia/vaultwarden) | Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs | `SelfHost` | **50.5k** |

### VPN

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Algo](https://github.com/trailofbits/algo) `Manual` | Set up a personal VPN in the cloud | `Cross` | **30k** |
| [Amnezia](https://github.com/amnezia-vpn/amnezia-client) `CLI+` | Amnezia VPN Client (Desktop+Mobile) | `Cross` | **8.8k** |
| [EasyTier](https://github.com/EasyTier/EasyTier) `CLI+` | A simple, decentralized mesh VPN with WireGuard support. | `Cross` | **7.9k** |
| [Gluetun](https://github.com/qdm12/gluetun) `CLI` | VPN client in a thin Docker container for multiple VPN providers, written in Go, and using OpenVPN or Wireguard, DNS over TLS, with a few proxy servers built-in. | `SelfHost` | **11.5k** |
| [headscale](https://github.com/juanfont/headscale) `CLI+` | An open source, self-hosted implementation of the Tailscale control server | `SelfHost` | **32.5k** |
| [NetBird](https://github.com/netbirdio/netbird) | Connect your devices into a secure WireGuard®-based overlay network with SSO, MFA and granular access controls. | `Cross` | **19.5k** |
| [Netmaker](https://github.com/gravitl/netmaker) | Netmaker makes networks with WireGuard. Netmaker automates fast, secure, and distributed virtual networks. | `SelfHost` `Web (Cloud)` | **10.9k** |
| [OpenVPN](https://github.com/OpenVPN/openvpn) `CLI` | OpenVPN  is  an open source VPN daemon | `Cross` | **12.7k** |
| [PiVPN](https://github.com/pivpn/pivpn) `Manual` `CLI` | The Simplest VPN installer, designed for Raspberry Pi | `N/A` | **7.8k** |
| [ProtonVPN](https://github.com/ProtonVPN/android-app) `CLI+` | Official ProtonVPN Android app | `Cross` | **3.1k** |
| [Tailscale](https://github.com/tailscale/tailscale) | The easiest, most secure way to use WireGuard and 2FA. | `SelfHost` | **25.8k** |
| [WireGuard Easy](https://github.com/wg-easy/wg-easy) | The easiest way to run WireGuard VPN + Web-based Admin UI. | `SelfHost` | **23.2k** |
| [ZeroTier](https://github.com/zerotier/ZeroTierOne) | A Smart Ethernet Switch for Earth | `Cross` `Mobile` | **16.1k** |

# Server - [Go to top](#table-of-contents)

### Arr

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [autobrr](https://github.com/autobrr/autobrr) | Modern, easy to use download automation for torrents and usenet. | `Cross` `SelfHost` | **2.1k** |
| [Bazarr](https://github.com/morpheus65535/bazarr) | Bazarr is a companion application to Sonarr and Radarr. It manages and downloads subtitles based on your requirements. You define your preferences by TV show or movie and Bazarr takes care of everything for you. | `Cross` `SelfHost` | **3.5k** |
| [Jellyseerr](https://github.com/Fallenbagel/jellyseerr) | Open-source media request and discovery manager for Jellyfin, Plex, and Emby. | `SelfHost` | **7k** |
| [Lidarr](https://github.com/Lidarr/Lidarr) | Looks and smells like Sonarr but made for music. | `Cross` `SelfHost` | **4.7k** |
| [Overseerr](https://github.com/sct/overseerr) | Request management and media discovery tool for the Plex ecosystem | `Windows` `Linux` `SelfHost` | **4.8k** |
| [Prowlarr](https://github.com/Prowlarr/Prowlarr) | Prowlarr is an indexer manager/proxy built on the popular *arr .net/reactjs base stack to integrate with your various PVR apps, supporting management of both Torrent Trackers and Usenet Indexers. | `Cross` `SelfHost` | **5.4k** |
| [Radarr](https://github.com/Radarr/Radarr) | Movie organizer/manager for usenet and torrent users. | `Cross` `SelfHost` | **12.4k** |
| [Sonarr](https://github.com/Sonarr/Sonarr) | Smart PVR for newsgroup and bittorrent users. | `Cross` `SelfHost` | **12.6k** |

### Dashboard

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Cockpit](https://github.com/cockpit-project/cockpit) | Cockpit is a web-based graphical interface for servers. | `Linux` | **12.7k** |
| [dashdot](https://github.com/MauriceNino/dashdot) | A simple, modern server dashboard, primarily used by smaller private servers | `SelfHost` | **3.1k** |
| [Dashy](https://github.com/Lissy93/dashy) | 🚀 A self-hostable personal dashboard built for you. Includes status-checking, widgets, themes, icon packs, a UI editor and tons more! | `SelfHost` | **23k** |
| [Glance](https://github.com/glanceapp/glance) | A self-hosted dashboard that puts all your feeds in one place | `SelfHost` | **29.2k** |
| [Heimdall](https://github.com/linuxserver/Heimdall) | An Application dashboard and launcher | `SelfHost` | **8.7k** |
| [homepage](https://github.com/gethomepage/homepage) | A highly customizable homepage (or startpage / application dashboard) with Docker and service API integrations. | `SelfHost` | **26.5k** |
| [Homer](https://github.com/bastienwirtz/homer) | A very simple static homepage for your server. | `SelfHost` | **10.7k** |

### Home Automation

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Domoticz](https://github.com/domoticz/domoticz) | Open source Home Automation System | `SelfHost` | **3.7k** |
| [ESPHome](https://github.com/esphome/esphome) | ESPHome is a system to control your ESP8266/ESP32 by simple yet powerful configuration files and control them remotely through Home Automation systems. | `SelfHost` | **10.1k** |
| [evcc](https://github.com/evcc-io/evcc) | solar charging ☀️🚘 | `Cross` `SelfHost` | **5.7k** |
| [Gladys](https://github.com/GladysAssistant/Gladys) | A privacy-first, open-source home assistant | `SelfHost` | **2.9k** |
| [Home Assistant](https://github.com/home-assistant/core) | :house_with_garden: Open source home automation that puts local control and privacy first. | `Cross` `SelfHost` | **82.4k** |

### Home Server

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [CapRover](https://github.com/caprover/caprover) | Scalable PaaS (automated Docker+nginx) - aka Heroku on Steroids | `Linux` | **14.6k** |
| [CasaOS](https://github.com/IceWhaleTech/CasaOS) | CasaOS - A simple, easy-to-use, elegant open-source Personal Cloud system. | `Linux` | **32.3k** |
| [Cosmos](https://github.com/azukaar/Cosmos-Server) | ☁️ The Most Secure and Easy Selfhosted Home Server. Take control of your data and privacy without sacrificing security and stability  (Authentication, anti-DDOS, anti-bot) | `SelfHost` | **5.2k** |
| [Runtipi](https://github.com/runtipi/runtipi) | Runtipi is a homeserver for everyone! One command setup, one click installs for your favorites self-hosted apps. ✨ | `SelfHost` | **9k** |
| [Sandstorm](https://github.com/sandstorm-io/sandstorm) | Sandstorm is a self-hostable web productivity suite. It's implemented as a security-hardened web app package manager. - Actively sponsored by our friends at LambdaTest | `SelfHost` | **7k** |

### Media Management

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [AntennaPod](https://github.com/AntennaPod/AntennaPod) | A podcast manager for Android | `Android` | **7.4k** |
| [audiobookshelf](https://github.com/advplyr/audiobookshelf) | Self-hosted audiobook and podcast server | `IOS` `Android` `SelfHost` | **10.6k** |
| [beets](https://github.com/beetbox/beets) `CLI` `Manual` | music library manager and MusicBrainz tagger | `Cross` | **14.1k** |
| [BookLore](https://github.com/booklore-app/booklore) | BookLore: A self-hosted, multi-user digital library with smart shelves, auto metadata, Kobo & KOReader sync, BookDrop imports, OPDS support, and a built-in reader for EPUB, PDF, and comics. | `SelfHost` | **5.6k** |
| [Calibre-Web](https://github.com/janeczku/calibre-web) | :books: Web app for browsing, reading and downloading eBooks stored in a Calibre database | `SelfHost` | **15.8k** |
| [Ente](https://github.com/ente-io/ente) | 🔒 End-to-end encrypted cloud for photos, videos and 2FA secrets. | `Web (Cloud)` | **22.6k** |
| [Immich](https://github.com/immich-app/immich) | High performance self-hosted photo and video management solution. | `SelfHost` | **83.5k** |
| [Jellyfin](https://github.com/jellyfin/jellyfin) | The Free Software Media System - Server Backend & API | `SelfHost` | **45.4k** |
| [Kavita](https://github.com/Kareadita/Kavita) | Kavita is a fast, feature rich, cross platform reading server. Built with the goal of being a full solution for all your reading needs. Setup your own server and share your reading collection with your friends and family. | `SelfHost` | **9.1k** |
| [Kodi](https://github.com/xbmc/xbmc) | Kodi is an award-winning free and open source home theater/media center software and entertainment hub for digital media. With its beautiful interface and powerful skinning engine, it's available for Android, BSD, Linux, macOS, iOS, tvOS and Windows. | `Cross` `SelfHost` | **20k** |
| [LibrePhotos](https://github.com/LibrePhotos/librephotos) | A self-hosted open source photo management service. This is the repository of the backend. | `SelfHost` | **7.8k** |
| [Librum](https://github.com/Librum-Reader/Librum) | The Librum client application | `SelfHost` | **5.2k** |
| [Lychee](https://github.com/LycheeOrg/Lychee) | A great looking and easy-to-use photo-management-system you can run on your server, to manage and share photos. | `SelfHost` | **4k** |
| [Manyfold](https://github.com/manyfold3d/manyfold) | A self-hosted digital asset manager for 3d print files. | `SelfHost` | **1.4k** |
| [Memories](https://github.com/pulsejet/memories) | Fast, modern and advanced photo management suite. Runs as a Nextcloud app. | `SelfHost` | **3.6k** |
| [PhotoPrism](https://github.com/photoprism/photoprism) | AI-Powered Photos App for the Decentralized Web 🌈💎✨ | `SelfHost` | **38.7k** |
| [Piwigo](https://github.com/Piwigo/Piwigo) | Manage your photos with Piwigo, a full featured open source photo gallery application for the web. Star us on Github! More than 200 plugins and themes available. Join us and contribute! | `SelfHost` | **3.6k** |
| [Tautulli](https://github.com/Tautulli/Tautulli) | A Python based monitoring and tracking tool for Plex Media Server. | `Cross` `SelfHost` | **6.2k** |
| [Tube Archivist](https://github.com/tubearchivist/tubearchivist?tab=readme-ov-file#installing) | Your self hosted YouTube media server | `SelfHost` | **7.1k** |

### Server Management

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [1Panel](https://github.com/1Panel-dev/1Panel) | 🔥 1Panel provides an intuitive web interface and MCP Server to manage websites, files, containers, databases, and LLMs on a Linux server. | `SelfHost` | **31.9k** |

### Surveillance

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Frigate](https://github.com/blakeblackshear/frigate) | NVR with realtime local object detection for IP cameras | `SelfHost` | **26.7k** |
| [Scrypted](https://github.com/koush/scrypted) | Scrypted is a high performance video integration and automation platform | `SelfHost` | **5.2k** |
| [Viseron](https://github.com/roflcoopter/viseron) | Self-hosted, local only NVR and AI Computer Vision software.  With features such as object detection, motion detection, face recognition and more, it gives you the power to keep an eye on your home, office or any other place you want to monitor. | `SelfHost` | **2.3k** |
| [ZoneMinder](https://github.com/ZoneMinder/zoneminder) | ZoneMinder is a free, open source Closed-circuit television software application developed for Linux which supports IP, USB and Analog cameras.  | `SelfHost` | **5.7k** |

# STEM - [Go to top](#table-of-contents)

### Autonomy

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Apollo](https://github.com/ApolloAuto/apollo) | An open autonomous driving platform | `SelfHost` | **26.2k** |
| [ArduPilot](https://github.com/ArduPilot/ardupilot) `Manual` | ArduPlane, ArduCopter, ArduRover, ArduSub source | `N/A` | **14k** |
| [Autoware](https://github.com/autowarefoundation/autoware) | Autoware - the world's leading open-source software project for autonomous driving | `SelfHost` | **10.5k** |
| [CARLA](https://github.com/carla-simulator/carla) | Open-source simulator for autonomous driving research. | `Windows` `Linux` | **13.2k** |
| [openpilot](https://github.com/commaai/openpilot) | openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 300+ supported cars. | `Linux` | **58.7k** |
| [PX4 Drone Autopilot](https://github.com/PX4/PX4-Autopilot) | PX4 Autopilot Software | `Cross` | **10.4k** |

### Control

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [MissionPlanner](https://github.com/ArduPilot/MissionPlanner) | Mission Planner Ground Control Station for ArduPilot (c# .net) | `Windows` | **2.1k** |
| [QGroundControl](https://github.com/mavlink/qgroundcontrol) | Cross-platform ground control station for drones (Android, iOS, Mac OS, Linux, Windows) | `Cross` `Mobile` | **4.1k** |
| [WebODM](https://github.com/OpenDroneMap/WebODM) | User-friendly, commercial-grade software for processing aerial imagery. ✈️ | `SelfHost` | **3.4k** |

### Engineering

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [KiCad](https://github.com/KiCad/kicad-source-mirror) | A Cross Platform and Open Source PCB Design Suite | `Cross` | **2.4k** |

### Firmware

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [EdgeTX](https://github.com/EdgeTX/edgetx) | EdgeTX is the cutting edge open source firmware for your R/C radio | `N/A` | **2k** |
| [INAV](https://github.com/iNavFlight/inav) | INAV: Navigation-enabled flight control software | `N/A` | **3.8k** |
| [Meshtastic](https://github.com/meshtastic/firmware) | The official firmware for Meshtastic, an open-source, off-grid mesh communication system. | `N/A` | **6.1k** |

### Robotics

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [OpenArm](https://github.com/enactic/openarm) | A fully open-source humanoid arm for physical AI research and deployment in contact-rich environments. | `Cross` | **1.5k** |
| [Webots](https://github.com/cyberbotics/webots) | Webots Robot Simulator | `Cross` | **3.9k** |
| [XLeRobot](https://github.com/Vector-Wangel/XLeRobot) | XLeRobot: Practical Dual-Arm Mobile Home Robot for $660 | `N/A` | **4k** |

### Rocketry

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [OpenRocket](https://github.com/openrocket/openrocket) | Model-rocketry aerodynamics and trajectory simulation software | `Cross` | **1.6k** |

### Simulation

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [A/B Street](https://github.com/a-b-street/abstreet) | Transportation planning and traffic simulation software for creating cities friendlier to walking, biking, and public transit | `Cross` | **8k** |
| [SUMO](https://github.com/eclipse-sumo/sumo) `Manual` | Eclipse SUMO is an open source, highly portable, microscopic and continuous traffic simulation package designed to handle large networks. It allows for intermodal simulation including pedestrians and comes with a large set of tools for scenario creation. | `Cross` | **3.8k** |

# Terminal - [Go to top](#table-of-contents)

### Prompt

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Liquid Prompt](https://github.com/liquidprompt/liquidprompt) `CLI` | A full-featured & carefully designed adaptive prompt for Bash & Zsh | `Cross` | **4.6k** |
| [Oh My Posh](https://github.com/JanDeDobbeleer/oh-my-posh) `CLI` | The most customisable and low-latency cross platform/shell prompt renderer | `Cross` | **20.5k** |
| [Pure](https://github.com/sindresorhus/pure) `CLI` | Pretty, minimal and fast ZSH prompt | `Cross` | **13.9k** |
| [Spaceship Prompt](https://github.com/spaceship-prompt/spaceship-prompt) `CLI` | 🚀✨ Minimalistic, powerful and extremely customizable Zsh prompt | `Cross` | **20.2k** |
| [starship](https://github.com/starship/starship) `CLI` | ☄🌌️  The minimal, blazing-fast, and infinitely customizable prompt for any shell! | `Cross` | **52k** |

### Shell

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [fish](https://github.com/fish-shell/fish-shell) `CLI` | The user-friendly command line shell. | `Cross` | **31.4k** |
| [Nushell](https://github.com/nushell/nushell) `CLI` | A new type of shell | `Cross` | **37.2k** |
| [xonsh](https://github.com/xonsh/xonsh) `CLI` | :shell: Python-powered shell. Full-featured and cross-platform. | `Cross` | **9k** |

### Terminal Emulator

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Alacritty](https://github.com/alacritty/alacritty) | A cross-platform, OpenGL terminal emulator. | `Cross` | **60.9k** |
| [Ghostty](https://github.com/ghostty-org/ghostty) | 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration. | `Cross` | **37.9k** |
| [kitty](https://github.com/kovidgoyal/kitty) | If you live in the terminal, kitty is made for you! Cross-platform, fast, feature-rich, GPU based. | `Cross` | **29.6k** |
| [Rio](https://github.com/raphamorim/rio) | A hardware-accelerated GPU terminal emulator focusing to run in desktops and browsers. | `Cross` | **6k** |
| [Tabby](https://github.com/Eugeny/tabby) | A terminal for a more modern age | `Cross` | **67k** |
| [Terminal](https://github.com/microsoft/terminal) | The new Windows Terminal and the original Windows console host, all in the same place! | `Windows` | **100.8k** |
| [Waveterm](https://github.com/wavetermdev/waveterm) | An open-source, cross-platform terminal for seamless workflows | `Cross` | **12.8k** |
| [WezTerm](https://github.com/wez/wezterm) | A GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust | `Cross` | **22.4k** |

### Terminal Multiplexer

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [tmux](https://github.com/tmux/tmux) `CLI` | tmux source code | `Cross` | **39.5k** |
| [Zellij](https://github.com/zellij-org/zellij) `CLI` | A terminal workspace with batteries included | `Cross` | **27k** |

### Terminal Utilities

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Atuin](https://github.com/atuinsh/atuin) `CLI` | ✨ Magical shell history | `Cross` | **26.6k** |
| [Atuin Desktop](https://github.com/atuinsh/desktop) | 📖 Runbooks that run  | `Cross` | **2k** |
| [delta](https://github.com/dandavison/delta) `CLI` | A syntax-highlighting pager for git, diff, grep, and blame output | `Cross` | **28k** |
| [eza](https://github.com/eza-community/eza) `CLI` | A modern alternative to ls | `Cross` | **18.3k** |
| [fzf](https://github.com/junegunn/fzf) `CLI` | :cherry_blossom: A command-line fuzzy finder | `Cross` | **74.9k** |
| [McFly](https://github.com/cantino/mcfly) `CLI` | Fly through your shell history. Great Scott! | `Cross` | **7.4k** |
| [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh) `CLI` | 🙃   A delightful community-driven (with 2,400+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (rails, git, macOS, hub, docker, homebrew, node, php, python, etc), 140+ themes to spice up your morning, and an auto-update tool that makes it easy to keep up with the latest updates from the community. | `Cross` | **182.5k** |
| [ShellGPT](https://github.com/TheR1D/shell_gpt) `CLI` | A command-line productivity tool powered by AI large language models like GPT-4, will help you accomplish your tasks faster and more efficiently. | `Cross` | **11.5k** |
| [sshx](https://github.com/ekzhang/sshx) | Fast, collaborative live terminal sharing over the web | `Cross` `Web (Cloud)` | **7.1k** |
| [television](https://github.com/alexpasmantier/television) `TUI` | A fast and hackable fuzzy finder for the terminal. | `Cross` | **3.6k** |
| [Term.Everything](https://github.com/mmulet/term.everything) `CLI` | Run any GUI app in the terminal❗ | `Linux` | **6.8k** |
| [zoxide](https://github.com/ajeetdsouza/zoxide) `CLI` | A smarter cd command. Supports all major shells. | `Cross` | **30.9k** |
| [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions) `CLI` | Fish-like autosuggestions for zsh | `Cross` | **34.1k** |

# Text - [Go to top](#table-of-contents)

### Document Editor

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Etherpad](https://github.com/ether/etherpad-lite) | Etherpad: A modern really-real-time collaborative document editor. | `SelfHost` `Web (Cloud)` | **17.9k** |

### Markdown Editor

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [CodiMD](https://github.com/hackmdio/codimd) | CodiMD - Realtime collaborative markdown notes on all platforms. | `SelfHost` | **9.9k** |
| [HedgeDoc](https://github.com/hedgedoc/hedgedoc) | HedgeDoc - Ideas grow better together | `SelfHost` | **6.6k** |
| [Zettlr](https://github.com/Zettlr/Zettlr) | Your One-Stop Publication Workbench | `Cross` | **12.1k** |

### Note Taking

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Better Notes](https://github.com/windingwind/zotero-better-notes) | Everything about note management. All in Zotero. | `plugin` | **7k** |
| [Blinko](https://github.com/blinko-space/blinko) | An open-source, self-hosted personal AI note tool prioritizing privacy, built using TypeScript . | `SelfHost` | **6.9k** |
| [flatnotes](https://github.com/dullage/flatnotes) | A self-hosted, database-less note taking web app that utilises a flat folder of markdown files for storage. | `SelfHost` | **2.5k** |
| [Joplin](https://github.com/laurent22/joplin) | Joplin - the privacy-focused note taking app with sync capabilities for Windows, macOS, Linux, Android and iOS. | `Cross` | **52k** |
| [jrnl](https://github.com/jrnl-org/jrnl) `CLI` | Collect your thoughts and notes without leaving the command line. | `Cross` | **7k** |
| [Memos](https://github.com/usememos/memos) | An open-source, self-hosted note-taking service. Your thoughts, your data, your control — no tracking, no ads, no subscription fees. | `SelfHost` | **45.7k** |
| [nb](https://github.com/xwmx/nb) `CLI` | CLI and local web plain text note‑taking, bookmarking, and archiving with linking, tagging, filtering, search, Git versioning & syncing, Pandoc conversion, + more, in a single portable script. | `Cross` | **7.8k** |
| [Notes](https://github.com/nuttyartist/notes) | Fast and beautiful note-taking app written in C++. Write down your thoughts. | `Cross` | **4.1k** |
| [Notesnook](https://github.com/streetwriters/notesnook) | A fully open source & end-to-end encrypted note taking alternative to Evernote. | `Cross` | **13.1k** |
| [Reor](https://github.com/reorproject/reor) | Private & local AI personal knowledge management app for high entropy people. | `Cross` | **8.4k** |
| [Rnote](https://github.com/flxzt/rnote) | Sketch and take handwritten notes. | `Cross` | **10.5k** |
| [SilverBullet](https://github.com/silverbulletmd/silverbullet) | An open source personal productivity platform built on Markdown, turbo charged with the scripting power of Lua | `Cross` | **4.1k** |
| [Simplenote](https://github.com/Automattic/simplenote-electron) | Simplenote for Web, Windows, and Linux | `Cross` `IOS` `Android` | **5.1k** |
| [Standard Notes](https://github.com/standardnotes/app) | Think fearlessly with end-to-end encrypted notes and files. For issues, visit https://standardnotes.com/forum or https://standardnotes.com/help. | `Cross` `IOS` `Android` | **6.1k** |
| [Trilium Notes](https://github.com/TriliumNext/Trilium) | Build your personal knowledge base with Trilium Notes | `Cross` | **32.7k** |
| [VNote](https://github.com/vnotex/vnote) | A pleasant note-taking platform in native C++. | `Cross` | **12.7k** |
| [Zotero](https://github.com/zotero/zotero) | Zotero is a free, easy-to-use tool to help you collect, organize, annotate, cite, and share your research sources. | `Cross` `IOS` `Chromium` `Firefox` | **12.8k** |

### Office Suite

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [CryptPad](https://github.com/cryptpad/cryptpad) | Collaborative office suite, end-to-end encrypted and open-source. | `SelfHost` | **7k** |
| [LibreOffice](https://github.com/LibreOffice/core) | Read-only LibreOffice core repo - no pull request (use gerrit instead https://gerrit.libreoffice.org/) - don't download zip, use https://dev-www.libreoffice.org/bundles/  instead | `Cross` | **3.4k** |
| [OnlyOffice](https://github.com/ONLYOFFICE/DesktopEditors) | Open-source office suite pack that comprises all the tools you need to work with documents, spreadsheets, presentations, PDFs, and PDF forms on Windows, Linux, and macOS | `Cross` | **4k** |

### Proofreading

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Harper](https://github.com/automattic/harper) | Offline, privacy-first grammar checker. Fast, open-source, Rust-powered | `VSCode` | **8.5k** |
| [LanguageTool](https://github.com/languagetool-org/languagetool) | Style and Grammar Checker for 25+ Languages | `SelfHost` `Web (Cloud)` | **13.7k** |
| [WritingTools](https://github.com/theJayTea/WritingTools) | The world's smartest system-wide grammar assistant; a better version of the Apple Intelligence Writing Tools. Works on Windows, Linux, & macOS, with the free Gemini API, local LLMs, & more. | `Cross` | **2k** |

### Spreadsheet

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Grist](https://github.com/gristlabs/grist-core) | Grist is the evolution of spreadsheets. | `SelfHost` `Web (Cloud)` | **10k** |

### Text Editor

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Amp](https://github.com/jmacdonald/amp) `TUI` | A complete text editor for your terminal. | `MacOS` `Linux` | **4k** |
| [CotEditor](https://github.com/coteditor/CotEditor) | Lightweight Plain-Text Editor for macOS | `MacOS` | **7.3k** |
| [CudaText](https://github.com/Alexey-T/CudaText) | Cross-platform text editor, written in Free Pascal | `Linux` | **2.8k** |
| [Emacs](https://github.com/emacs-mirror/emacs) | Mirror of GNU Emacs | `Cross` | **4.8k** |
| [Kakoune](https://github.com/mawww/kakoune) `CLI` | mawww's experiment for a better code editor | `Cross` | **10.6k** |
| [Lite XL](https://github.com/lite-xl/lite-xl) | A lightweight text editor written in Lua | `Cross` | **5.8k** |
| [Micro](https://github.com/zyedidia/micro) `CLI` | A modern and intuitive terminal-based text editor | `Cross` | **27.2k** |
| [NotepadNext](https://github.com/dail8859/NotepadNext) | A cross-platform, reimplementation of Notepad++ | `Cross` | **12.6k** |
| [Notepads](https://github.com/0x7c13/Notepads) | A modern, lightweight text editor with a minimalist design. | `Windows` | **9.7k** |
| [Overleaf](https://github.com/overleaf/overleaf) | A web-based collaborative LaTeX editor | `SelfHost` | **16.8k** |
| [Quill](https://github.com/slab/quill) | Quill is a modern WYSIWYG editor built for compatibility and extensibility | `Web (Cloud)` | **46.4k** |

### Wiki

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [BookStack](https://github.com/BookStackApp/BookStack) | A platform to create documentation/wiki content built with PHP & Laravel | `SelfHost` | **17.6k** |
| [DevDocs](https://github.com/freeCodeCamp/devdocs) | API Documentation Browser | `SelfHost` | **37.8k** |
| [Docmost](https://github.com/docmost/docmost) 💰 | Docmost is an open-source collaborative wiki and documentation software. It is an open-source alternative to Confluence and Notion. | `SelfHost` `Web (Cloud)` | **17.8k** |
| [MediaWiki](https://github.com/wikimedia/mediawiki) | 🌻 The collaborative editing software that runs Wikipedia. Mirror from https://gerrit.wikimedia.org/g/mediawiki/core. See https://mediawiki.org/wiki/Developer_access for contributing. | `SelfHost` | **4.8k** |
| [Wiki.js](https://github.com/requarks/wiki) | Wiki.js - A modern and powerful wiki app built on Node.js | `SelfHost` | **27.3k** |

# Utilities - [Go to top](#table-of-contents)

### Automation

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Ansible](https://github.com/ansible/ansible) `CLI+` | Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy and maintain. Automate everything from code deployment to network configuration to cloud management, in a language that approaches plain English, using SSH, with no agents to install on remote systems. https://docs.ansible.com. | `Cross` | **66.9k** |
| [Cronicle](https://github.com/jhuckaby/Cronicle) `CLI+` | A simple, distributed task scheduler and runner with a web based UI. | `Cross` `SelfHost` | **5.2k** |
| [Hammerspoon](https://github.com/Hammerspoon/hammerspoon) | Staggeringly powerful macOS desktop automation with Lua | `MacOS` | **13.9k** |
| [Healthchecks](https://github.com/healthchecks/healthchecks) | Open-source cron job and background task monitoring service, written in Python & Django | `SelfHost` `Web (Cloud)` | **9.6k** |
| [Keyboard Cowboy 3](https://github.com/zenangst/KeyboardCowboy) | :keyboard: The missing keyboard shortcut utility for macOS | `MacOS` | **1.9k** |
| [n8n](https://github.com/n8n-io/n8n) | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. | `Web (Cloud)` `SelfHost` | **154.3k** |
| [Script Kit](https://github.com/johnlindquist/kit) | Script Kit. Automate Anything. | `Cross` | **4.1k** |
| [Semaphore](https://github.com/semaphoreui/semaphore) | Modern UI and powerful API for Ansible, Terraform/OpenTofu/Terragrunt, PowerShell and other DevOps tools. | `Cross` | **12.7k** |

### Cleaner

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [BleachBit](https://github.com/bleachbit/bleachbit) | BleachBit system cleaner for Windows and Linux | `Windows` `Linux` | **3.9k** |
| [Bulk Crap Uninstaller](https://github.com/Klocman/Bulk-Crap-Uninstaller) | Remove large amounts of unwanted applications quickly. | `Windows` | **16.3k** |
| [Pearcleaner](https://github.com/alienator88/Pearcleaner) | A free, source-available and fair-code licensed mac app cleaner | `MacOS` | **9.4k** |
| [SD Maid SE](https://github.com/d4rken-org/sdmaid-se) | SD Maid 2/SE is Android's most thorough cleaning tool. | `Android` | **5.5k** |

### Clipboard Manager

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Clipboard](https://github.com/Slackadays/Clipboard) | 😎🏖️🐬 Your new, 𝙧𝙞𝙙𝙤𝙣𝙠𝙪𝙡𝙞𝙘𝙞𝙤𝙪𝙨𝙡𝙮 smart clipboard manager | `Cross` | **5.5k** |
| [CopyQ](https://github.com/hluk/CopyQ) | Clipboard manager with advanced features | `Cross` | **10.7k** |
| [Maccy](https://github.com/p0deje/Maccy) | Lightweight clipboard manager for macOS | `MacOS` | **17.4k** |

### Container Management

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [KDash](https://github.com/kdash-rs/kdash) `TUI` | A simple and fast dashboard for Kubernetes | `Cross` | **2.4k** |
| [KubeSphere](https://github.com/kubesphere/kubesphere) | The container platform tailored for Kubernetes multi-cloud, datacenter, and edge management ⎈ 🖥 ☁️ | `SelfHost` | **16.7k** |
| [lazydocker](https://github.com/jesseduffield/lazydocker) `TUI` | The lazier way to manage everything docker | `Cross` | **47.4k** |
| [Podman Desktop](https://github.com/podman-desktop/podman-desktop) | Podman Desktop is the best free and open source tool to work with Containers and Kubernetes for developers. Get an intuitive and user-friendly interface to effortlessly build, manage, and deploy containers and Kubernetes — all from your desktop. | `Cross` | **6.9k** |
| [Portainer](https://github.com/portainer/portainer) | Making Docker and Kubernetes management easy. | `SelfHost` | **35.1k** |
| [Rancher Desktop](https://github.com/rancher-sandbox/rancher-desktop) | Container Management and Kubernetes on the Desktop | `Cross` | **6.8k** |
| [WSL Manager](https://github.com/bostrot/wsl2-distro-manager) | A GUI to quickly manage your WSL2 instances | `Windows` | **2.6k** |

### Containers

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Argo CD](https://github.com/argoproj/argo-cd) | Declarative Continuous Deployment for Kubernetes | `SelfHost` | **21.1k** |
| [Colima](https://github.com/abiosoft/colima) `CLI` | Container runtimes on macOS (and Linux) with minimal setup | `Cross` | **25.3k** |
| [container](https://github.com/apple/container) | A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is written in Swift, and optimized for Apple silicon.  | `MacOS` | **22k** |
| [Dockge](https://github.com/louislam/dockge) | A fancy, easy-to-use and reactive self-hosted docker compose.yaml stack-oriented manager | `Cross` | **20.1k** |
| [Finch](https://github.com/runfinch/finch) `CLI` | The Finch CLI is an open source client for container development | `Cross` | **3.9k** |
| [WSL](https://github.com/microsoft/WSL) | Windows Subsystem for Linux | `Windows` | **30.3k** |

### Dotfiles Manager

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [chezmoi](https://github.com/twpayne/chezmoi) | Manage your dotfiles across multiple diverse machines, securely. | `Cross` | **16.5k** |
| [yadm](https://github.com/yadm-dev/yadm) `CLI` | Yet Another Dotfiles Manager | `Cross` | **6k** |

### File Manager

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Broot](https://github.com/Canop/broot) `TUI` | A new way to see and navigate directory trees : https://dystroy.org/broot | `Cross` | **12.1k** |
| [Electerm](https://github.com/electerm/electerm) | 📻Terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC client(linux, mac, win) | `Cross` | **13.2k** |
| [File Browser](https://github.com/filebrowser/filebrowser) | 📂 Web File Browser | `SelfHost` | **31.8k** |
| [FileGator](https://github.com/filegator/filegator) | Powerful Multi-User File Manager | `SelfHost` | **2.8k** |
| [Files](https://github.com/files-community/Files) | A modern file manager that helps users organize their files and folders. | `Windows` | **40k** |
| [Filestash](https://github.com/mickael-kerjean/filestash) | :file_folder: The Dropbox like web client for SFTP, S3, FTP, WebDAV, Git, Minio, LDAP, CalDAV, CardDAV, Mysql, Backblaze, ... | `SelfHost` | **13k** |
| [If](https://github.com/gokcehan/lf) `CLI` | Terminal file manager | `Cross` | **8.7k** |
| [joshuto](https://github.com/kamiyaa/joshuto) `TUI` | ranger-like terminal file manager written in Rust | `Cross` | **3.6k** |
| [nnn](https://github.com/jarun/nnn) `CLI` | n³ The unorthodox terminal file manager | `Linux` | **20.8k** |
| [Ranger](https://github.com/ranger/ranger) `CLI` | A VIM-inspired filemanager for the console | `Cross` | **16.6k** |
| [Spacedrive](https://github.com/spacedriveapp/spacedrive) 🛑 | Spacedrive is an open source cross-platform file explorer, powered by a virtual distributed filesystem written in Rust. | `Cross` | **35.5k** |
| [Superfile](https://github.com/yorukot/superfile) | Pretty fancy and modern terminal file manager | `Cross` | **15.7k** |
| [xplr](https://github.com/sayanarijit/xplr) `TUI` | A hackable, minimal, fast TUI file explorer | `Cross` | **4.6k** |
| [Yazi](https://github.com/sxyazi/yazi) `TUI` | 💥 Blazing fast terminal file manager written in Rust, based on async I/O. | `Cross` | **29.4k** |

### File Sharing

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Flying Carpet](https://github.com/spieglt/FlyingCarpet) | Cross-platform AirDrop. File transfer between Android, iOS, Linux, macOS, and Windows over ad hoc WiFi. No network infrastructure required, just two devices with WiFi chips (and optionally Bluetooth) in close range. | `Cross` `Mobile` | **4.7k** |
| [IPFS Desktop](https://github.com/ipfs/ipfs-desktop) | An unobtrusive and user-friendly desktop application for IPFS on Windows, Mac and Linux.  | `Cross` | **6.4k** |
| [LocalSend](https://github.com/localsend/localsend) `CLI+` | An open-source cross-platform alternative to AirDrop | `Cross` | **69.9k** |
| [OnionShare](https://github.com/onionshare/onionshare) | Securely and anonymously share files, host websites, and chat with friends using the Tor network | `Cross` | **6.7k** |
| [PairDrop](https://github.com/schlagmichdoch/PairDrop) | PairDrop: Transfer Files Cross-Platform. No Setup, No Signup. | `Web (Cloud)` | **9.1k** |
| [zipline](https://github.com/diced/zipline) | A ShareX/file upload server that is easy to use, packed with features, and with an easy setup! | `SelfHost` | **2.6k** |

### Keyboard Manager

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Kanata](https://github.com/jtroo/kanata) | Improve keyboard comfort and usability with advanced customization | `Cross` | **6.1k** |
| [Karabiner-Elements](https://github.com/pqrs-org/Karabiner-Elements) | Karabiner-Elements is a powerful tool for customizing keyboards on macOS | `MacOS` | **20.9k** |
| [Kmonad](https://github.com/kmonad/kmonad) | An advanced keyboard manager | `Cross` | **4.8k** |

### Launcher

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Albert](https://github.com/albertlauncher/albert) | A fast and flexible keyboard launcher | `Cross` | **7.7k** |
| [Flow Launcher](https://github.com/Flow-Launcher/Flow.Launcher) | :mag: Quick file search & app launcher for Windows with community-made plugins | `Windows` | **11.7k** |
| [Kando](https://github.com/kando-menu/kando) | 🌸 Do things with utmost efficiency. | `Cross` | **5.2k** |
| [kunkun](https://github.com/kunkunsh/kunkun) | An open source, cross-platform, extensible app launcher. | `Cross` | **1.2k** |
| [Leader Key](https://github.com/mikker/LeaderKey.app) | The *faster than your launcher* launcher | `MacOS` | **1.8k** |
| [LeaderKey](https://github.com/mikker/LeaderKey.app) | The *faster than your launcher* launcher | `MacOS` | **1.8k** |
| [Olauncher](https://github.com/tanujnotes/Olauncher) | Minimal AF Launcher for Android. Reduce your screen time. Daily wallpapers. | `Android` | **3k** |
| [Rofi](https://github.com/davatorium/rofi) `Manual` | Rofi: A window switcher, application launcher and dmenu replacement | `Cross` | **15.3k** |
| [Sol](https://github.com/ospfranco/sol) | MacOS launcher & command palette | `MacOS` | **2.5k** |
| [Ueli](https://github.com/oliverschwendener/ueli) | Cross-Platform Keystroke Launcher | `Cross` | **4.2k** |
| [Ulauncher](https://github.com/Ulauncher/Ulauncher) | Feature rich application Launcher for Linux | `Linux` | **4.2k** |
| [Vicinae](https://github.com/vicinaehq/vicinae) | A focused launcher for your desktop — native, fast, extensible | `Linux` | **3.8k** |
| [Wox](https://github.com/Wox-launcher/Wox) | A cross-platform launcher that simply works | `Cross` | **26.3k** |

### Package Manager

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Choco](https://github.com/chocolatey/choco) | Chocolatey - the package manager for Windows | `Windows` | **11.1k** |
| [Homebrew](https://github.com/Homebrew/brew) `CLI` | 🍺 The missing package manager for macOS (or Linux) | `MacOS` `Linux` | **45.3k** |
| [Nix](https://github.com/NixOS/nix) | Nix, the purely functional package manager | `Cross` | **15.4k** |
| [Scoop](https://github.com/ScoopInstaller/Scoop) `CLI` `Manual` | A command-line installer for Windows. | `Windows` | **23.1k** |
| [Spack](https://github.com/spack/spack) | A flexible package manager that supports multiple versions, configurations, platforms, and compilers. | `Cross` | **4.8k** |
| [WinGet](https://github.com/microsoft/winget-cli) `CLI` | WinGet is the Windows Package Manager. This project includes a CLI (Command Line Interface), PowerShell modules, and a COM (Component Object Model) API (Application Programming Interface). | `Windows` | **25k** |

### Remote Desktop

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [RustDesk](https://github.com/rustdesk/rustdesk) | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. | `Cross` | **102k** |

### System

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [auto-cpufreq](https://github.com/AdnanHodzic/auto-cpufreq) | Automatic CPU speed & power optimizer for Linux | `Linux` | **6.9k** |
| [Background Music](https://github.com/kyleneideck/BackgroundMusic) | Background Music, a macOS audio utility: automatically pause your music, set individual apps' volumes and record system audio. | `MacOS` | **18.1k** |

### System Monitoring

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [bottom](https://github.com/ClementTsang/bottom) `CLI` | Yet another cross-platform graphical process/system monitor. | `Cross` | **12.1k** |
| [Btop](https://github.com/aristocratos/btop) `TUI` | A monitor of resources | `Cross` | **27.8k** |
| [Glances](https://github.com/nicolargo/glances) `TUI` `Manual` | Glances an Eye on your system. A top/htop alternative for GNU/Linux, BSD, Mac OS and Windows operating systems. | `Cross` `SelfHost` | **30.5k** |
| [htop](https://github.com/htop-dev/htop) | htop - an interactive process viewer | `MacOS` `Linux` | **7.5k** |
| [LibreHardwareMonitor](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor) | Libre Hardware Monitor is free software that can monitor the temperature sensors, fan speeds, voltages, load and clock speeds of your computer. | `Windows` | **7.4k** |
| [NeoHtop](https://github.com/Abdenasser/neohtop) | 💪🏻 Blazing-fast system monitoring for your desktop (built with Rust, Tauri & Svelte) | `Cross` | **8.5k** |
| [nvitop](https://github.com/XuehaiPan/nvitop) `Manual` | An interactive NVIDIA-GPU process viewer and beyond, the one-stop solution for GPU process management. | `Cross` | **6.3k** |
| [NVTOP](https://github.com/Syllo/nvtop) `TUI` `Manual` | GPU & Accelerator process monitoring for AMD, Apple, Huawei, Intel, NVIDIA and Qualcomm | `Cross` | **9.8k** |
| [Stats](https://github.com/exelban/stats) | macOS system monitor in your menu bar | `MacOS` | **34.6k** |
| [System Informer](https://github.com/winsiderss/systeminformer) | A free, powerful, multi-purpose tool that helps you monitor system resources, debug software and detect malware. Brought to you by Winsider Seminars & Solutions, Inc. @ http://www.windows-internals.com | `Windows` | **13k** |
| [Vitals](https://github.com/corecoding/Vitals) | A glimpse into your computer's temperature, voltage, fan speed, memory usage and CPU load. | `Linux` | **1.8k** |

### Tools

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [balenaEtcher](https://github.com/balena-io/etcher) | Flash OS images to SD cards & USB drives, safely and easily. | `Cross` | **32.5k** |
| [ConvertX](https://github.com/C4illin/ConvertX) | 💾 Self-hosted online file converter. Supports 1000+ formats ⚙️ | `SelfHost` | **9.4k** |
| [Czkawka](https://github.com/qarmin/czkawka) | Multi functional app to find duplicates, empty folders, similar images etc. | `Windows` `Linux` | **26.9k** |
| [espanso](https://github.com/espanso/espanso) | A Privacy-first, Cross-platform Text Expander written in Rust | `Cross` | **12.4k** |
| [fd](https://github.com/sharkdp/fd) `CLI` | A simple, fast and user-friendly alternative to 'find' | `Cross` | **40.4k** |
| [File Converter](https://github.com/Tichau/FileConverter) | File Converter is a very simple tool which allows you to convert and compress files using the context menu in windows explorer. | `Windows` | **12.6k** |
| [fswatch](https://github.com/emcrisostomo/fswatch) `CLI` | A cross-platform file change monitor with multiple backends: Apple macOS File System Events, *BSD kqueue, Solaris/Illumos File Events Notification, Linux inotify, Microsoft Windows and a stat()-based backend. | `Cross` | **5.4k** |
| [inshellisense](https://github.com/microsoft/inshellisense) `CLI` | IDE style command line auto complete | `Cross` | **9.5k** |
| [MonitorControl](https://github.com/MonitorControl/MonitorControl) | 🖥 Control your display's brightness & volume on your Mac as if it was a native Apple Display. Use Apple Keyboard keys or custom shortcuts. Shows the native macOS OSDs. | `MacOS` | **31.6k** |
| [OpenRGB](https://github.com/CalcProgrammer1/OpenRGB) | Open source RGB lighting control that doesn't depend on manufacturer software. Supports Windows, Linux, MacOS.  Mirror of https://gitlab.com/CalcProgrammer1/OpenRGB.  Releases can be found on GitLab. | `Cross` | **3.6k** |
| [Pandoc](https://github.com/jgm/pandoc) | Universal markup converter | `Cross` | **40k** |
| [rga](https://github.com/phiresky/ripgrep-all) `CLI` | rga: ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, etc. | `Cross` | **9.2k** |
| [skim](https://github.com/skim-rs/skim) `TUI` | Fuzzy Finder in rust! | `Cross` | **6.1k** |

### Transcription

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Handy](https://github.com/cjpais/Handy) | A free, open source, and extensible speech-to-text application that works completely offline. | `MacOS` | **5.8k** |
| [Hyprnote](https://github.com/fastrepl/hyprnote) | Local-first AI Notepad for Private Meetings | `Cross` | **6.5k** |
| [WhisperLiveKit](https://github.com/QuentinFuxa/WhisperLiveKit) `Manual` | Simultaneous speech-to-text model | `SelfHost` | **8.3k** |

### Version Manager

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [asdf](https://github.com/asdf-vm/asdf) `CLI` | Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more | `Cross` | **24.6k** |
| [mise](https://github.com/jdx/mise) `CLI` | dev tools, env vars, task runner | `Cross` | **21.2k** |
| [nvm](https://github.com/nvm-sh/nvm) `CLI` | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions | `Cross` | **88.9k** |
| [pyenv](https://github.com/pyenv/pyenv) `CLI` | Simple Python version management | `Cross` | **43.6k** |
| [rbenv](https://github.com/rbenv/rbenv) `CLI` | Manage your app's Ruby environment | `Cross` | **16.6k** |
| [vfox](https://github.com/version-fox/vfox) `CLI` | A cross-platform and extendable version manager with support for Java, Node.js, Golang, Python, Flutter, .NET & more | `Cross` | **3.6k** |
| [XcodesApp](https://github.com/XcodesOrg/XcodesApp) | The easiest way to install and switch between multiple versions of Xcode - with a mouse click.  | `MacOS` | **8.1k** |

### Virtual Machine

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Lima](https://github.com/lima-vm/lima) | Linux virtual machines, with a focus on running containers | `MacOS` `Linux` | **18.3k** |
| [Quickemu](https://github.com/quickemu-project/quickemu) | Quickly create and run optimised Windows, macOS and Linux virtual machines | `MacOS` `Linux` | **12.8k** |
| [UTM](https://github.com/utmapp/UTM) | Virtual machines for iOS and macOS | `MacOS` | **31.4k** |
| [VirtualBuddy](https://github.com/insidegui/VirtualBuddy) | Virtualize macOS 12 and later on Apple Silicon, VirtualBuddy is a virtual machine GUI for macOS M1, M2, M3, M4 | `MacOS` | **6.9k** |

### Window Management

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [AeroSpace](https://github.com/nikitabobko/AeroSpace) | AeroSpace is an i3-like tiling window manager for macOS | `MacOS` | **16.6k** |
| [Amethyst](https://github.com/ianyh/Amethyst) | Automatic tiling window manager for macOS à la xmonad. | `MacOS` | **15.8k** |
| [GlazeWM](https://github.com/glzr-io/glazewm) | GlazeWM is a tiling window manager for Windows inspired by i3wm. | `Windows` | **10.4k** |
| [i3](https://github.com/i3/i3) | A tiling window manager for X11 | `Linux` | **10.2k** |
| [komorebi](https://github.com/LGUG2Z/komorebi) | A tiling window manager for Windows 🍉 | `Windows` | **13.2k** |
| [LeftWM](https://github.com/leftwm/leftwm) | A tiling window manager for Adventurers | `Linux` | **3k** |
| [Loop](https://github.com/MrKai77/Loop) | Window management made elegant. | `MacOS` | **9.4k** |
| [niri](https://github.com/YaLTeR/niri) | A scrollable-tiling Wayland compositor. | `Linux` | **14.4k** |
| [PaperWM](https://github.com/paperwm/PaperWM) | Tiled scrollable window management for GNOME Shell | `Linux` | **3.8k** |
| [Phoenix](https://github.com/kasper/phoenix) | A lightweight macOS window and app manager scriptable with JavaScript | `MacOS` | **4.5k** |
| [Rectangle](https://github.com/rxhanson/Rectangle) | Move and resize windows on macOS with keyboard shortcuts and snap areas | `MacOS` | **27.8k** |
| [yabai](https://github.com/koekeishiya/yabai) | A tiling window manager for macOS based on binary space partitioning | `MacOS` | **27.4k** |

# Other - [Go to top](#table-of-contents)

### Other

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [EOS](https://github.com/Akkudoktor-EOS/EOS) `Manual` | This repository features an Energy Optimization System (EOS) that optimizes energy distribution, usage for batteries, heat pumps& household devices. It includes predictive models for electricity prices (planned), load forecasting& dynamic optimization to maximize energy efficiency & minimize costs. Founder Dr. Andreas Schmitz (YouTube @akkudoktor) | `Cross` `SelfHost` | **1.5k** |
| [Grocy](https://github.com/grocy/grocy) | ERP beyond your fridge - Grocy is a web-based self-hosted groceries & household management solution for your home | `Windows` `SelfHost` | **8.3k** |
| [ImHex](https://github.com/WerWolv/ImHex) | 🔍 A Hex Editor for Reverse Engineers, Programmers and people who value their retinas when working at 3 AM. | `Cross` | **51k** |
| [Klipper](https://github.com/Klipper3d/klipper) | Klipper is a 3d-printer firmware | `N/A` | **11k** |
| [Mealie](https://github.com/mealie-recipes/mealie) | Mealie is a self hosted recipe manager and meal planner with a RestAPI backend and a reactive frontend application built in Vue for a pleasant user experience for the whole family. Easily add recipes into your database by providing the url and mealie will automatically import the relevant data or add a family recipe with the UI editor | `SelfHost` | **10.5k** |
| [Ryot](https://github.com/IgnisDa/ryot) | Roll your own tracker! | `Web (Cloud)` `SelfHost` `Chromium` `Firefox` | **2.8k** |
| [TeslaMate](https://github.com/teslamate-org/teslamate) | A self-hosted data logger for your Tesla  🚘 [main maintainer=@JakobLichterfeld] | `SelfHost` | **7.2k** |

### Uncategorized

| Name | Description | Platform(s) | Stars |
| --- | --- | --- | --- |
| [Anki](https://github.com/ankitects/anki) | Anki is a smart spaced repetition flashcard program | `Windows` `MacOS` | **24.5k** |
| [Anx Reader](https://github.com/Anxcye/anx-reader) | Featuring powerful AI capabilities and supporting various e-book formats, it makes reading smarter and more focused.  | `Windows` `MacOS` `Mobile` | **6.2k** |
| [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) | 🗃 Open source self-hosted web archiving. Takes URLs/browser history/bookmarks/Pocket/Pinboard/etc., saves HTML, JS, PDFs, media, and more... | `SelfHost` | **25.5k** |
| [Dawarich](https://github.com/Freika/dawarich) | Self-hostable alternative to Google Timeline (Google Location History) | `SelfHost` | **7.2k** |
| [HomeBox](https://github.com/sysadminsmedia/homebox) | A continuation of HomeBox the inventory and organization system built for the Home User | `SelfHost` | **4k** |
| [KitchenOwl](https://github.com/TomBursch/kitchenowl) | KitchenOwl is a self-hosted grocery list and recipe manager. The backend is made with Flask and the frontend with Flutter. Easily add items to your shopping list before you go shopping. You can also create recipes and add items based on what you want to cook. | `Cross` `Mobile` | **2.8k** |
| [KOReader](https://github.com/koreader/koreader) | An ebook reader application supporting PDF, DjVu, EPUB, FB2 and many more formats, running on Cervantes, Kindle, Kobo, PocketBook and Android devices | `Android` | **24k** |
| [Label Studio](https://github.com/HumanSignal/label-studio) | Label Studio is a multi-type data labeling and annotation tool with standardized output format | `SelfHost` | **25.3k** |
| [Pangolin](https://github.com/fosrl/pangolin) | Identity-based, multi-site remote access platform using WireGuard® | `SelfHost` | **16k** |
| [ProtonUp-Qt](https://github.com/DavidoTek/ProtonUp-Qt) | Install and manage GE-Proton, Luxtorpeda & more for Steam and Wine-GE & more for Lutris with this graphical user interface. | `Linux` | **1.6k** |
| [scrcpy](https://github.com/Genymobile/scrcpy) | Display and control your Android device | `Cross` | **130.7k** |
| [Seelen UI](https://github.com/eythaann/Seelen-UI) | The Fully Customizable Desktop Environment for Windows 10/11. | `Windows` | **14.4k** |
| [Vibe](https://github.com/thewh1teagle/vibe) | Transcribe on your own! | `Cross` | **4.5k** |
| [vim-plug](https://github.com/junegunn/vim-plug) | :hibiscus: Minimalist Vim Plugin Manager | `N/A` | **35.4k** |
| [XPipe](https://github.com/xpipe-io/xpipe) | Access your entire server infrastructure from your local desktop | `Cross` | **11.9k** |



## Honorable Mentions of Closed-Source Software
Some proprietary software just deserve recognition.
- [Davinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) - Professional Editing, Color, Effects and Audio Post!
- [Obsidian](https://obsidian.md/) - The free and flexible app for your private thoughts. 
- [LM Studio](https://lmstudio.ai/) - Discover, download, and run local LLMs
- [JetBrains](https://www.jetbrains.com/) - A rich suite of tools that provide an exceptional developer experience
- [Raycast](https://www.raycast.com/) - A collection of powerful productivity tools all within an extendable launcher.

## Removed Projects
Projects that were once on this list but removed - usually due to abandonement or going closed source. 

<details>
  <summary><b>Archive</b></summary> <br />
  
  - [eqMac](https://github.com/bitgapp/eqMac) - `Closed source`
  - [Hyper](https://github.com/vercel/hyper) - `Abandoned`
  - [DiffusionBee](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui) - `Closed source`
  - [Lunarvim](https://github.com/LunarVim/LunarVim) - `Abandoned`
  - [Motrix](https://github.com/agalwood/Motrix) - `Abandoned`
  - [StableSwarmUI](https://github.com/Stability-AI/StableSwarmUI) - `Abandoned`
  - [Trilium](https://github.com/zadam/trilium) - `Abandoned`
  - [Whisky](https://github.com/Whisky-App/Whisky) - `Abandoned`
  - [SpaceVim](https://github.com/SpaceVim/SpaceVim) - `Abandoned`
  - [Readarr](https://github.com/Readarr/Readarr) - `Abandoned`
  - [Lenovo Legion Toolkit](https://github.com/BartoszCichecki/LenovoLegionToolkit) - `Abandoned`
</details>

## FAQ
<details>
  <summary><b>Stars aren't a good metric to guage popularity/quality.</b></summary> <br />
The minimum star count of 1k has been a major point of contention. Admittedly, star counts don't always reflect project popularity and quality. Stars are biased towards developers because they are the ones with a GitHub account, thus leaving out the input of the end users. But no solution is going to be a one size fits all solution. It's critically important that as the list scales it doesn't devolve into a clutter trap, even if the price is some projects getting left out.
<p>&nbsp;</p>
Stars tend to be synonomous with community recognition, making it a good starting point for further vetting to check for contributors, future plans, and popularity. Most compotent software will have no trouble reaching the 1k star count. This requirement is also just the first step for further vetting.
<p>&nbsp;</p>
Artificial star counts (EX: buying stars) has also been brought up. This isn't that big of a problem, again, stars are just to quality a project for further vetting. We check community engagement, developer responsiveness and the project's statistics over time. A popular project should have lots of community activity, GitHub issues, pr's, etc. Evidence of foul play will disquality a project. 
</details>

## License
This project is released under the `MIT license`, hereby granting anyone to use, distribute, or modify this project for, but not limited to, commercial purposes. See the license tab for further information. 

<p>&nbsp;</p>

<p align="center">
<table>
<tbody>
<td align="center" width="2000px" height="100px">
<b><a href="#tags">Go To Top</a></b><br>
</td>
<td align="center" width="2000px" height="100px">
<b><a href="https://opensource.org/">Open Source Initiative</a></b><br>
</td>
</tbody>
</table>
</p> 

