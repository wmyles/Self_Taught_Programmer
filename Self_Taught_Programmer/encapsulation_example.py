class Data:
    def __init__(self):
        self.nums=[1,2,3,4,5]

    def change_data(self, index, n):
        self.nums[index]=n #smart, takes index value as a paramater along with value to place into said index
#two ways to change the above instance variable value->direct access seen here
data_one=Data()
data_one.nums[0]=100
print(data_one.nums)
# and using change data method
data_two=Data()
data_two.change_data(0,100)
print(data_two.nums)
