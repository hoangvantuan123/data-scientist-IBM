# Data-Air Quality

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

## Khám Phá Dữ Liệu

- Tên bộ dữ liệu: Air Quality
- Có bao nhiêu mẫu (samples): 9357 mẫu (số hàng)
- Có bao nhiêu lớp (classes): Không có lớp phân loại trong bộ dữ liệu này
- Có bao nhiêu thuộc tính (feature): 15 thuộc tính (số cột)
- Các thuộc tính của dữ liệu có những kiểu gì: Dữ liệu gồm có các thuộc tính dạng số thực và ngày giờ.
- Dữ liệu có bị mất mát (missing value) không? Có, dữ liệu bị thiếu ở nhiều thuộc tính khác nhau (và được gắn thẻ giá trị là -200), trong đó CO_GT, PT08_S3_NOx, NO2_GT, PT08_S4_NO2, PT08_S5_O3 là những thuộc tính bị mất dữ liệu nhiều nhất.

## Phân tích

| Date |  | Time |  | CO(GT) |  | PT08.S1(CO) |  | NMHC(GT) |  | C6H6(GT) |  | PT08.S2(NMHC) |  | NOx(GT) |  | PT08.S3(NOx) |  | NO2(GT) |  | PT08.S4(NO2) |  | PT08.S5(O3) |  | T |  | RH |  | AH |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Mean | 38251,1876 | Mean | 0,47910655 | Mean | -34,207524 | Mean | 1048,86965 | Mean | -159,09009 | Mean | 1,86557595 | Mean | 894,475963 | Mean | 168,6042 | Mean | 794,872333 | Mean | 58,1358983 | Mean | 1391,36327 | Mean | 974,951534 | Mean | 9,77659951 | Mean | 39,4836112 | Mean | -6,8376037 |
| Standard Error | 1,16356821 | Standard Error | 0,00298213 | Standard Error | 0,80281088 | Standard Error | 3,40961028 | Standard Error | 1,44512353 | Standard Error | 0,42778326 | Standard Error | 3,53882233 | Standard Error | 2,66122544 | Standard Error | 3,32856144 | Standard Error | 1,31220247 | Standard Error | 4,82978099 | Standard Error | 4,72361449 | Standard Error | 0,44663216 | Standard Error | 0,52946143 | Standard Error | 0,40293632 |
| Median | 38251 | Median | 0,45833333 | Median | 1,5 | Median | 1052,5 | Median | -200 | Median | 7,88665281 | Median | 894,5 | Median | 141 | Median | 794,25 | Median | 96 | Median | 1445,5 | Median | 942 | Median | 17,2000003 | Median | 48,5500002 | Median | 0,9768229 |
| Mode | 38057 | Mode | 0,75 | Mode | -200 | Mode | -200 | Mode | -200 | Mode | -200 | Mode | -200 | Mode | -200 | Mode | -200 | Mode | -200 | Mode | -200 | Mode | -200 | Mode | -200 | Mode | -200 | Mode | -200 |
| Standard Deviation | 112,5538 | Standard Deviation | 0,2884659 | Standard Deviation | 77,6571703 | Standard Deviation | 329,817015 | Standard Deviation | 139,789093 | Standard Deviation | 41,380154 | Standard Deviation | 342,315902 | Standard Deviation | 257,424561 | Standard Deviation | 321,977031 | Standard Deviation | 126,931428 | Standard Deviation | 467,192382 | Standard Deviation | 456,922728 | Standard Deviation | 43,2034376 | Standard Deviation | 51,2156448 | Standard Deviation | 38,9766702 |
| Sample Variance | 12668,3578 | Sample Variance | 0,08321258 | Sample Variance | 6030,63611 | Sample Variance | 108779,263 | Sample Variance | 19540,9905 | Sample Variance | 1712,31714 | Sample Variance | 117180,177 | Sample Variance | 66267,4048 | Sample Variance | 103669,209 | Sample Variance | 16111,5875 | Sample Variance | 218268,722 | Sample Variance | 208778,379 | Sample Variance | 1866,53702 | Sample Variance | 2623,04227 | Sample Variance | 1519,18082 |
| Kurtosis | -1,1999757 | Kurtosis | -1,2043176 | Kurtosis | 0,77830552 | Kurtosis | 5,83551159 | Kurtosis | 18,863824 | Kurtosis | 19,1887139 | Kurtosis | 2,36942543 | Kurtosis | 1,50556585 | Kurtosis | 3,10421494 | Kurtosis | 0,27571718 | Kurtosis | 3,26638758 | Kurtosis | 0,63795655 | Kurtosis | 18,7744751 | Kurtosis | 15,7643264 | Kurtosis | 20,6130917 |
| Skewness | 3,1518E-06 | Skewness | 0,00052855 | Skewness | -1,6661795 | Skewness | -1,7211263 | Skewness | 4,07578445 | Skewness | -4,5087745 | Skewness | -0,793153 | Skewness | 0,82525519 | Skewness | -0,3844639 | Skewness | -1,2257893 | Skewness | -1,2439438 | Skewness | -0,0345 | Skewness | -4,445411 | Skewness | -3,9324398 | Skewness | -4,7545703 |
| Range | 390 | Range | 0,95833333 | Range | 211,9 | Range | 2239,75 | Range | 1389 | Range | 263,741476 | Range | 2414 | Range | 1679 | Range | 2882,75 | Range | 539,7 | Range | 2975 | Range | 2722,75 | Range | 244,6 | Range | 288,725 | Range | 202,231036 |
| Minimum | 38056 | Minimum | 0 | Minimum | -200 | Minimum | -200 | Minimum | -200 | Minimum | -200 | Minimum | -200 | Minimum | -200 | Minimum | -200 | Minimum | -200 | Minimum | -200 | Minimum | -200 | Minimum | -200 | Minimum | -200 | Minimum | -200 |
| Maximum | 38446 | Maximum | 0,95833333 | Maximum | 11,9 | Maximum | 2039,75 | Maximum | 1189 | Maximum | 63,7414764 | Maximum | 2214 | Maximum | 1479 | Maximum | 2682,75 | Maximum | 339,7 | Maximum | 2775 | Maximum | 2522,75 | Maximum | 44,6000004 | Maximum | 88,7250004 | Maximum | 2,23103572 |
| Sum | 357916362 | Sum | 4483 | Sum | -320079,8 | Sum | 9814273,33 | Sum | -1488606 | Sum | 17456,1942 | Sum | 8369611,58 | Sum | 1577629,5 | Sum | 7437620,42 | Sum | 543977,6 | Sum | 13018986,1 | Sum | 9122621,5 | Sum | 91479,6416 | Sum | 369448,15 | Sum | -63979,458 |
| Count | 9357 | Count | 9357 | Count | 9357 | Count | 9357 | Count | 9357 | Count | 9357 | Count | 9357 | Count | 9357 | Count | 9357 | Count | 9357 | Count | 9357 | Count | 9357 | Count | 9357 | Count | 9357 | Count | 9357 |
| Confidence Level(95,0%) | 2,28084685 | Confidence Level(95,0%) | 0,00584562 | Confidence Level(95,0%) | 1,57368399 | Confidence Level(95,0%) | 6,68357798 | Confidence Level(95,0%) | 2,83275654 | Confidence Level(95,0%) | 0,83854827 | Confidence Level(95,0%) | 6,93686173 | Confidence Level(95,0%) | 5,21658088 | Confidence Level(95,0%) | 6,52470462 | Confidence Level(95,0%) | 2,57220235 | Confidence Level(95,0%) | 9,46742157 | Confidence Level(95,0%) | 9,25931213 | Confidence Level(95,0%) | 0,8754962 | Confidence Level(95,0%) | 1,0378596 | Confidence Level(95,0%) | 0,78984286 |

