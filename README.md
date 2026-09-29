# Computational Cognitive Neuroscience of Language (CCNL)

Visit **[comp-cogneuro-lang.github.io/ccnl](https://comp-cogneuro-lang.github.io/ccnl)** 🚀

_Built with [Lab Website Template](https://greene-lab.gitbook.io/lab-website-template-docs)_

## Adding a publication

Journal articles, chapters, and proceedings are listed in [`_data/sources.yaml`](_data/sources.yaml). This curated list is the only source for the Publications page.

1. If the paper has a DOI, add an entry. The title, authors, journal, and date are fetched automatically when the site rebuilds.

   ```yaml
   - id: doi:10.3758/s13423-024-02608-y
     type: article          # article | chapter | proceedings
     pdf: papers/magnuson-2024-srns-interactive.pdf   # optional
   ```

2. If there is no DOI, type in the details yourself:

   ```yaml
   - title: "Title of the paper"
     authors:
       - J. S. Magnuson
       - A. Coauthor
     publisher: "Book or journal, volume, pages"
     date: 2005-01-01
     link: https://...      # optional
     type: chapter
     pdf: papers/...pdf     # optional
   ```

3. To attach a PDF, put the file in `papers/` and add the `pdf:` line.

4. Commit to `main`. The site rebuilds and regenerates `_data/citations.yaml` automatically. Never edit `citations.yaml` by hand.

Technical reports are listed in `_data/tech-reports.yaml` and conference presentations in `_data/presentations.yaml`. Both are plain lists of `date` and `text`, with an optional `pdf`, and presentations also have a `kind`: `conference` or `keynote`.

### New works from ORCID

Every Monday, a GitHub Action (`.github/workflows/orcid-candidates.yaml`) checks Jim's ORCID record for works that are not yet in `sources.yaml`. It opens a pull request that appends them to the end of that file. To review the pull request:

- Delete any entries you don't want. To stop an item from being proposed again, add it to `_data/candidates-ignore.yaml`.
- Check each entry's `type` and add a `pdf:` line where you have one.
- Merge.

Nothing appears on the site until the pull request is merged. You can also run the check by hand from the Actions tab (workflow_dispatch) or locally:

```
python _cite/orcid_candidates.py --dry-run
```
