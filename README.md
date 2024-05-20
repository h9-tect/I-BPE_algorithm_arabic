# Incremental Byte Pair Encoding (I-BPE) Algorithm For arabic 
## used in AceGPT [paper](https://huggingface.co/FreedomIntelligence/AceGPT-v1.5-13B-Chat/blob/main/Second_Language_(Arabic)_Acquisition_of_LLMs_via_Progressive_Vocabulary_Expansion.pdf) 
## Introduction

The Incremental Byte Pair Encoding (I-BPE) algorithm is an extension of the standard Byte Pair Encoding (BPE) method. It dynamically expands the vocabulary during the training process, allowing the model to incorporate new tokens incrementally. This mimics human learning by gradually introducing new information and adapting over time.

## Algorithm

### Steps

1. **Initialize Vocabulary**
   - Start with an initial vocabulary consisting of individual characters or subwords.

2. **Define Vocabulary Size Stages**
   - Specify the target vocabulary sizes for each stage.

3. **Define Corpus Proportions**
   - Define the proportion of the training corpus to be used for new tokens at each stage.

4. **Iterative Expansion**
   - For each stage:
     1. Calculate the frequency of adjacent token pairs in the corpus.
     2. Identify the most frequent pair.
     3. Merge the most frequent pair to form a new token.
     4. Add the new token to the vocabulary.
     5. Adjust the corpus proportion.
     6. Repeat until the target vocabulary size is reached.

5. **Finalize Vocabulary**
   - After completing all stages, finalize the vocabulary for further training and application.

## Example Usage
```python


# Example usage 
initial_vocab = ['ا', 'ل', 'م']  # Initial vocabulary set with individual characters
stages = [5, 10, 15]  # Vocabulary sizes at each stage
corpus_proportions = [0.1, 0.2, 0.3]  # Proportions of training corpus at each stage
corpus = ['ا', 'ل', 'م', 'د', 'ر', 'س', 'ة', 'ا', 'ل', 'ك', 'ب', 'ي', 'ر', 'ة']  # Example corpus

ibpe = IBPE(initial_vocab, stages, corpus_proportions)
final_vocab = ibpe.run(corpus)

print("Final Vocabulary:", final_vocab)
```
### Initial Setup
- **Initial Vocabulary**: The algorithm starts with an initial vocabulary consisting of individual characters, e.g., `{'ا', 'ل', 'م'}`.

### Configuration
- **Stages**: Define the stages with target vocabulary sizes, e.g., `[5, 10, 15]`.
- **Corpus Proportions**: Define the corpus proportions for each stage, e.g., `[0.1, 0.2, 0.3]`.

### Running the Algorithm
1. **Initialize Vocabulary**: Begin with individual characters or subwords.
2. **Iterative Expansion**:
   - For each stage, calculate the frequency of adjacent pairs in the corpus.
   - Merge the most frequent pairs to form new tokens.
   - Add the new tokens to the vocabulary until the target size is reached.
   - Adjust the corpus to introduce new tokens progressively.
3. **Finalize Vocabulary**: The final vocabulary includes all tokens formed through iterative merging.

### Example Corpus
- An example Arabic corpus might be: `['ا', 'ل', 'م', 'د', 'ر', 'س', 'ة', 'ا', 'ل', 'ك', 'ب', 'ي', 'ر', 'ة']`.

## Explanation of Output

### Final Vocabulary
- The final vocabulary includes meaningful tokens representing common patterns in the corpus, e.g., `{'ا', 'ال', 'الم', 'المد', 'المدر', 'المدرس', 'المدرسة', 'المدرسةال', 'المدرسةالك', 'المدرسةالكب', 'المدرسةالكبي', 'المدرسةالكبير', 'المدرسةالكبيرة', 'ل', 'م'}`.

#### Why This is Successful:

1. **Initial Vocabulary**:
   - The process begins with a basic set of individual characters: `{'ا', 'ل', 'م'}`.
   - This simple start allows the algorithm to identify and build upon the most fundamental units of the language.

2. **Frequent Pair Merging**:
   - By calculating the frequency of adjacent pairs in the corpus, the algorithm identifies the most common sequences.
   - For instance, pairs like `('ا', 'ل')`, `('ل', 'م')`, etc., are merged to form new tokens such as `ال` (the definite article "the" in Arabic).

3. **Meaningful Tokens**:
   - The merging process continues iteratively, resulting in tokens that represent meaningful subwords or words.
   - Examples include:
     - `المدرسة`: Formed through multiple stages of merging, this token means "the school".
     - `المدرسةالكبيرة`: This token means "the large school", showing how the algorithm can capture longer phrases that are commonly used together.

4. **Dynamic Adjustment**:
   - The corpus is adjusted at each stage, ensuring that new tokens are introduced progressively.
   - This dynamic adjustment helps in maintaining a balance between known and new tokens, preventing the model from being overwhelmed by too many new tokens at once.

5. **Vocabulary Growth**:
   - The target vocabulary sizes `[5, 10, 15]` are achieved through careful and incremental expansion.
   - This structured growth helps in creating a comprehensive and representative vocabulary that covers frequent patterns in the corpus.

6. **Reduced Out-of-Vocabulary Rate**:
   - By progressively expanding the vocabulary, the algorithm reduces the out-of-vocabulary (OOV) rate.
   - This means the model is more likely to recognize and correctly process words and phrases that appear in the corpus, leading to better performance in language tasks.

7. **Adaptability and Robustness**:
   - The incremental approach ensures that the model adapts smoothly to new information, mimicking human learning.
   - This leads to a more robust language model that can handle a wide range of inputs effectively.
