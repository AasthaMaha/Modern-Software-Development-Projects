## Bugs fixed in program.py


1. **In divide_numbers()**
   - Bug: There was no handling for division by zero.
   - Identified by: 'test_numbers_corner()' failed in the beginning.
   - Fix: I added 'if b==0:' which checks to raise 'ZeroDivisionError'.

2. **In reverse_string()**
   - Bug: The function was always expecting the input to be a string.
   - Identified by: 'test_reverse_string_corner()' failed.
   - Fix: Added 'isinstance()' to check for raise 'TypeError' for non-string inputs. 

3. **In get_list_element()**
   - Bug: The boundary check was incorrect as it was not handling negatives inputs.
   As well as it returned 'Not found' instead of raising an exception.
   - Identified: 'test_get_list_element_corner()' failed.
   - Fix: By improving the index checking and replacing the 'Not found' with the 'IndexError' instead.