## Biểu Đồ Tương Quan

## Chuẩn Hoá Dữ Liệu

1. Min-Max Scaling: Chuyển đổi dữ liệu để nằm trong khoảng giá trị đã cho, ví dụ [0, 1] hoặc [-1, 1], bằng cách sử dụng công thức sau:
    
    [0,1]⇒ x_norm = (x - min(x)) / (max(x) - min(x))
    
    [-1,1]⇒ x_norm = (x - min(x)) / (max(x) - min(x))*2-1
    
    VD:
    
    | CO(GT) | CO(GT)_normalization_0_1 | CO(GT)_normalization_-1_1 |
    | --- | --- | --- |
    | 2,6 | 0,96 | 0,91 |
    | 2 | 0,95 | 0,91 |
    | 2,2 | 0,95 | 0,91 |
    | 2,2 | 0,95 | 0,91 |
    | 1,6 | 0,95 | 0,90 |
    | 1,2 | 0,95 | 0,90 |
    | 1,2 | 0,95 | 0,90 |
    | 1 | 0,95 | 0,90 |
    | 0,9 | 0,95 | 0,90 |
    | 0,6 | 0,95 | 0,89 |
    | -200 | 0,00 | -1,00 |
    | 0,7 | 0,95 | 0,89 |
    | 0,7 | 0,95 | 0,89 |
    | 1,1 | 0,95 | 0,90 |
    | 2 | 0,95 | 0,91 |
    | 2,2 | 0,95 | 0,91 |
    | 1,7 | 0,95 | 0,90 |
    | 1,5 | 0,95 | 0,90 |
