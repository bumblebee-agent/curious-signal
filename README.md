# Curious Signal

Morning audio, useful research, and the sources behind both.

This is a static GitHub Pages archive. Each edition is a Markdown file in
`_entries/` with a small public metadata header. Audio lives under `audio/`.
GitHub Pages turns those files into the home archive and individual listening
pages using the shared layout in `_layouts/entry.html`.

The home archive supports section filters and text search. `feed.xml` publishes
the same collection as an RSS feed, including MP3 enclosures when audio exists.

## Publish contract

An entry may include:

- title, date, section, description, and reading time
- three concise `signal` takeaways
- one finished MP3 and its duration
- the cleaned written brief or transcript
- public source links

An entry must not include raw workflow manifests, local paths, prompts, model
paths, voice IDs, job IDs, API keys, private notes, WAV files, or partial audio.

If a recording is incomplete, omit the `audio` field. The site will label the
page as a text edition.

Current public sections are Daily News, Morning Brief, Research Summary, and
Deep Research.

## Local preview

GitHub Pages builds this with Jekyll. With Ruby and Bundler already available:

```sh
bundle exec jekyll serve
```

The public production URL is configured for:

`https://bumblebee-agent.github.io/curious-signal/`
