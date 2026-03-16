Run a full audit of this educational content repository. This is NOT a software project — there is no npm, no tests, no build system. The audit checks the health of the content and documentation.

## Steps

1. **Orphaned files**: Search for LaTeX artifacts (`.aux`, `.log`, `.synctex.gz`), temp files (`~*`, `.DS_Store`), or any file that should be excluded by `.gitignore` but is still tracked or present on disk.

2. **Broken references**: Check all markdown files for internal links (e.g., `datos/inventarios/U03-inventario.json`, `repertorios/vocabulario.md`) and verify the referenced files actually exist at those paths.

3. **Pending placeholders**: Find all occurrences of `*pendiente*` across the project. List them grouped by file with line numbers.

4. **Control documents sync**: Verify that `CLAUDE.md`, `README.md`, `CHANGELOG.md`, and `ROADMAP.md` are consistent with the actual repo state:
   - Does the structure in CLAUDE.md match the real directory structure?
   - Does the status table in CLAUDE.md reflect the actual content state?
   - Does ROADMAP.md reflect completed and pending work accurately?
   - Is CHANGELOG.md up to date with recent git commits?

5. **Structural consistency**: Check naming conventions, folder organization, and patterns:
   - Do all units follow the same structure (`unidades/UXX/UXX-name.md`)?
   - Are agents, repertories, and references consistently named?
   - Are there files that seem misplaced or duplicated?

6. **Summary**: Present a clear report with findings grouped by severity (critical / warning / info) and suggest specific fixes for each issue found.
