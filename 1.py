


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [1,1, 0, 1, 1]
    m = []
    for i in range(1, len(height)-1):
        if height[i] >= height[i+1] and height[i] >= height[i-1]:
            m.append(i)
    print(m)
    water_list = []
    for i in range(len(m) -1):
        idx1, idx2 = m[i], m[i+1]
        top = min(height[idx1], height[idx2])
        for j in range(idx1+1, idx2):
            if height[j] < top:
                water_list.append(top - height[j])
    print(water_list)
    print(sum(water_list))
