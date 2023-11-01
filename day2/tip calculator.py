def main():
    bill = float(input('What was the bill?: '))
    split = int(input('how many people are splitting the bill? : '))
    tip = int(input('what percent tip are we leaving? ')) /100
    total_bill = round((bill * (1 + tip) / split),2)
    print(total_bill)


if __name__ == '__main__':
    main()