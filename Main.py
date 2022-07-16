class Snake:
    
    def __init__(self):
        self.length = 1

    def update_length(self):
        self.length = self.length * 2


    def snake_fill(self, n): 
        size_of_grid = int(n) ** 2
        counter=0

        while True:
            if self.length <= size_of_grid:
                self.update_length()      
                  
            else:
                print(f'The number of times before we run out of space is {counter - 1 }')
                break

            counter+=1





if __name__=='__main__':
    n = input ('Please enter n, where the grid is n x n : ')
    snake=Snake()
    snake.snake_fill(n)
