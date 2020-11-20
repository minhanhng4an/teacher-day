import streamlit as st

st.sidebar.image("images/logo.png",width=250)
st.title("Thank You, Teachers.")

st.image("https://scontent.fhan3-2.fna.fbcdn.net/v/t1.0-9/125547783_1453904614804066_5972756217967473930_o.jpg?_nc_cat=107&ccb=2&_nc_sid=0debeb&_nc_ohc=heol_ZwJrygAX_rbDIK&_nc_ht=scontent.fhan3-2.fna&oh=74753ae59cb5a5db3e392ebc74a4cf5c&oe=5FDD2E76",
        width=800,
        caption="Vietnamese Teacher's Day 2020 at CoderSchool")

st.markdown("""
I had more than one year working at [CoderSchool](https://www.coderschool.vn/en/) as a member of the Academic team. My job involed preparing materials and teaching our students the necessary knowledge and skills to get them ready for the job market. However, I wouldn't exactly call myself a teacher, as I believe it takes much more than that to be one. In the past, I had the priviledge to be taught by many wonderful teachers, who not only inspired us to pursue our dream, but also were role models because of their kindess and diligence. Three years later after my graduation, only when I took part in a similar role did I truly realize how hard it must be to be teacher!

So in this special blog post to celebrate the Vietnamese Teacher's Day, I would like to take the opportunity to have a closer investigation, with the help of data and visualization tools, into the difficulties and struggles of Vietnamese teachers in their mission to educate generations of students.

_The data in this blog is preprocessed and visualized using Python library Pandas and Matplotlib. If you are interested in learning how the charts are made, select the option Show/Hide Code on the left sidebar._""")

show_code = st.sidebar.checkbox("Show/Hide Code")


if show_code:
  with st.echo():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from cycler import cycler

else:
  import pandas as pd
  import matplotlib.pyplot as plt
  import numpy as np
  from cycler import cycler


if show_code:
  with st.echo():
    light_red = "#e74c3c" 
    dark_red = "#c0392b"
    green = "#27ae60"
    light_gray = "#95a5a6"
    dark_gray = "#7f8c8d"

    plt.style.use("seaborn")
    plt.rcParams["axes.facecolor"] = "#ecf0f1"
    plt.rcParams['axes.grid'] = False
    plt.rcParams['axes.prop_cycle'] = cycler(color=[light_red])

    title_fontdict = {"color":dark_gray, "weight":"bold"}
  
else:
  light_red = "#e74c3c" 
  dark_red = "#c0392b"
  green = "#27ae60"
  light_gray = "#95a5a6"
  dark_gray = "#7f8c8d"

  plt.style.use("seaborn")
  plt.rcParams["axes.facecolor"] = "#ecf0f1"
  plt.rcParams['axes.grid'] = False
  plt.rcParams['axes.prop_cycle'] = cycler(color=[light_red])

  title_fontdict = {"color":dark_gray, "weight":"bold"}

st.header("Increasing Pressure")
st.markdown("""The Pupil-Teacher ratio shows the average number of students that a full-time teacher takes care of. This statistic in Vietnam has been growing significantly over the last 5 years, especially between Grade 1 to 9. Higher Pupil-Teacher ratio generally means a great workloads and more responsibilities for teachers.""")

