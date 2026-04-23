def score_english_text(input_bytes):
    most_common = b'etaoin SHRDLU '
    score = 0 
    for bytes in input_bytes:
        if bytes in most_common:
            score += 1
    return score

hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
raw_bytes = bytes.fromhex(hex_string)
candidate = []

for key_candidate in range(256):
    decrypted_attempt = bytes([b ^ key_candidate for b in raw_bytes])
    current_score = score_english_text(decrypted_attempt)
    candidate.append({'key':key_candidate,
                      'score':current_score,
                      'plaintext': decrypted_attempt})
best_candidate = max(candidate, key = lambda x:x['score'])
print(f"Key Found: {best_candidate['key']} (Character: '{chr(best_candidate['key'])}')")
print(f"Message: {best_candidate['plaintext'].decode()}")

