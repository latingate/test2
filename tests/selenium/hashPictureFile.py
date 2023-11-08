import hashlib

def compute_hash(filepath, hash_algorithm):
    hasher = hashlib.new(hash_algorithm)
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

image_filepath = 'tst.png'
md5_hash = compute_hash(image_filepath, 'md5')
sha256_hash = compute_hash(image_filepath, 'sha256')

print(f"\nGenerate hash signature for a file - {image_filepath}")
print(f"MD5 hash of the image: {md5_hash}")
print(f"SHA-256 hash of the image: {sha256_hash}")
