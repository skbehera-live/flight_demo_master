Feature: To test flight application login screen.

	Scenario: Validate login with invalid credential
		Given open the url "http://newtours.demoaut.com/"
		Then validate landing page "Welcome: Mercury Tours"
		When login with username "mercury" and password "merucry"
		Then validate landing page "Find a Flight:Mercury Tours"
		 
	Scenario: Validate with valid credential
		Given open the url "http://newtours.demoaut.com/"
		Then validate landing page "Welcome: Mercury Tours"
		When login with username "mercury" and password "mercury"
		Then validate landing page "Find a Flight: Mercury Tours:"
		 