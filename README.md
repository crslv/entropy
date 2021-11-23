# Threat Hunting with File Entropy
Utility that will detect encrypted/compressed files in a specified directory

Entropy is the measurement of the randomness.  The concept originated in the study of thermodynamics, but Claude E. Shannon in applied the concept to digital communications his 1948 paper, “A Mathematical Theory of Communication.”  Shannon was interested in determining the theoretical maximum amount that a digital file could be compressed.

In simple terms, a file is compressed by replacing patterns of bits with shorter patterns of bits.  Therefore, the more entropy in the data file, the less it can be compressed.  Determining the entropy of a file is also useful to detect if it is likely to be encrypted.

In the field of cryptology, there are formal proofs that show that if an adversary can correctly distinguish an encrypted file from a file that is truly random with a greater than 50% probability then it is said that he has “the advantage.”  The adversary can then exploit that advantage and possibly break the encryption.  This concept of advantage applies to the mathematical analysis of encryption algorithms.  However in the real world, files that contain random data have no utility in a file system, therefore it is highly probable that files with high entropy are actually encrypted or compressed.

![Entropy-004](https://user-images.githubusercontent.com/79792556/124666087-30daec80-deb6-11eb-91a0-2ab9d1df3efc.jpg)