if show_code:
  with st.echo():
    # ----- Pupil-Teacher Ratio -----
    wb_data = pd.read_csv("data/data.csv")
    pt_ratio_vn = pd.read_csv("data/pt_ratio_vn.csv")

    pt_ratio_vn["Type"] = pt_ratio_vn["Type"].str.lower() # Lowercase indicator names

    year_range = np.arange(2014, 2021) # Data Range

    # School Level - User Input
    s_level = ["Total","Upper Secondary","Lower Secondary","Primary"]
    s_level_sbox = st.selectbox("Filter by School Level", s_level)

    # Map school level to global data indicators
    if s_level_sbox == "Total":
      s_level_choice = s_level[1:]
    else:
      s_level_choice = [s_level_sbox]

    s_level_choice = list(map(lambda x: "Pupil-teacher ratio, " + x.lower(),s_level_choice))

    # Filter data by indicator and user input
    pt_ratio_global = wb_data[wb_data["Indicator Name"].isin(s_level_choice)].mean() # Indicator
    pt_ratio_global.index = pt_ratio_global.index.astype("int") # Convert index to int
    pt_ratio_global = pt_ratio_global.loc[year_range] # Year Range

    pt_ratio_vn = pt_ratio_vn[pt_ratio_vn["Type"] == s_level_sbox.lower()].T.iloc[1:] # Indicator
    pt_ratio_vn.index = pt_ratio_vn.index.astype("int") # Convert index to int
    pt_ratio_vn = pt_ratio_vn.loc[year_range].squeeze() # Year Range

    # Draw plot
    fig, ax = plt.subplots()

    ax.set_title("Pupil-Teacher Ratio", title_fontdict)

    ax.plot(pt_ratio_global.index, pt_ratio_global.values, color=light_gray, marker="o", label="Global")
    for i, v in zip(pt_ratio_global.index, pt_ratio_global.values):
      ax.text(i, v * 1.005, round(v, 2), {"color":dark_gray,"ha":"center"})

    ax.plot(pt_ratio_vn.index, pt_ratio_vn.values, color=light_red, marker="o", label = "Vietnam")
    for i, v in zip(pt_ratio_vn.index, pt_ratio_vn.values):
      ax.text(i, v * 1.005, round(v, 2), {"color":dark_red,"ha":"center"})

    ax.legend(loc=4)

    ax.set_xlabel("Year")
    ax.set_ylabel("Ratio")

    st.pyplot(fig)

else:
  # ----- Pupil-Teacher Ratio -----
  wb_data = pd.read_csv("data/data.csv")
  pt_ratio_vn = pd.read_csv("data/pt_ratio_vn.csv")

  pt_ratio_vn["Type"] = pt_ratio_vn["Type"].str.lower() # Lowercase indicator names

  year_range = np.arange(2014, 2021) # Data Range

  # School Level - User Input
  s_level = ["Total","Upper Secondary","Lower Secondary","Primary"]
  s_level_sbox = st.selectbox("Filter by School Level", s_level)

  # Map school level to global data indicators
  if s_level_sbox == "Total":
    s_level_choice = s_level[1:]
  else:
    s_level_choice = [s_level_sbox]

  s_level_choice = list(map(lambda x: "Pupil-teacher ratio, " + x.lower(),s_level_choice))

  # Filter data by indicator and user input
  pt_ratio_global = wb_data[wb_data["Indicator Name"].isin(s_level_choice)].mean() # Indicator
  pt_ratio_global.index = pt_ratio_global.index.astype("int") # Convert index to int
  pt_ratio_global = pt_ratio_global.loc[year_range] # Year Range

  pt_ratio_vn = pt_ratio_vn[pt_ratio_vn["Type"] == s_level_sbox.lower()].T.iloc[1:] # Indicator
  pt_ratio_vn.index = pt_ratio_vn.index.astype("int") # Convert index to int
  pt_ratio_vn = pt_ratio_vn.loc[year_range].squeeze() # Year Range

  # Draw plot
  fig, ax = plt.subplots()

  ax.set_title("Pupil-Teacher Ratio", title_fontdict)

  ax.plot(pt_ratio_global.index, pt_ratio_global.values, color=light_gray, marker="o", label="Global")
  for i, v in zip(pt_ratio_global.index, pt_ratio_global.values):
    ax.text(i, v * 1.005, round(v, 2), {"color":dark_gray,"ha":"center"})

  ax.plot(pt_ratio_vn.index, pt_ratio_vn.values, color=light_red, marker="o", label = "Vietnam")
  for i, v in zip(pt_ratio_vn.index, pt_ratio_vn.values):
    ax.text(i, v * 1.005, round(v, 2), {"color":dark_red,"ha":"center"})

  ax.legend(loc=4)

  ax.set_xlabel("Year")
  ax.set_ylabel("Ratio")

  st.pyplot(fig)

