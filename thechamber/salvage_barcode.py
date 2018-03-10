from PIL import Image, ImageDraw


def get_binary(num):
    value ={
        "0": "11011001100",
        "1": "11001101100",
        "2": "11001100110",
        "3": "10010011000",
        "4": "10010001100",
        "5": "10001001100",
        "6": "10011001000",
        "7": "10011000100",
        "8": "10001100100",
        "9": "11001001000",
        "10": "11001000100",
        "11": "11000100100",
        "12": "10110011100",
        "13": "10011011100",
        "14": "10011001110",
        "15": "10111001100",
        "16": "10011101100",
        "17": "10011100110",
        "18": "11001110010",
        "19": "11001011100",
        "20": "11001001110",
        "21": "11011100100",
        "22": "11001110100",
        "23": "11101101110",
        "24": "11101001100",
        "25": "11100101100",
        "26": "11100100110",
        "27": "11101100100",
        "28": "11100110100",
        "29": "11100110010",
        "30": "11011011000",
        "31": "11011000110",
        "32": "11000110110",
        "33": "10100011000",
        "34": "10001011000",
        "35": "10001000110",
        "36": "10110001000",
        "37": "10001101000",
        "38": "10001100010",
        "39": "11010001000",
        "40": "11000101000",
        "41": "11000100010",
        "42": "10110111000",
        "43": "10110001110",
        "44": "10001101110",
        "45": "10111011000",
        "46": "10111000110",
        "47": "10001110110",
        "48": "11101110110",
        "49": "11010001110",
        "50": "11000101110",
        "51": "11011101000",
        "52": "11011100010",
        "53": "11011101110",
        "54": "11101011000",
        "55": "11101000110",
        "56": "11100010110",
        "57": "11101101000",
        "58": "11101100010",
        "59": "11100011010",
        "60": "11101111010",
        "61": "11001000010",
        "62": "11110001010",
        "63": "10100110000",
        "64": "10100001100",
        "65": "10010110000",
        "66": "10010000110",
        "67": "10000101100",
        "68": "10000100110",
        "69": "10110010000",
        "70": "10110000100",
        "71": "10011010000",
        "72": "10011000010",
        "73": "10000110100",
        "74": "10000110010",
        "75": "11000010010",
        "76": "11001010000",
        "77": "11110111010",
        "78": "11000010100",
        "79": "10001111010",
        "80": "10100111100",
        "81": "10010111100",
        "82": "10010011110",
        "83": "10111100100",
        "84": "10011110100",
        "85": "10011110010",
        "86": "11110100100",
        "87": "11110010100",
        "88": "11110010010",
        "89": "11011011110",
        "90": "11011110110",
        "91": "11110110110",
        "92": "10101111000",
        "93": "10100011110",
        "94": "10001011110",
        "95": "10111101000",
        "96": "10111100010",
        "97": "11110101000",
        "98": "11110100010",
        "99": "10111011110"
    }
    return value[num]


class Barcode:
    width = 2
    height = 60
    size = (width, height)
    whitespace = 20
    # binary = "11010000100110001010001100010001010111011110100010110001110001011011000010100100001011001100011101011"

    def __init__(self, binary):
        self.length = len(binary)
        num = int(1 / 4 * self.length)
        self.chunks = binary[:num], binary[num: 2*num], binary[num*2: num*3], binary[num*3:]
        pass


def generate_barcode(code):
    binary = convert_to_binary(code)
    bar = Barcode(binary)
    im_size = (bar.width * bar.length + bar.whitespace * 2, 60)
    im = Image.new("RGB", im_size, "white")
    draw = ImageDraw.Draw(im)

    # im.show()
    point1 = (bar.whitespace, 0)
    point2 = (point1[0] + bar.width, bar.height)
    for chunk in bar.chunks:
        for l in chunk:
            # print(l)
            color = "white"

            if l == str(1):
                # print(l)
                color = "black"

            else:
                # print(0)
                color = "white"
            draw.rectangle((point1[0], point1[1], point2[0], point2[1]), fill=color)
            point1 = (point2[0], point1[1])
            point2 = (point1[0] + bar.width, point2[1])
    # im.show()
    return im

def convert_to_binary(bct):
    i = 1
    start_binary = "11010011100"
    end_binary = "1100011101011"
    check_digit = 105
    odd = len(bct) % 2
    pairs = int(len(bct)/2)
    last_pair = 0
    binary = ""
    for pair in range(pairs):
        target = 2 + 2*pair
        combo = int(bct[last_pair: target])
        # print(combo)
        check_digit += combo * i
        last_pair = target
        i += 1
        # print(combo)
        binary += get_binary(str(combo))

    if odd == 1:
        last_num = int(bct[-1]) * i
        check_digit += last_num
        binary += get_binary(str(last_num))
        # print(bct[-1])

    print("Unmodified Check Digit: ", check_digit)
    check_digit %= 103
    print("Modified Check Digit: ",  check_digit)
    if check_digit == 100:
        check_digit = str(check_digit)
        # binary += get_binary(check_digit[:2])
        # binary += get_binary(check_digit[2])
        binary += "10111101110"
    else:
        print(binary)
        print(check_digit)
        binary += get_binary(str(check_digit))
    binary = start_binary + binary + end_binary
    bct += str(check_digit)
    # print(binary)
    # print(bct)
    return binary
