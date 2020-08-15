import json
import pathlib
import requests

from typing import List
from typing import Dict
from typing import Union

from federal_register.fields import document_fields
from federal_register.fields import public_document_fields


class FederalRegister():

    def __init__(self) -> None:
        """Initializes the `FederalRegisterClient` object."""

        self.api_base_url = 'https://www.federalregister.gov/api'
        self.api_version = 'v1'

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        Returns:
        ----
        (str): The string representation.
        """
        return "<FederalRegisterClient Connected: True>"

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
                [self.api_base_url, self.api_version, endpoint] + arguments
            )
        else:
            full_url = '/'.join(
                [self.api_base_url, self.api_version, endpoint]
            )

        full_url_with_format = full_url + '.json'

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

        # Make the request.
        if method == 'get':
            response = requests.get(url=url, params=params)

        # If it's a good response, send back.
        if response.ok:
            return response.json()

    def documents(self, fields: List[str] = 'all', per_page: int = 100, page_id: int = None, order: List[str] = ['newest'], terms: str = None,
                  publication_date_is: str = None, publication_date_year: str = None, publication_date_greater_than: str = None,
                  publication_date_less_than: str = None, effective_date_is: str = None, effective_date_year: str = None,
                  effective_date_greater_than: str = None, effective_date_less_than: str = None, agencies: List[str] = None,
                  document_type: List[str] = None, presidential_document_type: List[str] = None, presidents: List[str] = None,
                  docket_id: str = None, regulation_id: str = None, section_ids: List[str] = None, topic_ids: List[str] = None,
                  is_significant: str = None, cfr_title: int = None, cfr_part: int = None, location: str = None, location_within: int = None
                  ) -> dict:
        """Allows for a more specific search for documents by providing different filters to limit the results.

        Arguments:
        ----
        fields (List[str], optional): Which attributes of the documents to return; by default, 
            a reasonable set is returned, but a user can customize it to return exactly what 
            is needed. Defaults to 'all'.

        per_page (int, optional): The number of results to return per page.
            Defaults to 100.

        page_id (int, optional): The page of the result set. Defaults to None.

        order (List[str], optional): The order the results should be returned 
            in. Defaults to ['newest'].

        terms (str, optional): Full text search. Defaults to None.

        publication_date_is (str, optional): Exact publication date 
            match (YYYY-MM-DD). Defaults to None.

        publication_date_year (str, optional): Find documents published 
            in a given year (YYYY). Defaults to None.

        publication_date_greater_than (str, optional): Find documents published 
            on or after a given date (YYYY-MM-DD). Defaults to None.

        publication_date_less_than (str, optional): Find documents published on or 
            before a given date (YYYY-MM-DD). Defaults to None.

        effective_date_is (str, optional): Exact effective date 
            match (YYYY-MM-DD). Defaults to None.

        effective_date_year (str, optional): Find documents with an effective date 
            in a given year (YYYY). Defaults to None.

        effective_date_greater_than (str, optional): Find documents with an effective 
            date on or after a given date (YYYY-MM-DD). Defaults to None.

        effective_date_less_than (str, optional): Find documents with an effective date 
            on or before a given date (YYYY-MM-DD). Defaults to None.

        agencies (List[str], optional): Publishing agency. Defaults to None.

        document_type (List[str], optional): The Document Type. Defaults to None.

        presidential_document_type (List[str], optional): Presidential document type; only 
            available for Presidential Docuements. Defaults to None.

        presidents (List[str], optional): Signing President; only available for Presidential 
            Documents. Defaults to None.

        docket_id (str, optional): Agency docket number associated with 
            document. Defaults to None.

        regulation_id (str, optional): Regulation ID Number (RIN) associated 
            with document. Defaults to None.

        section_ids (List[str], optional): Limit to documents that appeared within 
            a particular section of FederalRegister.gov. Defaults to None.

        topic_ids (List[str], optional): Limit to documents associated with a particular 
            topic (CFR Indexing term). Defaults to None.

        is_significant (str, optional): Deemed Significant Under EO 12866. 
            Defaults to None.

        cfr_title (int, optional): Documents affecting the associated CFR 
            title. Defaults to None.

        cfr_part (int, optional): Part or part range (eg '17' or '1-50'); requires the 
            CFR title to be provided. Defaults to None.

        location (str, optional): Location search; enter zipcode or City and 
            State. Defaults to None.

        location_within (int, optional): Location search; maximum distance from 
            location in miles (max 200). Defaults to None.   

        Returns:
        ----
        dict: The federal document with the specified fields.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='documents'
        )

        # Grab all fields, if is `all`.
        if fields == 'all':
            fields = document_fields

        # Define the paramters.
        params = {
            'fields[]': fields,
            'per_page': per_page,
            'page': page_id,
            'order': order,
            'conditions[term]': terms,
            'conditions[publication_date][is]': publication_date_is,
            'conditions[publication_date][year]': publication_date_year,
            'conditions[publication_date][gte]': publication_date_greater_than,
            'conditions[publication_date][lte]': publication_date_less_than,
            'conditions[effective_date][is]': effective_date_is,
            'conditions[effective_date][year]': effective_date_year,
            'conditions[effective_date][gte]': effective_date_greater_than,
            'conditions[effective_date][lte]': effective_date_less_than,
            'conditions[agencies][]': agencies,
            'conditions[type][]': document_type,
            'conditions[presidential_document_type][]': presidential_document_type,
            'conditions[president][]': presidents,
            'conditions[docket_id]': docket_id,
            'conditions[regulation_id_number]': regulation_id,
            'conditions[sections][]': section_ids,
            'conditions[topics][]': topic_ids,
            'conditions[significant]': is_significant,
            'conditions[cfr][title]': cfr_title,
            'conditions[cfr][part]': cfr_part,
            'conditions[near][location]': location,
            'conditions[near][within]': location_within
        }

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get',
            params=params
        )

        return response

    def documents_facets(self, facet: str = 'daily', terms: str = None, publication_date_is: str = None, publication_date_year: str = None,
                         publication_date_greater_than: str = None, publication_date_less_than: str = None, effective_date_is: str = None,
                         effective_date_year: str = None, effective_date_greater_than: str = None, effective_date_less_than: str = None,
                         agencies: List[str] = None, document_type: List[str] = None, presidential_document_type: List[str] = None,
                         presidents: List[str] = None, docket_id: str = None, regulation_id: str = None, section_ids: List[str] = None,
                         topic_ids: List[str] = None, is_significant: str = None, cfr_title: int = None, cfr_part: int = None,
                         location: str = None, location_within: int = None
                         ) -> dict:
        """Allows for a more specific search for documents and grouping by facet.

        Arguments:
        ----
        facet (str, optional): What to group the returned documents 
            by for counting. Defaults to 'daily'.

        terms (str, optional): Full text search. Defaults to None.

        publication_date_is (str, optional): Exact publication date 
            match (YYYY-MM-DD). Defaults to None.

        publication_date_year (str, optional): Find documents published 
            in a given year (YYYY). Defaults to None.

        publication_date_greater_than (str, optional): Find documents published 
            on or after a given date (YYYY-MM-DD). Defaults to None.

        publication_date_less_than (str, optional): Find documents published on or 
            before a given date (YYYY-MM-DD). Defaults to None.

        effective_date_is (str, optional): Exact effective date 
            match (YYYY-MM-DD). Defaults to None.

        effective_date_year (str, optional): Find documents with an effective date 
            in a given year (YYYY). Defaults to None.

        effective_date_greater_than (str, optional): Find documents with an effective 
            date on or after a given date (YYYY-MM-DD). Defaults to None.

        effective_date_less_than (str, optional): Find documents with an effective date 
            on or before a given date (YYYY-MM-DD). Defaults to None.

        agencies (List[str], optional): Publishing agency. Defaults to None.

        document_type (List[str], optional): The Document Type. Defaults to None.

        presidential_document_type (List[str], optional): Presidential document type; only 
            available for Presidential Docuements. Defaults to None.

        presidents (List[str], optional): Signing President; only available for Presidential 
            Documents. Defaults to None.

        docket_id (str, optional): Agency docket number associated with 
            document. Defaults to None.

        regulation_id (str, optional): Regulation ID Number (RIN) associated 
            with document. Defaults to None.

        section_ids (List[str], optional): Limit to documents that appeared within 
            a particular section of FederalRegister.gov. Defaults to None.

        topic_ids (List[str], optional): Limit to documents associated with a particular 
            topic (CFR Indexing term). Defaults to None.

        is_significant (str, optional): Deemed Significant Under EO 12866. 
            Defaults to None.

        cfr_title (int, optional): Documents affecting the associated CFR 
            title. Defaults to None.

        cfr_part (int, optional): Part or part range (eg '17' or '1-50'); requires the 
            CFR title to be provided. Defaults to None.

        location (str, optional): Location search; enter zipcode or City and 
            State. Defaults to None.

        location_within (int, optional): Location search; maximum distance from 
            location in miles (max 200). Defaults to None.   

        Returns:
        ----
        dict: The federal document with the specified fields.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='documents/facets',
            arguments=[facet]
        )

        # Define the paramters.
        params = {
            'conditions[term]': terms,
            'conditions[publication_date][is]': publication_date_is,
            'conditions[publication_date][year]': publication_date_year,
            'conditions[publication_date][gte]': publication_date_greater_than,
            'conditions[publication_date][lte]': publication_date_less_than,
            'conditions[effective_date][is]': effective_date_is,
            'conditions[effective_date][year]': effective_date_year,
            'conditions[effective_date][gte]': effective_date_greater_than,
            'conditions[effective_date][lte]': effective_date_less_than,
            'conditions[agencies][]': agencies,
            'conditions[type][]': document_type,
            'conditions[presidential_document_type][]': presidential_document_type,
            'conditions[president][]': presidents,
            'conditions[docket_id]': docket_id,
            'conditions[regulation_id_number]': regulation_id,
            'conditions[sections][]': section_ids,
            'conditions[topics][]': topic_ids,
            'conditions[significant]': is_significant,
            'conditions[cfr][title]': cfr_title,
            'conditions[cfr][part]': cfr_part,
            'conditions[near][location]': location,
            'conditions[near][within]': location_within
        }

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get',
            params=params
        )

        return response

    def document_by_id(self, document_id: str, fields: List[str]) -> dict:
        """Fetch a single Federal Register document by their ID.

        Arguments:
        ----
        document_id (str): Federal Register document number.

        fields (List[str]): Which attributes of the documents to return; by 
            default, a reasonable set is returned, but a user can customize 
            it to return exactly what is needed.

        Returns:
        ----
        dict: The federal document with the specified fields.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='documents',
            arguments=[document_id]
        )

        if fields == 'all':
            fields = document_fields

        # Define the paramters.
        params = {
            'fields[]': fields
        }

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get',
            params=params
        )

        return response

    def documents_by_id(self, document_ids: List[str], fields: List[str]) -> dict:
        """Fetches multiple Federal Register documents by their IDs.

        Arguments:
        ----
        document_ids (List[str]): A list of Federal Register document numbers.

        fields (List[str]): Which attributes of the documents to return; by 
            default, a reasonable set is returned, but a user can customize 
            it to return exactly what is needed.

        Returns:
        ----
        dict: The federal document with the specified fields.
        """

        document_ids = ','.join(document_ids)

        # Build the URL.
        full_url = self._build_url(
            endpoint='documents',
            arguments=[document_ids]
        )

        if fields == 'all':
            fields = document_fields

        # Define the paramters.
        params = {
            'fields[]': fields
        }

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get',
            params=params
        )

        return response

    def agencies(self) -> dict:
        """Fetch all agency details.

        Returns:
        ----
        dict: A list of agencies with their details.
        """
        # Build the URL.
        full_url = self._build_url(
            endpoint='agencies'
        )

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get'
        )

        return response

    def agency_by_id(self, agency_slug: str) -> dict:
        """Fetch an agency by their Agency Slug.

        Arguments:
        ----
        agency_slug (str): The Federal Register slug for the agency

        Returns:
        ----
        dict: An agency resource with their details.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='agencies',
            arguments=[agency_slug]
        )

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get'
        )

        return response

    def public_inspection_document_by_id(self, document_id: str) -> dict:
        """Fetches a public inspection document by their ID.

        Arguments:
        ----
        document_id (str): Federal Register document number.

        Returns:
        ----
        dict: A public document resource.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='public-inspection-documents',
            arguments=[document_id]
        )

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get'
        )

        return response

    def public_inspection_documents_by_id(self, document_ids: List[str]) -> dict:
        """Fetches a collection of public inspection documents by their IDs.

        Arguments:
        ----
        document_ids (List[str]): A list of Federal Register document numbers.

        Returns:
        ----
        dict: A list of public document resources.
        """

        # Join the document IDs.
        document_ids = ','.join(document_ids)

        # Build the URL.
        full_url = self._build_url(
            endpoint='public-inspection-documents',
            arguments=[document_ids]
        )

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get'
        )

        return response

    def public_inspection_documents_current(self) -> dict:
        """Fetch all the public inspection documents that are currently on public inspection.

        Returns:
        ----
        dict: A list of public document resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='public-inspection-documents/current'
        )

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get'
        )

        return response

    def public_inspection_documents(self, available_on: str, fields: List[str] = 'all', per_page: int = 100, page_id: int = None,
                                    terms: str = None, agencies: List[str] = None, document_type: List[str] = None, special_filing_type: str = None,
                                    docket_id: str = None
                                    ) -> dict:
        """Allows for a more specific search for documents and grouping by facet.

        Arguments:
        ----
        available_on (str): Public Inspection issue date (YYYY-MM-DD).

        terms (str, optional): Full text search. Defaults to None.

        agencies (List[str], optional): Publishing agency. Defaults to None.

        document_type (List[str], optional): The Document Type. Defaults to None.

        special_filing_type (str, optional): Filing type: "0": Regular Filing "1": 
            Special Filing. Defaults to None.

        docket_id (str, optional): Agency docket number associated with 
            document. Defaults to None.

        Returns:
        ----
        dict: The federal document with the specified fields.
        """

        if fields == 'all':
            fields = public_document_fields

        # Build the URL.
        full_url = self._build_url(
            endpoint='public-inspection-documents'
        )

        # Define the paramters.
        params = {
            'fields[]': fields,
            'per_page': per_page,
            'page': page_id,
            'conditions[term]': terms,
            'conditions[available_on]': available_on,
            'conditions[agencies][]': agencies,
            'conditions[type][]': document_type,
            'conditions[special_filing]': special_filing_type,
            'conditions[docket_id]': docket_id
        }

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get',
            params=params
        )

        return response

    def suggested_searches(self, sections_ids: List[str]) -> dict:
        """Fetch all suggested searches or limit by FederalRegister.gov section.

        Arguments:
        ----
        sections_ids (List[str]): A list of Federal Register Section IDs for the different sections.

        Returns:
        ----
        dict: A list of search resources.
        """

        # Define the paramters.
        params = {
            'conditions[sections]': sections_ids
        }

        # Build the URL.
        full_url = self._build_url(
            endpoint='suggested_searches'
        )

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get',
            params=params
        )

        return response

    def suggested_searches_by_slug(self, slug_id: str) -> dict:
        """Fetch all suggested searches or limit by FederalRegister.gov section.

        Arguments:
        ----
        slug_ids (str): A Federal Register slug ID for the suggested search.

        Returns:
        ----
        dict: A list of search resources.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='suggested_searches',
            arguments=[slug_id]
        )

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get'
        )

        return response
