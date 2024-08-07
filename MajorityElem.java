class MajorityElem {
    public int majorityElement(int[] nums) {
        int count = 0;
        Integer candidate = null;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }

    public static void main(String[] args) {
        MajorityElem solution = new MajorityElem();

        int[] nums1 = {3, 2, 3};
        System.out.println("Teste 1: " + (solution.majorityElement(nums1) == 3 ? "Passed" : "Failed"));

        int[] nums2 = {2, 2, 1, 1, 1, 2, 2};
        System.out.println("Teste 2: " + (solution.majorityElement(nums2) == 2 ? "Passed" : "Failed"));
    }
}