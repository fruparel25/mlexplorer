<<<<<<< HEAD
import os
import streamlit as st
import base64
#EDA packages
import pandas as pd
import webbrowser

#viz packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
from PIL import Image
import streamlit.components.v1 as components


# HtmlFile = open("style.html", 'r', encoding='utf-8')
# source_code = HtmlFile.read() 
# components.html(source_code)

#download file
# import base64
# import time
# timestr=time.strftime("%Y%m%d-%H%M%S")



# def file_selector(selected_filename):
# 		filenames=pd.read_csv(selected_filename)
# 		return filenames
#fxn
# def text_downloader(raw_text):
# 	b64 = base64.b64encode(raw_text.encode()).decode()
# 	new_filename="clean_text_result_{}_.text".format(timestr)
# 	st.markdown("### Downoad File ###") 
# 	href=f'<a href="data:file/txt:base64,{b64}", download={new_filename}">click here !</a>'
# 	st.markdown(href,unsafe_allow_html=True)
def main():
	st.markdown("<h1 style='text-align: center; color: black;'>DATASET EXPLORER</h1>", unsafe_allow_html=True)

	#st.title("\t DATASET EXPLORER")
	st.subheader("Upload CSV File")
	st.set_option('deprecation.showPyplotGlobalUse', False)
	selected_filename=st.file_uploader("",type=["csv"])
	if selected_filename is not None:
		st.write(type(selected_filename))
		file_details={"filename":selected_filename.name,"filetype":selected_filename.type,"filesize":selected_filename.size}
		st.write(file_details)
		#return selected_filename
		df=pd.read_csv(selected_filename)

	#filename=pd.read_csv(selected_filename)
	# st.info("You selected {}".format(filename))

	#Read data
		
	# text=open(filename,"r")
	# text=' '.join([i for i in text])
	# raw_text=text.replace(","," ")
	# raw_text=pd.read_csv(filename).decode('utf-8')
		f=1
	#Show Dataset
		if st.checkbox("Show Dataset"):
			number=st.number_input("Number of rows to view",min_value=1,max_value=10)
			st.dataframe(df.head(number))
	#Show columns
		if st.button("Column names"):
			st.write(df.columns)
	#Show Shape
		if st.checkbox("Shape of Dataset"):
		
			data_dim=st.radio("Show Dimension by",("Rows","Columns"))
			if data_dim=='Rows':
				st.text("Number of Rows")
				st.write(df.shape[0])
			elif data_dim=='Columns':
				st.text("Number of Columns")
				st.write(df.shape[1])
			else:
				st.write(df.shape)
	#Select Columns
		if st.checkbox("Select columns to show:"):
			all_columns=df.columns.tolist()
			selected_columns=st.multiselect("Select",all_columns)
			new_df=df[selected_columns]
			st.dataframe(new_df)
	# #Show values
	# if st.button("Value Counts:"):
	# 	st.text("Value counts by Target/Class")
	# 	st.write(df.iloc[:,-1].value_counts())

	#show summary
		if st.checkbox("Summary"):
			st.write(df.describe().T)

	##Plot and Visualization
		st.subheader("Data Visualization")
	#correlation 
	# Seaborn Plot
		if st.checkbox("Correlation plot[Seaborn]"):
			st.write(sns.heatmap(df.corr(),annot=True))
			st.pyplot()
	



	#pie chart

		if st.checkbox("Pie Plot"):
			all_columns_names=df.columns.tolist()
			if st.button("Generate Plot",key = "<uniquevalueofsomesort>"):
				st.success("Generating A Pie Plot")
				st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
				st.pyplot()
	#Count Plot
		if st.checkbox("Plot of value counts"):
			st.text("Value counts By Target")
			all_columns_names=df.columns.tolist()
			primary_col=st.selectbox("Primary column to groupBy",all_columns_names)
			selected_columns_names=st.multiselect("Select Columns",all_columns_names)
			if st.button("Plot"):
				st.text("|Generate Plot")
				if selected_columns_names:
					vc_plot=df.groupby(primary_col)[selected_columns_names].count()
				else:
					vc_plot=df.iloc[:,-1].value_counts()
				st.write(vc_plot.plot(kind="bar"))
				st.pyplot()





	#customizable Plot

		st.subheader("Customizable Plot")
		all_columns_names=df.columns.tolist()
		type_of_plot=st.selectbox("Select type of plot",["area","bar","line","hist","box","kde"])
		selected_columns_names=st.multiselect("Select Columns To Plot",all_columns_names)

		if st.button("Generate Plot"):
			st.success("Generate Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))
		#Plot by stramlit
			if type_of_plot=='area':
				cust_data=df[selected_columns_names]
				st.area_chart(cust_data)
			elif type_of_plot=='bar':
				cust_data=df[selected_columns_names]
				st.bar_chart(cust_data)
			elif type_of_plot=='line':
				cust_data=df[selected_columns_names]
				st.line_chart(cust_data)
			#custom plot 
			elif type_of_plot:
				cust_plot=df[selected_columns_names].plot(kind=type_of_plot)
				st.set_option('deprecation.showPyplotGlobalUse', False)
				st.write(cust_plot)
				st.pyplot()
		##if st.button("Thanks"):
	
			#	st.balloons()
	file_ = open("first.gif", "rb")
	contents = file_.read()
	data_url = base64.b64encode(contents).decode("utf-8")
	file_.close()

	st.markdown(
    	f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    	unsafe_allow_html=True,
	)		
	# st.write(raw_text)
	# text_downloader(raw_text)
if __name__ == '__main__':
=======
import os
import streamlit as st
import base64
#EDA packages
import pandas as pd
import webbrowser

#viz packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
from PIL import Image
import streamlit.components.v1 as components


# HtmlFile = open("style.html", 'r', encoding='utf-8')
# source_code = HtmlFile.read() 
# components.html(source_code)

#download file
# import base64
# import time
# timestr=time.strftime("%Y%m%d-%H%M%S")



# def file_selector(selected_filename):
# 		filenames=pd.read_csv(selected_filename)
# 		return filenames
#fxn
# def text_downloader(raw_text):
# 	b64 = base64.b64encode(raw_text.encode()).decode()
# 	new_filename="clean_text_result_{}_.text".format(timestr)
# 	st.markdown("### Downoad File ###") 
# 	href=f'<a href="data:file/txt:base64,{b64}", download={new_filename}">click here !</a>'
# 	st.markdown(href,unsafe_allow_html=True)
def main():
	st.markdown("<h1 style='text-align: center; color: black;'>DATASET EXPLORER</h1>", unsafe_allow_html=True)

	#st.title("\t DATASET EXPLORER")
	st.subheader("Upload CSV File")
	st.set_option('deprecation.showPyplotGlobalUse', False)
	selected_filename=st.file_uploader("",type=["csv"])
	if selected_filename is not None:
		st.write(type(selected_filename))
		file_details={"filename":selected_filename.name,"filetype":selected_filename.type,"filesize":selected_filename.size}
		st.write(file_details)
		#return selected_filename
		df=pd.read_csv(selected_filename)

	#filename=pd.read_csv(selected_filename)
	# st.info("You selected {}".format(filename))

	#Read data
		
	# text=open(filename,"r")
	# text=' '.join([i for i in text])
	# raw_text=text.replace(","," ")
	# raw_text=pd.read_csv(filename).decode('utf-8')
		f=1
	#Show Dataset
		if st.checkbox("Show Dataset"):
			number=st.number_input("Number of rows to view",min_value=1,max_value=10)
			st.dataframe(df.head(number))
	#Show columns
		if st.button("Column names"):
			st.write(df.columns)
	#Show Shape
		if st.checkbox("Shape of Dataset"):
		
			data_dim=st.radio("Show Dimension by",("Rows","Columns"))
			if data_dim=='Rows':
				st.text("Number of Rows")
				st.write(df.shape[0])
			elif data_dim=='Columns':
				st.text("Number of Columns")
				st.write(df.shape[1])
			else:
				st.write(df.shape)
	#Select Columns
		if st.checkbox("Select columns to show:"):
			all_columns=df.columns.tolist()
			selected_columns=st.multiselect("Select",all_columns)
			new_df=df[selected_columns]
			st.dataframe(new_df)
	# #Show values
	# if st.button("Value Counts:"):
	# 	st.text("Value counts by Target/Class")
	# 	st.write(df.iloc[:,-1].value_counts())

	#show summary
		if st.checkbox("Summary"):
			st.write(df.describe().T)

	##Plot and Visualization
		st.subheader("Data Visualization")
	#correlation 
	# Seaborn Plot
		if st.checkbox("Correlation plot[Seaborn]"):
			st.write(sns.heatmap(df.corr(),annot=True))
			st.pyplot()
	



	#pie chart

		if st.checkbox("Pie Plot"):
			all_columns_names=df.columns.tolist()
			if st.button("Generate Plot",key = "<uniquevalueofsomesort>"):
				st.success("Generating A Pie Plot")
				st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
				st.pyplot()
	#Count Plot
		if st.checkbox("Plot of value counts"):
			st.text("Value counts By Target")
			all_columns_names=df.columns.tolist()
			primary_col=st.selectbox("Primary column to groupBy",all_columns_names)
			selected_columns_names=st.multiselect("Select Columns",all_columns_names)
			if st.button("Plot"):
				st.text("|Generate Plot")
				if selected_columns_names:
					vc_plot=df.groupby(primary_col)[selected_columns_names].count()
				else:
					vc_plot=df.iloc[:,-1].value_counts()
				st.write(vc_plot.plot(kind="bar"))
				st.pyplot()





	#customizable Plot

		st.subheader("Customizable Plot")
		all_columns_names=df.columns.tolist()
		type_of_plot=st.selectbox("Select type of plot",["area","bar","line","hist","box","kde"])
		selected_columns_names=st.multiselect("Select Columns To Plot",all_columns_names)

		if st.button("Generate Plot"):
			st.success("Generate Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))
		#Plot by stramlit
			if type_of_plot=='area':
				cust_data=df[selected_columns_names]
				st.area_chart(cust_data)
			elif type_of_plot=='bar':
				cust_data=df[selected_columns_names]
				st.bar_chart(cust_data)
			elif type_of_plot=='line':
				cust_data=df[selected_columns_names]
				st.line_chart(cust_data)
			#custom plot 
			elif type_of_plot:
				cust_plot=df[selected_columns_names].plot(kind=type_of_plot)
				st.set_option('deprecation.showPyplotGlobalUse', False)
				st.write(cust_plot)
				st.pyplot()
		##if st.button("Thanks"):
	
			#	st.balloons()
	file_ = open("first.gif", "rb")
	contents = file_.read()
	data_url = base64.b64encode(contents).decode("utf-8")
	file_.close()

	st.markdown(
    	f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    	unsafe_allow_html=True,
	)		
	# st.write(raw_text)
	# text_downloader(raw_text)
if __name__ == '__main__':
>>>>>>> b25be913c137ac6a7bc3b13a3244c0393193f545
	main()