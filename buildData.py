file = open('data.txt','w')
for i in range(2,12):
    for j in range(2,12):
        for k in range(2,12):
            # print cards
            file.write(str(i)+' '+str(j)+' '+str(k))
            answer = 'H'
            sum = i+j
            if sum == 10 and k < 10:
                answer = 'D'
            elif sum == 11:
                answer = 'D'
            elif sum == 9 and k > 2 and k < 7:
                answer = 'D'
            elif sum > 16:
                answer = 'S'
                if i != 11 and j != 11:
                    if sum == 17 and k == 11:
                        answer = 'Su'
                elif sum == 17:
                    if k > 2 and k < 7:
                        answer = 'D'
                    else:
                        answer = 'H'
                elif sum == 18:
                    if k > 2 and k < 7:
                        answer = 'D'
                    else:
                        answer = 'S'
                elif sum == 19:
                    if k == 6:
                        answer = 'D'
                    else:
                        answer = 'S'
            elif sum < 17:
                if sum > 12 and k > 1 and k < 7:
                    answer = 'S'
                elif sum == 12 and k > 3 and k < 7:
                    answer = 'S'
                if i == 11 or j == 11:
                    answer = 'H'
                    if sum == 16:
                        if k > 3 and k < 7:
                            answer = 'D'
                    elif sum == 15:
                        if k > 3 and k < 7:
                            answer = 'D'
                    elif sum == 14:
                        if k > 4 and k < 7:
                            answer = 'D'
                    elif sum == 13:
                        if k > 4 and k < 7:
                            answer = 'D'
                elif sum == 12 and k > 3 and k < 7:
                    answer = 'S'
                elif sum == 15 and k > 9:
                    answer = 'Su'
                elif sum == 16 and k > 8:
                    answer = 'Su'
            if i == 11 and j == 11:
                answer = 'Sp'
            if i == 8 and j == 8:
                if k > 1 and k < 11:
                    answer = 'Sp'
            if i == 2 and j == 2:
                if k > 1 and k < 8:
                    answer = 'Sp'
            if i == 3 and j == 3:
                if k > 1 and k < 8:
                    answer = 'Sp'
            if i == 7 and j == 7:
                if k > 1 and k < 8:
                    answer = 'Sp'
            if i == 6 and j == 6:
                if k > 1 and k < 7:
                    answer = 'Sp'
            if i == 9 and j == 9:
                if k > 1 and k < 8 and k != 7:
                    answer = 'Sp'
                else:
                    answer = 'S'
            file.write(' '+answer +'\n')
            
                    
                
                    
            
                    
