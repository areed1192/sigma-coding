import json
import pathlib
import requests

from typing import List
from typing import Dict
from typing import Union


class Congress():

    def __init__(self) -> None:
        """Initializes the `Congress` client object."""

        # Define the base url.
        self.api_base_url = 'https://www.govinfo.gov'

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        Returns:
        ----
        (str): The string representation.
        """
        return "<CongressClient Connected: True>"

    def save_to_json(self, content: Union[List, Dict], file_name: str) -> str:
        """Saves content to a JSON file.

        Arguments:
        ----
        content (Union[List, Dict]): The content to be saved to the JSON file.

        file_name (str): The file name or file path to the file.

        Returns:
        ----
        str: The path to the file.
        """

        # Grab the file path.
        file_path = pathlib.Path(file_name)

        # Save the content.
        with open(file=file_path, mode='w+') as data_file:
            json.dump(obj=content, fp=data_file, indent=2)

        return str(file_path)

    def _build_url(self, endpoint: str, arguments: List[str] = None) -> str:
        """Builds a full URL for the API Client.

        Arguments:
        ----
        endpoint (str): The endpoint to be requested.

        arguments (List[str]): Any additional arguments needed to be
            joined with the URL.

        Returns:
        ----
        str: The full `HTTPS` url.
        """

        # If we have arguments we need to join that.
        if arguments:
            full_url = '/'.join(
                [self.api_base_url, endpoint] + arguments
            )
        else:
            full_url = '/'.join(
                [self.api_base_url, endpoint]
            )

        full_url_with_format = full_url

        return full_url_with_format

    def _make_request(self, url: str, method: str, params: dict = None) -> dict:
        """Used to make all the request for the client.

        Arguments:
        ----
        url (str): The url to the specified endpoint.

        method (str): The request method to make.

        params (dict): Parameters to send along in the request.

        Returns:
        ----
        dict: The JSON content parsed.
        """

        # Define the headers.
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9'
        }

        # Make the request.
        if method == 'get':
            response = requests.get(url=url, headers=headers, verify=True)

        # If it's a good response, send back.
        if response.ok:
            return response.json()

    def data_sources(self) -> List[Dict]:
        """Grabs all the data sources provided.

        Returns:
        ----
        List[Dict]: A list of database resources.
        """

        # Build the URL.
        full_url = self._build_url(endpoint='bulkdata/json')

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def privacy_act_issuances(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the Privacy Act Issuances Resource.

        Arguments:
        ----
        Folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/PAI/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def code_of_federal_regulations(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the Code of Federal Regulations Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/CFR/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def federal_register(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the Federal Register Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/FR/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def bill_status(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the Bill Status Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/BILLSTATUS/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def commerce_business_daily(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the Commerce Business Daily Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/CBD/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def public_papers_president(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the Public Papers of the Presidents of the United States Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/PPP/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def supreme_court_decisions(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the Supreme Court Decisions 1937-1975 (FLITE) Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/SCD/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def congressional_bills(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the Congressional Bills Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/BILLS/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def us_government_manuals(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the United States Government Manual Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/GOVMAN/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def bill_summaries(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the Bill Summaries Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/BILLSUM/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def electronic_code_of_federal_regulation(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the Electronic Code of Federal Regulations Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/ECFR/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def house_rules_and_manual(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the House Rules and Manual Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/HMAN/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def private_and_public_laws(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the Public and Private Laws (xml uslm beta) Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/PLAW/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content

    def statutes_at_large(self, folder: str) -> List[Dict]:
        """Grabs the data resources for the specified folder under the Statutes at Large (xml uslm beta) Resource.

        Arguments:
        ----
        folder (str): The name of the folder resource to return.

        Returns:
        ----
        List[Dict]: A list of file resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='bulkdata/json/STATUTE/{folder}'.format(folder=folder)
        )

        # Make the request.
        content = self._make_request(
            url=full_url,
            method='get'
        )

        return content