st.markdown("""Another important factor that reflects the pressure that teachers have to suffer is working hour. Data collected from a survey conducted by the [Organisation for Economic Co-operation and Development (OECD)](https://data.oecd.org/education.htm) in 2018 ranked Vietnam 6th among 37 countries in teacher's weekly working hours. A Vietnamese teacher has to work 46.8 hour per week, 17% higher than the OECD average.""")

if show_code:
  with st.echo():
    # ----- Working Hours -----
    wh_data = pd.read_csv("data/working_hours.csv")
    wh_data.sort_values(by="Working Hour", ascending = False, inplace = True)

    plot_type = st.selectbox("Aggregation",["Top 10", "Average"])

    fig, ax = plt.subplots()

    if plot_type == "Top 10":
      wh_data = wh_data.head(10)
    else:
      wh_data_vn = wh_data[wh_data["Country"] == "Viet Nam"]
      wh_data["Country"] = "OECD Average"
      wh_data = wh_data.groupby("Country").mean().reset_index()
      wh_data = wh_data.append(wh_data_vn)

    ax.barh(wh_data["Country"], wh_data["Working Hour"])
    ax.set_xlim(30, wh_data["Working Hour"].max() * 1.1)

    bars = ax.get_children()

    for i, (c, w) in enumerate(zip(wh_data["Country"], wh_data["Working Hour"])):
      color = dark_red

      if c != "Viet Nam":
        bars[i].set_color(dark_gray)
        color = dark_gray

      ax.text(w * 1.01, i, round(w, 2), {"color":color ,"ha":"left","va":"center"})

    ax.set_title("Weekly Working Hours of Teachers in OECD Countries", title_fontdict)
    ax.set_xlabel("Hours")
    ax.set_ylabel("Country")

    st.pyplot(fig)

else:
    # ----- Working Hours -----
    wh_data = pd.read_csv("data/working_hours.csv")
    wh_data.sort_values(by="Working Hour", ascending = False, inplace = True)

    plot_type = st.selectbox("Aggregation",["Top 10", "Average"])

    fig, ax = plt.subplots()

    if plot_type == "Top 10":
      wh_data = wh_data.head(10)
    else:
      wh_data_vn = wh_data[wh_data["Country"] == "Viet Nam"]
      wh_data["Country"] = "OECD Average"
      wh_data = wh_data.groupby("Country").mean().reset_index()
      wh_data = wh_data.append(wh_data_vn)

    ax.barh(wh_data["Country"], wh_data["Working Hour"])
    ax.set_xlim(30, wh_data["Working Hour"].max() * 1.1)

    bars = ax.get_children()

    for i, (c, w) in enumerate(zip(wh_data["Country"], wh_data["Working Hour"])):
      color = dark_red

      if c != "Viet Nam":
        bars[i].set_color(dark_gray)
        color = dark_gray

      ax.text(w * 1.01, i, round(w, 2), {"color":color ,"ha":"left","va":"center"})

    ax.set_title("Weekly Working Hours of Teachers in OECD Countries", title_fontdict)
    ax.set_xlabel("Hours")
    ax.set_ylabel("Country")

    st.pyplot(fig)

