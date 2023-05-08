# Data-mining

1. Bộ dữ liệu Air Quality từ UCI: **[https://archive.ics.uci.edu/ml/datasets/Air+Quality](https://archive.ics.uci.edu/ml/datasets/Air+Quality)**
2. Bộ dữ liệu NASA Meteorite Landings từ Kaggle: **[https://www.kaggle.com/nasa/meteorite-landings](https://www.kaggle.com/nasa/meteorite-landings)**

## Bộ dữ liệu Air Quality từ UCI để thực hành khám phá dữ liệu với Excel.

*Tải xuống* **tập dữ liệu chất lượng không khí** : [Thư mục dữ liệu](https://archive.ics.uci.edu/ml/machine-learning-databases/00360/) 

| Tóm tắt : Chứa các phản hồi của một thiết bị đa cảm biến khí được triển khai trên thực địa tại một thành phố của Ý. Các phản hồi trung bình hàng giờ được ghi lại cùng với tham chiếu nồng độ khí từ máy phân tích được chứng nhận. |
| --- |

| Đặc điểm tập dữ liệu: | Đa biến, chuỗi thời gian | Số trường hợp: | 9358 | Khu vực: | Máy tính |
| --- | --- | --- | --- | --- | --- |
| Đặc điểm thuộc tính: | Thực tế | Số thuộc tính: | 15 | Ngày tặng | 2016-03-23 |
| Nhiệm vụ liên quan: | hồi quy | Giá trị bị mất? | Đúng | Số lượt truy cập web: | 728672 |

**Nguồn:**

Saverio De Vito ( saverio.devito **'@'** enea.it ), ENEA - Cơ quan Quốc gia về Công nghệ Mới, Năng lượng và Phát triển Kinh tế Bền vững

**Thông tin tập dữ liệu:**

Bộ dữ liệu chứa 9358 trường hợp phản hồi trung bình hàng giờ từ một dãy 5 cảm biến hóa học oxit kim loại được nhúng trong Thiết bị đa cảm biến hóa chất chất lượng không khí. Thiết bị được đặt trên cánh đồng trong một khu vực bị ô nhiễm đáng kể, ở mức đường, trong một thành phố của Ý. Dữ liệu được ghi lại từ tháng 3 năm 2004 đến tháng 2 năm 2005 (một năm) đại diện cho các bản ghi miễn phí dài nhất hiện có về phản ứng của các thiết bị cảm biến hóa học chất lượng không khí được triển khai tại hiện trường. Ground Truth nồng độ trung bình hàng giờ đối với CO, Hydrocacbon không chứa Metanic, Benzen, Tổng Nitơ Oxit (NOx) và Nitrogen Dioxide (NO2) và được cung cấp bởi một máy phân tích được chứng nhận tham chiếu cùng địa điểm. Bằng chứng về độ nhạy chéo cũng như cả khái niệm và độ lệch của cảm biến đều có mặt như được mô tả trong De Vito et al., Sens. And Act. B, Tập. 129,2, 2008 (yêu cầu trích dẫn) cuối cùng ảnh hưởng đến khả năng ước tính nồng độ của cảm biến. Các giá trị bị thiếu được gắn thẻ với giá trị -200.

Bộ dữ liệu này có thể được sử dụng riêng cho mục đích nghiên cứu. Mục đích thương mại được loại trừ hoàn toàn.

**Thông tin thuộc tính:**

1. Ngày (DD/MM/YYYY)
2. Thời gian (HH.MM.SS)
3. Nồng độ CO trung bình thực hàng giờ tính bằng mg/m^3 (máy phân tích tham chiếu)
4. Phản ứng cảm biến trung bình hàng giờ PT08.S1 (thiếc oxit) (nhắm mục tiêu CO trên danh nghĩa )
5. Nồng độ HydroCarbon Non Metanic tổng thể trung bình thực tính bằng microg/m^3 (máy phân tích tham chiếu)
6. Nồng độ Benzen trung bình thực trung bình hàng giờ tính bằng microg/m^3 (máy phân tích tham chiếu)
7. PT08.S2 (titania) Độ phản hồi của cảm biến trung bình mỗi giờ (trên danh nghĩa là NMHC được nhắm mục tiêu)
8. Nồng độ NOx trung bình thực theo giờ tính bằng ppb (máy phân tích tham chiếu)
9. PT08.S3 (oxit vonfram) Phản ứng cảm biến trung bình theo giờ (nhắm mục tiêu NOx trên danh nghĩa)
10. Nồng độ NO2 trung bình thực theo giờ tính bằng microg/m^3 (máy phân tích tham chiếu)
11. PT08.S4 (vonfram oxit) phản ứng trung bình hàng giờ của cảm biến (trên danh nghĩa là NO2)
12. PT08.S5 (indium oxide) phản ứng của cảm biến hàng giờ (trên danh nghĩa là O3)
13. Nhiệt độ tính bằng °C
14. Độ ẩm tương đối (%)
15. AH Độ ẩm tuyệt đối

**Giấy tờ liên quan:**

S. De Vito, E. Massera, M. Piga, L. Martinotto, G. Di Francia, Trên thực địa hiệu chuẩn mũi điện tử để ước tính benzen trong kịch bản giám sát ô nhiễm đô thị, Cảm biến và Thiết bị truyền động B: Hóa chất, Tập 129, Số phát hành 2, ngày 22 tháng 2 năm 2008, Trang 750-757, ISSN 0925-4005, [[Web Link]](http://dx.doi.org/10.1016/j.snb.2007.09.060) .

( [[Liên kết web]](http://www.sciencedirect.com/science/article/pii/S0925400507007691) )

Saverio De Vito, Marco Piga, Luca Martinotto, Girolamo Di Francia, Giám sát ô nhiễm đô thị CO, NO2 và NOx bằng mũi điện tử hiệu chuẩn tại hiện trường bằng cách tự động điều chỉnh bayesian, Cảm biến và Thiết bị truyền động B: Hóa chất, Tập 143, Số 1, ngày 4 tháng 12 năm 2009, Trang 182-191, ISSN 0925-4005, [[Web Link]](http://dx.doi.org/10.1016/j.snb.2009.08.041) .

( [[Liên kết web]](http://www.sciencedirect.com/science/article/pii/S092540050900673X) )

S. De Vito, G. Fattoruso, M. Pardo, F. Tortorella và G. Di Francia, 'Kỹ thuật học bán giám sát trong khứu giác nhân tạo: Cách tiếp cận mới đối với các vấn đề phân loại và chống trôi', trong Tạp chí cảm biến IEEE, tập. 12, không. 11, trang 3215-3224, tháng 11 năm 2012.

doi: 10.1109/JSEN.2012.2192425

T**rích dẫn:**

S. De Vito, E. Massera, M. Piga, L. Martinotto, G. Di Francia, Trên thực địa hiệu chuẩn mũi điện tử để ước tính benzen trong kịch bản giám sát ô nhiễm đô thị, Cảm biến và Thiết bị truyền động B: Hóa chất, Tập 129, Số phát hành 2, ngày 22 tháng 2 năm 2008, Trang 750-757, ISSN 0925-4005, [[Web Link]](http://dx.doi.org/10.1016/j.snb.2007.09.060) .

( [[Liên kết web]](http://www.sciencedirect.com/science/article/pii/S0925400507007691) )