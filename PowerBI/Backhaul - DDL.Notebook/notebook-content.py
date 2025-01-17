# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "0e3ff70b-2887-45eb-8633-761baceeff06",
# META       "default_lakehouse_name": "Fabric_Lakehouse_Demo",
# META       "default_lakehouse_workspace_id": "b80af03d-0784-4f79-a88f-b25d4f27f541",
# META       "known_lakehouses": [
# META         {
# META           "id": "0e3ff70b-2887-45eb-8633-761baceeff06"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE bronze.DimOffices (
# MAGIC 	id int NOT NULL,
# MAGIC 	STATUS varchar(30) NOT NULL,
# MAGIC 	lastmod timestamp NOT NULL,
# MAGIC 	lastuser varchar(30) NOT NULL,
# MAGIC 	legal_entity varchar(30) NOT NULL,
# MAGIC 	code varchar(8) NOT NULL,
# MAGIC 	parent varchar(8) NOT NULL,
# MAGIC 	dax_code varchar(10) ,
# MAGIC 	dax_post_comms varchar(30) NOT NULL,
# MAGIC 	owner_id int NOT NULL,
# MAGIC 	name varchar(50) ,
# MAGIC 	addr1 varchar(30) NOT NULL,
# MAGIC 	addr2 varchar(30) NOT NULL,
# MAGIC 	city varchar(30) NOT NULL,
# MAGIC 	state varchar(3) ,
# MAGIC 	zip varchar(10) NOT NULL,
# MAGIC 	intl_addr varchar(25) ,
# MAGIC 	country varchar(2) ,
# MAGIC 	tel varchar(12) NOT NULL,
# MAGIC 	fax varchar(12) NOT NULL,
# MAGIC 	tel_800 varchar(12) NOT NULL,
# MAGIC 	email varchar(60) NOT NULL,
# MAGIC 	check_custs varchar(30) NOT NULL,
# MAGIC 	use_flyj varchar(30) NOT NULL,
# MAGIC 	flyj_callback varchar(12) NOT NULL,
# MAGIC 	use_natl varchar(30) NOT NULL,
# MAGIC 	natl_id char(2) NOT NULL,
# MAGIC 	natl_callback varchar(12) NOT NULL,
# MAGIC 	use_tstop varchar(30) NOT NULL,
# MAGIC 	tstop_callback varchar(12) NOT NULL,
# MAGIC 	tstop_user varchar(255) ,
# MAGIC 	tstop_pass varchar(255) ,
# MAGIC 	fats_loadboard varchar(30) NOT NULL,
# MAGIC 	em_id int NOT NULL,
# MAGIC 	color varchar(30) NOT NULL,
# MAGIC 	company_name_inv varchar(64) ,
# MAGIC 	company_tagline_inv varchar(100) ,
# MAGIC 	company_name_bol varchar (500) NOT NULL,
# MAGIC 	company_name_cust varchar(64) ,
# MAGIC 	company_tagline_cust varchar(100) ,
# MAGIC 	company_name_carr varchar(64) ,
# MAGIC 	company_tagline_carr varchar(100) ,
# MAGIC 	remit_addr varchar (500) ,
# MAGIC 	finance_issues_email varchar(255) ,
# MAGIC 	outgoing_edi_loads int ,
# MAGIC 	show_204_weights_instruct int ,
# MAGIC 	show_204_contact_instruct int ,
# MAGIC 	show_204_locodata_instruct int ,
# MAGIC 	capreload_optin varchar(30) ,
# MAGIC 	edi214_reminders varchar(30) ,
# MAGIC 	edi214_scroll_when_checked varchar(30) ,
# MAGIC 	include_created_by_in_LOADWORKING varchar(30) ,
# MAGIC 	loads_moved_goal int ,
# MAGIC 	cust_total_goal float ,
# MAGIC 	carr_total_goal float ,
# MAGIC 	profit_total_goal decimal(10, 0) NOT NULL,
# MAGIC 	margin_percent_goal float ,
# MAGIC 	billing_associate_id int ,
# MAGIC 	enable_gps_tracking varchar(30) ,
# MAGIC 	interchange_office varchar(50) ,
# MAGIC 	dba varchar(50) ,
# MAGIC 	fk_auto_load_status_update int NOT NULL,
# MAGIC 	gps_tracking_fine_print_enabled int NOT NULL,
# MAGIC 	gps_tracking_fine_print_text varchar(500) ,
# MAGIC 	assignment_group_id int ,
# MAGIC 	bol_header_id int NOT NULL,
# MAGIC 	insurance_type varchar(30) ,
# MAGIC 	commission_basis varchar(30) NOT NULL,
# MAGIC 	commission_goal decimal(10, 2) ,
# MAGIC 	commission_pct decimal(3, 1) NOT NULL,
# MAGIC 	enable_econfirm int NOT NULL,
# MAGIC 	disable_auto_invoicing_office int ,
# MAGIC 	autopay_disabled int NOT NULL,
# MAGIC 	hide_comm_and_shared_revenue_report int ,
# MAGIC 	use_new_loadform int NOT NULL,
# MAGIC 	office_type varchar(30) NOT NULL,
# MAGIC 	account_clearance_email varchar(255) ,
# MAGIC 	show_loadform_settings int NOT NULL,
# MAGIC 	enable_account_clearance int NOT NULL,
# MAGIC 	Date_Added timestamp NOT NULL,
# MAGIC 	Date_Updated timestamp ,
# MAGIC 	share_approval_requests_email varchar(255) ,
# MAGIC 	billing_addr varchar (500) ,
# MAGIC 	bol_header_brand_id int ,
# MAGIC 	brand_id int NOT NULL,
# MAGIC 	carr_confirm_text varchar (500) NOT NULL,
# MAGIC 	carrier_payable_variance decimal(10, 2) ,
# MAGIC 	carrier_point_auto_bid_enabled tinyint NOT NULL,
# MAGIC 	carrier_point_auto_decline_enabled tinyint NOT NULL,
# MAGIC 	carrier_point_cust_agent_id int NOT NULL,
# MAGIC 	carrier_point_notification_email varchar(255) ,
# MAGIC 	carrier_point_password varchar(255) NOT NULL,
# MAGIC 	carrier_point_service_enabled tinyint NOT NULL,
# MAGIC 	carrier_point_username varchar(255) NOT NULL,
# MAGIC 	collections_email varchar(255) ,
# MAGIC 	commission_beta_date date ,
# MAGIC 	commission_decrease_threshold decimal(10, 2) ,
# MAGIC 	commission_post_email varchar (500) ,
# MAGIC 	copy_email_on_cust_invoices varchar (500) ,
# MAGIC 	credit_email varchar(255) NOT NULL,
# MAGIC 	credit_exceed_percentage int NOT NULL,
# MAGIC 	cust_invoice_questions_email varchar(255) ,
# MAGIC 	division varchar(11) NOT NULL,
# MAGIC 	driver_in_out_load_status_update tinyint NOT NULL,
# MAGIC 	enable_empty_notifications tinyint NOT NULL,
# MAGIC 	express_mail varchar (500) ,
# MAGIC 	finance_issue_waiting_on varchar(1000) ,
# MAGIC 	fk_alert_dispatcher tinyint NOT NULL,
# MAGIC 	invoice_process varchar(1000) ,
# MAGIC 	load_sequence int ,
# MAGIC 	office_group varchar(8) ,
# MAGIC 	payable_assignment_group_id int NOT NULL,
# MAGIC 	payable_associate_id int NOT NULL,
# MAGIC 	req_code_flag_reason tinyint NOT NULL,
# MAGIC 	req_code_operation tinyint NOT NULL,
# MAGIC 	req_code_revenue tinyint NOT NULL,
# MAGIC 	tstop_account_num varchar(24) ,
# MAGIC 	quickpay_enabled int NOT NULL,
# MAGIC 	payables_issues_email varchar(255) ,
# MAGIC 	dax_agent_code varchar(32) ,
# MAGIC 	customer_receivable_variance decimal(10, 2) NOT NULL,
# MAGIC 	charge_agent varchar(15) NOT NULL,
# MAGIC 	match_vendors varchar(32) NOT NULL,
# MAGIC 	enable_fee_calculations varchar(15) NOT NULL,
# MAGIC 	enable_rate_type_field varchar(15) NOT NULL,
# MAGIC 	auto_post_with_min_fields int NOT NULL,
# MAGIC 	enable_truckertools int NOT NULL,
# MAGIC 	commission_confirm_email varchar(255) ,
# MAGIC 	fk_alert_account_manager int NOT NULL
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE bronze.DimGeoData (
# MAGIC 	city varchar(255) NOT NULL,
# MAGIC 	st char(2) NOT NULL,
# MAGIC 	zip varchar(7) NOT NULL,
# MAGIC 	ac char(3) NOT NULL,
# MAGIC 	fips varchar(255) NOT NULL,
# MAGIC 	county varchar(255) NOT NULL,
# MAGIC 	pref varchar(255) NOT NULL,
# MAGIC 	tz varchar(8) NOT NULL,
# MAGIC 	dst char(1) NOT NULL,
# MAGIC 	lat decimal(8, 4) NOT NULL,
# MAGIC 	lon decimal(8, 4) NOT NULL,
# MAGIC 	msa varchar(255) NOT NULL,
# MAGIC 	pmsa varchar(255) NOT NULL,
# MAGIC 	abbr varchar(255) NOT NULL,
# MAGIC 	ma varchar(255) NOT NULL,
# MAGIC 	type varchar(255) NOT NULL,
# MAGIC 	country varchar(500) NOT NULL,
# MAGIC 	cbsa int,
# MAGIC 	div int,
# MAGIC 	population int,
# MAGIC 	updated_at timestamp NOT NULL,
# MAGIC 	Date_Added timestamp NOT NULL,
# MAGIC 	Date_Updated timestamp
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE bronze.MLEquipmentGroup (
# MAGIC 	ID int  NOT NULL,
# MAGIC 	EquipmentCode varchar(255),
# MAGIC 	EquipmentDescription varchar(255),
# MAGIC 	EquipmentGroup varchar(255),
# MAGIC 	DataSource int
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC 
# MAGIC CREATE or replace TABLE bronze.DimCarrier (
# MAGIC 	CarrierIDFromSourceSystem varchar(30) NOT NULL,
# MAGIC 	CarrierName varchar(100),
# MAGIC 	SCAC varchar(50),
# MAGIC 	Mode varchar(50),
# MAGIC 	MCNumber varchar(24),
# MAGIC 	URL varchar(100),
# MAGIC 	DataSourceId int NOT NULL,
# MAGIC 	DateAdded timestamp,
# MAGIC 	DateUpdated timestamp,
# MAGIC 	Type varchar(1000),
# MAGIC 	DOTNumber varchar(100),
# MAGIC 	ActiveDate timestamp
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE bronze.DimCustomer (
# MAGIC 	CustomerId varchar(20) NOT NULL,
# MAGIC 	CustomerName varchar(255),
# MAGIC 	CustomerGroupName varchar(255),
# MAGIC 	CustomerAcctNum varchar(255),
# MAGIC 	CustomerStatus varchar(15),
# MAGIC 	ParentName varchar(100),
# MAGIC 	ParentGroupName varchar(100),
# MAGIC 	IndustryGroupName varchar(100),
# MAGIC 	Address1 varchar(255),
# MAGIC 	Address2 varchar(255),
# MAGIC 	City varchar(255),
# MAGIC 	State varchar(255),
# MAGIC 	Zip varchar(255),
# MAGIC 	Phone varchar(255),
# MAGIC 	Fax varchar(255),
# MAGIC 	Country varchar(255),
# MAGIC 	Email varchar(150),
# MAGIC 	Website varchar(60),
# MAGIC 	CreditLimit decimal(18, 3),
# MAGIC 	FinanceGroup int,
# MAGIC 	SICCode varchar(255),
# MAGIC 	NAICSCode varchar(50),
# MAGIC 	NAICSDescription varchar(255),
# MAGIC 	QBShortName varchar(255),
# MAGIC 	PaymentTerms varchar(255),
# MAGIC 	OperationContactId int,
# MAGIC 	FinancialContactId int,
# MAGIC 	FinanceId int,
# MAGIC 	ContactMethod varchar(255),
# MAGIC 	ContactFullName varchar(40),
# MAGIC 	SalesRep varchar(8),
# MAGIC 	MasterCustId varchar(8),
# MAGIC 	BillToId varchar(7),
# MAGIC 	Company varchar(3),
# MAGIC 	Address_Fk int,
# MAGIC 	DataSourceID int NOT NULL,
# MAGIC 	DateAdded timestamp NOT NULL,
# MAGIC 	DateUpdated timestamp,
# MAGIC 	Size varchar(50)
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE bronze.DimDATMarketZones (
# MAGIC 	KMACode varchar(50) NOT NULL,
# MAGIC 	CityState varchar(50),
# MAGIC 	ReferenceCity varchar(50),
# MAGIC 	ReferenceState varchar(50),
# MAGIC 	Zip3 varchar(50) NOT NULL,
# MAGIC 	Zip3Reference varchar(50) NOT NULL,
# MAGIC 	Country varchar(50),
# MAGIC 	LaneGroupNameMarketArea varchar(50),
# MAGIC 	DateAdded timestamp NOT NULL,
# MAGIC 	DateUpdated timestamp
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE bronze.DimEquipment (
# MAGIC 	EquipmentKey varchar(50) NOT NULL,
# MAGIC 	EquipmentCode varchar(50),
# MAGIC 	EquipmentNumber varchar(20),
# MAGIC 	EquipmentDescription varchar(60),
# MAGIC 	DataSourceID int NOT NULL,
# MAGIC 	DateAdded timestamp NOT NULL,
# MAGIC 	DateUpdated timestamp
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE or replace TABLE bronze.DimIBO (
# MAGIC 	IBOName varchar(100) NOT NULL,
# MAGIC 	DateAdded date NOT NULL,
# MAGIC 	DateUpdated date,
# MAGIC 	IBOGlobalName varchar(100),
# MAGIC 	ExternalId varchar(100),
# MAGIC 	Phone varchar(25),
# MAGIC 	Email varchar(60),
# MAGIC 	BusinessUnit varchar(30),
# MAGIC 	IBOId int NOT NULL
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE bronze.FactDAT (
# MAGIC 	WeekEndingDate date,
# MAGIC 	AvgLineHaulRate float,
# MAGIC 	FuelSurcharge float,
# MAGIC 	NoofCompanies int,
# MAGIC 	NoofReports int,
# MAGIC 	YourOwnNoofReports int,
# MAGIC 	YourOwnAvgLinehaulRate decimal(18, 0),
# MAGIC 	OriginCity varchar(255),
# MAGIC 	OriginState varchar(255),
# MAGIC 	OriginPostalCode varchar(255),
# MAGIC 	DestCity varchar(255),
# MAGIC 	DestState varchar(255),
# MAGIC 	DestPostalCode varchar(255),
# MAGIC 	TruckType varchar(255),
# MAGIC 	EquipmentType varchar(50),
# MAGIC 	OriginCountry char(255),
# MAGIC 	DestCountry char(255),
# MAGIC 	PCMilerPracticalMileage decimal(18, 0),
# MAGIC 	TranscoreOriginCityState varchar(50),
# MAGIC 	TranscoreDestCityState varchar(50),
# MAGIC 	TranscoreOriginCode varchar(50),
# MAGIC 	TranscoreDestCode varchar(50),
# MAGIC 	TranscoreOriginReferenceCity varchar(50),
# MAGIC 	TranscoreDestReferenceCity varchar(50),
# MAGIC 	TranscoreOriginReferenceState varchar(50),
# MAGIC 	TranscoreDestReferenceState varchar(50),
# MAGIC 	TranscoreOriginZip3Reference varchar(50),
# MAGIC 	TranscoreDestZip3Reference varchar(50),
# MAGIC 	TranscoreOriginZip3 varchar(50),
# MAGIC 	TranscoreDestZip3 varchar(50),
# MAGIC 	TranscoreOriginCountry varchar(50),
# MAGIC 	TranscoreDestCountry varchar(50),
# MAGIC 	OriginMarketArea varchar(50),
# MAGIC 	DestMarketArea varchar(50),
# MAGIC 	DataSourceId int NOT NULL,
# MAGIC 	DateAdded timestamp NOT NULL,
# MAGIC 	DateUpdated timestamp,
# MAGIC 	FDAT_ID int  NOT NULL
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE bronze.FactLoad (
# MAGIC 	MoveId varchar(510) NOT NULL,
# MAGIC 	LoadId varchar(50) NOT NULL,
# MAGIC 	LoadSequence int,
# MAGIC 	IBOKey varchar(100),
# MAGIC 	CustomerKey varchar(70),
# MAGIC 	RequestedEquipmentKey varchar(40),
# MAGIC 	ActualEquipmentKey varchar(40),
# MAGIC 	ModeCategory varchar(1200),
# MAGIC 	CarrierId varchar(50),
# MAGIC 	Mode varchar(255),
# MAGIC 	Consignee varchar(500),
# MAGIC 	Shipper varchar(500),
# MAGIC 	LoadStatus varchar(255),
# MAGIC 	ShipDate date,
# MAGIC 	OriginMarketKey bigint,
# MAGIC 	DestMarketKey bigint,
# MAGIC 	OriginCity varchar(255),
# MAGIC 	OriginState varchar(255),
# MAGIC 	OriginCountry varchar(255),
# MAGIC 	OriginZip varchar(255),
# MAGIC 	DestCity varchar(255),
# MAGIC 	DestState varchar(255),
# MAGIC 	DestCountry varchar(255),
# MAGIC 	DestZip varchar(255),
# MAGIC 	PickupAppointmentEarliestTime varchar(10),
# MAGIC 	PickupAppointmentLatestTime varchar(10),
# MAGIC 	DeliveryAppointmentEarliestTime varchar(10),
# MAGIC 	DeliveryAppointmentLatestTime varchar(10),
# MAGIC 	PickupAppointmentDate date,
# MAGIC 	DeliveryAppointmentDate date,
# MAGIC 	ServiceDaysPerCarrier decimal(18, 0),
# MAGIC 	Lane varchar(400),
# MAGIC 	ActualPickupDate date,
# MAGIC 	ActualDeliveryDate date,
# MAGIC 	ExpectedEarliestPickupDate date,
# MAGIC 	ExpectedLatestPickupDate date,
# MAGIC 	ExpectedEarliestDeliveryDate date,
# MAGIC 	ExpectedLatestDeliveryDate date,
# MAGIC 	ActualPickupTime varchar(10),
# MAGIC 	ActualDeliveryTime varchar(10),
# MAGIC 	ExpectedEarliestPickupTime varchar(10),
# MAGIC 	ExpectedLatestPickupTime varchar(10),
# MAGIC 	ExpectedEarliestDeliveryTime varchar(10),
# MAGIC 	ExpectedLatestDeliveryTime varchar(10),
# MAGIC 	TransitTime varchar(10),
# MAGIC 	OnTimePickupFlag int,
# MAGIC 	OnTimeDeliveryFlag int,
# MAGIC 	DerivedOTPFlag float,
# MAGIC 	DerivedOTDFlag float,
# MAGIC 	Quantity bigint,
# MAGIC 	Weight real,
# MAGIC 	WeightUOM varchar(50),
# MAGIC 	QuantityUOM varchar(50),
# MAGIC 	Distance decimal(18, 0),
# MAGIC 	DerivedRevenue float,
# MAGIC 	DerivedVolume float,
# MAGIC 	DerivedAccessorialRevenue float,
# MAGIC 	DerivedFuelRevenue float,
# MAGIC 	DerivedLinehaulRevenue float,
# MAGIC 	TotalCost float,
# MAGIC 	TotalCarrierCost float,
# MAGIC 	LineHaulCost float,
# MAGIC 	FuelCost float,
# MAGIC 	AccessorialCost decimal(16,2),
# MAGIC 	TotalVendorCost decimal(16,2),
# MAGIC 	DerivedMargin float,
# MAGIC 	DataSourceId int NOT NULL,
# MAGIC 	DateAdded timestamp,
# MAGIC 	DateUpdated timestamp,
# MAGIC 	Dispatcher varchar(10),
# MAGIC 	RevenueCode varchar(10),
# MAGIC 	FactorId int,
# MAGIC 	FactorName varchar(100),
# MAGIC 	EDIFlag boolean,
# MAGIC 	OnProcessFlag boolean,
# MAGIC 	CarrierContractName varchar(255),
# MAGIC 	CarrierPro varchar(255),
# MAGIC 	NEWOnTimePickupFlag int,
# MAGIC 	NEWOnTimeDeliveryFlag int,
# MAGIC 	NEWDerivedOTPFlag float,
# MAGIC 	NEWDerivedOTDFlag float
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE bronze.FactMove (
# MAGIC 	FirstLoadPrimaryReference varchar(50) NOT NULL,
# MAGIC 	MoveId varchar(50) NOT NULL,
# MAGIC 	Movestatus varchar(100),
# MAGIC 	CustomerKey varchar(70),
# MAGIC 	SalesNumberSalesPeople varchar(255),
# MAGIC 	SalesNumberAgent varchar(255),
# MAGIC 	IBOKey varchar(100),
# MAGIC 	CustomerMode varchar(50),
# MAGIC 	CarrierMode varchar(50),
# MAGIC 	DestAddressKey bigint,
# MAGIC 	OriginAddressKey bigint,
# MAGIC 	OriginCity varchar(50),
# MAGIC 	OriginState varchar(50),
# MAGIC 	OriginCountry varchar(50),
# MAGIC 	OriginZip varchar(50),
# MAGIC 	DestCity varchar(50),
# MAGIC 	DestState varchar(50),
# MAGIC 	DestCountry varchar(50),
# MAGIC 	DestZip varchar(50),
# MAGIC 	LoadCount bigint,
# MAGIC 	ShipmentCount bigint,
# MAGIC 	Quantity bigint,
# MAGIC 	Weight real,
# MAGIC 	WeightUOM varchar(50),
# MAGIC 	QuantityUOM varchar(50),
# MAGIC 	Distance decimal(18, 0),
# MAGIC 	TotalRevenue float,
# MAGIC 	TotalCost float,
# MAGIC 	TotalCarrierCost float,
# MAGIC 	TotalLineHaulCost float,
# MAGIC 	TotalFuelCost float,
# MAGIC 	TotalAccessorialCost decimal(16,2),
# MAGIC 	TotalVendorCost decimal(16,2),
# MAGIC 	TotalLinehaulRevenue decimal(16,2),
# MAGIC 	TotalFuelRevenue decimal(16,2),
# MAGIC 	TotalAccessorialRevenue decimal(16,2),
# MAGIC 	Margin float,
# MAGIC 	FirstPickupActualDate date,
# MAGIC 	InvoiceDate date,
# MAGIC 	InvoiceDateUpd date,
# MAGIC 	FirstPickupActualTime varchar(10),
# MAGIC 	LastDropActualDate date,
# MAGIC 	LastDropActualTime varchar(10),
# MAGIC 	ExpectedEarliestPickupDate date,
# MAGIC 	ExpectedLatestPickupDate date,
# MAGIC 	ExpectedEarliestPickupTime varchar(10),
# MAGIC 	ExpectedLatestPickupTime varchar(10),
# MAGIC 	ExpectedEarliestDeliveryDate date,
# MAGIC 	ExpectedEarliestDeliveryTime varchar(10),
# MAGIC 	ExpectedLatestDeliveryDate date,
# MAGIC 	ExpectedLatestDeliveryTime varchar(10),
# MAGIC 	OnTimePickupFlag int,
# MAGIC 	OnTimeDeliveryFlag int,
# MAGIC 	RevenuePerMile float,
# MAGIC 	RevenuePerPound float,
# MAGIC 	CarrierCostPerMile float,
# MAGIC 	CarrierCostPerPound float,
# MAGIC 	DataSourceId int NOT NULL,
# MAGIC 	DateAdded timestamp NOT NULL,
# MAGIC 	DateUpdated timestamp,
# MAGIC 	Dispatcher varchar(10),
# MAGIC 	RevenueCode varchar(10),
# MAGIC 	MaxFreightClass varchar(50),
# MAGIC 	AcctManager varchar(255),
# MAGIC 	NEWOnTimePickupFlag int,
# MAGIC 	NEWOnTimeDeliveryFlag int,
# MAGIC 	CustAcctManager varchar(255)
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE bronze.LkpIBO (
# MAGIC 	IBOIdFromSourceSystem varchar(20) NOT NULL,
# MAGIC 	IBOid varchar(100) NOT NULL,
# MAGIC 	IBORegions varchar(50),
# MAGIC 	IndustryType varchar(50),
# MAGIC 	DataSourceId int NOT NULL,
# MAGIC 	DateAdded timestamp NOT NULL,
# MAGIC 	DateUpdated timestamp,
# MAGIC 	ExternalId varchar(100)
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE bronze.LKPModeGroup (
# MAGIC 	Mode varchar(255),
# MAGIC 	ModeGroup varchar(255),
# MAGIC 	LKPModeGroup_ID int  NOT NULL
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE Bronze.PostalCodes50Miles (
# MAGIC     Id int,
# MAGIC     PossibleZipCodes int,
# MAGIC     ZipCodes int,
# MAGIC     Miles float,
# MAGIC     PossibleLatitude float,
# MAGIC     PossibleLongitude float,
# MAGIC     ZipCodeLatitude float,
# MAGIC     ZipCodeLongitude float,
# MAGIC     PostalCodes50Miles_ID int not null
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