if show_code:
  with st.echo():
    # ---- Impact of Covid-19 ----
    st.header("Impacts of Covid-19")

    st.markdown("""Back to the beginning of March this year, CoderSchool had to switch to online classes due to the influence of Covid-19. Grade schools in Vietnam were closed a few weeks before we did, and universities oon followed. Nevertheless, many schools nationwide soon adopted online teaching. I still remember vividly how challenging it was for our team to maintain a good teaching quality in a completely different teaching environment. Despite only going through the period briefly, I could partly feel how much of a struggle it was for many teachers in Vietnam, who continued their works virtually. [A recent study](https://www.sciencedirect.com/science/article/pii/S235234092030682X) of 294 Vietnamese teachers uncovered the impacts of the pandemic to their work and life, financially, physically as well as mentally.""")

    teacher_covid_data = pd.read_csv("data/teacher_covid_data.csv")

    # School Type Survey Code
    s_type_code = {
      1: "Public",
      2: "Private (normal)",
      3: "Private (bilingual/international)",
      4: "Continuing Education Center",
      5: "Other"
    }

    # Map School Sype responses
    teacher_covid_data["School_type"].replace(s_type_code, inplace=True)


    # School Type - User Input
    s_type_sbox = st.selectbox("Filter by School Type", ["Total"] + list(s_type_code.values()))

    if s_type_sbox == "Total":
      s_type_choice = list(s_type_code.values())
    else:
      s_type_choice = [s_type_sbox]


    # Filter data by School Type
    teacher_covid_data = teacher_covid_data[teacher_covid_data["School_type"].isin(s_type_choice)]


    # Stress & Workload
    fig, axes = plt.subplots(2)

    fig.subplots_adjust(hspace = 0.4)

    for i, col in enumerate(["Onl_stress", "Onl_workload"]):

      mean_value = round(teacher_covid_data[col].mean(), 2)

      teacher_covid_sw = teacher_covid_data[col].value_counts().sort_index()
      teacher_covid_sw = teacher_covid_sw.reindex(np.arange(1, 6)).fillna(0)
      axes[i].bar(teacher_covid_sw.index, teacher_covid_sw.values)
      axes[i].set_ylim(0, teacher_covid_sw.values.max() * 1.2)
      axes[i].set_xticklabels(["0","1 - Totally Disagree", "2", "3", "4", "5 - Totally Agree"])
      axes[i].set_ylabel("No. of Responses")

      for j, v in zip(teacher_covid_sw.index, teacher_covid_sw.values):
        axes[i].text(j, v + 3, v, {"color":dark_red,"ha":"center"})  

      axes[i].text(0.5, teacher_covid_sw.max(), 
                  f"MEAN: {mean_value}", 
                  {"color":light_gray,"ha":"left","va":"top","weight":"bold","size":15})
    

    axes[0].set_title("I feel stressful because of online teaching", title_fontdict)
    axes[1].set_title("I feel that the teaching workload is much more than before COVID-19", title_fontdict)

    st.pyplot(fig)

else:
  # ---- Impact of Covid-19 ----
  st.header("Impacts of Covid-19")

  st.markdown("""Back to the beginning of March this year, CoderSchool had to switch to online classes due to the influence of Covid-19. Grade schools in Vietnam were closed a few weeks before we did, and universities oon followed. Nevertheless, many schools nationwide soon adopted online teaching. I still remember vividly how challenging it was for our team to maintain a good teaching quality in a completely different teaching environment. Despite only going through the period briefly, I could partly feel how much of a struggle it was for many teachers in Vietnam, who continued their works virtually. [A recent study](https://www.sciencedirect.com/science/article/pii/S235234092030682X) of 294 Vietnamese teachers uncovered the impacts of the pandemic to their work and life, financially, physically as well as mentally.""")

  teacher_covid_data = pd.read_csv("data/teacher_covid_data.csv")

  # School Type Survey Code
  s_type_code = {
    1: "Public",
    2: "Private (normal)",
    3: "Private (bilingual/international)",
    4: "Continuing Education Center",
    5: "Other"
  }

  # Map School Sype responses
  teacher_covid_data["School_type"].replace(s_type_code, inplace=True)


  # School Type - User Input
  s_type_sbox = st.selectbox("Filter by School Type", ["Total"] + list(s_type_code.values()))

  if s_type_sbox == "Total":
    s_type_choice = list(s_type_code.values())
  else:
    s_type_choice = [s_type_sbox]


  # Filter data by School Type
  teacher_covid_data = teacher_covid_data[teacher_covid_data["School_type"].isin(s_type_choice)]


  # Stress & Workload
  fig, axes = plt.subplots(2)

  fig.subplots_adjust(hspace = 0.4)

  for i, col in enumerate(["Onl_stress", "Onl_workload"]):

    mean_value = round(teacher_covid_data[col].mean(), 2)

    teacher_covid_sw = teacher_covid_data[col].value_counts().sort_index()
    teacher_covid_sw = teacher_covid_sw.reindex(np.arange(1, 6)).fillna(0)
    axes[i].bar(teacher_covid_sw.index, teacher_covid_sw.values)
    axes[i].set_ylim(0, teacher_covid_sw.values.max() * 1.2)
    axes[i].set_xticklabels(["0","1 - Totally Disagree", "2", "3", "4", "5 - Totally Agree"])
    axes[i].set_ylabel("No. of Responses")

    for j, v in zip(teacher_covid_sw.index, teacher_covid_sw.values):
      axes[i].text(j, v + 3, v, {"color":dark_red,"ha":"center"})  

    axes[i].text(0.5, teacher_covid_sw.max(), 
                f"MEAN: {mean_value}", 
                {"color":light_gray,"ha":"left","va":"top","weight":"bold","size":15})
  

  axes[0].set_title("I feel stressful because of online teaching", title_fontdict)
  axes[1].set_title("I feel that the teaching workload is much more than before COVID-19", title_fontdict)

  st.pyplot(fig)

