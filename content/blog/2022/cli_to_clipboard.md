+++
date = "2022-12-12"
draft = false
title = "Manipulate clipboard from the CLI"
categories = "TIL"
tags = ["cli", "macosx"]
+++


You can pipe content to  `pbcopy` to push it to the clipboard on MacOSX.

```bash
$> pwd | pbcopy
```

Paste it back

```bash
$> pbpaste

/home/sid/projects/
```

and you can do lots of things in the middle, without to storing to a temporary file.

```bash
$> curl https://dummyjson.com/products| pbcopy

$> pbpaste|jq '.[][].title'| sort
```
