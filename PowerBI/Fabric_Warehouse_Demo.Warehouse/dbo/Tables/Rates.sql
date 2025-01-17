CREATE TABLE [dbo].[Rates] (

	[RatingCarrier] varchar(255) NULL, 
	[OriginCity] varchar(255) NULL, 
	[DestinationCity] varchar(255) NULL, 
	[EquipmentLength] varchar(255) NULL, 
	[RateAmount] decimal(10,2) NULL, 
	[Authority] varchar(255) NULL, 
	[RouteDescription] varchar(-1) NULL, 
	[EffDateStart] date NULL, 
	[EffDateEnd] date NULL, 
	[OwningEnterprise] varchar(255) NULL, 
	[OriginLocationCode] varchar(255) NULL, 
	[DestinationLocationCode] varchar(255) NULL, 
	[BillMethod] varchar(255) NULL, 
	[Commodity] varchar(255) NULL, 
	[Equipment] varchar(255) NULL, 
	[EquipmentOwner] varchar(255) NULL, 
	[EquipmentGroup] varchar(255) NULL, 
	[PlanCode] varchar(255) NULL, 
	[ContractName] varchar(255) NULL, 
	[IntermediateLocation] varchar(255) NULL, 
	[Service] varchar(255) NULL, 
	[STCC] varchar(255) NULL, 
	[TranComments] varchar(-1) NULL, 
	[ConfirmationCode] varchar(255) NULL, 
	[RateMgmtCode1] varchar(255) NULL, 
	[RateMgmtCode2] varchar(255) NULL, 
	[RateMgmtCode3] varchar(255) NULL, 
	[RateMgmtCode4] varchar(255) NULL, 
	[RateMgmtCode5] varchar(255) NULL
);

