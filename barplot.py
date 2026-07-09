from matplotlib import pyplot as plt
Country = ["Nepal", "Srilanka", "Bangladesh", "India",
"Bhutan","Madhives","Pakistan","Afganistan"]
GDP_growth_rate = [6.4, 4.5, 8.3, 7.4, 5.8,8.7,3.2,2.1]
# plot bars with Country as x-coordinate and GDP_growth_rate as height
plt.figure(figsize=(8,4))
plt.barh(Country, GDP_growth_rate)
plt.title("GDP Growth Rates of SAARC Countries") # add a title
plt.ylabel("GDP Growth Rate") # label the y-axis
plt.xlabel("Country")#label the x-axis
# label x-axis with movie names at bar centers
plt.show()