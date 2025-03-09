# Architecture Decision Records (ADRs)

This repository contains **Architectural Decision Records (ADRs)** to document key technical decisions in our system.

## How to Write an ADR
1. Create a new file: `architecture/adr/XXXX-title.md`
2. Follow the ADR template.
3. Commit and push to Git.
4. Open a pull request for team review.

## Tools for Managing ADRs

### `adr-tools`
[`adr-tools`](https://github.com/npryce/adr-tools) is a CLI tool for managing ADRs easily. To install:
```sh
brew install adr-tools  # macOS
sudo apt install adr-tools  # Ubuntu
```
To create a new ADR:
```sh
adr new "Title of Decision"
```

### `MADR`
[`MADR`](https://adr.github.io/madr/) is a structured template for ADRs. To use it:
1. Clone the template:
   ```sh
   git clone https://github.com/adr/madr.git
   ```
2. Copy the `template/` folder into your project and follow the format.

---

By following this ADR process, we ensure **clear documentation, better decision-making, and a shared understanding** within the team.