st.markdown("""While the respondents were under little stress teaching online, many of them felt a much higher workload during this period. This is most likely due to the additional works required to redesign the lectures and logistics around managing virtual classes. The increased workload, combined with long and continuos screen time could be the major factors that led to the decrease in their physical health.""")

if show_code:
  with st.echo():
    # Health & Habit
    fig, axes = plt.subplots(2)

    fig.subplots_adjust(hspace = 0.4)

    for i, col in enumerate(["Feel_covid", "Feel_habit"]):

      mean_value = round(teacher_covid_data[col].mean(), 2)

      teacher_covid_hh = teacher_covid_data[col].value_counts().sort_index()
      teacher_covid_hh = teacher_covid_hh.reindex(np.arange(1, 6)).fillna(0)

      axes[i].bar(teacher_covid_hh.index, teacher_covid_hh.values)
      axes[i].set_ylim(0, teacher_covid_hh.values.max() * 1.2)
      axes[i].set_xticklabels(["0","1 - Totally Disagree", "2", "3", "4", "5 - Totally Agree"])
      axes[i].set_ylabel("No. of Responses")

      for j, v in zip(teacher_covid_hh.index, teacher_covid_hh.values):
        axes[i].text(j, v + 3, v, {"color":dark_red,"ha":"center"})   

      axes[i].text(0.5, teacher_covid_hh.max(), 
                  f"MEAN: {mean_value}", 
                  {"color":light_gray,"ha":"left","va":"top","weight":"bold","size":15})

    axes[0].set_title("In overall, COVID-19 is affecting your health?", title_fontdict)
    axes[1].set_title("COVID-19 changed your daily habit and make you tired?", title_fontdict)

    st.pyplot(fig)

else:
  # Health & Habit
  fig, axes = plt.subplots(2)

  fig.subplots_adjust(hspace = 0.4)

  for i, col in enumerate(["Feel_covid", "Feel_habit"]):

    mean_value = round(teacher_covid_data[col].mean(), 2)

    teacher_covid_hh = teacher_covid_data[col].value_counts().sort_index()
    teacher_covid_hh = teacher_covid_hh.reindex(np.arange(1, 6)).fillna(0)

    axes[i].bar(teacher_covid_hh.index, teacher_covid_hh.values)
    axes[i].set_ylim(0, teacher_covid_hh.values.max() * 1.2)
    axes[i].set_xticklabels(["0","1 - Totally Disagree", "2", "3", "4", "5 - Totally Agree"])
    axes[i].set_ylabel("No. of Responses")

    for j, v in zip(teacher_covid_hh.index, teacher_covid_hh.values):
      axes[i].text(j, v + 3, v, {"color":dark_red,"ha":"center"})   

    axes[i].text(0.5, teacher_covid_hh.max(), 
                f"MEAN: {mean_value}", 
                {"color":light_gray,"ha":"left","va":"top","weight":"bold","size":15})

  axes[0].set_title("In overall, COVID-19 is affecting your health?", title_fontdict)
  axes[1].set_title("COVID-19 changed your daily habit and make you tired?", title_fontdict)

  st.pyplot(fig)

