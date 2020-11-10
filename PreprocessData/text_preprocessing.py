import string
import re
from pyvi import ViTokenizer

def remove_punctuation(text):
    text = text.lower()
    text = text.replace('\n', ' ')
    # text = text.translate(str.maketrans(' ', ' ', string.punctuation))
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    text = regex.sub(' ', text)
    # scan deeper
    text = re.sub(r'[^\w\s]', ' ', text, re.UNICODE)
    # remove number
    text = re.sub('\d', ' ', text)
    return text

def tokenize_vietnamese(text):
    return ViTokenizer.tokenize(text)

def remove_stop_words(text): 
    # load list stopword
    stopwords = []
    with open(r'E:\NewsRSTopic\Data\PTIT\vietnamese-stopwords-dash.txt', 'r', encoding='utf-8') as f:
        all_ = f.read()
        for line in all_.splitlines():
            stopwords.append(line.rstrip())
    
    token_without_stopword = [word for word in text.split() if not word in stopwords and len(word)>2]
    return " ".join(token_without_stopword)

def preprocess_text(text):
    text = remove_punctuation(text)
    text = tokenize_vietnamese(text)
    text = remove_stop_words(text)
    return text

import pandas as pd
if __name__ == "__main__":
    t = preprocess_text("""SÁCH PYTHON CƠ BẢN\nHiện nay ngôn ngữ lập trình bậc cao Python đang nổi lên như một ngôn ngữ lập trình được sử dụng NHIỀU NHẤT trên thế giới. Điều này được giải thích bằng các lý do sau:\n\nPython là ngôn ngữ lập trình bậc cao khá đơn giản, dễ học, dễ viết.\nCách viết lệnh của Python khá đặc biệt, sử dụng các dấu cách (viết thụt vào) để mô tả các nhóm (block) lệnh. Đặc điểm này làm cho việc viết lệnh Python gần giống với cách viết, trình bày văn bản hàng ngày. Chính đặc điểm này làm cho ngôn ngữ lập trình Python rất dễ viết, trong sáng, ngày càng phát triển và được đưa vào môi trường giáo dục thay cho các ngôn ngữ truyền thống như Pascal, C hay Java.\nPython là ngôn ngữ mã nguồn mở và cho phép cộng đồng có thể đóng góp bằng cách bổ sung các module, các kho hàm số, thư viện thuật toán. Điều này làm cho Python phát triển BÙNG NỔ trong giới khoa học và giáo dục đại học. Đặc biệt trong một số ngành mũi nhọn của CNTT như IoT, trí tuệ nhân tạo (AI), dữ liệu lớn (big data) và CMCN 4.0, các phát triển rất nhanh thời gian gần đây của công nghệ đều gắn liền với Python.\nNgoài các lý do nêu trên, Python còn có một tính chất khác biệt nữa: Python là ngôn ngữ thông dịch và luôn có môi trường tương tác Python Shell đi kèm. Chính môi trường tương tác này sẽ giúp ích rất nhiều cho những người muốn làm quen và học Python.\n\nSách Pyhon cơ bản là cuốn sách đầu tiên, cơ bản, dành cho người mới bắt đầu học ngôn ngữ lập trình này.\nSách dày 254 trang, bao gồm 16 chương, cùng với trên 350 bài tập từ đơn giản đến phức tạp, phù hợp cho mọi đối tượng từ cấp THCS, THPT hoặc sinh viên đại học. Sách cũng có thể dùng cho giáo viên dạy Tin học các trường phổ thông và đại học.\nNội dung các chủ đề của sách Python cơ bản như sau:1. Bắt đầu với Python.2. Làm quen môi trường lập trình Python.3. Input và chuyển đổi dữ liệu.4. Hàm số.5. Đối tượng trong Python.6. Kiểu dữ liệu List. Mảng một chiều.7. List của List. Mảng nhiều chiều.8. Khái niệm Module.9. Xâu ký tự.10. Đọc và ghi tệp.11. Câu lệnh điều kiện.12. Đệ quy.13. Kiểu dữ liệu Từ điển.14. Kiểu dữ liệu Tập hợp.15. Đồ họa con Rùa.16. Bắt lỗi và kiểm soát lỗi trong Python.Mỗi chương sẽ bắt đầu bằng mô tả mục đích của chương, tiếp theo là dãy các hoạt động kiến thức cần học và dạy. Sách có thể dùng cho việc tự học hoặc giáo viên giảng dạy trên lớp. Sau mỗi chương là phần câu hỏi, bài tập chi tiết.""")