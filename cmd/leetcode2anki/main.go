package main

import (
	"flag"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"strings"

	"github.com/RSTdefg/ankit"
	"github.com/RSTdefg/ankit/leetcode"
)

var (
	cfg  leetcode.Config
	spec string
)

func init() {
	log.Print("leetcode2anki v0.1.0")
	flag.StringVar(&cfg.Path, "path", ".", "leetcode repo path")
	flag.StringVar(&cfg.Source, "db", "leetcode.db", "sqlite3 filename")
	flag.StringVar(&cfg.Lang, "lang", "golang", "programming language")

	flag.StringVar(&spec, "spec", "", "optional: the relative path of leetcode question that should be exported only")
}

func question(path string, info os.FileInfo) (leetcode.Key, error) {
	if path == "." {
		return nil, nil
	}
	// skip directory in repository
	if info.IsDir() {
		return nil, filepath.SkipDir
	}

	filename := filepath.Base(path)
	ext := filepath.Ext(filename)
	// only handle python file
	if ext != ".py" {
		return nil, nil
	}
	// identify leetcode question by title slug: filename
	slug := strings.TrimSuffix(filename, ext)
	return leetcode.KeyTitleSlug(slug), nil
}

func code(path string, _ leetcode.Lang) (string, error) {
	b, err := ioutil.ReadFile(path)
	return string(b), err
}

func main() {
	flag.Parse()

	if err := cfg.Valid(); err != nil {
		log.Fatal(err)
	}

	repo := leetcode.NewRepo(cfg, code, question)
	defer repo.Close()

	var r ankit.Reader = repo
	if spec != "" {
		path := filepath.Join(cfg.Path, spec)

		info, err := os.Lstat(path)
		if err != nil {
			log.Fatal(err)
		}

		key, err := repo.KeyFn(spec, info)
		if err != nil && err != filepath.SkipDir {
			log.Fatal(err)
		}

		q, err := repo.Question(key, path)
		if err != nil {
			log.Fatal(err)
		}

		r = ankit.OneNoteReader(q)
	}

	if err := ankit.Copy(os.Stdout, r); err != nil {
		log.Fatal(err)
	}
}
