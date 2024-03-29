class calc_carry:
    def __init__(self, n):
        self.n=n
        self.C_prev_left = [None] * (n+1)
        self.P_prev_left = [None] * (n+1)
        self.G_prev_left = [None] * (n+1)
        self.C_prev_right = [None] * (n+1)
        self.P_prev_right = [None] * (n+1)
        self.G_prev_right = [None] * (n+1)
        self.C_i_left = [None] * (n+1)
        self.C_i_right = [None] * (n+1)

    def operation(self, lastRow):
        n=self.n
        for i in range(0, n+1, 1):  # from 0 to n
            if i == 0:
                self.C_i_right[i] = 0
                self.C_i_left[i] = 0
                continue

            if i == 1:
                self.C_prev_right[i] = lastRow[i - 1].g_i_i_prev_right
                self.C_prev_left[i] = lastRow[i - 1].g_i_i_prev_left

            else:
                self.C_prev_right[i] = self.C_prev_right[i - 1]
                self.C_prev_left[i] = self.C_prev_left[i - 1]

            self.P_prev_right[i] = lastRow[i - 1].p_i_i_prev_right
            self.G_prev_right[i] = lastRow[i - 1].g_i_i_prev_right

            self.C_i_right[i] = (self.P_prev_right[i] & self.C_prev_right[i]) | self.G_prev_right[i]

            self.P_prev_left[i] = lastRow[i - 1].p_i_i_prev_left
            self.G_prev_left[i] = lastRow[i - 1].g_i_i_prev_left

            self.C_i_left[i] = (self.P_prev_left[i] & self.C_prev_left[i]) | self.G_prev_left[i]