2. Z-Score Normalization: Chuyển đổi dữ liệu sao cho giá trị trung bình bằng 0 và độ lệch chuẩn bằng 1, bằng cách sử dụng công thức sau:
x_norm = (x - mean(x)) / stdev(x)
    
    VD:
    
    | CO(GT) | CO(GT)_z-score |
    | --- | --- |
    | 2,6 | 0,47 |
    | 2 | 0,47 |
    | 2,2 | 0,47 |
    | 2,2 | 0,47 |
    | 1,6 | 0,46 |
    | 1,2 | 0,46 |
    | 1,2 | 0,46 |
    | 1 | 0,45 |
    | 0,9 | 0,45 |
    | 0,6 | 0,45 |
    | -200 | -2,13 |
    | 0,7 | 0,45 |
    | 0,7 | 0,45 |
    | 1,1 | 0,45 |
    | 2 | 0,47 |
    | 2,2 | 0,47 |
    | 1,7 | 0,46 |
    | 1,5 | 0,46 |
    
    ## Đo Độ Tương Đồng Của Dữ Liệu: Đo Độ Euclide
    
    Trong excel có thể sử dụng hai công thức sau:
    
    =SQRT(SUMSQ(A1:A2 - B1:B2))
    
    Trong đó:
    
    - A1:A2 là khoảng dữ liệu của thuộc tính 1 (ví dụ: CO(GT))
    - B1:B2 là khoảng dữ liệu của thuộc tính 2 (ví dụ: PT08.S1(CO))
    
    =SQRT(SUMXMY2(A2:A3,B2:B3))
    
    Trong đó:
    
    - A2:A3 và B2:B3 là phạm vi các giá trị của hai thuộc tính mà bạn muốn tính toán.
    
    VD:
    
    | CO(GT) | PT08.S1(CO) | Euclide_1 | Euclide_2 |
    | --- | --- | --- | --- |
    | 2,6 | 1360 | 1357,4 | 1357,4 |
    | 2 | 1292 | 1290,25 | 1290,3 |
    | 2,2 | 1402 | 1399,8 | 1399,8 |
    | 2,2 | 1376 | 1373,3 | 1373,3 |
    | 1,6 | 1272 | 1270,65 | 1270,7 |
    | 1,2 | 1197 | 1195,8 | 1195,8 |
    | 1,2 | 1185 | 1183,8 | 1183,8 |
    | 1 | 1136 | 1135,25 | 1135,3 |
    | 0,9 | 1094 | 1093,1 | 1093,1 |
    | 0,6 | 1010 | 1009,15 | 1009,2 |
    | -200 | 1011 | 1211 | 1211,0 |
    | 0,7 | 1066 | 1065,3 | 1065,3 |
    | 0,7 | 1052 | 1051,05 | 1051,1 |
    
    [AirQualityUCI.xlsx](Data-Air%20Quality%2028fb8fe5ea9548c08a6d17060b16c434/AirQualityUCI.xlsx)