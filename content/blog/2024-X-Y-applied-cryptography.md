---
title: Applied Cryptography
lang: en
layout: post
date: 2025-12-31
draft: true
---

This post summarizes my notes from the courses Applied Cryptography, Foundation of Cryptography at KTH and book Cryptography Engineering by Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno, which I read while taking the aformentioned courses.

*Pseudorandom generator:* is deterministic procedure mapping seed to longer pseudorandom string, such that no statistical test can distinguish the output of the generator from random sequence.

The definition is very generic, therefore we must be very careful before using the pseudorandom generator in practice. Example is, imagine we have a pseudorandom generator *PRG(s)* and construct a new *PRG_NEW(s)*, which take the seed *s*, constructs *s_new* by flipping the first bit of *s*, then outputs PRG_NEW(s) = PRG(s) | PRG(s_new). This may and may not be a pseudorandom generator based on the specific implementation of the PRG, it may ignore the first bit altogether making our new PRG_NEW output being a concatenation of two identical sequences. 
On the other hand we can constuct our PRG, such that also the PRG_NEW(s) fullfills the definition of pseudorandom generator. Imagine having a PRG_A(s), we have no further information about than being a pseudorandom generator. Then we can let it generate *2 * len(s) + 1* and define our PRG to (what continues was added later) to use the first bit (on position 0) to decide whether to return the first half of the text (bits 1 - len(s)) or the second half of the text (bits len(s)+1 - 2 * len(s) + 1).


Double DES. Is double DES more secure than the single DES? The question can be seen from a perspective of combinatorial problem. Similar to trying to find a way how to go from a one rubic cube state to the solved state. You start from the initial state and try all possible single moves and get all possibilities, then start from all of these.

If we have a single message and ciphertext pair. Therefore it helps, but not a lot. The resulting complexity is about 2.2^56. Because we can search the space from the both ends, and try to find the middle "ciphertext" that is match.

Therefore we used the 3DES as we suppose, there is no way how to take a shortcut to the middle, therefore from one side the computaional complexity is 2^112, and 2^56 to find the match.

Modes of operation. The actual blocks cipher can be look as a substitution cipher, where each block is equivalent to an ASCII char in the original substitution cipher. Two main ideas: let the previous block influence the following, add a counter which increases with each block.

The CBF mode and Initialization Vector. The initalization vector must be random otherwise c_1 = m_1 XOR E_k(c_0), c_2 = m_2 XOR E_k(c_0), then we can c_1 XOR c_2 = m_1 XOR m_2. 

CBD, CBF is self-synchronizing. Means that lossing the blocks does not really matter.
OFB mode is not self-synchronizing and is malleable. Allows batch processing.

Linear Cryptoanalysis of the SPN. We have equations of XOR of plaintext to XOR of ciphertext = XOR of keybits

Piling-Up Lemma
- Inclusion Exclusion to see the pattern instead of the induction written on the slides.
- Independent binary random variables => they are independent (as the cipher is a good one) otherwise we can break the cipher in another way.

2^-128 having a head on a chopping board and if it happends to be true, the head is off.
