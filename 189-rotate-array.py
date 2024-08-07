def rotate(nums, k):
    n = len(nums)
    # Se k > n. então, rodar o array k vezes, é o mesmo que rodar o array k % n vezes
    k = k % n
    # nums[:] -> Para criar uma cópia do array
    # nums[-k:] -> Vai selecionar os últimos k elementos do array
    # nums[:-k] -> Vai selecionar os primeiros n - k elementos do array
    nums[:] = nums[-k:] + nums[:-k]

nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate(nums1, k1)
print(nums1)