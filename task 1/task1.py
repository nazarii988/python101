import re #модуль для роботи з регулярними виразами

str = input("\nВведіть рядок: ")
word = ''.join([i for i in str if not i.isdigit()]) #генератор списку з умовою та приєднанням елементів
nums = re.findall(r'\d+', str) #шукає всі збіги з шаблоном string, тобто цілі числа
nums = [int(i) for i in nums] #генератор списку з додаванням цілих чисел

print("\nРядок без чисел:", word)
print("Числа з рядка:", nums)

WithLarge = ' '.join(word[0].upper() + word[1:-1] + word[-1:].upper() for word in word.split()) #утворення великих літер за допомогою позначень зрізу через зріз слів
print("\nРядок після змін:", WithLarge)

nums.remove(max(nums)) #видаляє максимальне значення в масиві чисел nums
numberIndex = [nums[i]**i for i in range(0,len(nums))] #генератор списку з піднесенням масиву чисел до степеню по їх індексу

print("Масив чисел в степені по їх індексу:", numberIndex)
print("\n")