st.markdown("""Covid-19 caused significant damage to the national and global economy. Unfortunately, a large number of Vietnamese teachers also had to suffer financially due to schools being closed down. The same study reported salary cuts among more than 60% respondents, some by a great deal.""")

if show_code:
  with st.echo():
    # Finance
    fig, ax = plt.subplots()

    teacher_covid_finance = (teacher_covid_data["Income_during"] - teacher_covid_data["Income_before"])

    mean_value = round(teacher_covid_finance.mean(),2)

    teacher_covid_finance = teacher_covid_finance.value_counts().sort_index()
    teacher_covid_finance = teacher_covid_finance.reindex(np.arange(-4, 5)).fillna(0)

    ax_xticks = np.arange(-4, 5)

    ax.bar(ax_xticks, teacher_covid_finance.values)
    ax.set_ylim(0, teacher_covid_finance.values.max() * 1.1)

    bars = ax.get_children()

    for i, (l, v) in enumerate(zip(ax_xticks, teacher_covid_finance.values)):
      color = dark_red

      if l == 0:
        bars[i].set_color(dark_gray)
        color = dark_gray
      elif l > 0:
        bars[i].set_color(green)
        color = green

      ax.text(l, v + 1, int(v), {"color":color,"ha":"center","va":"bottom"}) 

    ax.text(-4.5, teacher_covid_finance.max(), 
                  f"MEAN: {mean_value}", 
                  {"color":light_gray,"ha":"left","va":"top","weight":"bold","size":15})

    ax.set_title("Change in Salary Level during Covid-19", title_fontdict)
    ax.set_xlabel("Change in Salary Level")
    ax.set_ylabel("No. of Responses")

    ax.locator_params(nbins = 10)

    st.pyplot(fig)

else:
  # Finance
  fig, ax = plt.subplots()

  teacher_covid_finance = (teacher_covid_data["Income_during"] - teacher_covid_data["Income_before"])

  mean_value = round(teacher_covid_finance.mean(),2)

  teacher_covid_finance = teacher_covid_finance.value_counts().sort_index()
  teacher_covid_finance = teacher_covid_finance.reindex(np.arange(-4, 5)).fillna(0)

  ax_xticks = np.arange(-4, 5)

  ax.bar(ax_xticks, teacher_covid_finance.values)
  ax.set_ylim(0, teacher_covid_finance.values.max() * 1.1)

  bars = ax.get_children()

  for i, (l, v) in enumerate(zip(ax_xticks, teacher_covid_finance.values)):
    color = dark_red

    if l == 0:
      bars[i].set_color(dark_gray)
      color = dark_gray
    elif l > 0:
      bars[i].set_color(green)
      color = green

    ax.text(l, v + 1, int(v), {"color":color,"ha":"center","va":"bottom"}) 

  ax.text(-4.5, teacher_covid_finance.max(), 
                f"MEAN: {mean_value}", 
                {"color":light_gray,"ha":"left","va":"top","weight":"bold","size":15})

  ax.set_title("Change in Salary Level during Covid-19", title_fontdict)
  ax.set_xlabel("Change in Salary Level")
  ax.set_ylabel("No. of Responses")

  ax.locator_params(nbins = 10)

  st.pyplot(fig)



st.header("Final Words")

st.markdown("""Despite numerous problems and difficulties, the pandemic may present a silver lining in the opportunity to develop e-learning as supplementary method for delivering education. And teachers are the front line in this adaptation.

From this short blog, I would like to extend the most sincere appreciation to teachers all around Vietnam and the world, for their continuing and indispensable contribution to the development of the society. Happy Vietnamese Teacher's Day!""")

