driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://www.weightwatchers.com/us/")
assert "WW (Weight Watchers): Weight Loss & Wellness Help" in driver.title
elem_studio = driver.find_element_by_id("ela-menu-visitor-desktop-supplementa_find-a-studio")
elem_studio.click()
assert "Find a Studio & Meeting Near You | WW USA" in driver.title

elem_zip = driver.find_element_by_id("meetingSearch")
elem_zip.send_keys("10011")

# since we are blindly printing the first location name and distance so I believe
# the below code should print out the location name and distance whatever comes first.
# ideal way would be to get the container table id and then print the first element in the array.


elem_zip_results_name = driver.find_element_by_id("location__name")
print elem_zip_results_name.text

elem_zip_results_distance = driver.find_element_by_id("showDistance")
print elem_zip_results_distance.text

elem_zip_results_name.click()

##idea is to get the parent schdule-detailed element and iterate through schedule-detailed-day children
##elements and assign the day as the key and trainer info as the value(s) in the schedule{} dictionary
##when the definition is called using day as the key then it will return the trainer info

def returnSchedule(self, day):
	schedule = {}
	elem_schedule = driver.find_element_by_id("schedule-detailed")
	for (i=0; i<=length(elem_schedule); i++) {
		dayOfWeek = self.elem_schedule[i].find_element_by_id("schedule-detailed-day").text()
		trainer = self.elem_schedule[i].find_element_by_id("schedule-detailed-day-meetings").text()
		schedule.setdefault(dayOfWeek.append(value), trainer.append(value))
}
	for x, y in thisdict.items():
		if x.equals day:
			print(x, y)

returnSchedule("SUN")
