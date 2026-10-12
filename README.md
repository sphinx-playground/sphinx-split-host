# sphinx-split-sphinx

This is a stand-alone Sphinx repository that's part of a decoupled duo-repository framework and that serves as the documentation-pipeline repository for its companion isolated source target.

## Demonstrated features

* **Cross-Repository Commits**: Designed to absorb distributed feature updates across decoupled environments.
* **Absolute Configurations**: Utilizes explicit external routing to target and pull source material across Git boundaries.

## Repository layout

```text
sphinx-split-sphinx/
├── .github/                      # Directory for GitHub
│   └── workflows/                # Directory for GitHub workflows
│       └── ci.yml                # Advanced split-path CI pipeline
├── sphinx/                       # Directory for Sphinx
│   ├── resources/                # Directory for engine assets and data drawers
│   │   ├── images/               # Directory for images and visual assets
│   │   ├── rst/                  # Directory for all other reST files
│   │   │   ├── installation.rst  # Documentation
│   │   │   └── usage.rst         # Documentation
│   │   ├── scripts/              # Directory for scripts (build, cleanup, linting, or automation)
│   │   ├── static/               # Directory for custom CSS or fonts        
│   │   └── templates/            # Directory for custom HTML structural layouts
│   ├── conf.py                   # Sphinx configuration matrix
│   └── index.rst                 # Sphinx documentation master layout file (entry-page/gatekeeper)
├── .gitignore                    # Defensive tracking shield (ignores build artifacts).
├── LICENSE                       # License
└── README.md                     # Main document for the repository
```

---

*This repository is a work-in-progress and serves as a sandbox for exploring decoupled document-generation pipelines with Sphinx.*
