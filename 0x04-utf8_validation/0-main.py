#!/usr/bin/python3
validUTF8 = __import__('0-validate_utf8').validUTF8

# Test Case 1: Single-byte character (ASCII)
data = [65]
print(validUTF8(data))  # Should print True

# Test Case 2: Multi-byte character (ASCII)
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Should print True

# Test Case 3: Invalid UTF-8 encoding
data = [229, 65, 127, 256]
print(validUTF8(data))  # Should print False

# Test Case 4: Valid 2-byte character
data = [194, 128]
print(validUTF8(data))  # Should print True

# Test Case 5: Valid 3-byte character
data = [226, 152, 131]
print(validUTF8(data))  # Should print True

# Test Case 6: Valid 4-byte character
data = [240, 159, 152, 132]
print(validUTF8(data))  # Should print True

# Test Case 7: Invalid 4-byte character (exceeding limit)
data = [240, 159, 152, 132, 65]
print(validUTF8(data))  # Should print False

# Test Case 8: Invalid continuation byte
data = [195, 200]
print(validUTF8(data))  # Should print False

# Test Case 9: Overlong encoding
data = [197, 128]
print(validUTF8(data))  # Should print False

# Test Case 10: Invalid start byte
data = [128, 65]
print(validUTF8(data))  # Should print False

# Test
data = [467, 133, 108]
print(validUTF8(data))
