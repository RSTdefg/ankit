#!/bin/bash

problems_list=("two-sum" "add-two-numbers" "longest-substring-without-repeating-characters" "median-of-two-sorted-arrays" "longest-palindromic-substring" "reverse-integer" "regular-expression-matching" "container-with-most-water" "3sum" "letter-combinations-of-a-phone-number" "remove-nth-node-from-end-of-list" "valid-parentheses" "merge-two-sorted-lists" "generate-parentheses" "merge-k-sorted-lists" "reverse-nodes-in-k-group" "search-in-rotated-sorted-array" "valid-sudoku" "combination-sum" "combination-sum-ii" "trapping-rain-water" "multiply-strings" "jump-game-ii" "permutations" "rotate-image" "group-anagrams" "powx-n" "n-queens" "maximum-subarray" "spiral-matrix" "jump-game" "merge-intervals" "insert-interval" "unique-paths" "plus-one" "climbing-stairs" "edit-distance" "set-matrix-zeroes" "search-a-2d-matrix" "minimum-window-substring" "subsets" "word-search" "largest-rectangle-in-histogram" "subsets-ii" "decode-ways" "interleaving-string" "validate-binary-search-tree" "same-tree" "binary-tree-level-order-traversal" "maximum-depth-of-binary-tree" "construct-binary-tree-from-preorder-and-inorder-traversal" "balanced-binary-tree" "distinct-subsequences" "best-time-to-buy-and-sell-stock" "binary-tree-maximum-path-sum" "valid-palindrome" "word-ladder" "longest-consecutive-sequence" "surrounded-regions" "palindrome-partitioning" "clone-graph" "gas-station" "single-number" "copy-list-with-random-pointer" "word-break" "linked-list-cycle" "reorder-list" "lru-cache" "evaluate-reverse-polish-notation" "maximum-product-subarray" "find-minimum-in-rotated-sorted-array" "min-stack" "two-sum-ii---input-array-is-sorted" "reverse-bits" "number-of-1-bits" "house-robber" "binary-tree-right-side-view" "number-of-islands" "happy-number" "reverse-linked-list" "course-schedule" "implement-trie-(prefix-tree)" "course-schedule-ii" "design-add-and-search-words-data-structure" "word-search-ii" "house-robber-ii" "kth-largest-element-in-an-array" "contains-duplicate" "invert-binary-tree" "kth-smallest-element-in-a-bst" "lowest-common-ancestor-of-a-binary-search-tree" "product-of-array-except-self" "sliding-window-maximum" "valid-anagram" "meeting-rooms" "meeting-rooms-ii" "graph-valid-tree" "missing-number" "alien-dictionary" "encode-and-decode-strings" "walls-and-gates" "find-the-duplicate-number" "find-median-from-data-stream" "serialize-and-deserialize-binary-tree" "longest-increasing-subsequence" "best-time-to-buy-and-sell-stock-with-cooldown" "burst-balloons" "coin-change" "number-of-connected-components-in-an-undirected-graph" "longest-increasing-path-in-a-matrix" "reconstruct-itinerary" "counting-bits" "top-k-frequent-elements" "design-twitter" "sum-of-two-integers" "partition-equal-subset-sum" "pacific-atlantic-water-flow" "longest-repeating-character-replacement" "non-overlapping-intervals" "target-sum" "coin-change-ii" "diameter-of-binary-tree" "permutation-in-string" "subtree-of-another-tree" "task-scheduler" "palindromic-substrings" "valid-parenthesis-string" "redundant-connection" "max-area-of-island" "daily-temperatures" "network-delay-time" "min-cost-climbing-stairs" "partition-labels" "kth-largest-element-in-a-stream" "binary-search" "swim-in-rising-water" "cheapest-flights-within-k-stops" "hand-of-straights" "car-fleet" "koko-eating-bananas" "k-closest-points-to-origin" "time-based-key-value-store" "rotting-oranges" "last-stone-weight" "longest-common-subsequence" "count-good-nodes-in-binary-tree" "min-cost-to-connect-all-points" "minimum-interval-to-include-each-query" "merge-triplets-to-form-target-triplet" "detect-squares" )

for problem in "${problems_list[@]}"; do
  leetcode submission -l python3 $problem -o tmp
  sleep 1
done
