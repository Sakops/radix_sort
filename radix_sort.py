import copy


class RadixSort:
    def __init__(self):
        self.base = 7
        self.bucket_list_history = []

    def get_bucket_list_history(self):
        return self.bucket_list_history

    def sort(self, input_array):
        """
        Sorts a given list using radix sort in descending order
        @param input_array: list to be sorted
        @returns: a sorted list
        """
        self.bucket_list_history.clear()  # Clear history list at the beginning of sorting

        # Get the number of digits in the largest item
        max_value = max(input_array)
        num_digits = len(str(max_value))

        sorted_array = copy.deepcopy(input_array)  # Create a copy of the input array for sorting

        for digit_idx in range(num_digits):
            buckets = [[] for _ in range(self.base)]  # Create buckets for each digit

            for num in sorted_array:
                digit = (num // (self.base ** digit_idx)) % self.base
                buckets[digit].append(num)  # Add the number to the corresponding bucket

            self._add_bucket_list_to_history(buckets, digit_idx)  # Store the bucket list for the iteration

            # Update the sorted array by concatenating the buckets in reverse order
            sorted_array = [num for bucket in reversed(buckets) for num in bucket]

        return sorted_array

    def _add_bucket_list_to_history(self, bucket_list, iteration):
        """
        This method creates a snapshot (clone) of the bucket list and adds it to the bucket list history.
        @param bucket_list: current bucket list after assigning elements to be sorted to the buckets
        @param iteration: current iteration index
        """
        print(f"Iteration {iteration}: {bucket_list}")
        arr_clone = [bucket[:] for bucket in bucket_list]  # Create a shallow copy of each bucket
        self.bucket_list_history.append(arr_clone)
