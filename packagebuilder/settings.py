<?xml version="1.0" encoding="UTF-8"?>
<!--
Salesforce.com Metadata API version 52.0

Copyright 2006-2021 Salesforce.com, inc. All Rights Reserved
-->
<definitions targetNamespace="http://soap.sforce.com/2006/04/metadata" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/wsdl/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://soap.sforce.com/2006/04/metadata">
 <types>
  <xsd:schema elementFormDefault="qualified" targetNamespace="http://soap.sforce.com/2006/04/metadata">
   <xsd:complexType name="CancelDeployResult">
    <xsd:sequence>
     <xsd:element name="done" type="xsd:boolean"/>
     <xsd:element name="id" type="tns:ID"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DeployResult">
    <xsd:sequence>
     <xsd:element name="canceledBy" minOccurs="0" type="xsd:string"/>
     <xsd:element name="canceledByName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="checkOnly" type="xsd:boolean"/>
     <xsd:element name="completedDate" minOccurs="0" type="xsd:dateTime"/>
     <xsd:element name="createdBy" type="xsd:string"/>
     <xsd:element name="createdByName" type="xsd:string"/>
     <xsd:element name="createdDate" type="xsd:dateTime"/>
     <xsd:element name="details" type="tns:DeployDetails"/>
     <xsd:element name="done" type="xsd:boolean"/>
     <xsd:element name="errorMessage" minOccurs="0" type="xsd:string"/>
     <xsd:element name="errorStatusCode" minOccurs="0" type="tns:StatusCode"/>
     <xsd:element name="id" type="tns:ID"/>
     <xsd:element name="ignoreWarnings" type="xsd:boolean"/>
     <xsd:element name="lastModifiedDate" minOccurs="0" type="xsd:dateTime"/>
     <xsd:element name="numberComponentErrors" type="xsd:int"/>
     <xsd:element name="numberComponentsDeployed" type="xsd:int"/>
     <xsd:element name="numberComponentsTotal" type="xsd:int"/>
     <xsd:element name="numberTestErrors" type="xsd:int"/>
     <xsd:element name="numberTestsCompleted" type="xsd:int"/>
     <xsd:element name="numberTestsTotal" type="xsd:int"/>
     <xsd:element name="rollbackOnError" type="xsd:boolean"/>
     <xsd:element name="runTestsEnabled" type="xsd:boolean"/>
     <xsd:element name="startDate" minOccurs="0" type="xsd:dateTime"/>
     <xsd:element name="stateDetail" minOccurs="0" type="xsd:string"/>
     <xsd:element name="status" type="tns:DeployStatus"/>
     <xsd:element name="success" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DeployDetails">
    <xsd:sequence>
     <xsd:element name="componentFailures" minOccurs="0" maxOccurs="unbounded" type="tns:DeployMessage"/>
     <xsd:element name="componentSuccesses" minOccurs="0" maxOccurs="unbounded" type="tns:DeployMessage"/>
     <xsd:element name="retrieveResult" minOccurs="0" type="tns:RetrieveResult"/>
     <xsd:element name="runTestResult" minOccurs="0" type="tns:RunTestsResult"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DeployMessage">
    <xsd:sequence>
     <xsd:element name="changed" type="xsd:boolean"/>
     <xsd:element name="columnNumber" minOccurs="0" type="xsd:int"/>
     <xsd:element name="componentType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="created" type="xsd:boolean"/>
     <xsd:element name="createdDate" type="xsd:dateTime"/>
     <xsd:element name="deleted" type="xsd:boolean"/>
     <xsd:element name="fileName" type="xsd:string"/>
     <xsd:element name="fullName" type="xsd:string"/>
     <xsd:element name="id" minOccurs="0" type="xsd:string"/>
     <xsd:element name="lineNumber" minOccurs="0" type="xsd:int"/>
     <xsd:element name="problem" minOccurs="0" type="xsd:string"/>
     <xsd:element name="problemType" minOccurs="0" type="tns:DeployProblemType"/>
     <xsd:element name="success" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DeployProblemType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Warning"/>
     <xsd:enumeration value="Error"/>
     <xsd:enumeration value="Info"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="RetrieveResult">
    <xsd:sequence>
     <xsd:element name="done" type="xsd:boolean"/>
     <xsd:element name="errorMessage" minOccurs="0" type="xsd:string"/>
     <xsd:element name="errorStatusCode" minOccurs="0" type="tns:StatusCode"/>
     <xsd:element name="fileProperties" minOccurs="0" maxOccurs="unbounded" type="tns:FileProperties"/>
     <xsd:element name="id" type="xsd:string"/>
     <xsd:element name="messages" minOccurs="0" maxOccurs="unbounded" type="tns:RetrieveMessage"/>
     <xsd:element name="status" type="tns:RetrieveStatus"/>
     <xsd:element name="success" type="xsd:boolean"/>
     <xsd:element name="zipFile" type="xsd:base64Binary"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FileProperties">
    <xsd:sequence>
     <xsd:element name="createdById" type="xsd:string"/>
     <xsd:element name="createdByName" type="xsd:string"/>
     <xsd:element name="createdDate" type="xsd:dateTime"/>
     <xsd:element name="fileName" type="xsd:string"/>
     <xsd:element name="fullName" type="xsd:string"/>
     <xsd:element name="id" type="xsd:string"/>
     <xsd:element name="lastModifiedById" type="xsd:string"/>
     <xsd:element name="lastModifiedByName" type="xsd:string"/>
     <xsd:element name="lastModifiedDate" type="xsd:dateTime"/>
     <xsd:element name="manageableState" minOccurs="0" type="tns:ManageableState"/>
     <xsd:element name="namespacePrefix" minOccurs="0" type="xsd:string"/>
     <xsd:element name="type" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ManageableState">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="released"/>
     <xsd:enumeration value="deleted"/>
     <xsd:enumeration value="deprecated"/>
     <xsd:enumeration value="installed"/>
     <xsd:enumeration value="beta"/>
     <xsd:enumeration value="unmanaged"/>
     <xsd:enumeration value="installedEditable"/>
     <xsd:enumeration value="deprecatedEditable"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="RetrieveMessage">
    <xsd:sequence>
     <xsd:element name="fileName" type="xsd:string"/>
     <xsd:element name="problem" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="RetrieveStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Pending"/>
     <xsd:enumeration value="InProgress"/>
     <xsd:enumeration value="Succeeded"/>
     <xsd:enumeration value="Failed"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="RunTestsResult">
    <xsd:sequence>
     <xsd:element name="apexLogId" minOccurs="0" type="xsd:string"/>
     <xsd:element name="codeCoverage" minOccurs="0" maxOccurs="unbounded" type="tns:CodeCoverageResult"/>
     <xsd:element name="codeCoverageWarnings" minOccurs="0" maxOccurs="unbounded" type="tns:CodeCoverageWarning"/>
     <xsd:element name="failures" minOccurs="0" maxOccurs="unbounded" type="tns:RunTestFailure"/>
     <xsd:element name="flowCoverage" minOccurs="0" maxOccurs="unbounded" type="tns:FlowCoverageResult"/>
     <xsd:element name="flowCoverageWarnings" minOccurs="0" maxOccurs="unbounded" type="tns:FlowCoverageWarning"/>
     <xsd:element name="numFailures" type="xsd:int"/>
     <xsd:element name="numTestsRun" type="xsd:int"/>
     <xsd:element name="successes" minOccurs="0" maxOccurs="unbounded" type="tns:RunTestSuccess"/>
     <xsd:element name="totalTime" type="xsd:double"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CodeCoverageResult">
    <xsd:sequence>
     <xsd:element name="dmlInfo" minOccurs="0" maxOccurs="unbounded" type="tns:CodeLocation"/>
     <xsd:element name="id" type="tns:ID"/>
     <xsd:element name="locationsNotCovered" minOccurs="0" maxOccurs="unbounded" type="tns:CodeLocation"/>
     <xsd:element name="methodInfo" minOccurs="0" maxOccurs="unbounded" type="tns:CodeLocation"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="namespace" type="xsd:string" nillable="true"/>
     <xsd:element name="numLocations" type="xsd:int"/>
     <xsd:element name="numLocationsNotCovered" type="xsd:int"/>
     <xsd:element name="soqlInfo" minOccurs="0" maxOccurs="unbounded" type="tns:CodeLocation"/>
     <xsd:element name="soslInfo" minOccurs="0" maxOccurs="unbounded" type="tns:CodeLocation"/>
     <xsd:element name="type" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CodeLocation">
    <xsd:sequence>
     <xsd:element name="column" type="xsd:int"/>
     <xsd:element name="line" type="xsd:int"/>
     <xsd:element name="numExecutions" type="xsd:int"/>
     <xsd:element name="time" type="xsd:double"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CodeCoverageWarning">
    <xsd:sequence>
     <xsd:element name="id" type="tns:ID"/>
     <xsd:element name="message" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string" nillable="true"/>
     <xsd:element name="namespace" type="xsd:string" nillable="true"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RunTestFailure">
    <xsd:sequence>
     <xsd:element name="id" type="tns:ID"/>
     <xsd:element name="message" type="xsd:string"/>
     <xsd:element name="methodName" type="xsd:string" nillable="true"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="namespace" type="xsd:string" nillable="true"/>
     <xsd:element name="packageName" type="xsd:string"/>
     <xsd:element name="seeAllData" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="stackTrace" type="xsd:string" nillable="true"/>
     <xsd:element name="time" type="xsd:double"/>
     <xsd:element name="type" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowCoverageResult">
    <xsd:sequence>
     <xsd:element name="elementsNotCovered" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="flowId" type="xsd:string"/>
     <xsd:element name="flowName" type="xsd:string"/>
     <xsd:element name="flowNamespace" type="xsd:string" nillable="true"/>
     <xsd:element name="numElements" type="xsd:int"/>
     <xsd:element name="numElementsNotCovered" type="xsd:int"/>
     <xsd:element name="processType" type="tns:FlowProcessType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FlowProcessType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AutoLaunchedFlow"/>
     <xsd:enumeration value="Flow"/>
     <xsd:enumeration value="Workflow"/>
     <xsd:enumeration value="CustomEvent"/>
     <xsd:enumeration value="InvocableProcess"/>
     <xsd:enumeration value="LoginFlow"/>
     <xsd:enumeration value="ActionPlan"/>
     <xsd:enumeration value="JourneyBuilderIntegration"/>
     <xsd:enumeration value="UserProvisioningFlow"/>
     <xsd:enumeration value="Survey"/>
     <xsd:enumeration value="SurveyEnrich"/>
     <xsd:enumeration value="Appointments"/>
     <xsd:enumeration value="FSCLending"/>
     <xsd:enumeration value="DigitalForm"/>
     <xsd:enumeration value="FieldServiceMobile"/>
     <xsd:enumeration value="OrchestrationFlow"/>
     <xsd:enumeration value="FieldServiceWeb"/>
     <xsd:enumeration value="TransactionSecurityFlow"/>
     <xsd:enumeration value="ContactRequestFlow"/>
     <xsd:enumeration value="ActionCadenceFlow"/>
     <xsd:enumeration value="ManagedContentFlow"/>
     <xsd:enumeration value="CheckoutFlow"/>
     <xsd:enumeration value="CartAsyncFlow"/>
     <xsd:enumeration value="SalesEntryExperienceFlow"/>
     <xsd:enumeration value="CustomerLifecycle"/>
     <xsd:enumeration value="Journey"/>
     <xsd:enumeration value="RecommendationStrategy"/>
     <xsd:enumeration value="Orchestrator"/>
     <xsd:enumeration value="RoutingFlow"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowCoverageWarning">
    <xsd:sequence>
     <xsd:element name="flowId" type="xsd:string" nillable="true"/>
     <xsd:element name="flowName" type="xsd:string" nillable="true"/>
     <xsd:element name="flowNamespace" type="xsd:string" nillable="true"/>
     <xsd:element name="message" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RunTestSuccess">
    <xsd:sequence>
     <xsd:element name="id" type="tns:ID"/>
     <xsd:element name="methodName" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="namespace" type="xsd:string" nillable="true"/>
     <xsd:element name="seeAllData" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="time" type="xsd:double"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DeployStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Pending"/>
     <xsd:enumeration value="InProgress"/>
     <xsd:enumeration value="Succeeded"/>
     <xsd:enumeration value="SucceededPartial"/>
     <xsd:enumeration value="Failed"/>
     <xsd:enumeration value="Canceling"/>
     <xsd:enumeration value="Canceled"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="Metadata">
    <xsd:sequence>
     <xsd:element name="fullName" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AIApplication">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="masterLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="status" type="tns:AIApplicationStatus"/>
       <xsd:element name="type" type="tns:AIApplicationType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="AIApplicationStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Draft"/>
     <xsd:enumeration value="Migrated"/>
     <xsd:enumeration value="Enabled"/>
     <xsd:enumeration value="Disabled"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="AIApplicationType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="PredictionBuilder"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="AIApplicationConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="aiApplicationDeveloperName" type="xsd:string"/>
       <xsd:element name="applicationId" minOccurs="0" type="xsd:string"/>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="insightReasonEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="rank" minOccurs="0" type="xsd:int"/>
       <xsd:element name="scoringMode" minOccurs="0" type="tns:AIScoringMode"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="AIScoringMode">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Batch"/>
     <xsd:enumeration value="OnDemand"/>
     <xsd:enumeration value="Streaming"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="AIReplyRecommendationsSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableAIReplyRecommendations" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AccountInsightsSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableAccountInsights" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AccountIntelligenceSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableAccountLogos" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAutomatedAccountFields" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNewsStories" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AccountRelationshipShareRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="accessLevel" type="xsd:string"/>
       <xsd:element name="accountToCriteriaField" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="entityType" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="staticFormulaCriteria" minOccurs="0" type="xsd:string"/>
       <xsd:element name="type" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AccountSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableAccountHistoryTracking" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAccountInsightsInMobile" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAccountOwnerReport" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAccountTeams" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContactHistoryTracking" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRelateContactToMultipleAccounts" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showViewHierarchyLink" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ActionLinkGroupTemplate">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionLinkTemplates" minOccurs="0" maxOccurs="unbounded" type="tns:ActionLinkTemplate"/>
       <xsd:element name="category" type="tns:PlatformActionGroupCategory"/>
       <xsd:element name="executionsAllowed" type="tns:ActionLinkExecutionsAllowed"/>
       <xsd:element name="hoursUntilExpiration" minOccurs="0" type="xsd:int"/>
       <xsd:element name="isPublished" type="xsd:boolean"/>
       <xsd:element name="name" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ActionLinkTemplate">
    <xsd:sequence>
     <xsd:element name="actionUrl" type="xsd:string"/>
     <xsd:element name="headers" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isConfirmationRequired" type="xsd:boolean"/>
     <xsd:element name="isGroupDefault" type="xsd:boolean"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="labelKey" type="xsd:string"/>
     <xsd:element name="linkType" type="tns:ActionLinkType"/>
     <xsd:element name="method" type="tns:ActionLinkHttpMethod"/>
     <xsd:element name="position" type="xsd:int"/>
     <xsd:element name="requestBody" minOccurs="0" type="xsd:string"/>
     <xsd:element name="userAlias" minOccurs="0" type="xsd:string"/>
     <xsd:element name="userVisibility" type="tns:ActionLinkUserVisibility"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ActionLinkType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="API"/>
     <xsd:enumeration value="APIAsync"/>
     <xsd:enumeration value="Download"/>
     <xsd:enumeration value="UI"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ActionLinkHttpMethod">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="HttpDelete"/>
     <xsd:enumeration value="HttpHead"/>
     <xsd:enumeration value="HttpGet"/>
     <xsd:enumeration value="HttpPatch"/>
     <xsd:enumeration value="HttpPost"/>
     <xsd:enumeration value="HttpPut"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ActionLinkUserVisibility">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Creator"/>
     <xsd:enumeration value="Everyone"/>
     <xsd:enumeration value="EveryoneButCreator"/>
     <xsd:enumeration value="Manager"/>
     <xsd:enumeration value="CustomUser"/>
     <xsd:enumeration value="CustomExcludedUser"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="PlatformActionGroupCategory">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Primary"/>
     <xsd:enumeration value="Overflow"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ActionLinkExecutionsAllowed">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Once"/>
     <xsd:enumeration value="OncePerUser"/>
     <xsd:enumeration value="Unlimited"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ActionPlanTemplate">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionPlanTemplateItem" minOccurs="0" maxOccurs="unbounded" type="tns:ActionPlanTemplateItem"/>
       <xsd:element name="actionPlanTemplateItemDependencies" minOccurs="0" maxOccurs="unbounded" type="tns:ActionPlanTemplateItemDependency"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isAdHocItemCreationEnabled" type="xsd:boolean"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="targetEntityType" type="xsd:string"/>
       <xsd:element name="uniqueName" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ActionPlanTemplateItem">
    <xsd:sequence>
     <xsd:element name="actionPlanTemplateItemValue" minOccurs="0" maxOccurs="unbounded" type="tns:ActionPlanTemplateItemValue"/>
     <xsd:element name="displayOrder" minOccurs="0" type="xsd:int"/>
     <xsd:element name="isRequired" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="itemEntityType" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="uniqueName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ActionPlanTemplateItemValue">
    <xsd:sequence>
     <xsd:element name="itemEntityType" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="valueFormula" minOccurs="0" type="xsd:string"/>
     <xsd:element name="valueLiteral" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ActionPlanTemplateItemDependency">
    <xsd:sequence>
     <xsd:element name="creationType" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="previousTemplateItem" type="tns:ActionPlanTemplateItem"/>
     <xsd:element name="templateItem" type="tns:ActionPlanTemplateItem"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ActionsSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableDefaultQuickActionsOn" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMdpEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOfflineWebLinks" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableThirdPartyActions" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ActivitiesSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="allowUsersToRelateMultipleContactsToTasksAndEvents" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="autoRelateEventAttendees" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableActivityReminders" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableClickCreateEvents" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDragAndDropScheduling" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailTracking" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFlowTaskNotifsViaApex" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGroupTasks" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHideChildEventsPreference" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableListViewScheduling" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLogNote" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMLSingleClientProfile" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMultidayEvents" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRecurringEvents" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRecurringTasks" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRollUpActivToContactsAcct" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSidebarCalendarShortcut" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSimpleTaskCreateUI" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUNSTaskDelegatedToNotifications" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUserListViewCalendars" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="meetingRequestsLogo" minOccurs="0" type="xsd:string"/>
       <xsd:element name="showCustomLogoMeetingRequests" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showEventDetailsMultiUserCalendar" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showHomePageHoverLinksForEvents" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showMyTasksHoverLinks" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AddressSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="countriesAndStates" type="tns:CountriesAndStates"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CountriesAndStates">
    <xsd:sequence>
     <xsd:element name="countries" minOccurs="0" maxOccurs="unbounded" type="tns:Country"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Country">
    <xsd:sequence>
     <xsd:element name="active" type="xsd:boolean"/>
     <xsd:element name="integrationValue" type="xsd:string"/>
     <xsd:element name="isoCode" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="orgDefault" type="xsd:boolean"/>
     <xsd:element name="standard" type="xsd:boolean"/>
     <xsd:element name="states" minOccurs="0" maxOccurs="unbounded" type="tns:State"/>
     <xsd:element name="visible" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="State">
    <xsd:sequence>
     <xsd:element name="active" type="xsd:boolean"/>
     <xsd:element name="integrationValue" type="xsd:string"/>
     <xsd:element name="isoCode" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="standard" type="xsd:boolean"/>
     <xsd:element name="visible" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AnalyticSnapshot">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="groupColumn" minOccurs="0" type="xsd:string"/>
       <xsd:element name="mappings" minOccurs="0" maxOccurs="unbounded" type="tns:AnalyticSnapshotMapping"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="runningUser" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sourceReport" type="xsd:string"/>
       <xsd:element name="targetObject" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AnalyticSnapshotMapping">
    <xsd:sequence>
     <xsd:element name="aggregateType" minOccurs="0" type="tns:ReportSummaryType"/>
     <xsd:element name="sourceField" type="xsd:string"/>
     <xsd:element name="sourceType" type="tns:ReportJobSourceTypes"/>
     <xsd:element name="targetField" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ReportSummaryType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Sum"/>
     <xsd:enumeration value="Average"/>
     <xsd:enumeration value="Maximum"/>
     <xsd:enumeration value="Minimum"/>
     <xsd:enumeration value="Unique"/>
     <xsd:enumeration value="None"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ReportJobSourceTypes">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="tabular"/>
     <xsd:enumeration value="summary"/>
     <xsd:enumeration value="snapshot"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="AnalyticsSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="alwaysGenPreviews" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="analyticsAdoptionMetadata" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="canAccessAnalyticsViaAPI" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="canAnnotateDashboards" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="canEnableSavedView" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="canExploreDataConversationally" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="canShareAppsWithCommunities" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="canViewThumbnailAssets" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAnalyticsEncryption" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAnalyticsSharingEnable" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAutoCompleteCombo" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableC360GlobalProfileData" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDashboardComponentSnapshot" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDashboardFlexiTable" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDashboardToPDFEnable" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailReportsToPortalUsers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFirebirdEditor" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFloatingReportHeaders" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInsights" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLightningReportBuilder" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLotusNotesImages" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMassEnableReportBuilder" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNewChartsEngine" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNullDimension" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOrgHasMobileOfflineEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOrgHasWatchlistEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableQueryLiveConnectors" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRemoveFooterForRepDisplay" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRemoveFooterFromRepExp" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableReportHideXlsExportPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableReportInlineEditPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableReportNotificationsEnable" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRequestPrioritySchdl" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableS1AnalyticsEclairEnable" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableS3OutputConnector" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSFXJoinedReportsEnable" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSalesforceOutputConnector" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSecureImageSharing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSnowflakeOutputConnector" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSqlDataset" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSqlLiveDataset" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTableauHyperOutputConnector" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUseOldChartsLookAndFeel" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWaveAssetsNewDateVersion" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWaveCustomFiscal" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWaveIndexMVDim" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWaveIndexMVDimV2" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWaveRecordNavigation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWaveReplication" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWaveSharingInheritance" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWaveSqlInQueryApi" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWaveTrendedDatasetCleanup" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="maxHoursAppInProgress" minOccurs="0" type="xsd:int"/>
       <xsd:element name="recipePreCachingOptOut" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="replaceBlankMeasuresWithNulls" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="setWaveIsYearEndFiscalYear" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="sonicEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="turnOnTimeZones" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AnimationRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="animationFrequency" type="xsd:string"/>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="isActive" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="recordTypeContext" type="xsd:string"/>
       <xsd:element name="recordTypeName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sobjectType" type="xsd:string"/>
       <xsd:element name="targetField" type="xsd:string"/>
       <xsd:element name="targetFieldChangeToValues" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ApexEmailNotifications">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="apexEmailNotification" minOccurs="0" maxOccurs="unbounded" type="tns:ApexEmailNotification"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ApexEmailNotification">
    <xsd:sequence>
     <xsd:element name="email" minOccurs="0" type="xsd:string"/>
     <xsd:element name="user" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ApexSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableAggregateCodeCoverageOnly" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableApexAccessRightsPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableApexApprovalLockUnlock" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableApexCtrlImplicitWithSharingPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableApexPropertyGetterPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAuraApexCtrlAuthUserAccessCheckPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAuraApexCtrlGuestUserAccessCheckPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCompileOnDeploy" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDisableParallelApexTesting" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDoNotEmailDebugLog" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGaplessTestAutoNum" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMngdCtrlActionAccessPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNonCertifiedApexMdCrud" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRunDynamicTriggers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSecureNoArgConstructorPref" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ApexTestSuite">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="testClassName" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AppExperienceSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="doesHideAllAppsInAppLauncher" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AppMenu">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="appMenuItems" minOccurs="0" maxOccurs="unbounded" type="tns:AppMenuItem"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AppMenuItem">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="type" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AppointmentSchedulingPolicy">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="appointmentAssignmentPolicy" minOccurs="0" type="xsd:string"/>
       <xsd:element name="appointmentStartTimeInterval" type="xsd:string"/>
       <xsd:element name="extCalEventHandler" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="shouldCheckExternalCalendar" type="xsd:boolean"/>
       <xsd:element name="shouldConsiderCalendarEvents" type="xsd:boolean"/>
       <xsd:element name="shouldEnforceExcludedResource" type="xsd:boolean"/>
       <xsd:element name="shouldEnforceRequiredResource" type="xsd:boolean"/>
       <xsd:element name="shouldMatchSkill" type="xsd:boolean"/>
       <xsd:element name="shouldMatchSkillLevel" type="xsd:boolean"/>
       <xsd:element name="shouldRespectVisitingHours" type="xsd:boolean"/>
       <xsd:element name="shouldUsePrimaryMembers" type="xsd:boolean"/>
       <xsd:element name="shouldUseSecondaryMembers" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ApprovalProcess">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="allowRecall" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="allowedSubmitters" minOccurs="0" maxOccurs="unbounded" type="tns:ApprovalSubmitter"/>
       <xsd:element name="approvalPageFields" minOccurs="0" type="tns:ApprovalPageField"/>
       <xsd:element name="approvalStep" minOccurs="0" maxOccurs="unbounded" type="tns:ApprovalStep"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="emailTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="enableMobileDeviceAccess" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="entryCriteria" minOccurs="0" type="tns:ApprovalEntryCriteria"/>
       <xsd:element name="finalApprovalActions" minOccurs="0" type="tns:ApprovalAction"/>
       <xsd:element name="finalApprovalRecordLock" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="finalRejectionActions" minOccurs="0" type="tns:ApprovalAction"/>
       <xsd:element name="finalRejectionRecordLock" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="initialSubmissionActions" minOccurs="0" type="tns:ApprovalAction"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="nextAutomatedApprover" minOccurs="0" type="tns:NextAutomatedApprover"/>
       <xsd:element name="postTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="processOrder" minOccurs="0" type="xsd:int"/>
       <xsd:element name="recallActions" minOccurs="0" type="tns:ApprovalAction"/>
       <xsd:element name="recordEditability" type="tns:RecordEditabilityType"/>
       <xsd:element name="showApprovalHistory" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ApprovalSubmitter">
    <xsd:sequence>
     <xsd:element name="submitter" minOccurs="0" type="xsd:string"/>
     <xsd:element name="type" type="tns:ProcessSubmitterType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ProcessSubmitterType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="group"/>
     <xsd:enumeration value="role"/>
     <xsd:enumeration value="user"/>
     <xsd:enumeration value="roleSubordinates"/>
     <xsd:enumeration value="roleSubordinatesInternal"/>
     <xsd:enumeration value="owner"/>
     <xsd:enumeration value="creator"/>
     <xsd:enumeration value="partnerUser"/>
     <xsd:enumeration value="customerPortalUser"/>
     <xsd:enumeration value="portalRole"/>
     <xsd:enumeration value="portalRoleSubordinates"/>
     <xsd:enumeration value="allInternalUsers"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ApprovalPageField">
    <xsd:sequence>
     <xsd:element name="field" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ApprovalStep">
    <xsd:sequence>
     <xsd:element name="allowDelegate" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="approvalActions" minOccurs="0" type="tns:ApprovalAction"/>
     <xsd:element name="assignedApprover" type="tns:ApprovalStepApprover"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="entryCriteria" minOccurs="0" type="tns:ApprovalEntryCriteria"/>
     <xsd:element name="ifCriteriaNotMet" minOccurs="0" type="tns:StepCriteriaNotMetType"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="rejectBehavior" minOccurs="0" type="tns:ApprovalStepRejectBehavior"/>
     <xsd:element name="rejectionActions" minOccurs="0" type="tns:ApprovalAction"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ApprovalAction">
    <xsd:sequence>
     <xsd:element name="action" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowActionReference"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WorkflowActionReference">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="type" type="tns:WorkflowActionType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="WorkflowActionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="FieldUpdate"/>
     <xsd:enumeration value="KnowledgePublish"/>
     <xsd:enumeration value="Task"/>
     <xsd:enumeration value="Alert"/>
     <xsd:enumeration value="Send"/>
     <xsd:enumeration value="OutboundMessage"/>
     <xsd:enumeration value="FlowAction"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ApprovalStepApprover">
    <xsd:sequence>
     <xsd:element name="approver" minOccurs="0" maxOccurs="unbounded" type="tns:Approver"/>
     <xsd:element name="whenMultipleApprovers" minOccurs="0" type="tns:RoutingType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Approver">
    <xsd:sequence>
     <xsd:element name="name" minOccurs="0" type="xsd:string"/>
     <xsd:element name="type" type="tns:NextOwnerType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="NextOwnerType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="adhoc"/>
     <xsd:enumeration value="user"/>
     <xsd:enumeration value="userHierarchyField"/>
     <xsd:enumeration value="relatedUserField"/>
     <xsd:enumeration value="queue"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="RoutingType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Unanimous"/>
     <xsd:enumeration value="FirstResponse"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ApprovalEntryCriteria">
    <xsd:sequence>
     <xsd:element name="booleanFilter" minOccurs="0" type="xsd:string"/>
     <xsd:element name="criteriaItems" minOccurs="0" maxOccurs="unbounded" type="tns:FilterItem"/>
     <xsd:element name="formula" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FilterItem">
    <xsd:sequence>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="operation" type="tns:FilterOperation"/>
     <xsd:element name="value" minOccurs="0" type="xsd:string"/>
     <xsd:element name="valueField" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FilterOperation">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="equals"/>
     <xsd:enumeration value="notEqual"/>
     <xsd:enumeration value="lessThan"/>
     <xsd:enumeration value="greaterThan"/>
     <xsd:enumeration value="lessOrEqual"/>
     <xsd:enumeration value="greaterOrEqual"/>
     <xsd:enumeration value="contains"/>
     <xsd:enumeration value="notContain"/>
     <xsd:enumeration value="startsWith"/>
     <xsd:enumeration value="includes"/>
     <xsd:enumeration value="excludes"/>
     <xsd:enumeration value="within"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DuplicateRuleFilterItem">
    <xsd:complexContent>
     <xsd:extension base="tns:FilterItem">
      <xsd:sequence>
       <xsd:element name="sortOrder" type="xsd:int"/>
       <xsd:element name="table" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="StepCriteriaNotMetType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ApproveRecord"/>
     <xsd:enumeration value="RejectRecord"/>
     <xsd:enumeration value="GotoNextStep"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ApprovalStepRejectBehavior">
    <xsd:sequence>
     <xsd:element name="type" type="tns:StepRejectBehaviorType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="StepRejectBehaviorType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="RejectRequest"/>
     <xsd:enumeration value="BackToPrevious"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="NextAutomatedApprover">
    <xsd:sequence>
     <xsd:element name="useApproverFieldOfRecordOwner" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="userHierarchyField" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="RecordEditabilityType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AdminOnly"/>
     <xsd:enumeration value="AdminOrCurrentApprover"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ArchiveSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableEntityArchivingEnabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AssignmentRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="ruleEntry" minOccurs="0" maxOccurs="unbounded" type="tns:RuleEntry"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="RuleEntry">
    <xsd:sequence>
     <xsd:element name="assignedTo" minOccurs="0" type="xsd:string"/>
     <xsd:element name="assignedToType" minOccurs="0" type="tns:AssignToLookupValueType"/>
     <xsd:element name="booleanFilter" minOccurs="0" type="xsd:string"/>
     <xsd:element name="businessHours" minOccurs="0" type="xsd:string"/>
     <xsd:element name="businessHoursSource" minOccurs="0" type="tns:BusinessHoursSourceType"/>
     <xsd:element name="criteriaItems" minOccurs="0" maxOccurs="unbounded" type="tns:FilterItem"/>
     <xsd:element name="disableEscalationWhenModified" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="escalationAction" minOccurs="0" maxOccurs="unbounded" type="tns:EscalationAction"/>
     <xsd:element name="escalationStartTime" minOccurs="0" type="tns:EscalationStartTimeType"/>
     <xsd:element name="formula" minOccurs="0" type="xsd:string"/>
     <xsd:element name="notifyCcRecipients" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="overrideExistingTeams" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="replyToEmail" minOccurs="0" type="xsd:string"/>
     <xsd:element name="senderEmail" minOccurs="0" type="xsd:string"/>
     <xsd:element name="senderName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="team" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="template" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="AssignToLookupValueType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="User"/>
     <xsd:enumeration value="Queue"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="BusinessHoursSourceType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="Case"/>
     <xsd:enumeration value="Static"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EscalationAction">
    <xsd:sequence>
     <xsd:element name="assignedTo" minOccurs="0" type="xsd:string"/>
     <xsd:element name="assignedToTemplate" minOccurs="0" type="xsd:string"/>
     <xsd:element name="assignedToType" minOccurs="0" type="tns:AssignToLookupValueType"/>
     <xsd:element name="minutesToEscalation" minOccurs="0" type="xsd:int"/>
     <xsd:element name="notifyCaseOwner" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="notifyEmail" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="notifyTo" minOccurs="0" type="xsd:string"/>
     <xsd:element name="notifyToTemplate" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="EscalationStartTimeType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="CaseCreation"/>
     <xsd:enumeration value="CaseLastModified"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="AssignmentRules">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="assignmentRule" minOccurs="0" maxOccurs="unbounded" type="tns:AssignmentRule"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Audience">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="audienceName" type="xsd:string"/>
       <xsd:element name="container" type="xsd:string"/>
       <xsd:element name="criteria" type="tns:AudienceCriteria"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="formula" minOccurs="0" type="xsd:string"/>
       <xsd:element name="formulaFilterType" minOccurs="0" type="tns:FormulaFilterType"/>
       <xsd:element name="isDefaultAudience" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="targets" minOccurs="0" type="tns:PersonalizationTargetInfos"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AudienceCriteria">
    <xsd:sequence>
     <xsd:element name="criterion" minOccurs="0" maxOccurs="unbounded" type="tns:AudienceCriterion"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AudienceCriterion">
    <xsd:sequence>
     <xsd:element name="criteriaNumber" minOccurs="0" type="xsd:int"/>
     <xsd:element name="criterionValue" minOccurs="0" type="tns:AudienceCriteriaValue"/>
     <xsd:element name="operator" minOccurs="0" type="tns:AudienceCriterionOperator"/>
     <xsd:element name="type" type="tns:AudienceCriterionType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AudienceCriteriaValue">
    <xsd:sequence>
     <xsd:element name="city" minOccurs="0" type="xsd:string"/>
     <xsd:element name="country" minOccurs="0" type="xsd:string"/>
     <xsd:element name="domain" minOccurs="0" type="xsd:string"/>
     <xsd:element name="entityField" minOccurs="0" type="xsd:string"/>
     <xsd:element name="entityType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="fieldValue" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isEnabled" minOccurs="0" type="xsd:string"/>
     <xsd:element name="permissionName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="permissionType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="profile" minOccurs="0" type="xsd:string"/>
     <xsd:element name="subdivision" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="AudienceCriterionOperator">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Equal"/>
     <xsd:enumeration value="NotEqual"/>
     <xsd:enumeration value="GreaterThan"/>
     <xsd:enumeration value="GreaterThanOrEqual"/>
     <xsd:enumeration value="LessThan"/>
     <xsd:enumeration value="LessThanOrEqual"/>
     <xsd:enumeration value="Contains"/>
     <xsd:enumeration value="StartsWith"/>
     <xsd:enumeration value="Includes"/>
     <xsd:enumeration value="NotIncludes"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="AudienceCriterionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Default"/>
     <xsd:enumeration value="Profile"/>
     <xsd:enumeration value="FieldBased"/>
     <xsd:enumeration value="GeoLocation"/>
     <xsd:enumeration value="Domain"/>
     <xsd:enumeration value="Permission"/>
     <xsd:enumeration value="Audience"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FormulaFilterType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AllCriteriaMatch"/>
     <xsd:enumeration value="AnyCriterionMatches"/>
     <xsd:enumeration value="CustomLogicMatches"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="PersonalizationTargetInfos">
    <xsd:sequence>
     <xsd:element name="target" minOccurs="0" maxOccurs="unbounded" type="tns:PersonalizationTargetInfo"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PersonalizationTargetInfo">
    <xsd:sequence>
     <xsd:element name="groupName" type="xsd:string"/>
     <xsd:element name="priority" minOccurs="0" type="xsd:int"/>
     <xsd:element name="targetType" type="xsd:string"/>
     <xsd:element name="targetValue" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AuraDefinitionBundle">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="SVGContent" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="apiVersion" minOccurs="0" type="xsd:double"/>
       <xsd:element name="auraDefinitions" minOccurs="0" type="tns:AuraDefinitions"/>
       <xsd:element name="controllerContent" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="designContent" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="documentationContent" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="helperContent" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="markup" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="modelContent" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="packageVersions" minOccurs="0" maxOccurs="unbounded" type="tns:PackageVersion"/>
       <xsd:element name="rendererContent" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="styleContent" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="testsuiteContent" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="type" minOccurs="0" type="tns:AuraBundleType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AuraDefinitions">
    <xsd:sequence>
     <xsd:element name="auraDefinition" minOccurs="0" maxOccurs="unbounded" type="tns:AuraDefinition"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AuraDefinition">
    <xsd:sequence>
     <xsd:element name="defType" type="xsd:string"/>
     <xsd:element name="source" type="xsd:base64Binary"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PackageVersion">
    <xsd:sequence>
     <xsd:element name="majorNumber" type="xsd:int"/>
     <xsd:element name="minorNumber" type="xsd:int"/>
     <xsd:element name="namespace" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="AuraBundleType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Application"/>
     <xsd:enumeration value="Component"/>
     <xsd:enumeration value="Event"/>
     <xsd:enumeration value="Interface"/>
     <xsd:enumeration value="Tokens"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="AuthProvider">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="appleTeam" minOccurs="0" type="xsd:string"/>
       <xsd:element name="authorizeUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="consumerKey" minOccurs="0" type="xsd:string"/>
       <xsd:element name="consumerSecret" minOccurs="0" type="xsd:string"/>
       <xsd:element name="customMetadataTypeRecord" minOccurs="0" type="xsd:string"/>
       <xsd:element name="defaultScopes" minOccurs="0" type="xsd:string"/>
       <xsd:element name="ecKey" minOccurs="0" type="xsd:string"/>
       <xsd:element name="errorUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="executionUser" minOccurs="0" type="xsd:string"/>
       <xsd:element name="friendlyName" type="xsd:string"/>
       <xsd:element name="iconUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="idTokenIssuer" minOccurs="0" type="xsd:string"/>
       <xsd:element name="includeOrgIdInIdentifier" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="linkKickoffUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="logoutUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="oauthKickoffUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="plugin" minOccurs="0" type="xsd:string"/>
       <xsd:element name="portal" minOccurs="0" type="xsd:string"/>
       <xsd:element name="providerType" type="tns:AuthProviderType"/>
       <xsd:element name="registrationHandler" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sendAccessTokenInHeader" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="sendClientCredentialsInHeader" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="sendSecretInApis" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="ssoKickoffUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="tokenUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="userInfoUrl" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="AuthProviderType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Facebook"/>
     <xsd:enumeration value="Janrain"/>
     <xsd:enumeration value="Salesforce"/>
     <xsd:enumeration value="OpenIdConnect"/>
     <xsd:enumeration value="MicrosoftACS"/>
     <xsd:enumeration value="LinkedIn"/>
     <xsd:enumeration value="Twitter"/>
     <xsd:enumeration value="Google"/>
     <xsd:enumeration value="GitHub"/>
     <xsd:enumeration value="Custom"/>
     <xsd:enumeration value="Apple"/>
     <xsd:enumeration value="Evergreen"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="AutoResponseRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="ruleEntry" minOccurs="0" maxOccurs="unbounded" type="tns:RuleEntry"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AutoResponseRules">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="autoResponseRule" minOccurs="0" maxOccurs="unbounded" type="tns:AutoResponseRule"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AutomatedContactsSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableAddContactAutomatically" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAddContactRoleAutomatically" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAddContactRoleWithSuggestion" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAddContactWithSuggestion" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="BlacklistedConsumer">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="blockedByApiWhitelisting" type="xsd:boolean"/>
       <xsd:element name="consumerKey" type="xsd:string"/>
       <xsd:element name="consumerName" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="BlockchainSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableBcp" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableBcpCoin" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Bot">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="botMlDomain" minOccurs="0" type="tns:LocalMlDomain"/>
       <xsd:element name="botUser" minOccurs="0" type="xsd:string"/>
       <xsd:element name="botVersions" minOccurs="0" maxOccurs="unbounded" type="tns:BotVersion"/>
       <xsd:element name="contextVariables" minOccurs="0" maxOccurs="unbounded" type="tns:ConversationContextVariable"/>
       <xsd:element name="conversationChannelProviders" minOccurs="0" maxOccurs="unbounded" type="tns:ConversationDefinitionChannelProvider"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" minOccurs="0" type="xsd:string"/>
       <xsd:element name="logPrivateConversationData" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="richContentEnabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="LocalMlDomain">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="mlIntents" minOccurs="0" maxOccurs="unbounded" type="tns:MlIntent"/>
     <xsd:element name="mlSlotClasses" minOccurs="0" maxOccurs="unbounded" type="tns:MlSlotClass"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="MlIntent">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="mlIntentUtterances" minOccurs="0" maxOccurs="unbounded" type="tns:MlIntentUtterance"/>
     <xsd:element name="relatedMlIntents" minOccurs="0" maxOccurs="unbounded" type="tns:MlRelatedIntent"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="MlIntentUtterance">
    <xsd:sequence>
     <xsd:element name="language" minOccurs="0" type="tns:Language"/>
     <xsd:element name="utterance" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="Language">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="en_US"/>
     <xsd:enumeration value="de"/>
     <xsd:enumeration value="es"/>
     <xsd:enumeration value="fr"/>
     <xsd:enumeration value="it"/>
     <xsd:enumeration value="ja"/>
     <xsd:enumeration value="sv"/>
     <xsd:enumeration value="ko"/>
     <xsd:enumeration value="zh_TW"/>
     <xsd:enumeration value="zh_CN"/>
     <xsd:enumeration value="pt_BR"/>
     <xsd:enumeration value="nl_NL"/>
     <xsd:enumeration value="da"/>
     <xsd:enumeration value="th"/>
     <xsd:enumeration value="fi"/>
     <xsd:enumeration value="ru"/>
     <xsd:enumeration value="es_MX"/>
     <xsd:enumeration value="no"/>
     <xsd:enumeration value="hu"/>
     <xsd:enumeration value="pl"/>
     <xsd:enumeration value="cs"/>
     <xsd:enumeration value="tr"/>
     <xsd:enumeration value="in"/>
     <xsd:enumeration value="ro"/>
     <xsd:enumeration value="vi"/>
     <xsd:enumeration value="uk"/>
     <xsd:enumeration value="iw"/>
     <xsd:enumeration value="el"/>
     <xsd:enumeration value="bg"/>
     <xsd:enumeration value="en_GB"/>
     <xsd:enumeration value="ar"/>
     <xsd:enumeration value="sk"/>
     <xsd:enumeration value="pt_PT"/>
     <xsd:enumeration value="hr"/>
     <xsd:enumeration value="sl"/>
     <xsd:enumeration value="fr_CA"/>
     <xsd:enumeration value="ka"/>
     <xsd:enumeration value="sr"/>
     <xsd:enumeration value="sh"/>
     <xsd:enumeration value="en_AU"/>
     <xsd:enumeration value="en_MY"/>
     <xsd:enumeration value="en_IN"/>
     <xsd:enumeration value="en_PH"/>
     <xsd:enumeration value="en_CA"/>
     <xsd:enumeration value="ro_MD"/>
     <xsd:enumeration value="bs"/>
     <xsd:enumeration value="mk"/>
     <xsd:enumeration value="lv"/>
     <xsd:enumeration value="lt"/>
     <xsd:enumeration value="et"/>
     <xsd:enumeration value="sq"/>
     <xsd:enumeration value="sh_ME"/>
     <xsd:enumeration value="mt"/>
     <xsd:enumeration value="ga"/>
     <xsd:enumeration value="eu"/>
     <xsd:enumeration value="cy"/>
     <xsd:enumeration value="is"/>
     <xsd:enumeration value="ms"/>
     <xsd:enumeration value="tl"/>
     <xsd:enumeration value="lb"/>
     <xsd:enumeration value="rm"/>
     <xsd:enumeration value="hy"/>
     <xsd:enumeration value="hi"/>
     <xsd:enumeration value="ur"/>
     <xsd:enumeration value="bn"/>
     <xsd:enumeration value="de_AT"/>
     <xsd:enumeration value="de_CH"/>
     <xsd:enumeration value="ta"/>
     <xsd:enumeration value="ar_DZ"/>
     <xsd:enumeration value="ar_BH"/>
     <xsd:enumeration value="ar_EG"/>
     <xsd:enumeration value="ar_IQ"/>
     <xsd:enumeration value="ar_JO"/>
     <xsd:enumeration value="ar_KW"/>
     <xsd:enumeration value="ar_LB"/>
     <xsd:enumeration value="ar_LY"/>
     <xsd:enumeration value="ar_MA"/>
     <xsd:enumeration value="ar_OM"/>
     <xsd:enumeration value="ar_QA"/>
     <xsd:enumeration value="ar_SA"/>
     <xsd:enumeration value="ar_SD"/>
     <xsd:enumeration value="ar_SY"/>
     <xsd:enumeration value="ar_TN"/>
     <xsd:enumeration value="ar_AE"/>
     <xsd:enumeration value="ar_YE"/>
     <xsd:enumeration value="zh_SG"/>
     <xsd:enumeration value="zh_HK"/>
     <xsd:enumeration value="en_HK"/>
     <xsd:enumeration value="en_IE"/>
     <xsd:enumeration value="en_SG"/>
     <xsd:enumeration value="en_ZA"/>
     <xsd:enumeration value="fr_BE"/>
     <xsd:enumeration value="fr_LU"/>
     <xsd:enumeration value="fr_CH"/>
     <xsd:enumeration value="de_BE"/>
     <xsd:enumeration value="de_LU"/>
     <xsd:enumeration value="it_CH"/>
     <xsd:enumeration value="nl_BE"/>
     <xsd:enumeration value="es_AR"/>
     <xsd:enumeration value="es_BO"/>
     <xsd:enumeration value="es_CL"/>
     <xsd:enumeration value="es_CO"/>
     <xsd:enumeration value="es_CR"/>
     <xsd:enumeration value="es_DO"/>
     <xsd:enumeration value="es_EC"/>
     <xsd:enumeration value="es_SV"/>
     <xsd:enumeration value="es_GT"/>
     <xsd:enumeration value="es_HN"/>
     <xsd:enumeration value="es_NI"/>
     <xsd:enumeration value="es_PA"/>
     <xsd:enumeration value="es_PY"/>
     <xsd:enumeration value="es_PE"/>
     <xsd:enumeration value="es_PR"/>
     <xsd:enumeration value="es_US"/>
     <xsd:enumeration value="es_UY"/>
     <xsd:enumeration value="es_VE"/>
     <xsd:enumeration value="ca"/>
     <xsd:enumeration value="af"/>
     <xsd:enumeration value="sw"/>
     <xsd:enumeration value="zu"/>
     <xsd:enumeration value="xh"/>
     <xsd:enumeration value="te"/>
     <xsd:enumeration value="ml"/>
     <xsd:enumeration value="kn"/>
     <xsd:enumeration value="mr"/>
     <xsd:enumeration value="gu"/>
     <xsd:enumeration value="en_NZ"/>
     <xsd:enumeration value="mi"/>
     <xsd:enumeration value="my"/>
     <xsd:enumeration value="fa"/>
     <xsd:enumeration value="km"/>
     <xsd:enumeration value="am"/>
     <xsd:enumeration value="kk"/>
     <xsd:enumeration value="ht"/>
     <xsd:enumeration value="sm"/>
     <xsd:enumeration value="haw"/>
     <xsd:enumeration value="zh_MY"/>
     <xsd:enumeration value="ru_LT"/>
     <xsd:enumeration value="ru_PL"/>
     <xsd:enumeration value="ru_AM"/>
     <xsd:enumeration value="ru_KZ"/>
     <xsd:enumeration value="ru_KG"/>
     <xsd:enumeration value="ru_BY"/>
     <xsd:enumeration value="ru_MD"/>
     <xsd:enumeration value="ru_UA"/>
     <xsd:enumeration value="eo"/>
     <xsd:enumeration value="iw_EO"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="MlRelatedIntent">
    <xsd:sequence>
     <xsd:element name="relatedMlIntent" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="MlSlotClass">
    <xsd:sequence>
     <xsd:element name="dataType" type="tns:MlSlotClassDataType"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="extractionRegex" minOccurs="0" type="xsd:string"/>
     <xsd:element name="extractionType" minOccurs="0" type="tns:MlSlotClassExtractionType"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="mlSlotClassValues" minOccurs="0" maxOccurs="unbounded" type="tns:MlSlotClassValue"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="MlSlotClassDataType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Text"/>
     <xsd:enumeration value="Number"/>
     <xsd:enumeration value="Boolean"/>
     <xsd:enumeration value="Date"/>
     <xsd:enumeration value="DateTime"/>
     <xsd:enumeration value="Currency"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="MlSlotClassExtractionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Pattern"/>
     <xsd:enumeration value="Value"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="MlSlotClassValue">
    <xsd:sequence>
     <xsd:element name="synonymGroup" minOccurs="0" type="tns:SynonymGroup"/>
     <xsd:element name="value" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SynonymGroup">
    <xsd:sequence>
     <xsd:element name="languages" minOccurs="0" maxOccurs="unbounded" type="tns:Language"/>
     <xsd:element name="terms" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BotVersion">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="botDialogGroups" minOccurs="0" maxOccurs="unbounded" type="tns:BotDialogGroup"/>
       <xsd:element name="botDialogs" minOccurs="0" maxOccurs="unbounded" type="tns:BotDialog"/>
       <xsd:element name="conversationSystemDialogs" minOccurs="0" maxOccurs="unbounded" type="tns:ConversationSystemDialog"/>
       <xsd:element name="conversationVariables" minOccurs="0" maxOccurs="unbounded" type="tns:ConversationVariable"/>
       <xsd:element name="entryDialog" type="xsd:string"/>
       <xsd:element name="mainMenuDialog" type="xsd:string"/>
       <xsd:element name="nlpProviders" minOccurs="0" maxOccurs="unbounded" type="tns:ConversationDefinitionNlpProvider"/>
       <xsd:element name="responseDelayMilliseconds" minOccurs="0" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="BotDialogGroup">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BotDialog">
    <xsd:sequence>
     <xsd:element name="botDialogGroup" minOccurs="0" type="xsd:string"/>
     <xsd:element name="botSteps" minOccurs="0" maxOccurs="unbounded" type="tns:BotStep"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="mlIntent" minOccurs="0" type="xsd:string"/>
     <xsd:element name="mlIntentTrainingEnabled" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showInFooterMenu" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BotStep">
    <xsd:sequence>
     <xsd:element name="booleanFilter" minOccurs="0" type="xsd:string"/>
     <xsd:element name="botInvocation" minOccurs="0" type="tns:BotInvocation"/>
     <xsd:element name="botMessages" minOccurs="0" maxOccurs="unbounded" type="tns:BotMessage"/>
     <xsd:element name="botNavigation" minOccurs="0" type="tns:BotNavigation"/>
     <xsd:element name="botStepConditions" minOccurs="0" maxOccurs="unbounded" type="tns:BotStepCondition"/>
     <xsd:element name="botSteps" minOccurs="0" maxOccurs="unbounded" type="tns:BotStep"/>
     <xsd:element name="botVariableOperation" minOccurs="0" type="tns:BotVariableOperation"/>
     <xsd:element name="conversationRecordLookup" minOccurs="0" type="tns:ConversationRecordLookup"/>
     <xsd:element name="conversationSystemMessage" minOccurs="0" type="tns:ConversationSystemMessage"/>
     <xsd:element name="type" type="tns:BotStepType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BotInvocation">
    <xsd:sequence>
     <xsd:element name="invocationActionName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="invocationActionType" minOccurs="0" type="tns:ConversationInvocableTargetType"/>
     <xsd:element name="invocationMappings" minOccurs="0" maxOccurs="unbounded" type="tns:BotInvocationMapping"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ConversationInvocableTargetType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="apex"/>
     <xsd:enumeration value="flow"/>
     <xsd:enumeration value="standardInvocableAction"/>
     <xsd:enumeration value="logFeedback"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="BotInvocationMapping">
    <xsd:sequence>
     <xsd:element name="parameterName" type="xsd:string"/>
     <xsd:element name="type" type="tns:BotInvocationMappingType"/>
     <xsd:element name="value" minOccurs="0" type="xsd:string"/>
     <xsd:element name="variableName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="variableType" minOccurs="0" type="tns:ConversationVariableType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="BotInvocationMappingType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Input"/>
     <xsd:enumeration value="Output"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ConversationVariableType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ConversationVariable"/>
     <xsd:enumeration value="ContextVariable"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="BotMessage">
    <xsd:sequence>
     <xsd:element name="message" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BotNavigation">
    <xsd:sequence>
     <xsd:element name="botNavigationLinks" minOccurs="0" maxOccurs="unbounded" type="tns:BotNavigationLink"/>
     <xsd:element name="type" type="tns:BotNavigationType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BotNavigationLink">
    <xsd:sequence>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="targetBotDialog" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="BotNavigationType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Call"/>
     <xsd:enumeration value="Redirect"/>
     <xsd:enumeration value="TransferToAgent"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="BotStepCondition">
    <xsd:sequence>
     <xsd:element name="leftOperandName" type="xsd:string"/>
     <xsd:element name="leftOperandType" type="tns:ConversationVariableType"/>
     <xsd:element name="operatorType" type="tns:BotStepConditionOperatorType"/>
     <xsd:element name="rightOperandValue" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="BotStepConditionOperatorType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Equals"/>
     <xsd:enumeration value="NotEquals"/>
     <xsd:enumeration value="IsSet"/>
     <xsd:enumeration value="IsNotSet"/>
     <xsd:enumeration value="GreaterThan"/>
     <xsd:enumeration value="LessThan"/>
     <xsd:enumeration value="GreaterThanOrEqualTo"/>
     <xsd:enumeration value="LessThanOrEqualTo"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="BotVariableOperation">
    <xsd:sequence>
     <xsd:element name="askCollectIfSet" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="autoSelectIfSingleChoice" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="botInvocation" minOccurs="0" type="tns:BotInvocation"/>
     <xsd:element name="botMessages" minOccurs="0" maxOccurs="unbounded" type="tns:BotMessage"/>
     <xsd:element name="botQuickReplyOptions" minOccurs="0" maxOccurs="unbounded" type="tns:BotQuickReplyOption"/>
     <xsd:element name="botVariableOperands" minOccurs="0" maxOccurs="unbounded" type="tns:BotVariableOperand"/>
     <xsd:element name="invalidInputBotNavigation" minOccurs="0" type="tns:BotNavigation"/>
     <xsd:element name="optionalCollect" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="quickReplyOptionTemplate" minOccurs="0" type="xsd:string"/>
     <xsd:element name="quickReplyType" minOccurs="0" type="tns:BotQuickReplyType"/>
     <xsd:element name="quickReplyWidgetType" minOccurs="0" type="tns:BotWidgetType"/>
     <xsd:element name="retryMessages" minOccurs="0" maxOccurs="unbounded" type="tns:BotMessage"/>
     <xsd:element name="sourceVariableName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sourceVariableType" minOccurs="0" type="tns:ConversationVariableType"/>
     <xsd:element name="type" type="tns:BotVariableOperationType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BotQuickReplyOption">
    <xsd:sequence>
     <xsd:element name="literalValue" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BotVariableOperand">
    <xsd:sequence>
     <xsd:element name="disableAutoFill" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="sourceName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sourceType" minOccurs="0" type="tns:ConversationVariableOperandSourceType"/>
     <xsd:element name="sourceValue" minOccurs="0" type="xsd:string"/>
     <xsd:element name="targetName" type="xsd:string"/>
     <xsd:element name="targetType" type="tns:ConversationVariableType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ConversationVariableOperandSourceType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="StandardConversationVariable"/>
     <xsd:enumeration value="ConversationVariable"/>
     <xsd:enumeration value="ContextVariable"/>
     <xsd:enumeration value="MlSlotClass"/>
     <xsd:enumeration value="StandardMlSlotClass"/>
     <xsd:enumeration value="Value"/>
     <xsd:enumeration value="BotDefinition"/>
     <xsd:enumeration value="Queue"/>
     <xsd:enumeration value="FlowDefinition"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="BotQuickReplyType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Static"/>
     <xsd:enumeration value="Dynamic"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="BotWidgetType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Menu"/>
     <xsd:enumeration value="Buttons"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="BotVariableOperationType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Set"/>
     <xsd:enumeration value="Unset"/>
     <xsd:enumeration value="Collect"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ConversationRecordLookup">
    <xsd:sequence>
     <xsd:element name="SObjectType" type="xsd:string"/>
     <xsd:element name="conditions" minOccurs="0" maxOccurs="unbounded" type="tns:ConversationRecordLookupCondition"/>
     <xsd:element name="filterLogic" minOccurs="0" type="xsd:string"/>
     <xsd:element name="lookupFields" minOccurs="0" maxOccurs="unbounded" type="tns:ConversationRecordLookupField"/>
     <xsd:element name="maxLookupResults" type="xsd:int"/>
     <xsd:element name="sortFieldName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sortOrder" minOccurs="0" type="tns:SortOrder"/>
     <xsd:element name="sourceVariableName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sourceVariableType" minOccurs="0" type="tns:ConversationVariableType"/>
     <xsd:element name="targetVariableName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ConversationRecordLookupCondition">
    <xsd:sequence>
     <xsd:element name="leftOperand" type="xsd:string"/>
     <xsd:element name="operatorType" type="xsd:string"/>
     <xsd:element name="rightOperandName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="rightOperandType" minOccurs="0" type="tns:ConversationVariableType"/>
     <xsd:element name="rightOperandValue" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sortOrder" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ConversationRecordLookupField">
    <xsd:sequence>
     <xsd:element name="fieldName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="SortOrder">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Asc"/>
     <xsd:enumeration value="Desc"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ConversationSystemMessage">
    <xsd:sequence>
     <xsd:element name="systemMessageMappings" minOccurs="0" maxOccurs="unbounded" type="tns:ConversationSystemMessageMapping"/>
     <xsd:element name="type" type="tns:ConversationSystemMessageType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ConversationSystemMessageMapping">
    <xsd:sequence>
     <xsd:element name="mappingType" type="tns:ConversationMappingType"/>
     <xsd:element name="parameterType" type="tns:ConversationSystemMessageParamType"/>
     <xsd:element name="variableName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ConversationMappingType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Input"/>
     <xsd:enumeration value="Output"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ConversationSystemMessageParamType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Transfer"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ConversationSystemMessageType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Transfer"/>
     <xsd:enumeration value="EndChat"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="BotStepType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Navigation"/>
     <xsd:enumeration value="Invocation"/>
     <xsd:enumeration value="VariableOperation"/>
     <xsd:enumeration value="Message"/>
     <xsd:enumeration value="Wait"/>
     <xsd:enumeration value="Group"/>
     <xsd:enumeration value="SystemMessage"/>
     <xsd:enumeration value="RecordLookup"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ConversationSystemDialog">
    <xsd:sequence>
     <xsd:element name="dialog" type="xsd:string"/>
     <xsd:element name="type" type="tns:ConversationSystemDialogType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ConversationSystemDialogType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="TransferFailed"/>
     <xsd:enumeration value="ErrorHandling"/>
     <xsd:enumeration value="KnowledgeFallback"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ConversationVariable">
    <xsd:sequence>
     <xsd:element name="SObjectType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="collectionType" minOccurs="0" type="tns:ConversationVariableCollectionType"/>
     <xsd:element name="dataType" type="tns:ConversationDataType"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ConversationVariableCollectionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="List"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ConversationDataType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Text"/>
     <xsd:enumeration value="Number"/>
     <xsd:enumeration value="Boolean"/>
     <xsd:enumeration value="Object"/>
     <xsd:enumeration value="Date"/>
     <xsd:enumeration value="DateTime"/>
     <xsd:enumeration value="Currency"/>
     <xsd:enumeration value="Id"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ConversationDefinitionNlpProvider">
    <xsd:sequence>
     <xsd:element name="language" minOccurs="0" type="tns:Language"/>
     <xsd:element name="nlpProviderName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="nlpProviderType" type="tns:ConversationDefinitionNlpProviderType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ConversationDefinitionNlpProviderType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="EinsteinAi"/>
     <xsd:enumeration value="Apex"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ConversationContextVariable">
    <xsd:sequence>
     <xsd:element name="SObjectType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="contextVariableMappings" minOccurs="0" maxOccurs="unbounded" type="tns:ConversationContextVariableMapping"/>
     <xsd:element name="dataType" type="tns:ConversationDataType"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ConversationContextVariableMapping">
    <xsd:sequence>
     <xsd:element name="SObjectType" type="xsd:string"/>
     <xsd:element name="fieldName" type="xsd:string"/>
     <xsd:element name="messageType" type="tns:MessageType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="MessageType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Text"/>
     <xsd:enumeration value="Facebook"/>
     <xsd:enumeration value="Line"/>
     <xsd:enumeration value="GoogleHome"/>
     <xsd:enumeration value="Alexa"/>
     <xsd:enumeration value="Omega"/>
     <xsd:enumeration value="AppleBusinessChat"/>
     <xsd:enumeration value="WeChat"/>
     <xsd:enumeration value="WebChat"/>
     <xsd:enumeration value="WhatsApp"/>
     <xsd:enumeration value="Phone"/>
     <xsd:enumeration value="EmbeddedMessaging"/>
     <xsd:enumeration value="Voice"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ConversationDefinitionChannelProvider">
    <xsd:sequence>
     <xsd:element name="agentRequired" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="chatButtonName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BotSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableBots" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="BrandingSet">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="brandingSetProperty" minOccurs="0" maxOccurs="unbounded" type="tns:BrandingSetProperty"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="type" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="BrandingSetProperty">
    <xsd:sequence>
     <xsd:element name="propertyName" type="xsd:string"/>
     <xsd:element name="propertyValue" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BriefcaseDefinition">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="briefcaseRules" minOccurs="0" maxOccurs="unbounded" type="tns:BriefcaseRule"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isActive" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="BriefcaseRule">
    <xsd:sequence>
     <xsd:element name="briefcaseRuleFilters" minOccurs="0" maxOccurs="unbounded" type="tns:BriefcaseRuleFilter"/>
     <xsd:element name="filterLogic" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isAscendingOrder" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="orderBy" minOccurs="0" type="xsd:string"/>
     <xsd:element name="queryScope" minOccurs="0" type="tns:FilterScope"/>
     <xsd:element name="recordLimit" minOccurs="0" type="xsd:int"/>
     <xsd:element name="targetEntity" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BriefcaseRuleFilter">
    <xsd:sequence>
     <xsd:element name="filterOperator" type="tns:BriefcaseFilterOperator"/>
     <xsd:element name="filterSeqNumber" type="xsd:int"/>
     <xsd:element name="filterValue" type="xsd:string"/>
     <xsd:element name="targetEntityField" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="BriefcaseFilterOperator">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="e"/>
     <xsd:enumeration value="l"/>
     <xsd:enumeration value="g"/>
     <xsd:enumeration value="m"/>
     <xsd:enumeration value="h"/>
     <xsd:enumeration value="s"/>
     <xsd:enumeration value="d"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FilterScope">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Everything"/>
     <xsd:enumeration value="Mine"/>
     <xsd:enumeration value="Queue"/>
     <xsd:enumeration value="Delegated"/>
     <xsd:enumeration value="MyTerritory"/>
     <xsd:enumeration value="MyTeamTerritory"/>
     <xsd:enumeration value="Team"/>
     <xsd:enumeration value="SalesTeam"/>
     <xsd:enumeration value="AssignedToMe"/>
     <xsd:enumeration value="MineAndMyGroups"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="BusinessHoursEntry">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="default" type="xsd:boolean"/>
       <xsd:element name="fridayEndTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="fridayStartTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="mondayEndTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="mondayStartTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="name" minOccurs="0" type="xsd:string"/>
       <xsd:element name="saturdayEndTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="saturdayStartTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="sundayEndTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="sundayStartTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="thursdayEndTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="thursdayStartTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="timeZoneId" minOccurs="0" type="xsd:string"/>
       <xsd:element name="tuesdayEndTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="tuesdayStartTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="wednesdayEndTime" minOccurs="0" type="xsd:time"/>
       <xsd:element name="wednesdayStartTime" minOccurs="0" type="xsd:time"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="BusinessHoursSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="businessHours" minOccurs="0" maxOccurs="unbounded" type="tns:BusinessHoursEntry"/>
       <xsd:element name="holidays" minOccurs="0" maxOccurs="unbounded" type="tns:Holiday"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Holiday">
    <xsd:sequence>
     <xsd:element name="activityDate" minOccurs="0" type="xsd:date"/>
     <xsd:element name="businessHours" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="endTime" minOccurs="0" type="xsd:time"/>
     <xsd:element name="isRecurring" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="name" minOccurs="0" type="xsd:string"/>
     <xsd:element name="recurrenceDayOfMonth" minOccurs="0" type="xsd:int"/>
     <xsd:element name="recurrenceDayOfWeek" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="recurrenceDayOfWeekMask" minOccurs="0" type="xsd:int"/>
     <xsd:element name="recurrenceEndDate" minOccurs="0" type="xsd:date"/>
     <xsd:element name="recurrenceInstance" minOccurs="0" type="xsd:string"/>
     <xsd:element name="recurrenceInterval" minOccurs="0" type="xsd:int"/>
     <xsd:element name="recurrenceMonthOfYear" minOccurs="0" type="xsd:string"/>
     <xsd:element name="recurrenceStartDate" minOccurs="0" type="xsd:date"/>
     <xsd:element name="recurrenceType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="startTime" minOccurs="0" type="xsd:time"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BusinessProcess">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="values" minOccurs="0" maxOccurs="unbounded" type="tns:PicklistValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PicklistValue">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="color" minOccurs="0" type="xsd:string"/>
       <xsd:element name="default" type="xsd:boolean"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="allowEmail" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="closed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="controllingFieldValues" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="converted" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="cssExposed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="forecastCategory" minOccurs="0" type="tns:ForecastCategories"/>
       <xsd:element name="highPriority" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="probability" minOccurs="0" type="xsd:int"/>
       <xsd:element name="reverseRole" minOccurs="0" type="xsd:string"/>
       <xsd:element name="reviewed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="won" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ForecastCategories">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Omitted"/>
     <xsd:enumeration value="Pipeline"/>
     <xsd:enumeration value="BestCase"/>
     <xsd:enumeration value="Forecast"/>
     <xsd:enumeration value="Closed"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="BusinessProcessGroup">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="businessProcessDefinitions" minOccurs="0" maxOccurs="unbounded" type="tns:BusinessProcessDefinition"/>
       <xsd:element name="customerSatisfactionMetric" type="tns:SurveyQuestionType"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="BusinessProcessDefinition">
    <xsd:sequence>
     <xsd:element name="businessProcessFeedbacks" minOccurs="0" maxOccurs="unbounded" type="tns:BusinessProcessFeedback"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="masterLabel" type="xsd:string"/>
     <xsd:element name="sequenceNumber" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="BusinessProcessFeedback">
    <xsd:sequence>
     <xsd:element name="actionName" type="xsd:string"/>
     <xsd:element name="actionParam" type="xsd:string"/>
     <xsd:element name="actionType" type="tns:ExpFeedbackCollType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ExpFeedbackCollType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="SURVEY"/>
     <xsd:enumeration value="PHONE_CALL"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SurveyQuestionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="MultiChoice"/>
     <xsd:enumeration value="RadioButton"/>
     <xsd:enumeration value="FreeText"/>
     <xsd:enumeration value="Date"/>
     <xsd:enumeration value="Rating"/>
     <xsd:enumeration value="CSAT"/>
     <xsd:enumeration value="Slider"/>
     <xsd:enumeration value="Picklist"/>
     <xsd:enumeration value="NPS"/>
     <xsd:enumeration value="StackRank"/>
     <xsd:enumeration value="Currency"/>
     <xsd:enumeration value="Number"/>
     <xsd:enumeration value="DateTime"/>
     <xsd:enumeration value="Toggle"/>
     <xsd:enumeration value="MultiSelectPicklist"/>
     <xsd:enumeration value="Image"/>
     <xsd:enumeration value="Boolean"/>
     <xsd:enumeration value="ShortText"/>
     <xsd:enumeration value="Attachment"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="CMSConnectSource">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="cmsConnectAsset" minOccurs="0" maxOccurs="unbounded" type="tns:CMSConnectAsset"/>
       <xsd:element name="cmsConnectLanguage" minOccurs="0" maxOccurs="unbounded" type="tns:CMSConnectLanguage"/>
       <xsd:element name="cmsConnectPersonalization" minOccurs="0" type="tns:CMSConnectPersonalization"/>
       <xsd:element name="cmsConnectResourceType" minOccurs="0" maxOccurs="unbounded" type="tns:CMSConnectResourceType"/>
       <xsd:element name="connectionType" type="tns:CMSSourceConnectionType"/>
       <xsd:element name="cssScope" minOccurs="0" type="xsd:string"/>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="languageEnabled" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="namedCredential" minOccurs="0" type="xsd:string"/>
       <xsd:element name="personalizationEnabled" minOccurs="0" type="xsd:string"/>
       <xsd:element name="rootPath" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sortOrder" type="xsd:int"/>
       <xsd:element name="status" type="tns:CMSConnectionStatus"/>
       <xsd:element name="type" type="tns:CMSConnectionSourceType"/>
       <xsd:element name="websiteUrl" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CMSConnectAsset">
    <xsd:sequence>
     <xsd:element name="assetPath" type="xsd:string"/>
     <xsd:element name="assetType" type="xsd:string"/>
     <xsd:element name="sortOrder" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CMSConnectLanguage">
    <xsd:sequence>
     <xsd:element name="cmsLanguage" type="xsd:string"/>
     <xsd:element name="language" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CMSConnectPersonalization">
    <xsd:sequence>
     <xsd:element name="connectorPage" type="xsd:string"/>
     <xsd:element name="connectorPageAsset" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CMSConnectResourceType">
    <xsd:sequence>
     <xsd:element name="cmsConnectResourceDefinition" minOccurs="0" maxOccurs="unbounded" type="tns:CMSConnectResourceDefinition"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="masterLabel" type="xsd:string"/>
     <xsd:element name="resourceType" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CMSConnectResourceDefinition">
    <xsd:sequence>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="masterLabel" type="xsd:string"/>
     <xsd:element name="options" type="xsd:int"/>
     <xsd:element name="payloadType" type="xsd:string"/>
     <xsd:element name="resourceIdPath" minOccurs="0" type="xsd:string"/>
     <xsd:element name="resourceNamePath" minOccurs="0" type="xsd:string"/>
     <xsd:element name="resourcePath" type="xsd:string"/>
     <xsd:element name="rootNodePath" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="CMSSourceConnectionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Public"/>
     <xsd:enumeration value="Authenticated"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="CMSConnectionStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ACTIVE"/>
     <xsd:enumeration value="INACTIVE"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="CMSConnectionSourceType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AEM"/>
     <xsd:enumeration value="Drupal"/>
     <xsd:enumeration value="WordPress"/>
     <xsd:enumeration value="SDL"/>
     <xsd:enumeration value="Sitecore"/>
     <xsd:enumeration value="Other"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="CallCenter">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="adapterUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="customSettings" minOccurs="0" type="xsd:string"/>
       <xsd:element name="displayName" type="xsd:string"/>
       <xsd:element name="displayNameLabel" type="xsd:string"/>
       <xsd:element name="internalNameLabel" type="xsd:string"/>
       <xsd:element name="sections" minOccurs="0" maxOccurs="unbounded" type="tns:CallCenterSection"/>
       <xsd:element name="version" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CallCenterSection">
    <xsd:sequence>
     <xsd:element name="items" minOccurs="0" maxOccurs="unbounded" type="tns:CallCenterItem"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CallCenterItem">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="value" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CallCenterRoutingMap">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="callCenter" type="xsd:string"/>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="externalId" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="referenceRecord" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CallCoachingMediaProvider">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="isActive" type="xsd:boolean"/>
       <xsd:element name="providerDescription" type="xsd:string"/>
       <xsd:element name="providerName" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CampaignInfluenceModel">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isDefaultModel" type="xsd:boolean"/>
       <xsd:element name="isModelLocked" type="xsd:boolean"/>
       <xsd:element name="modelDescription" minOccurs="0" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="recordPreference" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CampaignSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="aiAttributionTimeframe" minOccurs="0" type="xsd:int"/>
       <xsd:element name="enableAIAttribution" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAccountsAsCM" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAutoCampInfluenceDisabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableB2bmaCampaignInfluence2" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCampaignHistoryTrackEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCampaignInfluence2" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCampaignMemberTWCF" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEKAI" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSuppressNoValueCI2" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CanvasMetadata">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="accessMethod" type="xsd:string"/>
       <xsd:element name="canvasOptions" minOccurs="0" type="xsd:string"/>
       <xsd:element name="canvasUrl" type="xsd:string"/>
       <xsd:element name="lifecycleClass" minOccurs="0" type="xsd:string"/>
       <xsd:element name="locationOptions" minOccurs="0" type="xsd:string"/>
       <xsd:element name="samlInitiationMethod" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CareRequestConfiguration">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="careRequestRecordType" type="xsd:string"/>
       <xsd:element name="careRequestRecords" minOccurs="0" maxOccurs="unbounded" type="tns:CareRequestRecords"/>
       <xsd:element name="careRequestType" type="xsd:string"/>
       <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isDefaultRecordType" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CareRequestRecords">
    <xsd:sequence>
     <xsd:element name="careRequestRecord" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CaseSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="caseAssignNotificationTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="caseAutoProcUser" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="caseCloseNotificationTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="caseCommentNotificationTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="caseCreateNotificationTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="caseFeedItemSettings" minOccurs="0" maxOccurs="unbounded" type="tns:FeedItemSettings"/>
       <xsd:element name="caseFeedReadUnreadLtng" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="caseMergeInLightning" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="closeCaseThroughStatusChange" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="defaultCaseFeedLayoutOn" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="defaultCaseOwner" minOccurs="0" type="xsd:string"/>
       <xsd:element name="defaultCaseOwnerType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="defaultCaseUser" minOccurs="0" type="xsd:string"/>
       <xsd:element name="emailActionDefaultsHandlerClass" minOccurs="0" type="xsd:string"/>
       <xsd:element name="emailToCase" minOccurs="0" type="tns:EmailToCaseSettings"/>
       <xsd:element name="enableCaseFeed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCaseSwarming" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCollapseEmailThread" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDraftEmails" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEarlyEscalationRuleTriggers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailActionDefaultsHandler" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailContactOnCasePost" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEscalateQfiToCaseInternal" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEscalateQfiToCaseNetworks" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableExtNetworksCaseFeedEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMultiLangSolnSrchCSS" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMultiLangSolnSrchPKB" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMultiLangSolution" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSolutionCategory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSolutionInlineCategory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSolutionShortSummary" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSuggestedArticlesApplication" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSuggestedArticlesCustomerPortal" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSuggestedArticlesPartnerPortal" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSuggestedSolutions" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="escalateCaseBefore" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="genericMessageEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="keepCaseMergeRecords" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="keepRecordTypeOnAssignmentRule" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="notifyContactOnCaseComment" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="notifyDefaultCaseOwner" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="notifyOwnerOnCaseComment" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="notifyOwnerOnCaseOwnerChange" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="predictiveSupportEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showEmailAttachmentsInCaseAttachmentsRL" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showFewerCloseActions" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="systemUserEmail" minOccurs="0" type="xsd:string"/>
       <xsd:element name="useSystemEmailAddress" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="useSystemUserAsDefaultCaseUser" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="visibleInCssCheckbox" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="webToCase" minOccurs="0" type="tns:WebToCaseSettings"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FeedItemSettings">
    <xsd:sequence>
     <xsd:element name="characterLimit" minOccurs="0" type="xsd:int"/>
     <xsd:element name="displayFormat" minOccurs="0" type="tns:FeedItemDisplayFormat"/>
     <xsd:element name="feedItemType" type="tns:FeedItemType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FeedItemDisplayFormat">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Default"/>
     <xsd:enumeration value="HideBlankLines"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FeedItemType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="TrackedChange"/>
     <xsd:enumeration value="UserStatus"/>
     <xsd:enumeration value="TextPost"/>
     <xsd:enumeration value="AdvancedTextPost"/>
     <xsd:enumeration value="LinkPost"/>
     <xsd:enumeration value="ContentPost"/>
     <xsd:enumeration value="PollPost"/>
     <xsd:enumeration value="RypplePost"/>
     <xsd:enumeration value="ProfileSkillPost"/>
     <xsd:enumeration value="DashboardComponentSnapshot"/>
     <xsd:enumeration value="ApprovalPost"/>
     <xsd:enumeration value="CaseCommentPost"/>
     <xsd:enumeration value="ReplyPost"/>
     <xsd:enumeration value="EmailMessageEvent"/>
     <xsd:enumeration value="CallLogPost"/>
     <xsd:enumeration value="ChangeStatusPost"/>
     <xsd:enumeration value="AttachArticleEvent"/>
     <xsd:enumeration value="MilestoneEvent"/>
     <xsd:enumeration value="ActivityEvent"/>
     <xsd:enumeration value="ChatTranscriptPost"/>
     <xsd:enumeration value="CollaborationGroupCreated"/>
     <xsd:enumeration value="CollaborationGroupUnarchived"/>
     <xsd:enumeration value="SocialPost"/>
     <xsd:enumeration value="QuestionPost"/>
     <xsd:enumeration value="FacebookPost"/>
     <xsd:enumeration value="BasicTemplateFeedItem"/>
     <xsd:enumeration value="CreateRecordEvent"/>
     <xsd:enumeration value="CanvasPost"/>
     <xsd:enumeration value="AnnouncementPost"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EmailToCaseSettings">
    <xsd:sequence>
     <xsd:element name="enableE2CAttachmentAsFile" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableE2CSourceTracking" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableEmailToCase" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableHtmlEmail" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableOnDemandEmailToCase" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableThreadIDInBody" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableThreadIDInSubject" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="notifyOwnerOnNewCaseEmail" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="overEmailLimitAction" minOccurs="0" type="tns:EmailToCaseOnFailureActionType"/>
     <xsd:element name="preQuoteSignature" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="routingAddresses" minOccurs="0" maxOccurs="unbounded" type="tns:EmailToCaseRoutingAddress"/>
     <xsd:element name="unauthorizedSenderAction" minOccurs="0" type="tns:EmailToCaseOnFailureActionType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="EmailToCaseOnFailureActionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Bounce"/>
     <xsd:enumeration value="Discard"/>
     <xsd:enumeration value="Requeue"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EmailToCaseRoutingAddress">
    <xsd:sequence>
     <xsd:element name="addressType" minOccurs="0" type="tns:EmailToCaseRoutingAddressType"/>
     <xsd:element name="authorizedSenders" minOccurs="0" type="xsd:string"/>
     <xsd:element name="caseOrigin" minOccurs="0" type="xsd:string"/>
     <xsd:element name="caseOwner" minOccurs="0" type="xsd:string"/>
     <xsd:element name="caseOwnerType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="casePriority" minOccurs="0" type="xsd:string"/>
     <xsd:element name="createTask" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="emailAddress" minOccurs="0" type="xsd:string"/>
     <xsd:element name="emailServicesAddress" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isVerified" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="routingName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="saveEmailHeaders" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="taskStatus" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="EmailToCaseRoutingAddressType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="EmailToCase"/>
     <xsd:enumeration value="Outlook"/>
     <xsd:enumeration value="GmailOAuth"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="WebToCaseSettings">
    <xsd:sequence>
     <xsd:element name="caseOrigin" minOccurs="0" type="xsd:string"/>
     <xsd:element name="defaultResponseTemplate" minOccurs="0" type="xsd:string"/>
     <xsd:element name="enableWebToCase" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CaseSubjectParticle">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="index" type="xsd:int"/>
       <xsd:element name="textField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="type" type="tns:CaseSubjectParticleType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="CaseSubjectParticleType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ProvidedString"/>
     <xsd:enumeration value="Source"/>
     <xsd:enumeration value="MessageType"/>
     <xsd:enumeration value="SocialHandle"/>
     <xsd:enumeration value="SocialNetwork"/>
     <xsd:enumeration value="Sentiment"/>
     <xsd:enumeration value="RealName"/>
     <xsd:enumeration value="Content"/>
     <xsd:enumeration value="PipeSeparator"/>
     <xsd:enumeration value="ColonSeparator"/>
     <xsd:enumeration value="HyphenSeparator"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ChannelLayout">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="doesExcludeFieldLabels" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesExcludeFiles" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enabledChannels" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="layoutItems" minOccurs="0" maxOccurs="unbounded" type="tns:ChannelLayoutItem"/>
       <xsd:element name="recordType" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ChannelLayoutItem">
    <xsd:sequence>
     <xsd:element name="field" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ChannelObjectLinkingRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionForNoRecordFound" type="tns:ActionForNoRecordFound"/>
       <xsd:element name="actionForSingleRecordFound" type="tns:ActionForSingleRecordFound"/>
       <xsd:element name="channelType" type="tns:ChannelType"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isLinkedRecordOpenedAsSubTab" type="xsd:boolean"/>
       <xsd:element name="isRuleActive" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="objectToLink" type="tns:ObjectToLink"/>
       <xsd:element name="ruleName" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ActionForNoRecordFound">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="CreateNewRecordAndLink"/>
     <xsd:enumeration value="PromptAgent"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ActionForSingleRecordFound">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AutoLink"/>
     <xsd:enumeration value="PromptAgent"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ChannelType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="FacebookMessenger"/>
     <xsd:enumeration value="Text"/>
     <xsd:enumeration value="WeChat"/>
     <xsd:enumeration value="WhatsApp"/>
     <xsd:enumeration value="Phone"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ObjectToLink">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Contact"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ChatterAnswersSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="emailFollowersOnBestAnswer" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="emailFollowersOnReply" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="emailOwnerOnPrivateReply" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="emailOwnerOnReply" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAnswerViaEmail" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableChatterAnswers" type="xsd:boolean"/>
       <xsd:element name="enableFacebookSSO" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInlinePublisher" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableReputation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRichTextEditor" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="facebookAuthProvider" minOccurs="0" type="xsd:string"/>
       <xsd:element name="showInPortals" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ChatterEmailsMDSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableChatterDigestEmailsApiOnly" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableChatterEmailAttachment" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCollaborationEmail" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDisplayAppDownloadBadges" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailReplyToChatter" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailToChatter" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="noQnOwnNotifyOnCaseCmt" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="noQnOwnNotifyOnRep" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="noQnSubNotifyOnBestR" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="noQnSubNotifyOnRep" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ChatterExtension">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="compositionComponent" type="xsd:string"/>
       <xsd:element name="description" type="xsd:string"/>
       <xsd:element name="extensionName" type="xsd:string"/>
       <xsd:element name="headerText" minOccurs="0" type="xsd:string"/>
       <xsd:element name="hoverText" minOccurs="0" type="xsd:string"/>
       <xsd:element name="icon" type="xsd:string"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="renderComponent" type="xsd:string"/>
       <xsd:element name="type" type="tns:ChatterExtensionType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ChatterExtensionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Lightning"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ChatterSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="allowChatterGroupArchiving" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="allowRecordsInChatterGroup" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableApprovalRequest" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCaseFeedRelativeTimestamps" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableChatter" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableChatterEmoticons" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFeedEdit" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFeedPinning" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFeedsDraftPosts" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFeedsRichText" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInviteCsnUsers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOutOfOfficeEnabledPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRichLinkPreviewsInFeed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTodayRecsInFeed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="unlistedGroupsEnabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CleanDataService">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="cleanRules" minOccurs="0" maxOccurs="unbounded" type="tns:CleanRule"/>
       <xsd:element name="description" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="matchEngine" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CleanRule">
    <xsd:sequence>
     <xsd:element name="bulkEnabled" type="xsd:boolean"/>
     <xsd:element name="bypassTriggers" type="xsd:boolean"/>
     <xsd:element name="bypassWorkflow" type="xsd:boolean"/>
     <xsd:element name="description" type="xsd:string"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="fieldMappings" minOccurs="0" maxOccurs="unbounded" type="tns:FieldMapping"/>
     <xsd:element name="masterLabel" type="xsd:string"/>
     <xsd:element name="matchRule" type="xsd:string"/>
     <xsd:element name="sourceSobjectType" type="xsd:string"/>
     <xsd:element name="status" type="tns:CleanRuleStatus"/>
     <xsd:element name="targetSobjectType" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FieldMapping">
    <xsd:sequence>
     <xsd:element name="SObjectType" type="xsd:string"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="fieldMappingRows" minOccurs="0" maxOccurs="unbounded" type="tns:FieldMappingRow"/>
     <xsd:element name="masterLabel" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FieldMappingRow">
    <xsd:sequence>
     <xsd:element name="SObjectType" type="xsd:string"/>
     <xsd:element name="fieldMappingFields" minOccurs="0" maxOccurs="unbounded" type="tns:FieldMappingField"/>
     <xsd:element name="fieldName" type="xsd:string"/>
     <xsd:element name="mappingOperation" type="tns:MappingOperation"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FieldMappingField">
    <xsd:sequence>
     <xsd:element name="dataServiceField" type="xsd:string"/>
     <xsd:element name="dataServiceObjectName" type="xsd:string"/>
     <xsd:element name="priority" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="MappingOperation">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Autofill"/>
     <xsd:enumeration value="Overwrite"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="CleanRuleStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Inactive"/>
     <xsd:enumeration value="Active"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="CommandAction">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionType" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="intents" minOccurs="0" maxOccurs="unbounded" type="tns:CommandActionIntent"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="parameters" minOccurs="0" maxOccurs="unbounded" type="tns:CommandActionParam"/>
       <xsd:element name="responseTemplates" minOccurs="0" maxOccurs="unbounded" type="tns:CommandActionResponse"/>
       <xsd:element name="target" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CommandActionIntent">
    <xsd:sequence>
     <xsd:element name="phrase" type="xsd:string"/>
     <xsd:element name="responseTemplates" minOccurs="0" maxOccurs="unbounded" type="tns:CommandActionResponse"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CommandActionResponse">
    <xsd:sequence>
     <xsd:element name="template" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CommandActionParam">
    <xsd:sequence>
     <xsd:element name="defaultValue" minOccurs="0" type="xsd:string"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="required" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="type" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CommerceSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="commerceEnabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CommunitiesSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="applyLoginPageTypeToEmbeddedLogin" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="blockEmbeddedLoginUnknownURLRedirect" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="canModerateAllFeedPosts" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="canModerateInternalFeedPosts" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="embeddedVisualforcePages" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCommunityWorkspaces" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCspContactVisibilityPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCspNotesOnAccConPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEnablePRM" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableExternalAccHierPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGuestPermDisOptOutCruc" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGuestRecordReassignOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGuestSecurityOptOutCruc" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGuvSecurityOptOutPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInviteChatterGuestEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNetPortalUserReportOpts" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNetworksEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOotbProfExtUserOpsEnable" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePRMAccRelPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePowerCustomerCaseStatus" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePreventBadgeGuestAccess" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRelaxPartnerAccountFieldPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUnsupportedBrowserModalPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUsernameUniqForOrgPref" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Community">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="chatterAnswersFacebookSsoUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="communityFeedPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="dataCategoryName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="emailFooterDocument" minOccurs="0" type="xsd:string"/>
       <xsd:element name="emailHeaderDocument" minOccurs="0" type="xsd:string"/>
       <xsd:element name="emailNotificationUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="enableChatterAnswers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePrivateQuestions" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="expertsGroup" minOccurs="0" type="xsd:string"/>
       <xsd:element name="portal" minOccurs="0" type="xsd:string"/>
       <xsd:element name="reputationLevels" minOccurs="0" type="tns:ReputationLevels"/>
       <xsd:element name="showInPortal" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="site" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ReputationLevels">
    <xsd:sequence>
     <xsd:element name="chatterAnswersReputationLevels" minOccurs="0" maxOccurs="unbounded" type="tns:ChatterAnswersReputationLevel"/>
     <xsd:element name="ideaReputationLevels" minOccurs="0" maxOccurs="unbounded" type="tns:IdeaReputationLevel"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ChatterAnswersReputationLevel">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="value" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="IdeaReputationLevel">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="value" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CommunityTemplateDefinition">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="baseTemplate" minOccurs="0" type="tns:CommunityBaseTemplate"/>
       <xsd:element name="bundlesInfo" minOccurs="0" maxOccurs="unbounded" type="tns:CommunityTemplateBundleInfo"/>
       <xsd:element name="category" type="tns:CommunityTemplateCategory"/>
       <xsd:element name="defaultBrandingSet" minOccurs="0" type="xsd:string"/>
       <xsd:element name="defaultThemeDefinition" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="enableExtendedCleanUpOnDelete" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="navigationLinkSet" minOccurs="0" maxOccurs="unbounded" type="tns:NavigationLinkSet"/>
       <xsd:element name="pageSetting" minOccurs="0" maxOccurs="unbounded" type="tns:CommunityTemplatePageSetting"/>
       <xsd:element name="publisher" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="CommunityBaseTemplate">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="c"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="CommunityTemplateBundleInfo">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="image" minOccurs="0" type="xsd:string"/>
     <xsd:element name="order" type="xsd:int"/>
     <xsd:element name="title" type="xsd:string"/>
     <xsd:element name="type" type="tns:CommunityTemplateBundleInfoType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="CommunityTemplateBundleInfoType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Highlight"/>
     <xsd:enumeration value="PreviewImage"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="CommunityThemeBundleInfo">
    <xsd:complexContent>
     <xsd:extension base="tns:CommunityTemplateBundleInfo">
      <xsd:sequence/>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="CommunityTemplateCategory">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="IT"/>
     <xsd:enumeration value="Marketing"/>
     <xsd:enumeration value="Sales"/>
     <xsd:enumeration value="Service"/>
     <xsd:enumeration value="Commerce"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="NavigationLinkSet">
    <xsd:sequence>
     <xsd:element name="navigationMenuItem" minOccurs="0" maxOccurs="unbounded" type="tns:NavigationMenuItem"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="NavigationMenuItem">
    <xsd:sequence>
     <xsd:element name="defaultListViewId" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="menuItemBranding" minOccurs="0" type="tns:NavigationMenuItemBranding"/>
     <xsd:element name="position" type="xsd:int"/>
     <xsd:element name="publiclyAvailable" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="subMenu" minOccurs="0" type="tns:NavigationSubMenu"/>
     <xsd:element name="target" minOccurs="0" type="xsd:string"/>
     <xsd:element name="targetPreference" minOccurs="0" type="xsd:string"/>
     <xsd:element name="type" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="NavigationMenuItemBranding">
    <xsd:sequence>
     <xsd:element name="tileImage" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="NavigationSubMenu">
    <xsd:sequence>
     <xsd:element name="navigationMenuItem" minOccurs="0" maxOccurs="unbounded" type="tns:NavigationMenuItem"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CommunityTemplatePageSetting">
    <xsd:sequence>
     <xsd:element name="page" type="xsd:string"/>
     <xsd:element name="themeLayout" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CommunityThemeDefinition">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="bundlesInfo" minOccurs="0" maxOccurs="unbounded" type="tns:CommunityThemeBundleInfo"/>
       <xsd:element name="customThemeLayoutType" minOccurs="0" maxOccurs="unbounded" type="tns:CommunityCustomThemeLayoutType"/>
       <xsd:element name="defaultBrandingSet" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="enableExtendedCleanUpOnDelete" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="publisher" minOccurs="0" type="xsd:string"/>
       <xsd:element name="themeRouteOverride" minOccurs="0" maxOccurs="unbounded" type="tns:CommunityThemeRouteOverride"/>
       <xsd:element name="themeSetting" minOccurs="0" maxOccurs="unbounded" type="tns:CommunityThemeSetting"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CommunityCustomThemeLayoutType">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CommunityThemeRouteOverride">
    <xsd:sequence>
     <xsd:element name="customThemeLayoutType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="pageAttributes" type="xsd:string"/>
     <xsd:element name="pageType" type="xsd:string"/>
     <xsd:element name="themeLayoutType" minOccurs="0" type="tns:CommunityThemeLayoutType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="CommunityThemeLayoutType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Login"/>
     <xsd:enumeration value="Home"/>
     <xsd:enumeration value="Inner"/>
     <xsd:enumeration value="ServiceNotAvailable"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="CommunityThemeSetting">
    <xsd:sequence>
     <xsd:element name="customThemeLayoutType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="themeLayout" type="xsd:string"/>
     <xsd:element name="themeLayoutType" minOccurs="0" type="tns:CommunityThemeLayoutType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CompactLayout">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CompanySettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCustomFiscalYear" type="xsd:boolean"/>
       <xsd:element name="fiscalYear" minOccurs="0" type="tns:FiscalYearSettings"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FiscalYearSettings">
    <xsd:sequence>
     <xsd:element name="fiscalYearNameBasedOn" minOccurs="0" type="xsd:string"/>
     <xsd:element name="startMonth" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ConnectedApp">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="attributes" minOccurs="0" maxOccurs="unbounded" type="tns:ConnectedAppAttribute"/>
       <xsd:element name="canvas" minOccurs="0" type="tns:CanvasMetadata"/>
       <xsd:element name="canvasConfig" minOccurs="0" type="tns:ConnectedAppCanvasConfig"/>
       <xsd:element name="contactEmail" type="xsd:string"/>
       <xsd:element name="contactPhone" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="iconUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="infoUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="ipRanges" minOccurs="0" maxOccurs="unbounded" type="tns:ConnectedAppIpRange"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="logoUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="mobileAppConfig" minOccurs="0" type="tns:ConnectedAppMobileDetailConfig"/>
       <xsd:element name="mobileStartUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="oauthConfig" minOccurs="0" type="tns:ConnectedAppOauthConfig"/>
       <xsd:element name="oauthPolicy" minOccurs="0" type="tns:ConnectedAppOauthPolicy"/>
       <xsd:element name="permissionSetName" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="plugin" minOccurs="0" type="xsd:string"/>
       <xsd:element name="pluginExecutionUser" minOccurs="0" type="xsd:string"/>
       <xsd:element name="profileName" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="samlConfig" minOccurs="0" type="tns:ConnectedAppSamlConfig"/>
       <xsd:element name="sessionPolicy" minOccurs="0" type="tns:ConnectedAppSessionPolicy"/>
       <xsd:element name="startUrl" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ConnectedAppAttribute">
    <xsd:sequence>
     <xsd:element name="formula" type="xsd:string"/>
     <xsd:element name="key" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ConnectedAppCanvasConfig">
    <xsd:sequence>
     <xsd:element name="accessMethod" type="tns:AccessMethod"/>
     <xsd:element name="canvasUrl" type="xsd:string"/>
     <xsd:element name="lifecycleClass" minOccurs="0" type="xsd:string"/>
     <xsd:element name="locations" minOccurs="0" maxOccurs="unbounded" type="tns:CanvasLocationOptions"/>
     <xsd:element name="options" minOccurs="0" maxOccurs="unbounded" type="tns:CanvasOptions"/>
     <xsd:element name="samlInitiationMethod" minOccurs="0" type="tns:SamlInitiationMethod"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="AccessMethod">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Get"/>
     <xsd:enumeration value="Post"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="CanvasLocationOptions">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="Chatter"/>
     <xsd:enumeration value="UserProfile"/>
     <xsd:enumeration value="Visualforce"/>
     <xsd:enumeration value="Aura"/>
     <xsd:enumeration value="Publisher"/>
     <xsd:enumeration value="ChatterFeed"/>
     <xsd:enumeration value="ServiceDesk"/>
     <xsd:enumeration value="OpenCTI"/>
     <xsd:enumeration value="AppLauncher"/>
     <xsd:enumeration value="MobileNav"/>
     <xsd:enumeration value="PageLayout"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="CanvasOptions">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="HideShare"/>
     <xsd:enumeration value="HideHeader"/>
     <xsd:enumeration value="PersonalEnabled"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SamlInitiationMethod">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="IdpInitiated"/>
     <xsd:enumeration value="SpInitiated"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ConnectedAppIpRange">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="end" type="xsd:string"/>
     <xsd:element name="start" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ConnectedAppMobileDetailConfig">
    <xsd:sequence>
     <xsd:element name="applicationBinaryFile" minOccurs="0" type="xsd:base64Binary"/>
     <xsd:element name="applicationBinaryFileName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="applicationBundleIdentifier" minOccurs="0" type="xsd:string"/>
     <xsd:element name="applicationFileLength" minOccurs="0" type="xsd:int"/>
     <xsd:element name="applicationIconFile" minOccurs="0" type="xsd:string"/>
     <xsd:element name="applicationIconFileName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="applicationInstallUrl" minOccurs="0" type="xsd:string"/>
     <xsd:element name="devicePlatform" type="tns:DevicePlatformType"/>
     <xsd:element name="deviceType" minOccurs="0" type="tns:DeviceType"/>
     <xsd:element name="minimumOsVersion" minOccurs="0" type="xsd:string"/>
     <xsd:element name="privateApp" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="version" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DevicePlatformType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ios"/>
     <xsd:enumeration value="android"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="DeviceType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="phone"/>
     <xsd:enumeration value="tablet"/>
     <xsd:enumeration value="minitablet"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ConnectedAppOauthConfig">
    <xsd:sequence>
     <xsd:element name="assetTokenConfig" minOccurs="0" type="tns:ConnectedAppOauthAssetToken"/>
     <xsd:element name="callbackUrl" type="xsd:string"/>
     <xsd:element name="certificate" minOccurs="0" type="xsd:string"/>
     <xsd:element name="consumerKey" minOccurs="0" type="xsd:string"/>
     <xsd:element name="consumerSecret" minOccurs="0" type="xsd:string"/>
     <xsd:element name="idTokenConfig" minOccurs="0" type="tns:ConnectedAppOauthIdToken"/>
     <xsd:element name="isAdminApproved" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="isConsumerSecretOptional" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="isIntrospectAllTokens" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="isSecretRequiredForRefreshToken" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="scopes" minOccurs="0" maxOccurs="unbounded" type="tns:ConnectedAppOauthAccessScope"/>
     <xsd:element name="singleLogoutUrl" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ConnectedAppOauthAssetToken">
    <xsd:sequence>
     <xsd:element name="assetAudiences" type="xsd:string"/>
     <xsd:element name="assetIncludeAttributes" type="xsd:boolean"/>
     <xsd:element name="assetIncludeCustomPerms" type="xsd:boolean"/>
     <xsd:element name="assetSigningCertId" type="xsd:string"/>
     <xsd:element name="assetValidityPeriod" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ConnectedAppOauthIdToken">
    <xsd:sequence>
     <xsd:element name="idTokenAudience" minOccurs="0" type="xsd:string"/>
     <xsd:element name="idTokenIncludeAttributes" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="idTokenIncludeCustomPerms" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="idTokenIncludeStandardClaims" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="idTokenValidity" minOccurs="0" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ConnectedAppOauthAccessScope">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Basic"/>
     <xsd:enumeration value="Api"/>
     <xsd:enumeration value="Web"/>
     <xsd:enumeration value="Full"/>
     <xsd:enumeration value="Chatter"/>
     <xsd:enumeration value="CustomApplications"/>
     <xsd:enumeration value="RefreshToken"/>
     <xsd:enumeration value="OpenID"/>
     <xsd:enumeration value="Profile"/>
     <xsd:enumeration value="Email"/>
     <xsd:enumeration value="Address"/>
     <xsd:enumeration value="Phone"/>
     <xsd:enumeration value="OfflineAccess"/>
     <xsd:enumeration value="CustomPermissions"/>
     <xsd:enumeration value="Wave"/>
     <xsd:enumeration value="Eclair"/>
     <xsd:enumeration value="Pardot"/>
     <xsd:enumeration value="Lightning"/>
     <xsd:enumeration value="Content"/>
     <xsd:enumeration value="CDPIngest"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ConnectedAppOauthPolicy">
    <xsd:sequence>
     <xsd:element name="ipRelaxation" type="xsd:string"/>
     <xsd:element name="refreshTokenPolicy" type="xsd:string"/>
     <xsd:element name="singleLogoutUrl" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ConnectedAppSamlConfig">
    <xsd:sequence>
     <xsd:element name="acsUrl" type="xsd:string"/>
     <xsd:element name="certificate" minOccurs="0" type="xsd:string"/>
     <xsd:element name="encryptionCertificate" minOccurs="0" type="xsd:string"/>
     <xsd:element name="encryptionType" minOccurs="0" type="tns:SamlEncryptionType"/>
     <xsd:element name="entityUrl" type="xsd:string"/>
     <xsd:element name="issuer" minOccurs="0" type="xsd:string"/>
     <xsd:element name="samlIdpSLOBindingEnum" minOccurs="0" type="tns:SamlIdpSLOBinding"/>
     <xsd:element name="samlNameIdFormat" minOccurs="0" type="tns:SamlNameIdFormatType"/>
     <xsd:element name="samlSigningAlgoType" minOccurs="0" type="tns:SamlSigningAlgoType"/>
     <xsd:element name="samlSloUrl" minOccurs="0" type="xsd:string"/>
     <xsd:element name="samlSubjectCustomAttr" minOccurs="0" type="xsd:string"/>
     <xsd:element name="samlSubjectType" type="tns:SamlSubjectType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="SamlEncryptionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AES_128"/>
     <xsd:enumeration value="AES_256"/>
     <xsd:enumeration value="Triple_Des"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SamlIdpSLOBinding">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="RedirectBinding"/>
     <xsd:enumeration value="PostBinding"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SamlNameIdFormatType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Unspecified"/>
     <xsd:enumeration value="EmailAddress"/>
     <xsd:enumeration value="Persistent"/>
     <xsd:enumeration value="Transient"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SamlSigningAlgoType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="SHA1"/>
     <xsd:enumeration value="SHA256"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SamlSubjectType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Username"/>
     <xsd:enumeration value="FederationId"/>
     <xsd:enumeration value="UserId"/>
     <xsd:enumeration value="SpokeId"/>
     <xsd:enumeration value="CustomAttribute"/>
     <xsd:enumeration value="PersistentId"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ConnectedAppSessionPolicy">
    <xsd:sequence>
     <xsd:element name="policyAction" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sessionLevel" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sessionTimeout" minOccurs="0" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ConnectedAppSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableAdminApprovedAppsOnly" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAdminApprovedAppsOnlyForExternalUser" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSkipUserProvisioningWizardWelcomePage" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ContentSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCMSC2CConnections" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableChatterFileLink" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContent" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContentAutoAssign" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContentDistForPortalUsers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContentDistPwOptionsBit1" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContentDistPwOptionsBit2" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContentDistribution" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContentSupportMultiLanguage" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContentWorkspaceAccess" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDeleteFileInContentPacks" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFileShareSetByRecord" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFilesUsrShareNetRestricted" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableJPGPreviews" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLibraryManagedFiles" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableShowChatterFilesInContent" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSiteGuestUserToUploadFiles" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUploadFilesOnAttachments" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="setValidContentTypeForAtchDocDownload" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="skipContentAssetTriggers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="skipContentAssetTriggersOnDeploy" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ContractSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="autoCalculateEndDate" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="autoExpirationDelay" minOccurs="0" type="xsd:string"/>
       <xsd:element name="autoExpirationRecipient" minOccurs="0" type="xsd:string"/>
       <xsd:element name="autoExpireContracts" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContractHistoryTracking" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="notifyOwnersOnContractExpiration" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ConversationVendorInfo">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="bridgeComponent" minOccurs="0" type="xsd:string"/>
       <xsd:element name="clientAuthMode" type="tns:ClientAuthMode"/>
       <xsd:element name="connectorUrl" type="xsd:string"/>
       <xsd:element name="customLoginUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="integrationClassName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="serverAuthMode" type="tns:ServerAuthMode"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ClientAuthMode">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="SSO"/>
     <xsd:enumeration value="Custom"/>
     <xsd:enumeration value="Mixed"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ServerAuthMode">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="OAuth"/>
     <xsd:enumeration value="None"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ConversationalIntelligenceSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCallCoaching" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCallCoachingZoom" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CorsWhitelistOrigin">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="urlPattern" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CspTrustedSite">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="context" minOccurs="0" type="tns:CspTrustedSiteContext"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="endpointUrl" type="xsd:string"/>
       <xsd:element name="isActive" type="xsd:boolean"/>
       <xsd:element name="isApplicableToConnectSrc" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isApplicableToFontSrc" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isApplicableToFrameSrc" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isApplicableToImgSrc" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isApplicableToMediaSrc" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isApplicableToStyleSrc" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="mobileExtension" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="CspTrustedSiteContext">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="All"/>
     <xsd:enumeration value="LEX"/>
     <xsd:enumeration value="Communities"/>
     <xsd:enumeration value="FieldServiceMobileExtension"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="CurrencySettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCurrencyEffectiveDates" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCurrencySymbolWithMultiCurrency" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMultiCurrency" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isMultiCurrencyActivationAllowed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isParenCurrencyConvDisabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomApplication">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionOverrides" minOccurs="0" maxOccurs="unbounded" type="tns:AppActionOverride"/>
       <xsd:element name="brand" minOccurs="0" type="tns:AppBrand"/>
       <xsd:element name="consoleConfig" minOccurs="0" type="tns:ServiceCloudConsoleConfig"/>
       <xsd:element name="defaultLandingTab" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="formFactors" minOccurs="0" maxOccurs="unbounded" type="tns:FormFactor"/>
       <xsd:element name="isNavAutoTempTabsDisabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isNavPersonalizationDisabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isServiceCloudConsole" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" minOccurs="0" type="xsd:string"/>
       <xsd:element name="logo" minOccurs="0" type="xsd:string"/>
       <xsd:element name="navType" minOccurs="0" type="tns:NavType"/>
       <xsd:element name="preferences" minOccurs="0" type="tns:AppPreferences"/>
       <xsd:element name="profileActionOverrides" minOccurs="0" maxOccurs="unbounded" type="tns:AppProfileActionOverride"/>
       <xsd:element name="setupExperience" minOccurs="0" type="xsd:string"/>
       <xsd:element name="subscriberTabs" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="tabs" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="uiType" minOccurs="0" type="tns:UiType"/>
       <xsd:element name="utilityBar" minOccurs="0" type="xsd:string"/>
       <xsd:element name="workspaceConfig" minOccurs="0" type="tns:AppWorkspaceConfig"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AppActionOverride">
    <xsd:complexContent>
     <xsd:extension base="tns:ActionOverride">
      <xsd:sequence>
       <xsd:element name="pageOrSobjectType" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ActionOverride">
    <xsd:sequence>
     <xsd:element name="actionName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="comment" minOccurs="0" type="xsd:string"/>
     <xsd:element name="content" minOccurs="0" type="xsd:string"/>
     <xsd:element name="formFactor" minOccurs="0" type="tns:FormFactor"/>
     <xsd:element name="skipRecordTypeSelect" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="type" minOccurs="0" type="tns:ActionOverrideType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FormFactor">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Small"/>
     <xsd:enumeration value="Medium"/>
     <xsd:enumeration value="Large"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ActionOverrideType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Default"/>
     <xsd:enumeration value="Standard"/>
     <xsd:enumeration value="Scontrol"/>
     <xsd:enumeration value="Visualforce"/>
     <xsd:enumeration value="Flexipage"/>
     <xsd:enumeration value="LightningComponent"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="AppBrand">
    <xsd:sequence>
     <xsd:element name="footerColor" minOccurs="0" type="xsd:string"/>
     <xsd:element name="headerColor" minOccurs="0" type="xsd:string"/>
     <xsd:element name="logo" minOccurs="0" type="xsd:string"/>
     <xsd:element name="logoVersion" minOccurs="0" type="xsd:int"/>
     <xsd:element name="shouldOverrideOrgTheme" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ServiceCloudConsoleConfig">
    <xsd:sequence>
     <xsd:element name="componentList" minOccurs="0" type="tns:AppComponentList"/>
     <xsd:element name="detailPageRefreshMethod" type="xsd:string"/>
     <xsd:element name="footerColor" minOccurs="0" type="xsd:string"/>
     <xsd:element name="headerColor" minOccurs="0" type="xsd:string"/>
     <xsd:element name="keyboardShortcuts" type="tns:KeyboardShortcuts"/>
     <xsd:element name="listPlacement" type="tns:ListPlacement"/>
     <xsd:element name="listRefreshMethod" type="xsd:string"/>
     <xsd:element name="liveAgentConfig" minOccurs="0" type="tns:LiveAgentConfig"/>
     <xsd:element name="primaryTabColor" minOccurs="0" type="xsd:string"/>
     <xsd:element name="pushNotifications" minOccurs="0" maxOccurs="unbounded" type="tns:PushNotification"/>
     <xsd:element name="tabLimitConfig" minOccurs="0" type="tns:TabLimitConfig"/>
     <xsd:element name="whitelistedDomains" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AppComponentList">
    <xsd:sequence>
     <xsd:element name="alignment" type="xsd:string"/>
     <xsd:element name="components" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="KeyboardShortcuts">
    <xsd:sequence>
     <xsd:element name="customShortcuts" minOccurs="0" maxOccurs="unbounded" type="tns:CustomShortcut"/>
     <xsd:element name="defaultShortcuts" minOccurs="0" maxOccurs="unbounded" type="tns:DefaultShortcut"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CustomShortcut">
    <xsd:complexContent>
     <xsd:extension base="tns:DefaultShortcut">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="eventName" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DefaultShortcut">
    <xsd:sequence>
     <xsd:element name="action" type="xsd:string"/>
     <xsd:element name="active" type="xsd:boolean"/>
     <xsd:element name="keyCommand" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ListPlacement">
    <xsd:sequence>
     <xsd:element name="height" minOccurs="0" type="xsd:int"/>
     <xsd:element name="location" type="xsd:string"/>
     <xsd:element name="units" minOccurs="0" type="xsd:string"/>
     <xsd:element name="width" minOccurs="0" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LiveAgentConfig">
    <xsd:sequence>
     <xsd:element name="enableLiveChat" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="openNewAccountSubtab" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="openNewCaseSubtab" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="openNewContactSubtab" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="openNewLeadSubtab" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="openNewVFPageSubtab" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="pageNamesToOpen" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="showKnowledgeArticles" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PushNotification">
    <xsd:sequence>
     <xsd:element name="fieldNames" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="objectName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="TabLimitConfig">
    <xsd:sequence>
     <xsd:element name="maxNumberOfPrimaryTabs" minOccurs="0" type="xsd:string"/>
     <xsd:element name="maxNumberOfSubTabs" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="NavType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Standard"/>
     <xsd:enumeration value="Console"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="AppPreferences">
    <xsd:sequence>
     <xsd:element name="enableCustomizeMyTabs" type="xsd:boolean"/>
     <xsd:element name="enableKeyboardShortcuts" type="xsd:boolean"/>
     <xsd:element name="enableListViewHover" type="xsd:boolean"/>
     <xsd:element name="enableListViewReskin" type="xsd:boolean"/>
     <xsd:element name="enableMultiMonitorComponents" type="xsd:boolean"/>
     <xsd:element name="enablePinTabs" type="xsd:boolean"/>
     <xsd:element name="enableTabHover" type="xsd:boolean"/>
     <xsd:element name="enableTabLimits" type="xsd:boolean"/>
     <xsd:element name="saveUserSessions" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AppProfileActionOverride">
    <xsd:complexContent>
     <xsd:extension base="tns:ProfileActionOverride">
      <xsd:sequence>
       <xsd:element name="profile" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ProfileActionOverride">
    <xsd:sequence>
     <xsd:element name="actionName" type="xsd:string"/>
     <xsd:element name="content" minOccurs="0" type="xsd:string"/>
     <xsd:element name="formFactor" type="tns:FormFactor"/>
     <xsd:element name="pageOrSobjectType" type="xsd:string"/>
     <xsd:element name="recordType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="type" type="tns:ActionOverrideType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="UiType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Aloha"/>
     <xsd:enumeration value="Lightning"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="AppWorkspaceConfig">
    <xsd:sequence>
     <xsd:element name="mappings" minOccurs="0" maxOccurs="unbounded" type="tns:WorkspaceMapping"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WorkspaceMapping">
    <xsd:sequence>
     <xsd:element name="fieldName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="tab" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CustomApplicationComponent">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="buttonIconUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="buttonStyle" minOccurs="0" type="xsd:string"/>
       <xsd:element name="buttonText" minOccurs="0" type="xsd:string"/>
       <xsd:element name="buttonWidth" minOccurs="0" type="xsd:int"/>
       <xsd:element name="height" minOccurs="0" type="xsd:int"/>
       <xsd:element name="isHeightFixed" type="xsd:boolean"/>
       <xsd:element name="isHidden" type="xsd:boolean"/>
       <xsd:element name="isWidthFixed" type="xsd:boolean"/>
       <xsd:element name="visualforcePage" type="xsd:string"/>
       <xsd:element name="width" minOccurs="0" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomFeedFilter">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="criteria" minOccurs="0" maxOccurs="unbounded" type="tns:FeedFilterCriterion"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FeedFilterCriterion">
    <xsd:sequence>
     <xsd:element name="feedItemType" type="tns:FeedItemType"/>
     <xsd:element name="feedItemVisibility" minOccurs="0" type="tns:FeedItemVisibility"/>
     <xsd:element name="relatedSObjectType" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FeedItemVisibility">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AllUsers"/>
     <xsd:enumeration value="InternalUsers"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="CustomField">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="businessOwnerGroup" minOccurs="0" type="xsd:string"/>
       <xsd:element name="businessOwnerUser" minOccurs="0" type="xsd:string"/>
       <xsd:element name="businessStatus" minOccurs="0" type="xsd:string"/>
       <xsd:element name="caseSensitive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="complianceGroup" minOccurs="0" type="xsd:string"/>
       <xsd:element name="customDataType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="defaultValue" minOccurs="0" type="xsd:string"/>
       <xsd:element name="deleteConstraint" minOccurs="0" type="tns:DeleteConstraint"/>
       <xsd:element name="deprecated" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="displayFormat" minOccurs="0" type="xsd:string"/>
       <xsd:element name="encryptionScheme" minOccurs="0" type="tns:EncryptionScheme"/>
       <xsd:element name="escapeMarkup" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="externalDeveloperName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="externalId" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="fieldManageability" minOccurs="0" type="tns:FieldManageability"/>
       <xsd:element name="formula" minOccurs="0" type="xsd:string"/>
       <xsd:element name="formulaTreatBlanksAs" minOccurs="0" type="tns:TreatBlanksAs"/>
       <xsd:element name="inlineHelpText" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isAIPredictionField" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isConvertLeadDisabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isFilteringDisabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isNameField" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isSortingDisabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" minOccurs="0" type="xsd:string"/>
       <xsd:element name="length" minOccurs="0" type="xsd:int"/>
       <xsd:element name="lookupFilter" minOccurs="0" type="tns:LookupFilter"/>
       <xsd:element name="maskChar" minOccurs="0" type="tns:EncryptedFieldMaskChar"/>
       <xsd:element name="maskType" minOccurs="0" type="tns:EncryptedFieldMaskType"/>
       <xsd:element name="metadataRelationshipControllingField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="mktDataLakeFieldAttributes" minOccurs="0" type="tns:MktDataLakeFieldAttributes"/>
       <xsd:element name="mktDataModelFieldAttributes" minOccurs="0" type="tns:MktDataModelFieldAttributes"/>
       <xsd:element name="populateExistingRows" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="precision" minOccurs="0" type="xsd:int"/>
       <xsd:element name="referenceTargetField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="referenceTo" minOccurs="0" type="xsd:string"/>
       <xsd:element name="relationshipLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="relationshipName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="relationshipOrder" minOccurs="0" type="xsd:int"/>
       <xsd:element name="reparentableMasterDetail" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="required" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="restrictedAdminField" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="scale" minOccurs="0" type="xsd:int"/>
       <xsd:element name="securityClassification" minOccurs="0" type="xsd:string"/>
       <xsd:element name="startingNumber" minOccurs="0" type="xsd:int"/>
       <xsd:element name="stripMarkup" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="summarizedField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="summaryFilterItems" minOccurs="0" maxOccurs="unbounded" type="tns:FilterItem"/>
       <xsd:element name="summaryForeignKey" minOccurs="0" type="xsd:string"/>
       <xsd:element name="summaryOperation" minOccurs="0" type="tns:SummaryOperations"/>
       <xsd:element name="trackFeedHistory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="trackHistory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="trackTrending" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="translateData" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="type" minOccurs="0" type="tns:FieldType"/>
       <xsd:element name="unique" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="valueSet" minOccurs="0" type="tns:ValueSet"/>
       <xsd:element name="visibleLines" minOccurs="0" type="xsd:int"/>
       <xsd:element name="writeRequiresMasterRead" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="DeleteConstraint">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Cascade"/>
     <xsd:enumeration value="Restrict"/>
     <xsd:enumeration value="SetNull"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="EncryptionScheme">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="ProbabilisticEncryption"/>
     <xsd:enumeration value="CaseSensitiveDeterministicEncryption"/>
     <xsd:enumeration value="CaseInsensitiveDeterministicEncryption"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FieldManageability">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="DeveloperControlled"/>
     <xsd:enumeration value="SubscriberControlled"/>
     <xsd:enumeration value="Locked"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="TreatBlanksAs">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="BlankAsBlank"/>
     <xsd:enumeration value="BlankAsZero"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="LookupFilter">
    <xsd:sequence>
     <xsd:element name="active" type="xsd:boolean"/>
     <xsd:element name="booleanFilter" minOccurs="0" type="xsd:string"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="errorMessage" minOccurs="0" type="xsd:string"/>
     <xsd:element name="filterItems" minOccurs="0" maxOccurs="unbounded" type="tns:FilterItem"/>
     <xsd:element name="infoMessage" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isOptional" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="EncryptedFieldMaskChar">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="asterisk"/>
     <xsd:enumeration value="X"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="EncryptedFieldMaskType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="all"/>
     <xsd:enumeration value="creditCard"/>
     <xsd:enumeration value="ssn"/>
     <xsd:enumeration value="lastFour"/>
     <xsd:enumeration value="sin"/>
     <xsd:enumeration value="nino"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="MktDataLakeFieldAttributes">
    <xsd:sequence>
     <xsd:element name="dateFormat" minOccurs="0" type="xsd:string"/>
     <xsd:element name="definitionCreationType" minOccurs="0" type="tns:DefinitionCreationType"/>
     <xsd:element name="externalName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isEventDate" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="isInternalOrganization" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="isRecordModified" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="primaryIndexOrder" minOccurs="0" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DefinitionCreationType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Standard"/>
     <xsd:enumeration value="Custom"/>
     <xsd:enumeration value="System"/>
     <xsd:enumeration value="Derived"/>
     <xsd:enumeration value="Bridge"/>
     <xsd:enumeration value="Curated"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="MktDataModelFieldAttributes">
    <xsd:sequence>
     <xsd:element name="definitionCreationType" minOccurs="0" type="tns:DefinitionCreationType"/>
     <xsd:element name="invalidMergeActionType" minOccurs="0" type="tns:InvalidMergeActionType"/>
     <xsd:element name="isDynamicLookup" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="primaryIndexOrder" minOccurs="0" type="xsd:int"/>
     <xsd:element name="refAttrDeveloperName" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="InvalidMergeActionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Drop"/>
     <xsd:enumeration value="Keep"/>
     <xsd:enumeration value="Override"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SummaryOperations">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="count"/>
     <xsd:enumeration value="sum"/>
     <xsd:enumeration value="min"/>
     <xsd:enumeration value="max"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FieldType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AutoNumber"/>
     <xsd:enumeration value="Lookup"/>
     <xsd:enumeration value="MasterDetail"/>
     <xsd:enumeration value="Checkbox"/>
     <xsd:enumeration value="Currency"/>
     <xsd:enumeration value="Date"/>
     <xsd:enumeration value="DateTime"/>
     <xsd:enumeration value="Email"/>
     <xsd:enumeration value="Number"/>
     <xsd:enumeration value="Percent"/>
     <xsd:enumeration value="Phone"/>
     <xsd:enumeration value="Picklist"/>
     <xsd:enumeration value="MultiselectPicklist"/>
     <xsd:enumeration value="Text"/>
     <xsd:enumeration value="TextArea"/>
     <xsd:enumeration value="LongTextArea"/>
     <xsd:enumeration value="Html"/>
     <xsd:enumeration value="Url"/>
     <xsd:enumeration value="EncryptedText"/>
     <xsd:enumeration value="Summary"/>
     <xsd:enumeration value="Hierarchy"/>
     <xsd:enumeration value="File"/>
     <xsd:enumeration value="MetadataRelationship"/>
     <xsd:enumeration value="Location"/>
     <xsd:enumeration value="ExternalLookup"/>
     <xsd:enumeration value="IndirectLookup"/>
     <xsd:enumeration value="CustomDataType"/>
     <xsd:enumeration value="Time"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ValueSet">
    <xsd:sequence>
     <xsd:element name="controllingField" minOccurs="0" type="xsd:string"/>
     <xsd:element name="restricted" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="valueSetDefinition" minOccurs="0" type="tns:ValueSetValuesDefinition"/>
     <xsd:element name="valueSetName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="valueSettings" minOccurs="0" maxOccurs="unbounded" type="tns:ValueSettings"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ValueSetValuesDefinition">
    <xsd:sequence>
     <xsd:element name="sorted" type="xsd:boolean"/>
     <xsd:element name="value" minOccurs="0" maxOccurs="unbounded" type="tns:CustomValue"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CustomValue">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="color" minOccurs="0" type="xsd:string"/>
       <xsd:element name="default" type="xsd:boolean"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="StandardValue">
    <xsd:complexContent>
     <xsd:extension base="tns:CustomValue">
      <xsd:sequence>
       <xsd:element name="allowEmail" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="closed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="converted" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="cssExposed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="forecastCategory" minOccurs="0" type="tns:ForecastCategories"/>
       <xsd:element name="groupingString" minOccurs="0" type="xsd:string"/>
       <xsd:element name="highPriority" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="probability" minOccurs="0" type="xsd:int"/>
       <xsd:element name="reverseRole" minOccurs="0" type="xsd:string"/>
       <xsd:element name="reviewed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="won" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ValueSettings">
    <xsd:sequence>
     <xsd:element name="controllingFieldValue" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="valueName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CustomHelpMenuSection">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="customHelpMenuItems" minOccurs="0" maxOccurs="unbounded" type="tns:CustomHelpMenuItem"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomHelpMenuItem">
    <xsd:sequence>
     <xsd:element name="linkUrl" type="xsd:string"/>
     <xsd:element name="masterLabel" type="xsd:string"/>
     <xsd:element name="sortOrder" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CustomIndex">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence/>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomLabel">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="categories" minOccurs="0" type="xsd:string"/>
       <xsd:element name="language" type="xsd:string"/>
       <xsd:element name="protected" type="xsd:boolean"/>
       <xsd:element name="shortDescription" type="xsd:string"/>
       <xsd:element name="value" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomLabels">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="labels" minOccurs="0" maxOccurs="unbounded" type="tns:CustomLabel"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomMetadata">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" minOccurs="0" type="xsd:string"/>
       <xsd:element name="protected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="values" minOccurs="0" maxOccurs="unbounded" type="tns:CustomMetadataValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomMetadataValue">
    <xsd:sequence>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="value" type="xsd:anyType" nillable="true"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CustomNotificationType">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="customNotifTypeName" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="desktop" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="mobile" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomObject">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionOverrides" minOccurs="0" maxOccurs="unbounded" type="tns:ActionOverride"/>
       <xsd:element name="allowInChatterGroups" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="articleTypeChannelDisplay" minOccurs="0" type="tns:ArticleTypeChannelDisplay"/>
       <xsd:element name="businessProcesses" minOccurs="0" maxOccurs="unbounded" type="tns:BusinessProcess"/>
       <xsd:element name="compactLayoutAssignment" minOccurs="0" type="xsd:string"/>
       <xsd:element name="compactLayouts" minOccurs="0" maxOccurs="unbounded" type="tns:CompactLayout"/>
       <xsd:element name="customHelp" minOccurs="0" type="xsd:string"/>
       <xsd:element name="customHelpPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="customSettingsType" minOccurs="0" type="tns:CustomSettingsType"/>
       <xsd:element name="deploymentStatus" minOccurs="0" type="tns:DeploymentStatus"/>
       <xsd:element name="deprecated" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="enableActivities" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableBulkApi" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDataTranslation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDivisions" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEnhancedLookup" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFeeds" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHistory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLicensing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePublishStatusTracking" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableReports" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSearch" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSharing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableStreamingApi" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="eventType" minOccurs="0" type="tns:PlatformEventType"/>
       <xsd:element name="externalDataSource" minOccurs="0" type="xsd:string"/>
       <xsd:element name="externalName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="externalRepository" minOccurs="0" type="xsd:string"/>
       <xsd:element name="externalSharingModel" minOccurs="0" type="tns:SharingModel"/>
       <xsd:element name="fieldSets" minOccurs="0" maxOccurs="unbounded" type="tns:FieldSet"/>
       <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="tns:CustomField"/>
       <xsd:element name="gender" minOccurs="0" type="tns:Gender"/>
       <xsd:element name="historyRetentionPolicy" minOccurs="0" type="tns:HistoryRetentionPolicy"/>
       <xsd:element name="household" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="indexes" minOccurs="0" maxOccurs="unbounded" type="tns:Index"/>
       <xsd:element name="label" minOccurs="0" type="xsd:string"/>
       <xsd:element name="listViews" minOccurs="0" maxOccurs="unbounded" type="tns:ListView"/>
       <xsd:element name="mktDataLakeAttributes" minOccurs="0" type="tns:MktDataLakeAttributes"/>
       <xsd:element name="mktDataModelAttributes" minOccurs="0" type="tns:MktDataModelAttributes"/>
       <xsd:element name="nameField" minOccurs="0" type="tns:CustomField"/>
       <xsd:element name="pluralLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="profileSearchLayouts" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileSearchLayouts"/>
       <xsd:element name="publishBehavior" minOccurs="0" type="tns:PlatformEventPublishBehavior"/>
       <xsd:element name="recordTypeTrackFeedHistory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="recordTypeTrackHistory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="recordTypes" minOccurs="0" maxOccurs="unbounded" type="tns:RecordType"/>
       <xsd:element name="searchLayouts" minOccurs="0" type="tns:SearchLayouts"/>
       <xsd:element name="sharingModel" minOccurs="0" type="tns:SharingModel"/>
       <xsd:element name="sharingReasons" minOccurs="0" maxOccurs="unbounded" type="tns:SharingReason"/>
       <xsd:element name="sharingRecalculations" minOccurs="0" maxOccurs="unbounded" type="tns:SharingRecalculation"/>
       <xsd:element name="startsWith" minOccurs="0" type="tns:StartsWith"/>
       <xsd:element name="validationRules" minOccurs="0" maxOccurs="unbounded" type="tns:ValidationRule"/>
       <xsd:element name="visibility" minOccurs="0" type="tns:SetupObjectVisibility"/>
       <xsd:element name="webLinks" minOccurs="0" maxOccurs="unbounded" type="tns:WebLink"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ArticleTypeChannelDisplay">
    <xsd:sequence>
     <xsd:element name="articleTypeTemplates" minOccurs="0" maxOccurs="unbounded" type="tns:ArticleTypeTemplate"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ArticleTypeTemplate">
    <xsd:sequence>
     <xsd:element name="channel" type="tns:Channel"/>
     <xsd:element name="page" minOccurs="0" type="xsd:string"/>
     <xsd:element name="template" type="tns:Template"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="Channel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AllChannels"/>
     <xsd:enumeration value="App"/>
     <xsd:enumeration value="Pkb"/>
     <xsd:enumeration value="Csp"/>
     <xsd:enumeration value="Prm"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="Template">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Page"/>
     <xsd:enumeration value="Tab"/>
     <xsd:enumeration value="Toc"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="CustomSettingsType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="List"/>
     <xsd:enumeration value="Hierarchy"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="DeploymentStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="InDevelopment"/>
     <xsd:enumeration value="Deployed"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="PlatformEventType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="HighVolume"/>
     <xsd:enumeration value="StandardVolume"/>
     <xsd:enumeration value="ExternalEvent"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SharingModel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Private"/>
     <xsd:enumeration value="Read"/>
     <xsd:enumeration value="ReadSelect"/>
     <xsd:enumeration value="ReadWrite"/>
     <xsd:enumeration value="ReadWriteTransfer"/>
     <xsd:enumeration value="FullAccess"/>
     <xsd:enumeration value="ControlledByParent"/>
     <xsd:enumeration value="ControlledByLeadOrContact"/>
     <xsd:enumeration value="ControlledByCampaign"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FieldSet">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="availableFields" minOccurs="0" maxOccurs="unbounded" type="tns:FieldSetItem"/>
       <xsd:element name="description" type="xsd:string"/>
       <xsd:element name="displayedFields" minOccurs="0" maxOccurs="unbounded" type="tns:FieldSetItem"/>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FieldSetItem">
    <xsd:sequence>
     <xsd:element name="field" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isFieldManaged" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="isRequired" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="Gender">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Neuter"/>
     <xsd:enumeration value="Masculine"/>
     <xsd:enumeration value="Feminine"/>
     <xsd:enumeration value="AnimateMasculine"/>
     <xsd:enumeration value="ClassI"/>
     <xsd:enumeration value="ClassIII"/>
     <xsd:enumeration value="ClassV"/>
     <xsd:enumeration value="ClassVII"/>
     <xsd:enumeration value="ClassIX"/>
     <xsd:enumeration value="ClassXI"/>
     <xsd:enumeration value="ClassXIV"/>
     <xsd:enumeration value="ClassXV"/>
     <xsd:enumeration value="ClassXVI"/>
     <xsd:enumeration value="ClassXVII"/>
     <xsd:enumeration value="ClassXVIII"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="HistoryRetentionPolicy">
    <xsd:sequence>
     <xsd:element name="archiveAfterMonths" type="xsd:int"/>
     <xsd:element name="archiveRetentionYears" type="xsd:int"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Index">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="tns:IndexField"/>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="IndexField">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="sortDirection" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ListView">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="booleanFilter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="columns" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="division" minOccurs="0" type="xsd:string"/>
       <xsd:element name="filterScope" type="tns:FilterScope"/>
       <xsd:element name="filters" minOccurs="0" maxOccurs="unbounded" type="tns:ListViewFilter"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="language" minOccurs="0" type="tns:Language"/>
       <xsd:element name="queue" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sharedTo" minOccurs="0" type="tns:SharedTo"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ListViewFilter">
    <xsd:sequence>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="operation" type="tns:FilterOperation"/>
     <xsd:element name="value" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SharedTo">
    <xsd:sequence>
     <xsd:element name="allCustomerPortalUsers" minOccurs="0" type="xsd:string"/>
     <xsd:element name="allInternalUsers" minOccurs="0" type="xsd:string"/>
     <xsd:element name="allPartnerUsers" minOccurs="0" type="xsd:string"/>
     <xsd:element name="channelProgramGroup" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="channelProgramGroups" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="group" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="groups" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="guestUser" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="managerSubordinates" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="managers" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="portalRole" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="portalRoleAndSubordinates" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="queue" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="role" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="roleAndSubordinates" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="roleAndSubordinatesInternal" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="roles" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="rolesAndSubordinates" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="territories" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="territoriesAndSubordinates" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="territory" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="territoryAndSubordinates" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="MktDataLakeAttributes">
    <xsd:sequence>
     <xsd:element name="creationType" minOccurs="0" type="tns:DefinitionCreationType"/>
     <xsd:element name="dataSource" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isEnabled" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="objectCategory" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="MktDataModelAttributes">
    <xsd:sequence>
     <xsd:element name="creationType" minOccurs="0" type="tns:DefinitionCreationType"/>
     <xsd:element name="dataModelTaxonomy" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isEnabled" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="isSegmentable" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="objectCategory" minOccurs="0" type="xsd:string"/>
     <xsd:element name="referenceEntityGroup" minOccurs="0" type="xsd:string"/>
     <xsd:element name="referenceEntityName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="referenceEntitySubjectArea" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileSearchLayouts">
    <xsd:sequence>
     <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="profileName" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="PlatformEventPublishBehavior">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="PublishAfterCommit"/>
     <xsd:enumeration value="PublishImmediately"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="RecordType">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="businessProcess" minOccurs="0" type="xsd:string"/>
       <xsd:element name="compactLayoutAssignment" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="picklistValues" minOccurs="0" maxOccurs="unbounded" type="tns:RecordTypePicklistValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="RecordTypePicklistValue">
    <xsd:sequence>
     <xsd:element name="picklist" type="xsd:string"/>
     <xsd:element name="values" minOccurs="0" maxOccurs="unbounded" type="tns:PicklistValue"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SearchLayouts">
    <xsd:sequence>
     <xsd:element name="customTabListAdditionalFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="excludedStandardButtons" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="listViewButtons" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="lookupDialogsAdditionalFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="lookupFilterFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="lookupPhoneDialogsAdditionalFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="massQuickActions" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="searchFilterFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="searchResultsAdditionalFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="searchResultsCustomButtons" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SharingReason">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SharingRecalculation">
    <xsd:sequence>
     <xsd:element name="className" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="StartsWith">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Consonant"/>
     <xsd:enumeration value="Vowel"/>
     <xsd:enumeration value="Special"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ValidationRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="errorConditionFormula" type="xsd:string"/>
       <xsd:element name="errorDisplayField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="errorMessage" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="SetupObjectVisibility">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="PackageProtected"/>
     <xsd:enumeration value="Protected"/>
     <xsd:enumeration value="Public"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="WebLink">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="availability" type="tns:WebLinkAvailability"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="displayType" type="tns:WebLinkDisplayType"/>
       <xsd:element name="encodingKey" minOccurs="0" type="tns:Encoding"/>
       <xsd:element name="hasMenubar" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="hasScrollbars" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="hasToolbar" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="height" minOccurs="0" type="xsd:int"/>
       <xsd:element name="isResizable" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="linkType" type="tns:WebLinkType"/>
       <xsd:element name="masterLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="openType" type="tns:WebLinkWindowType"/>
       <xsd:element name="page" minOccurs="0" type="xsd:string"/>
       <xsd:element name="position" minOccurs="0" type="tns:WebLinkPosition"/>
       <xsd:element name="protected" type="xsd:boolean"/>
       <xsd:element name="requireRowSelection" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="scontrol" minOccurs="0" type="xsd:string"/>
       <xsd:element name="showsLocation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showsStatus" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="url" minOccurs="0" type="xsd:string"/>
       <xsd:element name="width" minOccurs="0" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="WebLinkAvailability">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="online"/>
     <xsd:enumeration value="offline"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="WebLinkDisplayType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="link"/>
     <xsd:enumeration value="button"/>
     <xsd:enumeration value="massActionButton"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="Encoding">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="UTF-8"/>
     <xsd:enumeration value="ISO-8859-1"/>
     <xsd:enumeration value="Shift_JIS"/>
     <xsd:enumeration value="ISO-2022-JP"/>
     <xsd:enumeration value="EUC-JP"/>
     <xsd:enumeration value="ks_c_5601-1987"/>
     <xsd:enumeration value="Big5"/>
     <xsd:enumeration value="GB2312"/>
     <xsd:enumeration value="Big5-HKSCS"/>
     <xsd:enumeration value="x-SJIS_0213"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="WebLinkType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="url"/>
     <xsd:enumeration value="sControl"/>
     <xsd:enumeration value="javascript"/>
     <xsd:enumeration value="page"/>
     <xsd:enumeration value="flow"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="WebLinkWindowType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="newWindow"/>
     <xsd:enumeration value="sidebar"/>
     <xsd:enumeration value="noSidebar"/>
     <xsd:enumeration value="replace"/>
     <xsd:enumeration value="onClickJavaScript"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="WebLinkPosition">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="fullScreen"/>
     <xsd:enumeration value="none"/>
     <xsd:enumeration value="topLeft"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="CustomObjectTranslation">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="caseValues" minOccurs="0" maxOccurs="unbounded" type="tns:ObjectNameCaseValue"/>
       <xsd:element name="fieldSets" minOccurs="0" maxOccurs="unbounded" type="tns:FieldSetTranslation"/>
       <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="tns:CustomFieldTranslation"/>
       <xsd:element name="gender" minOccurs="0" type="tns:Gender"/>
       <xsd:element name="layouts" minOccurs="0" maxOccurs="unbounded" type="tns:LayoutTranslation"/>
       <xsd:element name="nameFieldLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="quickActions" minOccurs="0" maxOccurs="unbounded" type="tns:QuickActionTranslation"/>
       <xsd:element name="recordTypes" minOccurs="0" maxOccurs="unbounded" type="tns:RecordTypeTranslation"/>
       <xsd:element name="sharingReasons" minOccurs="0" maxOccurs="unbounded" type="tns:SharingReasonTranslation"/>
       <xsd:element name="standardFields" minOccurs="0" maxOccurs="unbounded" type="tns:StandardFieldTranslation"/>
       <xsd:element name="startsWith" minOccurs="0" type="tns:StartsWith"/>
       <xsd:element name="validationRules" minOccurs="0" maxOccurs="unbounded" type="tns:ValidationRuleTranslation"/>
       <xsd:element name="webLinks" minOccurs="0" maxOccurs="unbounded" type="tns:WebLinkTranslation"/>
       <xsd:element name="workflowTasks" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowTaskTranslation"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ObjectNameCaseValue">
    <xsd:sequence>
     <xsd:element name="article" minOccurs="0" type="tns:Article"/>
     <xsd:element name="caseType" minOccurs="0" type="tns:CaseType"/>
     <xsd:element name="plural" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="possessive" minOccurs="0" type="tns:Possessive"/>
     <xsd:element name="value" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="Article">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="Indefinite"/>
     <xsd:enumeration value="Definite"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="CaseType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Nominative"/>
     <xsd:enumeration value="Accusative"/>
     <xsd:enumeration value="Genitive"/>
     <xsd:enumeration value="Dative"/>
     <xsd:enumeration value="Inessive"/>
     <xsd:enumeration value="Elative"/>
     <xsd:enumeration value="Illative"/>
     <xsd:enumeration value="Adessive"/>
     <xsd:enumeration value="Ablative"/>
     <xsd:enumeration value="Allative"/>
     <xsd:enumeration value="Essive"/>
     <xsd:enumeration value="Translative"/>
     <xsd:enumeration value="Partitive"/>
     <xsd:enumeration value="Objective"/>
     <xsd:enumeration value="Subjective"/>
     <xsd:enumeration value="Instrumental"/>
     <xsd:enumeration value="Prepositional"/>
     <xsd:enumeration value="Locative"/>
     <xsd:enumeration value="Vocative"/>
     <xsd:enumeration value="Sublative"/>
     <xsd:enumeration value="Superessive"/>
     <xsd:enumeration value="Delative"/>
     <xsd:enumeration value="Causalfinal"/>
     <xsd:enumeration value="Essiveformal"/>
     <xsd:enumeration value="Termanative"/>
     <xsd:enumeration value="Distributive"/>
     <xsd:enumeration value="Ergative"/>
     <xsd:enumeration value="Adverbial"/>
     <xsd:enumeration value="Abessive"/>
     <xsd:enumeration value="Comitative"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="Possessive">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="First"/>
     <xsd:enumeration value="Second"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FieldSetTranslation">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CustomFieldTranslation">
    <xsd:sequence>
     <xsd:element name="caseValues" minOccurs="0" maxOccurs="unbounded" type="tns:ObjectNameCaseValue"/>
     <xsd:element name="gender" minOccurs="0" type="tns:Gender"/>
     <xsd:element name="help" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="lookupFilter" minOccurs="0" type="tns:LookupFilterTranslation"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="picklistValues" minOccurs="0" maxOccurs="unbounded" type="tns:PicklistValueTranslation"/>
     <xsd:element name="relationshipLabel" minOccurs="0" type="xsd:string"/>
     <xsd:element name="startsWith" minOccurs="0" type="tns:StartsWith"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LookupFilterTranslation">
    <xsd:sequence>
     <xsd:element name="errorMessage" type="xsd:string"/>
     <xsd:element name="informationalMessage" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PicklistValueTranslation">
    <xsd:sequence>
     <xsd:element name="masterLabel" type="xsd:string"/>
     <xsd:element name="translation" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LayoutTranslation">
    <xsd:sequence>
     <xsd:element name="layout" type="xsd:string"/>
     <xsd:element name="layoutType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sections" minOccurs="0" maxOccurs="unbounded" type="tns:LayoutSectionTranslation"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LayoutSectionTranslation">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="section" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="QuickActionTranslation">
    <xsd:sequence>
     <xsd:element name="aspect" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RecordTypeTranslation">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SharingReasonTranslation">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="StandardFieldTranslation">
    <xsd:sequence>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ValidationRuleTranslation">
    <xsd:sequence>
     <xsd:element name="errorMessage" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WebLinkTranslation">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WorkflowTaskTranslation">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="subject" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CustomPageWebLink">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="availability" type="tns:WebLinkAvailability"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="displayType" type="tns:WebLinkDisplayType"/>
       <xsd:element name="encodingKey" minOccurs="0" type="tns:Encoding"/>
       <xsd:element name="hasMenubar" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="hasScrollbars" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="hasToolbar" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="height" minOccurs="0" type="xsd:int"/>
       <xsd:element name="isResizable" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="linkType" type="tns:WebLinkType"/>
       <xsd:element name="masterLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="openType" type="tns:WebLinkWindowType"/>
       <xsd:element name="page" minOccurs="0" type="xsd:string"/>
       <xsd:element name="position" minOccurs="0" type="tns:WebLinkPosition"/>
       <xsd:element name="protected" type="xsd:boolean"/>
       <xsd:element name="requireRowSelection" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="scontrol" minOccurs="0" type="xsd:string"/>
       <xsd:element name="showsLocation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showsStatus" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="url" minOccurs="0" type="xsd:string"/>
       <xsd:element name="width" minOccurs="0" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomPermission">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="connectedApp" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isLicensed" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="requiredPermission" minOccurs="0" maxOccurs="unbounded" type="tns:CustomPermissionDependencyRequired"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomPermissionDependencyRequired">
    <xsd:sequence>
     <xsd:element name="customPermission" type="xsd:string"/>
     <xsd:element name="dependency" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CustomSite">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="allowHomePage" type="xsd:boolean"/>
       <xsd:element name="allowStandardAnswersPages" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="allowStandardIdeasPages" type="xsd:boolean"/>
       <xsd:element name="allowStandardLookups" type="xsd:boolean"/>
       <xsd:element name="allowStandardPortalPages" type="xsd:boolean"/>
       <xsd:element name="allowStandardSearch" type="xsd:boolean"/>
       <xsd:element name="analyticsTrackingCode" minOccurs="0" type="xsd:string"/>
       <xsd:element name="authorizationRequiredPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="bandwidthExceededPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="browserXssProtection" type="xsd:boolean"/>
       <xsd:element name="cachePublicVisualforcePagesInProxyServers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="changePasswordPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="chatterAnswersForgotPasswordConfirmPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="chatterAnswersForgotPasswordPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="chatterAnswersHelpPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="chatterAnswersLoginPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="chatterAnswersRegistrationPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="clickjackProtectionLevel" type="tns:SiteClickjackProtectionLevel"/>
       <xsd:element name="contentSniffingProtection" type="xsd:boolean"/>
       <xsd:element name="customWebAddresses" minOccurs="0" maxOccurs="unbounded" type="tns:SiteWebAddress"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="enableAuraRequests" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="favoriteIcon" minOccurs="0" type="xsd:string"/>
       <xsd:element name="fileNotFoundPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="forgotPasswordPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="genericErrorPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="guestProfile" minOccurs="0" type="xsd:string"/>
       <xsd:element name="inMaintenancePage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="inactiveIndexPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="indexPage" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="myProfilePage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="portal" minOccurs="0" type="xsd:string"/>
       <xsd:element name="redirectToCustomDomain" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="referrerPolicyOriginWhenCrossOrigin" type="xsd:boolean"/>
       <xsd:element name="robotsTxtPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="selfRegPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="serverIsDown" minOccurs="0" type="xsd:string"/>
       <xsd:element name="siteAdmin" minOccurs="0" type="xsd:string"/>
       <xsd:element name="siteGuestRecordDefaultOwner" minOccurs="0" type="xsd:string"/>
       <xsd:element name="siteIframeWhiteListUrls" minOccurs="0" maxOccurs="unbounded" type="tns:SiteIframeWhiteListUrl"/>
       <xsd:element name="siteRedirectMappings" minOccurs="0" maxOccurs="unbounded" type="tns:SiteRedirectMapping"/>
       <xsd:element name="siteTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="siteType" type="tns:SiteType"/>
       <xsd:element name="subdomain" minOccurs="0" type="xsd:string"/>
       <xsd:element name="urlPathPrefix" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="SiteClickjackProtectionLevel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AllowAllFraming"/>
     <xsd:enumeration value="External"/>
     <xsd:enumeration value="SameOriginOnly"/>
     <xsd:enumeration value="NoFraming"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="SiteWebAddress">
    <xsd:sequence>
     <xsd:element name="certificate" minOccurs="0" type="xsd:string"/>
     <xsd:element name="domainName" type="xsd:string"/>
     <xsd:element name="primary" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SiteIframeWhiteListUrl">
    <xsd:sequence>
     <xsd:element name="url" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SiteRedirectMapping">
    <xsd:sequence>
     <xsd:element name="action" type="tns:SiteRedirect"/>
     <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="source" type="xsd:string"/>
     <xsd:element name="target" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="SiteRedirect">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Permanent"/>
     <xsd:enumeration value="Temporary"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SiteType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Siteforce"/>
     <xsd:enumeration value="Visualforce"/>
     <xsd:enumeration value="ChatterNetwork"/>
     <xsd:enumeration value="ChatterNetworkPicasso"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="CustomTab">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionOverrides" minOccurs="0" maxOccurs="unbounded" type="tns:ActionOverride"/>
       <xsd:element name="auraComponent" minOccurs="0" type="xsd:string"/>
       <xsd:element name="customObject" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="flexiPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="frameHeight" minOccurs="0" type="xsd:int"/>
       <xsd:element name="hasSidebar" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="icon" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" minOccurs="0" type="xsd:string"/>
       <xsd:element name="lwcComponent" minOccurs="0" type="xsd:string"/>
       <xsd:element name="motif" minOccurs="0" type="xsd:string"/>
       <xsd:element name="page" minOccurs="0" type="xsd:string"/>
       <xsd:element name="scontrol" minOccurs="0" type="xsd:string"/>
       <xsd:element name="splashPageLink" minOccurs="0" type="xsd:string"/>
       <xsd:element name="url" minOccurs="0" type="xsd:string"/>
       <xsd:element name="urlEncodingKey" minOccurs="0" type="tns:Encoding"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomerDataPlatformSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCustomerDataPlatform" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Dashboard">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="backgroundEndColor" type="xsd:string"/>
       <xsd:element name="backgroundFadeDirection" type="tns:ChartBackgroundDirection"/>
       <xsd:element name="backgroundStartColor" type="xsd:string"/>
       <xsd:element name="chartTheme" minOccurs="0" type="tns:ChartTheme"/>
       <xsd:element name="colorPalette" minOccurs="0" type="tns:ChartColorPalettes"/>
       <xsd:element name="dashboardChartTheme" minOccurs="0" type="tns:ChartTheme"/>
       <xsd:element name="dashboardColorPalette" minOccurs="0" type="tns:ChartColorPalettes"/>
       <xsd:element name="dashboardFilters" minOccurs="0" maxOccurs="unbounded" type="tns:DashboardFilter"/>
       <xsd:element name="dashboardGridLayout" minOccurs="0" type="tns:DashboardGridLayout"/>
       <xsd:element name="dashboardResultRefreshedDate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="dashboardResultRunningUser" minOccurs="0" type="xsd:string"/>
       <xsd:element name="dashboardType" minOccurs="0" type="tns:DashboardType"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="folderName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isGridLayout" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="leftSection" minOccurs="0" type="tns:DashboardComponentSection"/>
       <xsd:element name="middleSection" minOccurs="0" type="tns:DashboardComponentSection"/>
       <xsd:element name="numSubscriptions" minOccurs="0" type="xsd:int"/>
       <xsd:element name="rightSection" minOccurs="0" type="tns:DashboardComponentSection"/>
       <xsd:element name="runningUser" minOccurs="0" type="xsd:string"/>
       <xsd:element name="textColor" type="xsd:string"/>
       <xsd:element name="title" type="xsd:string"/>
       <xsd:element name="titleColor" type="xsd:string"/>
       <xsd:element name="titleSize" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ChartBackgroundDirection">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="TopToBottom"/>
     <xsd:enumeration value="LeftToRight"/>
     <xsd:enumeration value="Diagonal"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ChartTheme">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="light"/>
     <xsd:enumeration value="dark"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ChartColorPalettes">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Default"/>
     <xsd:enumeration value="gray"/>
     <xsd:enumeration value="colorSafe"/>
     <xsd:enumeration value="unity"/>
     <xsd:enumeration value="justice"/>
     <xsd:enumeration value="nightfall"/>
     <xsd:enumeration value="sunrise"/>
     <xsd:enumeration value="bluegrass"/>
     <xsd:enumeration value="tropic"/>
     <xsd:enumeration value="heat"/>
     <xsd:enumeration value="dusk"/>
     <xsd:enumeration value="pond"/>
     <xsd:enumeration value="watermelon"/>
     <xsd:enumeration value="fire"/>
     <xsd:enumeration value="water"/>
     <xsd:enumeration value="earth"/>
     <xsd:enumeration value="accessible"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DashboardFilter">
    <xsd:sequence>
     <xsd:element name="dashboardFilterOptions" minOccurs="0" maxOccurs="unbounded" type="tns:DashboardFilterOption"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DashboardFilterOption">
    <xsd:sequence>
     <xsd:element name="operator" type="tns:DashboardFilterOperation"/>
     <xsd:element name="values" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DashboardFilterOperation">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="equals"/>
     <xsd:enumeration value="notEqual"/>
     <xsd:enumeration value="lessThan"/>
     <xsd:enumeration value="greaterThan"/>
     <xsd:enumeration value="lessOrEqual"/>
     <xsd:enumeration value="greaterOrEqual"/>
     <xsd:enumeration value="contains"/>
     <xsd:enumeration value="notContain"/>
     <xsd:enumeration value="startsWith"/>
     <xsd:enumeration value="includes"/>
     <xsd:enumeration value="excludes"/>
     <xsd:enumeration value="between"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DashboardGridLayout">
    <xsd:sequence>
     <xsd:element name="dashboardGridComponents" minOccurs="0" maxOccurs="unbounded" type="tns:DashboardGridComponent"/>
     <xsd:element name="numberOfColumns" type="xsd:int"/>
     <xsd:element name="rowHeight" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DashboardGridComponent">
    <xsd:sequence>
     <xsd:element name="colSpan" type="xsd:int"/>
     <xsd:element name="columnIndex" type="xsd:int"/>
     <xsd:element name="dashboardComponent" type="tns:DashboardComponent"/>
     <xsd:element name="rowIndex" type="xsd:int"/>
     <xsd:element name="rowSpan" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DashboardComponent">
    <xsd:sequence>
     <xsd:element name="autoselectColumnsFromReport" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="chartAxisRange" minOccurs="0" type="tns:ChartRangeType"/>
     <xsd:element name="chartAxisRangeMax" minOccurs="0" type="xsd:double"/>
     <xsd:element name="chartAxisRangeMin" minOccurs="0" type="xsd:double"/>
     <xsd:element name="chartSummary" minOccurs="0" maxOccurs="unbounded" type="tns:ChartSummary"/>
     <xsd:element name="componentChartTheme" minOccurs="0" type="tns:ChartTheme"/>
     <xsd:element name="componentType" type="tns:DashboardComponentType"/>
     <xsd:element name="dashboardFilterColumns" minOccurs="0" maxOccurs="unbounded" type="tns:DashboardFilterColumn"/>
     <xsd:element name="dashboardTableColumn" minOccurs="0" maxOccurs="unbounded" type="tns:DashboardTableColumn"/>
     <xsd:element name="decimalPrecision" minOccurs="0" type="xsd:int"/>
     <xsd:element name="displayUnits" minOccurs="0" type="tns:ChartUnits"/>
     <xsd:element name="drillDownUrl" minOccurs="0" type="xsd:string"/>
     <xsd:element name="drillEnabled" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="drillToDetailEnabled" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableHover" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="expandOthers" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="flexComponentProperties" minOccurs="0" type="tns:DashboardFlexTableComponentProperties"/>
     <xsd:element name="footer" minOccurs="0" type="xsd:string"/>
     <xsd:element name="gaugeMax" minOccurs="0" type="xsd:double"/>
     <xsd:element name="gaugeMin" minOccurs="0" type="xsd:double"/>
     <xsd:element name="groupingColumn" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="groupingSortProperties" minOccurs="0" type="tns:DashboardComponentGroupingSortProperties"/>
     <xsd:element name="header" minOccurs="0" type="xsd:string"/>
     <xsd:element name="indicatorBreakpoint1" minOccurs="0" type="xsd:double"/>
     <xsd:element name="indicatorBreakpoint2" minOccurs="0" type="xsd:double"/>
     <xsd:element name="indicatorHighColor" minOccurs="0" type="xsd:string"/>
     <xsd:element name="indicatorLowColor" minOccurs="0" type="xsd:string"/>
     <xsd:element name="indicatorMiddleColor" minOccurs="0" type="xsd:string"/>
     <xsd:element name="legendPosition" minOccurs="0" type="tns:ChartLegendPosition"/>
     <xsd:element name="maxValuesDisplayed" minOccurs="0" type="xsd:int"/>
     <xsd:element name="metricLabel" minOccurs="0" type="xsd:string"/>
     <xsd:element name="page" minOccurs="0" type="xsd:string"/>
     <xsd:element name="pageHeightInPixels" minOccurs="0" type="xsd:int"/>
     <xsd:element name="report" minOccurs="0" type="xsd:string"/>
     <xsd:element name="scontrol" minOccurs="0" type="xsd:string"/>
     <xsd:element name="scontrolHeightInPixels" minOccurs="0" type="xsd:int"/>
     <xsd:element name="showPercentage" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showPicturesOnCharts" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showPicturesOnTables" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showRange" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showTotal" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showValues" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="sortBy" minOccurs="0" type="tns:DashboardComponentFilter"/>
     <xsd:element name="title" minOccurs="0" type="xsd:string"/>
     <xsd:element name="useReportChart" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ChartRangeType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Auto"/>
     <xsd:enumeration value="Manual"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ChartSummary">
    <xsd:sequence>
     <xsd:element name="aggregate" minOccurs="0" type="tns:ReportSummaryType"/>
     <xsd:element name="axisBinding" minOccurs="0" type="tns:ChartAxis"/>
     <xsd:element name="column" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ChartAxis">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="x"/>
     <xsd:enumeration value="y"/>
     <xsd:enumeration value="y2"/>
     <xsd:enumeration value="r"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="DashboardComponentType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Bar"/>
     <xsd:enumeration value="BarGrouped"/>
     <xsd:enumeration value="BarStacked"/>
     <xsd:enumeration value="BarStacked100"/>
     <xsd:enumeration value="Column"/>
     <xsd:enumeration value="ColumnGrouped"/>
     <xsd:enumeration value="ColumnStacked"/>
     <xsd:enumeration value="ColumnStacked100"/>
     <xsd:enumeration value="Line"/>
     <xsd:enumeration value="LineGrouped"/>
     <xsd:enumeration value="Pie"/>
     <xsd:enumeration value="Table"/>
     <xsd:enumeration value="Metric"/>
     <xsd:enumeration value="Gauge"/>
     <xsd:enumeration value="LineCumulative"/>
     <xsd:enumeration value="LineGroupedCumulative"/>
     <xsd:enumeration value="Scontrol"/>
     <xsd:enumeration value="VisualforcePage"/>
     <xsd:enumeration value="Donut"/>
     <xsd:enumeration value="Funnel"/>
     <xsd:enumeration value="ColumnLine"/>
     <xsd:enumeration value="ColumnLineGrouped"/>
     <xsd:enumeration value="ColumnLineStacked"/>
     <xsd:enumeration value="ColumnLineStacked100"/>
     <xsd:enumeration value="Scatter"/>
     <xsd:enumeration value="ScatterGrouped"/>
     <xsd:enumeration value="FlexTable"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DashboardFilterColumn">
    <xsd:sequence>
     <xsd:element name="column" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DashboardTableColumn">
    <xsd:sequence>
     <xsd:element name="aggregateType" minOccurs="0" type="tns:ReportSummaryType"/>
     <xsd:element name="calculatePercent" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="column" type="xsd:string"/>
     <xsd:element name="decimalPlaces" minOccurs="0" type="xsd:int"/>
     <xsd:element name="showSubTotal" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showTotal" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="sortBy" minOccurs="0" type="tns:DashboardComponentFilter"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DashboardComponentFilter">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="RowLabelAscending"/>
     <xsd:enumeration value="RowLabelDescending"/>
     <xsd:enumeration value="RowValueAscending"/>
     <xsd:enumeration value="RowValueDescending"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ChartUnits">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Auto"/>
     <xsd:enumeration value="Integer"/>
     <xsd:enumeration value="Hundreds"/>
     <xsd:enumeration value="Thousands"/>
     <xsd:enumeration value="Millions"/>
     <xsd:enumeration value="Billions"/>
     <xsd:enumeration value="Trillions"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DashboardFlexTableComponentProperties">
    <xsd:sequence>
     <xsd:element name="decimalPrecision" minOccurs="0" type="xsd:int"/>
     <xsd:element name="flexTableColumn" minOccurs="0" maxOccurs="unbounded" type="tns:DashboardComponentColumn"/>
     <xsd:element name="flexTableSortInfo" minOccurs="0" type="tns:DashboardComponentSortInfo"/>
     <xsd:element name="hideChatterPhotos" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DashboardComponentColumn">
    <xsd:sequence>
     <xsd:element name="breakPoint1" minOccurs="0" type="xsd:double"/>
     <xsd:element name="breakPoint2" minOccurs="0" type="xsd:double"/>
     <xsd:element name="breakPointOrder" minOccurs="0" type="xsd:int"/>
     <xsd:element name="highRangeColor" minOccurs="0" type="xsd:int"/>
     <xsd:element name="lowRangeColor" minOccurs="0" type="xsd:int"/>
     <xsd:element name="midRangeColor" minOccurs="0" type="xsd:int"/>
     <xsd:element name="reportColumn" type="xsd:string"/>
     <xsd:element name="showSubTotal" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showTotal" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="type" type="tns:DashboardComponentColumnType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DashboardComponentColumnType">
    <xsd:restriction base="xsd:string"/>
   </xsd:simpleType>
   <xsd:complexType name="DashboardComponentSortInfo">
    <xsd:sequence>
     <xsd:element name="sortColumn" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sortOrder" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DashboardComponentGroupingSortProperties">
    <xsd:sequence>
     <xsd:element name="groupingSorts" minOccurs="0" maxOccurs="unbounded" type="tns:DashboardComponentGroupingSort"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DashboardComponentGroupingSort">
    <xsd:sequence>
     <xsd:element name="groupingLevel" type="xsd:string"/>
     <xsd:element name="inheritedReportGroupingSort" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sortColumn" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sortOrder" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ChartLegendPosition">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Right"/>
     <xsd:enumeration value="Bottom"/>
     <xsd:enumeration value="OnChart"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="DashboardType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="SpecifiedUser"/>
     <xsd:enumeration value="LoggedInUser"/>
     <xsd:enumeration value="MyTeamUser"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DashboardComponentSection">
    <xsd:sequence>
     <xsd:element name="columnSize" type="tns:DashboardComponentSize"/>
     <xsd:element name="components" minOccurs="0" maxOccurs="unbounded" type="tns:DashboardComponent"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DashboardComponentSize">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Narrow"/>
     <xsd:enumeration value="Medium"/>
     <xsd:enumeration value="Wide"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DataCategoryGroup">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="dataCategory" type="tns:DataCategory"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="objectUsage" minOccurs="0" type="tns:ObjectUsage"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DataCategory">
    <xsd:sequence>
     <xsd:element name="dataCategory" minOccurs="0" maxOccurs="unbounded" type="tns:DataCategory"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ObjectUsage">
    <xsd:sequence>
     <xsd:element name="object" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DataDotComSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableAccountExportButtonOff" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAccountImportButtonOff" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAllowDupeContactFromLead" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAllowDupeLeadFromContact" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContactExportButtonOff" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContactImportButtonOff" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDDCSocialKeyEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDataDotComCleanEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDataDotComOptOutsEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDatacloudAPIEnabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PlatformEventSubscriberConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="batchSize" minOccurs="0" type="xsd:int"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="platformEventConsumer" type="xsd:string"/>
       <xsd:element name="user" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CareProviderSearchConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="mappedObject" type="tns:ProviderSearchObjectMapping"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="sourceField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="targetField" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CareSystemFieldMapping">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="externalIdField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="role" type="tns:SourceSystemFieldRole"/>
       <xsd:element name="sourceSystem" minOccurs="0" type="xsd:string"/>
       <xsd:element name="targetObject" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DynamicTrigger">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="apexClass" type="xsd:string"/>
       <xsd:element name="customFieldDefinition" minOccurs="0" type="xsd:string"/>
       <xsd:element name="firesOnTriggerEventsAfterInsert" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="firesOnTriggerEventsAfterUpdate" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="firesOnTriggerEventsBeforeInsert" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="firesOnTriggerEventsBeforeUpdate" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ForecastingSourceDefinition">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="categoryField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="dateField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="familyField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="measureField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sourceObject" type="xsd:string"/>
       <xsd:element name="territory2Field" minOccurs="0" type="xsd:string"/>
       <xsd:element name="userField" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ForecastingTypeSource">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="forecastingSourceDefinition" type="xsd:string"/>
       <xsd:element name="forecastingType" type="xsd:string"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="parentSourceDefinition" minOccurs="0" type="xsd:string"/>
       <xsd:element name="relationField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sourceGroup" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SchedulingRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="schedulingCategory" type="tns:SchedulingCategory"/>
       <xsd:element name="schedulingRuleParameters" minOccurs="0" maxOccurs="unbounded" type="tns:SchedulingRuleParameter"/>
       <xsd:element name="schedulingRuleType" type="tns:SchedulingRuleType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SchedulingRuleParameter">
    <xsd:sequence>
     <xsd:element name="schedulingParameterKey" type="tns:SchedulingParameterKey"/>
     <xsd:element name="value" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RelatedRecordAssocCriteria">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionExpression" minOccurs="0" type="xsd:string"/>
       <xsd:element name="associationType" type="tns:AssociationType"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="eventType" type="tns:AssociationEventType"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="preCondition" type="xsd:string"/>
       <xsd:element name="referenceObject" type="xsd:string"/>
       <xsd:element name="status" type="tns:AssociationStatusType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ProviderSearchObjectMapping">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="HealthcareProvider"/>
     <xsd:enumeration value="HealthcarePractitionerFacility"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SourceSystemFieldRole">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="NotApplicable"/>
     <xsd:enumeration value="Patient"/>
     <xsd:enumeration value="ServiceProvider"/>
     <xsd:enumeration value="RemoteMonitoringPatient"/>
     <xsd:enumeration value="RemoteMonitoringDevice"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SchedulingCategory">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="B"/>
     <xsd:enumeration value="A"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SchedulingRuleType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="M"/>
     <xsd:enumeration value="B"/>
     <xsd:enumeration value="W"/>
     <xsd:enumeration value="A"/>
     <xsd:enumeration value="R"/>
     <xsd:enumeration value="C"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SchedulingParameterKey">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="L"/>
     <xsd:enumeration value="R"/>
     <xsd:enumeration value="W"/>
     <xsd:enumeration value="T"/>
     <xsd:enumeration value="C"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="AssociationType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="BranchManagement"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="AssociationEventType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Create"/>
     <xsd:enumeration value="Update"/>
     <xsd:enumeration value="Delete"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="AssociationStatusType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Draft"/>
     <xsd:enumeration value="Active"/>
     <xsd:enumeration value="Inactive"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="BranchManagementSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableBranchAssociation" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PlatformSlackSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="slackCapabilitiesEnabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WorkforceEngagementSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableMachineLearningForecasting" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWorkforceEngagement" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MailMergeSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableExtendedMailMerge" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="saveMailMergeDocsAsSalesforceDocs" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SourceTrackingSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableSourceTrackingSandboxes" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="OrgSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCustomerSuccessPortal" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIncludeContractStatus" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMakeDeploymentsMandatory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableManageSelfServiceUsers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOrgFeedSentimentAnalysis" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRADeploymentAttributeOnly" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableResetDivisionOnLogin" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AppAnalyticsSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableSimulationMode" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DevHubSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableDevOpsCenter" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePackaging2" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableScratchOrgManagementPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableShapeExportPref" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MapsAndLocationSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableAddressAutoComplete" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMapsAndLocation" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DelegateGroup">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="customObjects" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="groups" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="loginAccess" type="xsd:boolean"/>
       <xsd:element name="permissionSets" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="profiles" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="roles" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DeploymentSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="doesSkipAsyncApexValidation" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DiscoveryGoal">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="deployedModels" minOccurs="0" maxOccurs="unbounded" type="tns:DiscoveryDeployedModel"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="modelCards" minOccurs="0" maxOccurs="unbounded" type="tns:DiscoveryModelCard"/>
       <xsd:element name="outcome" type="tns:DiscoveryGoalOutcome"/>
       <xsd:element name="predictionType" type="tns:DiscoveryPredictionType"/>
       <xsd:element name="pushbackField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="pushbackType" minOccurs="0" type="tns:DiscoveryPushbackType"/>
       <xsd:element name="subscribedEntity" minOccurs="0" type="xsd:string"/>
       <xsd:element name="terminalStateFilters" minOccurs="0" maxOccurs="unbounded" type="tns:DiscoveryFilter"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DiscoveryDeployedModel">
    <xsd:sequence>
     <xsd:element name="active" type="xsd:boolean"/>
     <xsd:element name="aiModel" type="xsd:string"/>
     <xsd:element name="classificationThreshold" minOccurs="0" type="xsd:double"/>
     <xsd:element name="fieldMappings" minOccurs="0" maxOccurs="unbounded" type="tns:DiscoveryFieldMap"/>
     <xsd:element name="filters" minOccurs="0" maxOccurs="unbounded" type="tns:DiscoveryFilter"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="prescribableFields" minOccurs="0" maxOccurs="unbounded" type="tns:DiscoveryPrescribableField"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DiscoveryFieldMap">
    <xsd:sequence>
     <xsd:element name="mappedField" type="xsd:string"/>
     <xsd:element name="modelField" type="xsd:string"/>
     <xsd:element name="sobjectFieldJoinKey" minOccurs="0" type="xsd:string"/>
     <xsd:element name="source" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sourceFieldJoinKey" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sourceType" type="tns:DiscoveryFieldMapSourceType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DiscoveryFieldMapSourceType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="SalesforceField"/>
     <xsd:enumeration value="AnalyticsDatasetField"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DiscoveryFilter">
    <xsd:sequence>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="operator" type="tns:DiscoveryFilterOperator"/>
     <xsd:element name="type" minOccurs="0" type="tns:DiscoveryFilterFieldType"/>
     <xsd:element name="values" minOccurs="0" maxOccurs="unbounded" type="tns:DiscoveryFilterValue"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DiscoveryFilterOperator">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Equal"/>
     <xsd:enumeration value="NotEqual"/>
     <xsd:enumeration value="GreaterThan"/>
     <xsd:enumeration value="GreaterThanOrEqual"/>
     <xsd:enumeration value="LessThan"/>
     <xsd:enumeration value="LessThanOrEqual"/>
     <xsd:enumeration value="Between"/>
     <xsd:enumeration value="NotBetween"/>
     <xsd:enumeration value="InSet"/>
     <xsd:enumeration value="NotIn"/>
     <xsd:enumeration value="Contains"/>
     <xsd:enumeration value="StartsWith"/>
     <xsd:enumeration value="EndsWith"/>
     <xsd:enumeration value="IsNull"/>
     <xsd:enumeration value="IsNotNull"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="DiscoveryFilterFieldType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Text"/>
     <xsd:enumeration value="Number"/>
     <xsd:enumeration value="Date"/>
     <xsd:enumeration value="DateTime"/>
     <xsd:enumeration value="Boolean"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DiscoveryFilterValue">
    <xsd:sequence>
     <xsd:element name="type" type="tns:DiscoveryFilterValueType"/>
     <xsd:element name="value" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DiscoveryFilterValueType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Constant"/>
     <xsd:enumeration value="PlaceHolder"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DiscoveryPrescribableField">
    <xsd:sequence>
     <xsd:element name="customDefinitions" minOccurs="0" maxOccurs="unbounded" type="tns:DiscoveryCustomPrescribableFieldDefinition"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DiscoveryCustomPrescribableFieldDefinition">
    <xsd:sequence>
     <xsd:element name="filters" minOccurs="0" maxOccurs="unbounded" type="tns:DiscoveryFilter"/>
     <xsd:element name="template" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DiscoveryModelCard">
    <xsd:sequence>
     <xsd:element name="contactEmail" minOccurs="0" type="xsd:string"/>
     <xsd:element name="contactName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sections" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DiscoveryGoalOutcome">
    <xsd:sequence>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="fieldLabel" type="xsd:string"/>
     <xsd:element name="goal" type="tns:DiscoveryOutcomeGoal"/>
     <xsd:element name="mappedField" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DiscoveryOutcomeGoal">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Minimize"/>
     <xsd:enumeration value="Maximize"/>
     <xsd:enumeration value="None"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="DiscoveryPredictionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Unknown"/>
     <xsd:enumeration value="Regression"/>
     <xsd:enumeration value="Classification"/>
     <xsd:enumeration value="MulticlassClassification"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="DiscoveryPushbackType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AiRecordInsight"/>
     <xsd:enumeration value="Direct"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DiscoverySettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableEinsteinAnswersPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEinsteinArticleRecommendations" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DocumentChecklistSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="dciCustomSharing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="deleteDCIWithFiles" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DocumentType">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isActive" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DuplicateRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionOnInsert" type="tns:DupeActionType"/>
       <xsd:element name="actionOnUpdate" type="tns:DupeActionType"/>
       <xsd:element name="alertText" type="xsd:string" nillable="true"/>
       <xsd:element name="description" type="xsd:string" nillable="true"/>
       <xsd:element name="duplicateRuleFilter" type="tns:DuplicateRuleFilter" nillable="true"/>
       <xsd:element name="duplicateRuleMatchRules" minOccurs="0" maxOccurs="unbounded" type="tns:DuplicateRuleMatchRule" nillable="true"/>
       <xsd:element name="isActive" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="operationsOnInsert" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="operationsOnUpdate" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="securityOption" type="tns:DupeSecurityOptionType"/>
       <xsd:element name="sortOrder" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="DupeActionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Allow"/>
     <xsd:enumeration value="Block"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DuplicateRuleFilter">
    <xsd:sequence>
     <xsd:element name="booleanFilter" type="xsd:string" nillable="true"/>
     <xsd:element name="duplicateRuleFilterItems" minOccurs="0" maxOccurs="unbounded" type="tns:DuplicateRuleFilterItem"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DuplicateRuleMatchRule">
    <xsd:sequence>
     <xsd:element name="matchRuleSObjectType" type="xsd:string"/>
     <xsd:element name="matchingRule" type="xsd:string"/>
     <xsd:element name="objectMapping" type="tns:ObjectMapping" nillable="true"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ObjectMapping">
    <xsd:sequence>
     <xsd:element name="inputObject" type="xsd:string"/>
     <xsd:element name="mappingFields" minOccurs="0" maxOccurs="unbounded" type="tns:ObjectMappingField"/>
     <xsd:element name="outputObject" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ObjectMappingField">
    <xsd:sequence>
     <xsd:element name="inputField" type="xsd:string"/>
     <xsd:element name="outputField" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DupeSecurityOptionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="EnforceSharingRules"/>
     <xsd:enumeration value="BypassSharingRules"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EACSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="autoPopulateGoogleMeetLinks" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableActivityCapture" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableActivityMetrics" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableActivitySyncEngine" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEACForEveryonePref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEnforceEacSharingPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInboxActivitySharing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInsightsInTimeline" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInsightsInTimelineEacStd" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="provisionProductivityFeatures" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="syncInternalEvents" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EinsteinAgentSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="einsteinAgentRecommendations" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="reRunAttributeBasedRules" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="runAssignmentRules" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EinsteinAssistantSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableEinsteinAssistantDataExtractionEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEinsteinAssistantEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEinsteinEnableVoiceLogging" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EmailAdministrationSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableComplianceBcc" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailConsentManagement" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailSenderIdCompliance" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailSpfCompliance" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailToSalesforce" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailTrackingIPBlocklist" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailWorkflowApproval" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEnhancedEmailEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHandleBouncedEmails" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHtmlEmail" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInternationalEmailAddresses" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableListEmailLogActivities" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableResendBouncedEmails" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRestrictTlsToDomains" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSendThroughGmailPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSendViaExchangePref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSendViaGmailPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUseOrgFootersForExtTrans" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="sendEmailsEvenWhenAutomationUpdatesSameRecord" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="sendMassEmailNotification" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="sendTextOnlySystemEmails" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EmailIntegrationSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="doesEmailLogAsEmailMessageInOutlook" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesGmailStayConnectedToSalesforce" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContactAndEventSync" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmailTrackingInMobile" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEngageForOutlook" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGmailIntegration" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInboxMobileIntune" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOutlookIntegration" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOutlookMobileIntegration" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableProductivityFeatures" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSupplementalContactInfoInMobile" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isLayoutCustomizationAllowed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="orgIsSyncingEventsOutbound" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="shouldUseTrustedDomainsList" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EmailServicesFunction">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="apexClass" type="xsd:string"/>
       <xsd:element name="attachmentOption" type="tns:EmailServicesAttOptions"/>
       <xsd:element name="authenticationFailureAction" type="tns:EmailServicesErrorAction"/>
       <xsd:element name="authorizationFailureAction" type="tns:EmailServicesErrorAction"/>
       <xsd:element name="authorizedSenders" minOccurs="0" type="xsd:string"/>
       <xsd:element name="emailServicesAddresses" minOccurs="0" maxOccurs="unbounded" type="tns:EmailServicesAddress"/>
       <xsd:element name="errorRoutingAddress" minOccurs="0" type="xsd:string"/>
       <xsd:element name="functionInactiveAction" type="tns:EmailServicesErrorAction"/>
       <xsd:element name="functionName" type="xsd:string"/>
       <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isAuthenticationRequired" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isErrorRoutingEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isTextAttachmentsAsBinary" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isTlsRequired" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="overLimitAction" type="tns:EmailServicesErrorAction"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="EmailServicesAttOptions">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="TextOnly"/>
     <xsd:enumeration value="BinaryOnly"/>
     <xsd:enumeration value="All"/>
     <xsd:enumeration value="NoContent"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="EmailServicesErrorAction">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="UseSystemDefault"/>
     <xsd:enumeration value="Bounce"/>
     <xsd:enumeration value="Discard"/>
     <xsd:enumeration value="Requeue"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EmailServicesAddress">
    <xsd:sequence>
     <xsd:element name="authorizedSenders" minOccurs="0" type="xsd:string"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="localPart" type="xsd:string"/>
     <xsd:element name="runAsUser" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="EmailTemplateSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableTemplateEnhancedFolderPref" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EmbeddedServiceBranding">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="contrastInvertedColor" minOccurs="0" type="xsd:string"/>
       <xsd:element name="contrastPrimaryColor" minOccurs="0" type="xsd:string"/>
       <xsd:element name="embeddedServiceConfig" type="xsd:string"/>
       <xsd:element name="font" minOccurs="0" type="xsd:string"/>
       <xsd:element name="height" minOccurs="0" type="xsd:int"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="navBarColor" minOccurs="0" type="xsd:string"/>
       <xsd:element name="navBarTextColor" minOccurs="0" type="xsd:string"/>
       <xsd:element name="primaryColor" minOccurs="0" type="xsd:string"/>
       <xsd:element name="secondaryColor" minOccurs="0" type="xsd:string"/>
       <xsd:element name="secondaryNavBarColor" minOccurs="0" type="xsd:string"/>
       <xsd:element name="width" minOccurs="0" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EmbeddedServiceConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="areGuestUsersAllowed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="authMethod" minOccurs="0" type="tns:EmbeddedServiceAuthMethod"/>
       <xsd:element name="branding" minOccurs="0" type="xsd:string"/>
       <xsd:element name="deploymentFeature" type="tns:EmbeddedServiceDeploymentFeature"/>
       <xsd:element name="deploymentType" type="tns:EmbeddedServiceDeploymentType"/>
       <xsd:element name="embeddedServiceAppointmentSettings" minOccurs="0" type="tns:EmbeddedServiceAppointmentSettings"/>
       <xsd:element name="embeddedServiceCustomComponents" minOccurs="0" maxOccurs="unbounded" type="tns:EmbeddedServiceCustomComponent"/>
       <xsd:element name="embeddedServiceCustomLabels" minOccurs="0" maxOccurs="unbounded" type="tns:EmbeddedServiceCustomLabel"/>
       <xsd:element name="embeddedServiceCustomizations" minOccurs="0" maxOccurs="unbounded" type="tns:EmbeddedServiceCustomization"/>
       <xsd:element name="embeddedServiceFlowConfig" minOccurs="0" type="tns:EmbeddedServiceFlowConfig"/>
       <xsd:element name="embeddedServiceFlows" minOccurs="0" maxOccurs="unbounded" type="tns:EmbeddedServiceFlow"/>
       <xsd:element name="embeddedServiceLayouts" minOccurs="0" maxOccurs="unbounded" type="tns:EmbeddedServiceLayout"/>
       <xsd:element name="isEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="shouldHideAuthDialog" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="site" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="EmbeddedServiceAuthMethod">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="CommunitiesLogin"/>
     <xsd:enumeration value="CustomLogin"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="EmbeddedServiceDeploymentFeature">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="EmbeddedMessaging"/>
     <xsd:enumeration value="LiveAgent"/>
     <xsd:enumeration value="Flows"/>
     <xsd:enumeration value="FieldService"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="EmbeddedServiceDeploymentType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Web"/>
     <xsd:enumeration value="Mobile"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EmbeddedServiceAppointmentSettings">
    <xsd:sequence>
     <xsd:element name="appointmentConfirmImg" minOccurs="0" type="xsd:string"/>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="homeImg" minOccurs="0" type="xsd:string"/>
     <xsd:element name="logoImg" minOccurs="0" type="xsd:string"/>
     <xsd:element name="shouldShowExistingAppointment" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="shouldShowNewAppointment" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="EmbeddedServiceCustomComponent">
    <xsd:sequence>
     <xsd:element name="componentBundleType" minOccurs="0" type="tns:EmbeddedServiceComponentBundleType"/>
     <xsd:element name="customComponent" minOccurs="0" type="xsd:string"/>
     <xsd:element name="customComponentType" minOccurs="0" type="tns:EmbeddedServiceCustomComponentType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="EmbeddedServiceComponentBundleType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AuraDefinitionBundle"/>
     <xsd:enumeration value="LightningComponentBundle"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="EmbeddedServiceCustomComponentType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="LA_Prechat"/>
     <xsd:enumeration value="LA_Minimized"/>
     <xsd:enumeration value="LA_PlainTextChatMessage"/>
     <xsd:enumeration value="LA_ChatHeader"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EmbeddedServiceCustomLabel">
    <xsd:sequence>
     <xsd:element name="customLabel" minOccurs="0" type="xsd:string"/>
     <xsd:element name="feature" minOccurs="0" type="tns:EmbeddedServiceFeature"/>
     <xsd:element name="labelKey" minOccurs="0" type="tns:EmbeddedServiceLabelKey"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="EmbeddedServiceFeature">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="NotInUse"/>
     <xsd:enumeration value="Base"/>
     <xsd:enumeration value="LiveAgent"/>
     <xsd:enumeration value="FieldService"/>
     <xsd:enumeration value="Flows"/>
     <xsd:enumeration value="ChannelMenu"/>
     <xsd:enumeration value="EmbeddedMessaging"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="EmbeddedServiceLabelKey">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="LA_Container_Base_Close"/>
     <xsd:enumeration value="LA_Container_Base_Minimize"/>
     <xsd:enumeration value="LA_Container_Base_EndOfDialog"/>
     <xsd:enumeration value="LA_Container_Base_MinimizedContainerAssistiveText"/>
     <xsd:enumeration value="LA_Chat_Body_ChatWindowAgent"/>
     <xsd:enumeration value="LA_Chat_Body_InputTextPlaceholder"/>
     <xsd:enumeration value="LA_Chat_Body_AgentTypingUpdate"/>
     <xsd:enumeration value="LA_Chat_Body_Send"/>
     <xsd:enumeration value="LA_Chat_Body_ChatStartTime"/>
     <xsd:enumeration value="LA_Chat_Body_MessageAreaTransferred"/>
     <xsd:enumeration value="LA_Chat_Body_FileTransferCanceled"/>
     <xsd:enumeration value="LA_Chat_Body_FileTransferSuccess"/>
     <xsd:enumeration value="LA_Chat_Body_FileTransferFailure"/>
     <xsd:enumeration value="LA_Chat_Body_FileTransferRequested"/>
     <xsd:enumeration value="LA_Chat_Body_TransferFailed"/>
     <xsd:enumeration value="LA_Chat_ExtendedHeader_ShowExtendedHeader"/>
     <xsd:enumeration value="LA_Chat_ExtendedHeader_HideExtendedHeader"/>
     <xsd:enumeration value="LA_Chat_ExtendedHeader_ChatStateHeaderGreeting"/>
     <xsd:enumeration value="LA_Chat_ExtendedHeader_SaveTranscript"/>
     <xsd:enumeration value="LA_Chat_ExtendedHeader_EndChatAction"/>
     <xsd:enumeration value="LA_Chat_FileTransfer_FileUpload"/>
     <xsd:enumeration value="LA_Chat_FileTransfer_UploadFile"/>
     <xsd:enumeration value="LA_Chat_FileTransfer_SelectNewFile"/>
     <xsd:enumeration value="LA_Chat_FileTransfer_UsePreviousElementToUploadFile"/>
     <xsd:enumeration value="LA_Chat_FileTransfer_RemoveFile"/>
     <xsd:enumeration value="LA_Chat_Minimized_MessageNotification"/>
     <xsd:enumeration value="LA_Chat_Minimized_SingleMessageNotification"/>
     <xsd:enumeration value="LA_Chat_Minimized_AgentSaysNotification"/>
     <xsd:enumeration value="LA_Chat_Minimized_IdleTimeoutMinimizedWarning"/>
     <xsd:enumeration value="LA_Chat_Minimized_IdleTimeoutMinimizedEndChat"/>
     <xsd:enumeration value="LA_Chat_Ended_ChatEnd"/>
     <xsd:enumeration value="LA_Chat_Ended_ChatEndAgent"/>
     <xsd:enumeration value="LA_Chat_Ended_ChatEndConnection"/>
     <xsd:enumeration value="LA_Chat_Ended_ChatButtonClose"/>
     <xsd:enumeration value="LA_Chat_Ended_PostChatButton"/>
     <xsd:enumeration value="LA_Chat_Ended_IdleTimeoutEndChatMessage"/>
     <xsd:enumeration value="LA_Chat_Reconnecting_ReconnectingChasitorIssue"/>
     <xsd:enumeration value="LA_Chat_Reconnecting_ReconnectingMinimizedMessage"/>
     <xsd:enumeration value="LA_Chat_Timeout_IdleTimeoutWarningQuestion"/>
     <xsd:enumeration value="LA_Chat_AgentTransfer_BannerInProgressTransfer"/>
     <xsd:enumeration value="LA_Chat_AgentTransfer_MinimizedInProgressTransfer"/>
     <xsd:enumeration value="LA_Chat_AgentTransfer_BannerTransferred"/>
     <xsd:enumeration value="LA_Chat_AgentTransfer_BannerReconnected"/>
     <xsd:enumeration value="LA_Chat_CloseConfirmation_ChatStateHeader"/>
     <xsd:enumeration value="LA_Chat_CloseConfirmation_ChatStateBody"/>
     <xsd:enumeration value="LA_Chat_CloseConfirmation_ChatStateResume"/>
     <xsd:enumeration value="LA_Chat_CloseConfirmation_ChatStateEnd"/>
     <xsd:enumeration value="LA_Chat_UnseenMessage_UnseenMessage"/>
     <xsd:enumeration value="LA_Chat_UnseenMessage_SingleUnseenMessage"/>
     <xsd:enumeration value="LA_OfflineSupport_SupportForm_HeaderText"/>
     <xsd:enumeration value="LA_OfflineSupport_Error_ErrorDialogTitle"/>
     <xsd:enumeration value="LA_OfflineSupport_Error_ErrorDialogBody"/>
     <xsd:enumeration value="LA_OfflineSupport_Error_ErrorDialogButton"/>
     <xsd:enumeration value="LA_OfflineSupport_SupportForm_SupportFormTitle"/>
     <xsd:enumeration value="LA_OfflineSupport_SupportForm_SupportFormSubtitle"/>
     <xsd:enumeration value="LA_OfflineSupport_SupportForm_SupportFormButton"/>
     <xsd:enumeration value="LA_OfflineSupport_SupportForm_BannerAltText"/>
     <xsd:enumeration value="LA_OfflineSupport_CloseConfirmation_ConfirmationDialogTitle"/>
     <xsd:enumeration value="LA_OfflineSupport_CloseConfirmation_ConfirmationDialogBody"/>
     <xsd:enumeration value="LA_OfflineSupport_CloseConfirmation_ConfirmationDialogButton"/>
     <xsd:enumeration value="LA_OfflineSupport_Minimized_ConfirmationMinimizedText"/>
     <xsd:enumeration value="LA_OfflineSupport_Minimized_ErrorMinimizedText"/>
     <xsd:enumeration value="LA_PostChat_Base_PostChat"/>
     <xsd:enumeration value="LA_PreChat_Base_LiveChat"/>
     <xsd:enumeration value="LA_PreChat_Base_Instructions"/>
     <xsd:enumeration value="LA_PreChat_Base_BannerAltText"/>
     <xsd:enumeration value="LA_PreChat_Base_PrechatAssistiveText"/>
     <xsd:enumeration value="LA_PreChat_Base_StartChat"/>
     <xsd:enumeration value="LA_PreChat_Base_FieldError"/>
     <xsd:enumeration value="LA_Waiting_WithoutQueuePos_WaitingGreeting"/>
     <xsd:enumeration value="LA_Waiting_WithoutQueuePos_WaitingDefaultName"/>
     <xsd:enumeration value="LA_Waiting_WithoutQueuePos_WaitingMessage"/>
     <xsd:enumeration value="LA_Waiting_WithoutQueuePos_WaitingCancelChatRequest"/>
     <xsd:enumeration value="LA_Waiting_WithQueuePos_WaitingQueuePosMessageFirstLine"/>
     <xsd:enumeration value="LA_Waiting_WithQueuePos_WaitingQueuePosMessageSecondLine"/>
     <xsd:enumeration value="LA_Waiting_WithQueuePos_WaitingQueuePosZeroMessage"/>
     <xsd:enumeration value="LA_Waiting_WithQueuePos_WaitingQueuePosConnectingMessage"/>
     <xsd:enumeration value="LA_Waiting_WithQueuePos_WaitingQueuePosMaxNumber"/>
     <xsd:enumeration value="LA_Waiting_WithQueuePos_WaitingQueuePosMaxMessageFirstLine"/>
     <xsd:enumeration value="LA_Waiting_WithQueuePos_WaitingQueuePosMaxMessageSecondLine"/>
     <xsd:enumeration value="LA_Waiting_Minimized_MinimizedWaitingMessage"/>
     <xsd:enumeration value="LA_Waiting_Minimized_MinimizedQueuePosMessage"/>
     <xsd:enumeration value="LA_Waiting_Minimized_MinimizedQueuePosZeroMessage"/>
     <xsd:enumeration value="LA_Waiting_Minimized_MinimizedQueuePosAssistiveMessage"/>
     <xsd:enumeration value="LA_Waiting_Minimized_MinimizedQueuePosZeroAssistiveMessage"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorNoAgentTitle"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorNoAgentHeader"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorNoAgentBodyApology"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorBlockedTitleAndHeader"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorBlockedBody"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorBlockedCloseButton"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorNoConnectionTitle"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorNoConnectionHeader"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorNoConnectionBodyApology"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorTryAgainButton"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorExitChatButton"/>
     <xsd:enumeration value="LA_Waiting_CloseConfirmation_WaitingStateHeader"/>
     <xsd:enumeration value="LA_Waiting_CloseConfirmation_WaitingStateBodyApology"/>
     <xsd:enumeration value="LA_Waiting_CloseConfirmation_WaitingStateLeave"/>
     <xsd:enumeration value="LA_Waiting_CloseConfirmation_WaitingStateContinue"/>
     <xsd:enumeration value="LA_Chat_Timeout_IdleTimeoutWarningRequest"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorNoAgentBodyRequest"/>
     <xsd:enumeration value="LA_Waiting_Error_ErrorNoConnectionBodyRequest"/>
     <xsd:enumeration value="LA_Waiting_CloseConfirmation_WaitingStateBodyWarning"/>
     <xsd:enumeration value="LA_General_CloseSessionWarningTitle"/>
     <xsd:enumeration value="LA_General_CloseSessionWarningBody"/>
     <xsd:enumeration value="LA_General_CloseSessionWarningButton"/>
     <xsd:enumeration value="LA_Chat_Body_ChooseOption"/>
     <xsd:enumeration value="LA_Waiting_Base_BannerAssistiveText"/>
     <xsd:enumeration value="LA_Chat_Group_Chat_HeaderTitle"/>
     <xsd:enumeration value="LA_Chat_Group_Chat_ExtendedHeaderGreeting"/>
     <xsd:enumeration value="LA_Chat_Group_Chat_AgentJoinedChat"/>
     <xsd:enumeration value="LA_Chat_Group_Chat_AgentLeftChat"/>
     <xsd:enumeration value="LA_Chat_Group_Chat_MinimizedStateMessage"/>
     <xsd:enumeration value="LA_Chat_WithQueuePos_QueuePosTransferringMessage"/>
     <xsd:enumeration value="LA_Chat_Ended_ChatEndChatbot"/>
     <xsd:enumeration value="LA_Chat_Body_InputTextAssistiveText"/>
     <xsd:enumeration value="LA_Waiting_Header_Text"/>
     <xsd:enumeration value="FS_Container_Base_Back"/>
     <xsd:enumeration value="FS_Container_AuthenticationFailure_Title"/>
     <xsd:enumeration value="FS_Container_AuthenticationFailure_Body"/>
     <xsd:enumeration value="FS_Container_AuthenticationFailure_Button"/>
     <xsd:enumeration value="FS_AppointmentDetail_Error_AccessDenied"/>
     <xsd:enumeration value="FS_AppointmentDetail_Error_NoAppointmentFound"/>
     <xsd:enumeration value="FS_AppointmentDetail_Error_ButtonOK"/>
     <xsd:enumeration value="FS_AppointmentList_Base_ActiveAppointmentTab"/>
     <xsd:enumeration value="FS_AppointmentList_Base_ClosedAppointmentTab"/>
     <xsd:enumeration value="FS_AppointmentList_Base_Header"/>
     <xsd:enumeration value="FS_AppointmentList_Base_NewAppointmentButtonLabel"/>
     <xsd:enumeration value="FS_AppointmentList_Error_GenericErrorStatement"/>
     <xsd:enumeration value="FS_AppointmentList_Empty_NoAppointmentsTitleUpcomingTab"/>
     <xsd:enumeration value="FS_AppointmentList_Empty_NoAppointmentsDescriptionUpcomingTab"/>
     <xsd:enumeration value="FS_AppointmentList_Empty_NoAppointmentsTitlePastTab"/>
     <xsd:enumeration value="FS_AppointmentList_Empty_NoAppointmentsDescriptionPastTab"/>
     <xsd:enumeration value="FS_Confirmation_Base_Scheduled"/>
     <xsd:enumeration value="FS_Confirmation_Base_Assigned"/>
     <xsd:enumeration value="FS_Confirmation_Base_Arriving"/>
     <xsd:enumeration value="FS_Confirmation_Base_InProgress"/>
     <xsd:enumeration value="FS_Confirmation_Base_Dispatched"/>
     <xsd:enumeration value="FS_Confirmation_Base_Completed"/>
     <xsd:enumeration value="FS_Confirmation_Base_HeaderText"/>
     <xsd:enumeration value="FS_Confirmation_Base_AddCalendar"/>
     <xsd:enumeration value="FS_Confirmation_Base_ViewAppointment"/>
     <xsd:enumeration value="FS_Flows_Error_Title"/>
     <xsd:enumeration value="FS_Flows_Error_Body"/>
     <xsd:enumeration value="FS_Flows_Error_ConfirmButton"/>
     <xsd:enumeration value="FS_Flows_Error_CancelOrModifyError"/>
     <xsd:enumeration value="FS_Flows_NewAppointmentCloseConfirmation_Title"/>
     <xsd:enumeration value="FS_Flows_NewAppointmentCloseConfirmation_Body"/>
     <xsd:enumeration value="FS_Flows_NewAppointmentCloseConfirmation_ButtonClose"/>
     <xsd:enumeration value="FS_Flows_NewAppointmentCloseConfirmation_ButtonCancel"/>
     <xsd:enumeration value="FS_Flows_CancelAppointmentCloseConfirmation_Title"/>
     <xsd:enumeration value="FS_Flows_CancelAppointmentCloseConfirmation_Body"/>
     <xsd:enumeration value="FS_Flows_CancelAppointmentCloseConfirmation_ButtonClose"/>
     <xsd:enumeration value="FS_Flows_CancelAppointmentCloseConfirmation_ButtonCancel"/>
     <xsd:enumeration value="FS_Flows_CancelAppointmentCloseConfirmation_Footer"/>
     <xsd:enumeration value="FS_Flows_ModifyAppointmentCloseConfirmation_Title"/>
     <xsd:enumeration value="FS_Flows_ModifyAppointmentCloseConfirmation_Body"/>
     <xsd:enumeration value="FS_Flows_ModifyAppointmentCloseConfirmation_ButtonClose"/>
     <xsd:enumeration value="FS_Flows_ModifyAppointmentCloseConfirmation_ButtonCancel"/>
     <xsd:enumeration value="FS_Flows_ModifyAppointmentCloseConfirmation_Footer"/>
     <xsd:enumeration value="FS_Scheduling_Base_HeaderText"/>
     <xsd:enumeration value="FS_Scheduling_Base_RecommendedTab"/>
     <xsd:enumeration value="FS_Scheduling_Base_ByDateTab"/>
     <xsd:enumeration value="FS_Scheduling_Base_PreviousWeekAssistiveText"/>
     <xsd:enumeration value="FS_Scheduling_Base_NextWeekAssistiveText"/>
     <xsd:enumeration value="FS_Scheduling_Base_DatePickerAssistiveText"/>
     <xsd:enumeration value="FS_Scheduling_Error_UnexpectedError"/>
     <xsd:enumeration value="FS_Scheduling_Error_NoAvailableTimeslotsError"/>
     <xsd:enumeration value="FS_Scheduling_Error_NoAvailableTimeslotsByDateError"/>
     <xsd:enumeration value="FS_Welcome_Base_GreetingTitle"/>
     <xsd:enumeration value="FS_Welcome_Base_NewAppointmentButton"/>
     <xsd:enumeration value="FS_Welcome_Base_ExistingAppointmentsButton"/>
     <xsd:enumeration value="FS_Confirmation_Base_DoneButton"/>
     <xsd:enumeration value="FS_AppointmentList_Error_GenericErrorRequest"/>
     <xsd:enumeration value="FS_AppointmentHome_Base_CancelAppointmentButton"/>
     <xsd:enumeration value="FS_AppointmentHome_Base_ModifyAppointmentButton"/>
     <xsd:enumeration value="FS_AppointmentHome_Base_ErrorTitle"/>
     <xsd:enumeration value="FS_Scheduling_Base_TimePickerAssistiveText"/>
     <xsd:enumeration value="FS_ResourceDetail_Base_Header"/>
     <xsd:enumeration value="FS_AppointmentHome_Base_DefaultCardHeaderText"/>
     <xsd:enumeration value="FS_Error_Dialog_Title"/>
     <xsd:enumeration value="FS_Error_Dialog_Body"/>
     <xsd:enumeration value="FS_Error_Dialog_Confirm_Button"/>
     <xsd:enumeration value="CM_Container_Header_Primary_Greeting"/>
     <xsd:enumeration value="CM_Container_Header_Secondary_Greeting"/>
     <xsd:enumeration value="CM_Container_MenuItems_WebChatAvailable"/>
     <xsd:enumeration value="CM_Container_MenuItems_WebChatUnavailable"/>
     <xsd:enumeration value="CM_Container_MenuItems_WebChatLoading"/>
     <xsd:enumeration value="CM_Container_MenuItems_ChannelLabel"/>
     <xsd:enumeration value="CM_Container_Button_AssistiveText"/>
     <xsd:enumeration value="CM_Container_MenuItems_AssistiveText"/>
     <xsd:enumeration value="CM_Container_MenuItems_WebLinkNewTabAssistiveText"/>
     <xsd:enumeration value="EM_Container_Base_DefaultHeaderText"/>
     <xsd:enumeration value="EM_Container_Base_Minimize"/>
     <xsd:enumeration value="EM_Container_Base_Close"/>
     <xsd:enumeration value="EM_Container_Base_CloseConversation"/>
     <xsd:enumeration value="EM_Container_Base_DefaultMinimizedText"/>
     <xsd:enumeration value="EM_Container_Base_MinimizedButtonAssistiveText"/>
     <xsd:enumeration value="EM_Container_Base_MinimizedNotifDismissButtonAssistiveText"/>
     <xsd:enumeration value="EM_Container_Base_HeaderGreetingAnnouncement"/>
     <xsd:enumeration value="EM_Container_Base_NinePlusUnseenMessageCount"/>
     <xsd:enumeration value="EM_Container_Base_ZeroUnseenMessagesAssistiveText"/>
     <xsd:enumeration value="EM_Container_Base_UnseenMessagesAssistiveText"/>
     <xsd:enumeration value="EM_Container_Base_NinePlusUnseenMessagesAssistiveText"/>
     <xsd:enumeration value="EM_Container_Base_InputFooterTextAreaPlaceHolder"/>
     <xsd:enumeration value="EM_Container_Base_PrechatFirstName"/>
     <xsd:enumeration value="EM_Container_Base_PrechatLastName"/>
     <xsd:enumeration value="EM_Container_Base_PrechatSubject"/>
     <xsd:enumeration value="EM_Container_Base_PrechatEmail"/>
     <xsd:enumeration value="EM_Container_Base_BeforeUnloadWarningMessage"/>
     <xsd:enumeration value="EM_Container_Base_StartBookendText"/>
     <xsd:enumeration value="EM_Container_Base_EndBookendText"/>
     <xsd:enumeration value="EM_Container_Base_ChatMessageMetadataAssistiveText"/>
     <xsd:enumeration value="EM_Container_Base_ParticipantJoinText"/>
     <xsd:enumeration value="EM_Container_Base_ParticipantLeaveText"/>
     <xsd:enumeration value="EM_Container_Base_InputFooterTextAreaAssistiveText"/>
     <xsd:enumeration value="EM_Container_Base_InputFooterSendButtonAssistiveText"/>
     <xsd:enumeration value="EM_Container_Base_PrechatStateSubmitButton"/>
     <xsd:enumeration value="EM_Container_Base_InvalidEmailFormFieldError"/>
     <xsd:enumeration value="EM_Container_Base_RequiredFormFieldError"/>
     <xsd:enumeration value="EM_Container_Base_NotificationDismissButtonText"/>
     <xsd:enumeration value="EM_Container_Base_ConversationEndedMinimizedText"/>
     <xsd:enumeration value="EM_Container_Base_ExpiredJWT"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EmbeddedServiceCustomization">
    <xsd:sequence>
     <xsd:element name="customizationName" type="xsd:string"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="embeddedServiceResources" minOccurs="0" maxOccurs="unbounded" type="tns:EmbeddedServiceResource"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="EmbeddedServiceResource">
    <xsd:sequence>
     <xsd:element name="resource" type="xsd:string"/>
     <xsd:element name="resourceType" type="tns:EmbeddedServiceResourceType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="EmbeddedServiceResourceType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="SettingsFile"/>
     <xsd:enumeration value="ChatInvitation"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EmbeddedServiceFlowConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enabled" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EmbeddedServiceFlow">
    <xsd:sequence>
     <xsd:element name="flow" type="xsd:string"/>
     <xsd:element name="flowType" type="tns:EmbeddedServiceFlowType"/>
     <xsd:element name="isAuthenticationRequired" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="EmbeddedServiceFlowType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="FL_Flow"/>
     <xsd:enumeration value="FS_NewAppointment"/>
     <xsd:enumeration value="FS_ModifyAppointment"/>
     <xsd:enumeration value="FS_CancelAppointment"/>
     <xsd:enumeration value="LA_Survey"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EmbeddedServiceLayout">
    <xsd:sequence>
     <xsd:element name="embeddedServiceLayoutRules" minOccurs="0" maxOccurs="unbounded" type="tns:EmbeddedServiceLayoutRule"/>
     <xsd:element name="layout" type="xsd:string"/>
     <xsd:element name="layoutType" minOccurs="0" type="tns:EmbeddedServiceLayoutType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="EmbeddedServiceLayoutRule">
    <xsd:sequence>
     <xsd:element name="appointmentStatus" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="EmbeddedServiceLayoutType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="FS_AppointmentHome"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EmbeddedServiceLiveAgent">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="avatarImg" minOccurs="0" type="xsd:string"/>
       <xsd:element name="embeddedServiceConfig" type="xsd:string"/>
       <xsd:element name="embeddedServiceQuickActions" minOccurs="0" maxOccurs="unbounded" type="tns:EmbeddedServiceQuickAction"/>
       <xsd:element name="enabled" type="xsd:boolean"/>
       <xsd:element name="fontSize" type="tns:EmbeddedServiceFontSize"/>
       <xsd:element name="isOfflineCaseEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isQueuePositionEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="liveAgentChatUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="liveAgentContentUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="liveChatButton" type="xsd:string"/>
       <xsd:element name="liveChatDeployment" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="offlineCaseBackgroundImg" minOccurs="0" type="xsd:string"/>
       <xsd:element name="prechatBackgroundImg" minOccurs="0" type="xsd:string"/>
       <xsd:element name="prechatEnabled" type="xsd:boolean"/>
       <xsd:element name="prechatJson" minOccurs="0" type="xsd:string"/>
       <xsd:element name="scenario" type="tns:EmbeddedServiceScenario"/>
       <xsd:element name="smallCompanyLogoImg" minOccurs="0" type="xsd:string"/>
       <xsd:element name="waitingStateBackgroundImg" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EmbeddedServiceQuickAction">
    <xsd:sequence>
     <xsd:element name="embeddedServiceLiveAgent" type="xsd:string"/>
     <xsd:element name="order" type="xsd:int"/>
     <xsd:element name="quickActionDefinition" type="xsd:string"/>
     <xsd:element name="quickActionType" minOccurs="0" type="tns:EmbeddedServiceQuickActionType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="EmbeddedServiceQuickActionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Prechat"/>
     <xsd:enumeration value="OfflineCase"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="EmbeddedServiceFontSize">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Small"/>
     <xsd:enumeration value="Medium"/>
     <xsd:enumeration value="Large"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="EmbeddedServiceScenario">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Sales"/>
     <xsd:enumeration value="Service"/>
     <xsd:enumeration value="Basic"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EmbeddedServiceMenuSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="branding" minOccurs="0" type="xsd:string"/>
       <xsd:element name="embeddedServiceCustomLabels" minOccurs="0" maxOccurs="unbounded" type="tns:EmbeddedServiceCustomLabel"/>
       <xsd:element name="embeddedServiceCustomizations" minOccurs="0" maxOccurs="unbounded" type="tns:EmbeddedServiceCustomization"/>
       <xsd:element name="embeddedServiceMenuItems" minOccurs="0" maxOccurs="unbounded" type="tns:EmbeddedServiceMenuItem"/>
       <xsd:element name="isEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="site" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EmbeddedServiceMenuItem">
    <xsd:sequence>
     <xsd:element name="channel" minOccurs="0" type="xsd:string"/>
     <xsd:element name="channelType" minOccurs="0" type="tns:EmbeddedServiceChannelType"/>
     <xsd:element name="customUrl" minOccurs="0" type="xsd:string"/>
     <xsd:element name="displayOrder" minOccurs="0" type="xsd:int"/>
     <xsd:element name="embeddedServiceCustomLabels" minOccurs="0" maxOccurs="unbounded" type="tns:EmbeddedServiceCustomLabel"/>
     <xsd:element name="iconUrl" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isDisplayedOnPageLoad" type="xsd:boolean"/>
     <xsd:element name="itemName" type="xsd:string"/>
     <xsd:element name="osOptionsHideInIOS" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="osOptionsHideInLinuxOS" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="osOptionsHideInMacOS" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="osOptionsHideInOtherOS" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="osOptionsHideInWindowsOS" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="phoneNumber" minOccurs="0" type="xsd:string"/>
     <xsd:element name="shouldOpenUrlInSameTab" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="EmbeddedServiceChannelType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="EmbeddedServiceConfig"/>
     <xsd:enumeration value="MessagingChannel"/>
     <xsd:enumeration value="Phone"/>
     <xsd:enumeration value="CustomURL"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EmployeeFieldAccessSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableEmployeeFieldMaskDefaults" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmployeeFieldMasking" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EmployeeUserSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="emailEncoding" type="xsd:string"/>
       <xsd:element name="enableEmployeeAutoCreateUser" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEmployeeIsSourceOfTruth" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="permset" minOccurs="0" type="xsd:string"/>
       <xsd:element name="profile" type="xsd:string"/>
       <xsd:element name="usernameSuffix" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EncryptionKeySettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="canOptOutOfDerivationWithBYOK" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCacheOnlyKeys" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableReplayDetection" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EnhancedNotesSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableEnhancedNotes" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTasksOnEnhancedNotes" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EntitlementProcess">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="SObjectType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="active" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="businessHours" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="entryStartDateField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="exitCriteriaBooleanFilter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="exitCriteriaFilterItems" minOccurs="0" maxOccurs="unbounded" type="tns:FilterItem"/>
       <xsd:element name="exitCriteriaFormula" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isRecordTypeApplied" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isVersionDefault" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="milestones" minOccurs="0" maxOccurs="unbounded" type="tns:EntitlementProcessMilestoneItem"/>
       <xsd:element name="name" minOccurs="0" type="xsd:string"/>
       <xsd:element name="recordType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="versionMaster" minOccurs="0" type="xsd:string"/>
       <xsd:element name="versionNotes" minOccurs="0" type="xsd:string"/>
       <xsd:element name="versionNumber" minOccurs="0" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EntitlementProcessMilestoneItem">
    <xsd:sequence>
     <xsd:element name="businessHours" minOccurs="0" type="xsd:string"/>
     <xsd:element name="criteriaBooleanFilter" minOccurs="0" type="xsd:string"/>
     <xsd:element name="milestoneCriteriaFilterItems" minOccurs="0" maxOccurs="unbounded" type="tns:FilterItem"/>
     <xsd:element name="milestoneCriteriaFormula" minOccurs="0" type="xsd:string"/>
     <xsd:element name="milestoneName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="minutesCustomClass" minOccurs="0" type="xsd:string"/>
     <xsd:element name="minutesToComplete" minOccurs="0" type="xsd:int"/>
     <xsd:element name="successActions" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowActionReference"/>
     <xsd:element name="timeTriggers" minOccurs="0" maxOccurs="unbounded" type="tns:EntitlementProcessMilestoneTimeTrigger"/>
     <xsd:element name="useCriteriaStartTime" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="EntitlementProcessMilestoneTimeTrigger">
    <xsd:sequence>
     <xsd:element name="actions" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowActionReference"/>
     <xsd:element name="timeLength" minOccurs="0" type="xsd:int"/>
     <xsd:element name="workflowTimeTriggerUnit" type="tns:MilestoneTimeUnits"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="MilestoneTimeUnits">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Minutes"/>
     <xsd:enumeration value="Hours"/>
     <xsd:enumeration value="Days"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="EntitlementSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="assetLookupLimitedToActiveEntitlementsOnAccount" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="assetLookupLimitedToActiveEntitlementsOnContact" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="assetLookupLimitedToSameAccount" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="assetLookupLimitedToSameContact" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEntitlementVersioning" type="xsd:boolean"/>
       <xsd:element name="enableEntitlements" type="xsd:boolean"/>
       <xsd:element name="enableMilestoneFeedItem" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMilestoneStoppedTime" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="entitlementLookupLimitedToActiveStatus" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="entitlementLookupLimitedToSameAccount" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="entitlementLookupLimitedToSameAsset" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="entitlementLookupLimitedToSameContact" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="ignoreMilestoneBusinessHours" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EntitlementTemplate">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="businessHours" minOccurs="0" type="xsd:string"/>
       <xsd:element name="casesPerEntitlement" minOccurs="0" type="xsd:int"/>
       <xsd:element name="entitlementProcess" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isPerIncident" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="term" minOccurs="0" type="xsd:int"/>
       <xsd:element name="type" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EntityImplements">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="fieldImplements" minOccurs="0" maxOccurs="unbounded" type="tns:FieldImplements"/>
       <xsd:element name="isDefault" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FieldImplements">
    <xsd:sequence>
     <xsd:element name="field" minOccurs="0" type="xsd:string"/>
     <xsd:element name="interfaceField" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="EscalationRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="ruleEntry" minOccurs="0" maxOccurs="unbounded" type="tns:RuleEntry"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EscalationRules">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="escalationRule" minOccurs="0" maxOccurs="unbounded" type="tns:EscalationRule"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EssentialsSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="emailConnectorEnabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EventSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableApexLimitEvents" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDeleteMonitoringData" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDynamicStreamingChannel" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEventLogWaveIntegration" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLoginForensics" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableStreamingApi" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTerminateOldestSession" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTransactionSecurityPolicies" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ExperienceBundle">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="experienceResources" minOccurs="0" type="tns:ExperienceResources"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="type" type="tns:SiteType"/>
       <xsd:element name="urlPathPrefix" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ExperienceResources">
    <xsd:sequence>
     <xsd:element name="experienceResource" minOccurs="0" maxOccurs="unbounded" type="tns:ExperienceResource"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ExperienceResource">
    <xsd:sequence>
     <xsd:element name="fileName" type="xsd:string"/>
     <xsd:element name="format" type="xsd:string"/>
     <xsd:element name="source" minOccurs="0" type="xsd:base64Binary"/>
     <xsd:element name="type" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ExperienceBundleSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableExperienceBundleMetadata" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ExternalDataSource">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="authProvider" minOccurs="0" type="xsd:string"/>
       <xsd:element name="certificate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="customConfiguration" minOccurs="0" type="xsd:string"/>
       <xsd:element name="customHttpHeaders" minOccurs="0" maxOccurs="unbounded" type="tns:CustomHttpHeader"/>
       <xsd:element name="endpoint" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isWritable" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="oauthRefreshToken" minOccurs="0" type="xsd:string"/>
       <xsd:element name="oauthScope" minOccurs="0" type="xsd:string"/>
       <xsd:element name="oauthToken" minOccurs="0" type="xsd:string"/>
       <xsd:element name="password" minOccurs="0" type="xsd:string"/>
       <xsd:element name="principalType" type="tns:ExternalPrincipalType"/>
       <xsd:element name="protocol" type="tns:AuthenticationProtocol"/>
       <xsd:element name="repository" minOccurs="0" type="xsd:string"/>
       <xsd:element name="type" type="tns:ExternalDataSourceType"/>
       <xsd:element name="username" minOccurs="0" type="xsd:string"/>
       <xsd:element name="version" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomHttpHeader">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="headerFieldName" type="xsd:string"/>
     <xsd:element name="headerFieldValue" type="xsd:string"/>
     <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ExternalPrincipalType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Anonymous"/>
     <xsd:enumeration value="PerUser"/>
     <xsd:enumeration value="NamedUser"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="AuthenticationProtocol">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="NoAuthentication"/>
     <xsd:enumeration value="Oauth"/>
     <xsd:enumeration value="Password"/>
     <xsd:enumeration value="AwsSv4"/>
     <xsd:enumeration value="Jwt"/>
     <xsd:enumeration value="JwtExchange"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ExternalDataSourceType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="contentHubItem"/>
     <xsd:enumeration value="Datajourney"/>
     <xsd:enumeration value="OpenSearch"/>
     <xsd:enumeration value="ContentHubIsotope"/>
     <xsd:enumeration value="Identity"/>
     <xsd:enumeration value="outgoingemail"/>
     <xsd:enumeration value="SciApi"/>
     <xsd:enumeration value="SimpleURL"/>
     <xsd:enumeration value="usermobileconfig"/>
     <xsd:enumeration value="Wrapper"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ExternalServiceRegistration">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="namedCredential" minOccurs="0" type="xsd:string"/>
       <xsd:element name="operations" minOccurs="0" maxOccurs="unbounded" type="tns:ExternalServiceOperation"/>
       <xsd:element name="registrationProviderType" minOccurs="0" type="tns:ExternalServiceRegistrationProviderType"/>
       <xsd:element name="schema" minOccurs="0" type="xsd:string"/>
       <xsd:element name="schemaType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="schemaUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="status" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ExternalServiceOperation">
    <xsd:sequence>
     <xsd:element name="active" type="xsd:boolean"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ExternalServiceRegistrationProviderType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="MuleSoft"/>
     <xsd:enumeration value="Custom"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ExternalServicesSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableIgnoreUnsupportedOperations" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FieldRestrictionRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="classification" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="description" type="xsd:string"/>
       <xsd:element name="enforcementType" type="tns:EnforcementType"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="recordFilter" type="xsd:string"/>
       <xsd:element name="targetEntity" type="xsd:string"/>
       <xsd:element name="userCriteria" type="xsd:string"/>
       <xsd:element name="version" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="EnforcementType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Scoping"/>
     <xsd:enumeration value="Restrict"/>
     <xsd:enumeration value="FieldRestrict"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FieldServiceSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="apptAssistantExpiration" minOccurs="0" type="xsd:int"/>
       <xsd:element name="apptAssistantInfoUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="apptAssistantRadiusUnitValue" minOccurs="0" type="tns:ApptAssistantRadiusUnit"/>
       <xsd:element name="apptAssistantRadiusValue" minOccurs="0" type="xsd:int"/>
       <xsd:element name="apptAssistantStatus" minOccurs="0" type="xsd:string"/>
       <xsd:element name="doesAllowEditSaForCrew" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesShareSaParentWoWithAr" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesShareSaWithAr" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWorkOrders" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWorkPlansAutoGeneration" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="fieldServiceNotificationsOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="fieldServiceOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isGeoCodeSyncEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isLocationHistoryEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="o2EngineEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="objectMappingItem" minOccurs="0" maxOccurs="unbounded" type="tns:ObjectMappingItem"/>
       <xsd:element name="optimizationServiceAccess" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="serviceAppointmentsDueDateOffsetOrgValue" minOccurs="0" type="xsd:int"/>
       <xsd:element name="workOrderDurationSource" minOccurs="0" type="tns:WorkOrderDurationSource"/>
       <xsd:element name="workOrderLineItemSearchFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="workOrderSearchFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ApptAssistantRadiusUnit">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Kilometer"/>
     <xsd:enumeration value="Meter"/>
     <xsd:enumeration value="Mile"/>
     <xsd:enumeration value="Yard"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ObjectMappingItem">
    <xsd:sequence>
     <xsd:element name="mappingType" type="tns:MappingType"/>
     <xsd:element name="objectMapping" type="tns:ObjectMapping"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="MappingType">
    <xsd:restriction base="xsd:string"/>
   </xsd:simpleType>
   <xsd:simpleType name="WorkOrderDurationSource">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="WorkType"/>
     <xsd:enumeration value="TotalFromWorkPlan"/>
     <xsd:enumeration value="Custom"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FileUploadAndDownloadSecuritySettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="dispositions" minOccurs="0" maxOccurs="unbounded" type="tns:FileTypeDispositionAssignmentBean"/>
       <xsd:element name="noHtmlUploadAsAttachment" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FileTypeDispositionAssignmentBean">
    <xsd:sequence>
     <xsd:element name="behavior" type="tns:FileDownloadBehavior"/>
     <xsd:element name="fileType" type="tns:FileType"/>
     <xsd:element name="securityRiskFileType" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FileDownloadBehavior">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="DOWNLOAD"/>
     <xsd:enumeration value="EXECUTE_IN_BROWSER"/>
     <xsd:enumeration value="HYBRID"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FileType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="UNKNOWN"/>
     <xsd:enumeration value="PDF"/>
     <xsd:enumeration value="POWER_POINT"/>
     <xsd:enumeration value="POWER_POINT_X"/>
     <xsd:enumeration value="POWER_POINT_M"/>
     <xsd:enumeration value="POWER_POINT_T"/>
     <xsd:enumeration value="WORD"/>
     <xsd:enumeration value="WORD_X"/>
     <xsd:enumeration value="WORD_M"/>
     <xsd:enumeration value="WORD_T"/>
     <xsd:enumeration value="PPS"/>
     <xsd:enumeration value="PPSX"/>
     <xsd:enumeration value="EXCEL"/>
     <xsd:enumeration value="EXCEL_X"/>
     <xsd:enumeration value="EXCEL_M"/>
     <xsd:enumeration value="EXCEL_T"/>
     <xsd:enumeration value="GOOGLE_DOCUMENT"/>
     <xsd:enumeration value="GOOGLE_PRESENTATION"/>
     <xsd:enumeration value="GOOGLE_SPREADSHEET"/>
     <xsd:enumeration value="GOOGLE_DRAWING"/>
     <xsd:enumeration value="GOOGLE_FORM"/>
     <xsd:enumeration value="GOOGLE_SCRIPT"/>
     <xsd:enumeration value="LINK"/>
     <xsd:enumeration value="SLIDE"/>
     <xsd:enumeration value="AAC"/>
     <xsd:enumeration value="ACGI"/>
     <xsd:enumeration value="AI"/>
     <xsd:enumeration value="AVI"/>
     <xsd:enumeration value="BMP"/>
     <xsd:enumeration value="BOXNOTE"/>
     <xsd:enumeration value="CSV"/>
     <xsd:enumeration value="EPS"/>
     <xsd:enumeration value="EXE"/>
     <xsd:enumeration value="FLASH"/>
     <xsd:enumeration value="GIF"/>
     <xsd:enumeration value="GZIP"/>
     <xsd:enumeration value="HTM"/>
     <xsd:enumeration value="HTML"/>
     <xsd:enumeration value="HTX"/>
     <xsd:enumeration value="JPEG"/>
     <xsd:enumeration value="JPE"/>
     <xsd:enumeration value="PJP"/>
     <xsd:enumeration value="PJPEG"/>
     <xsd:enumeration value="JFIF"/>
     <xsd:enumeration value="JPG"/>
     <xsd:enumeration value="JS"/>
     <xsd:enumeration value="JSON"/>
     <xsd:enumeration value="MHTM"/>
     <xsd:enumeration value="MHTML"/>
     <xsd:enumeration value="MP3"/>
     <xsd:enumeration value="M4A"/>
     <xsd:enumeration value="M4V"/>
     <xsd:enumeration value="MP4"/>
     <xsd:enumeration value="MPEG"/>
     <xsd:enumeration value="MPG"/>
     <xsd:enumeration value="MOV"/>
     <xsd:enumeration value="MSG"/>
     <xsd:enumeration value="ODP"/>
     <xsd:enumeration value="ODS"/>
     <xsd:enumeration value="ODT"/>
     <xsd:enumeration value="OGV"/>
     <xsd:enumeration value="PNG"/>
     <xsd:enumeration value="PSD"/>
     <xsd:enumeration value="RTF"/>
     <xsd:enumeration value="QUIPDOC"/>
     <xsd:enumeration value="QUIPSHEET"/>
     <xsd:enumeration value="QUIPCHAT"/>
     <xsd:enumeration value="QUIPSLIDES"/>
     <xsd:enumeration value="QUIPTEMPLATE"/>
     <xsd:enumeration value="SHTM"/>
     <xsd:enumeration value="SHTML"/>
     <xsd:enumeration value="SNOTE"/>
     <xsd:enumeration value="MCONTENT"/>
     <xsd:enumeration value="STYPI"/>
     <xsd:enumeration value="SVG"/>
     <xsd:enumeration value="SVGZ"/>
     <xsd:enumeration value="JPGZ"/>
     <xsd:enumeration value="TEXT"/>
     <xsd:enumeration value="THTML"/>
     <xsd:enumeration value="USDZ"/>
     <xsd:enumeration value="VISIO"/>
     <xsd:enumeration value="VTT"/>
     <xsd:enumeration value="WMV"/>
     <xsd:enumeration value="WRF"/>
     <xsd:enumeration value="XML"/>
     <xsd:enumeration value="ZIP"/>
     <xsd:enumeration value="XZIP"/>
     <xsd:enumeration value="WMA"/>
     <xsd:enumeration value="XSN"/>
     <xsd:enumeration value="INSIGHT"/>
     <xsd:enumeration value="TRTF"/>
     <xsd:enumeration value="TXML"/>
     <xsd:enumeration value="WEBVIEW"/>
     <xsd:enumeration value="RFC822"/>
     <xsd:enumeration value="ASF"/>
     <xsd:enumeration value="DWG"/>
     <xsd:enumeration value="JAR"/>
     <xsd:enumeration value="XJS"/>
     <xsd:enumeration value="OPX"/>
     <xsd:enumeration value="XPSD"/>
     <xsd:enumeration value="TIF"/>
     <xsd:enumeration value="TIFF"/>
     <xsd:enumeration value="WAV"/>
     <xsd:enumeration value="CSS"/>
     <xsd:enumeration value="THUMB720BY480"/>
     <xsd:enumeration value="THUMB240BY180"/>
     <xsd:enumeration value="THUMB120BY90"/>
     <xsd:enumeration value="ALLTHUMBS"/>
     <xsd:enumeration value="PAGED_FLASH"/>
     <xsd:enumeration value="XMOB"/>
     <xsd:enumeration value="PACK"/>
     <xsd:enumeration value="C"/>
     <xsd:enumeration value="CPP"/>
     <xsd:enumeration value="WORDT"/>
     <xsd:enumeration value="INI"/>
     <xsd:enumeration value="JAVA"/>
     <xsd:enumeration value="LOG"/>
     <xsd:enumeration value="POWER_POINTT"/>
     <xsd:enumeration value="SQL"/>
     <xsd:enumeration value="XHTML"/>
     <xsd:enumeration value="EXCELT"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FilesConnectSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableContentHubAllowed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContentHubCvtLinksAllowed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContentHubEOSearchLayout" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlexiPage">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="flexiPageRegions" minOccurs="0" maxOccurs="unbounded" type="tns:FlexiPageRegion"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="parentFlexiPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="platformActionlist" minOccurs="0" type="tns:PlatformActionList"/>
       <xsd:element name="quickActionList" minOccurs="0" type="tns:QuickActionList"/>
       <xsd:element name="sobjectType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="template" type="tns:FlexiPageTemplateInstance"/>
       <xsd:element name="type" type="tns:FlexiPageType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlexiPageRegion">
    <xsd:sequence>
     <xsd:element name="appendable" minOccurs="0" type="tns:RegionFlagStatus"/>
     <xsd:element name="itemInstances" minOccurs="0" maxOccurs="unbounded" type="tns:ItemInstance"/>
     <xsd:element name="mode" minOccurs="0" type="tns:FlexiPageRegionMode"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="prependable" minOccurs="0" type="tns:RegionFlagStatus"/>
     <xsd:element name="replaceable" minOccurs="0" type="tns:RegionFlagStatus"/>
     <xsd:element name="type" type="tns:FlexiPageRegionType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="RegionFlagStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="disabled"/>
     <xsd:enumeration value="enabled"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ItemInstance">
    <xsd:sequence>
     <xsd:element name="componentInstance" minOccurs="0" type="tns:ComponentInstance"/>
     <xsd:element name="fieldInstance" minOccurs="0" type="tns:FieldInstance"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ComponentInstance">
    <xsd:sequence>
     <xsd:element name="componentInstanceProperties" minOccurs="0" maxOccurs="unbounded" type="tns:ComponentInstanceProperty"/>
     <xsd:element name="componentName" type="xsd:string"/>
     <xsd:element name="identifier" minOccurs="0" type="xsd:string"/>
     <xsd:element name="visibilityRule" minOccurs="0" type="tns:UiFormulaRule"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ComponentInstanceProperty">
    <xsd:sequence>
     <xsd:element name="name" minOccurs="0" type="xsd:string"/>
     <xsd:element name="type" minOccurs="0" type="tns:ComponentInstancePropertyTypeEnum"/>
     <xsd:element name="value" minOccurs="0" type="xsd:string"/>
     <xsd:element name="valueList" minOccurs="0" type="tns:ComponentInstancePropertyList"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ComponentInstancePropertyTypeEnum">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="decorator"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ComponentInstancePropertyList">
    <xsd:sequence>
     <xsd:element name="valueListItems" minOccurs="0" maxOccurs="unbounded" type="tns:ComponentInstancePropertyListItem"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ComponentInstancePropertyListItem">
    <xsd:sequence>
     <xsd:element name="value" minOccurs="0" type="xsd:string"/>
     <xsd:element name="visibilityRule" minOccurs="0" type="tns:UiFormulaRule"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="UiFormulaRule">
    <xsd:sequence>
     <xsd:element name="booleanFilter" minOccurs="0" type="xsd:string"/>
     <xsd:element name="criteria" minOccurs="0" maxOccurs="unbounded" type="tns:UiFormulaCriterion"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="UiFormulaCriterion">
    <xsd:sequence>
     <xsd:element name="leftValue" type="xsd:string"/>
     <xsd:element name="operator" type="xsd:string"/>
     <xsd:element name="rightValue" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FieldInstance">
    <xsd:sequence>
     <xsd:element name="fieldInstanceProperties" minOccurs="0" maxOccurs="unbounded" type="tns:FieldInstanceProperty"/>
     <xsd:element name="fieldItem" type="xsd:string"/>
     <xsd:element name="identifier" minOccurs="0" type="xsd:string"/>
     <xsd:element name="visibilityRule" minOccurs="0" type="tns:UiFormulaRule"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FieldInstanceProperty">
    <xsd:sequence>
     <xsd:element name="name" minOccurs="0" type="xsd:string"/>
     <xsd:element name="value" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FlexiPageRegionMode">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Append"/>
     <xsd:enumeration value="Prepend"/>
     <xsd:enumeration value="Replace"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FlexiPageRegionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Region"/>
     <xsd:enumeration value="Facet"/>
     <xsd:enumeration value="Background"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="PlatformActionList">
    <xsd:sequence>
     <xsd:element name="actionListContext" type="tns:PlatformActionListContext"/>
     <xsd:element name="platformActionListItems" minOccurs="0" maxOccurs="unbounded" type="tns:PlatformActionListItem"/>
     <xsd:element name="relatedSourceEntity" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="PlatformActionListContext">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ListView"/>
     <xsd:enumeration value="RelatedList"/>
     <xsd:enumeration value="ListViewRecord"/>
     <xsd:enumeration value="RelatedListRecord"/>
     <xsd:enumeration value="Record"/>
     <xsd:enumeration value="FeedElement"/>
     <xsd:enumeration value="Chatter"/>
     <xsd:enumeration value="Global"/>
     <xsd:enumeration value="Flexipage"/>
     <xsd:enumeration value="MruList"/>
     <xsd:enumeration value="MruRow"/>
     <xsd:enumeration value="RecordEdit"/>
     <xsd:enumeration value="Photo"/>
     <xsd:enumeration value="BannerPhoto"/>
     <xsd:enumeration value="ObjectHomeChart"/>
     <xsd:enumeration value="ListViewDefinition"/>
     <xsd:enumeration value="Dockable"/>
     <xsd:enumeration value="Lookup"/>
     <xsd:enumeration value="Assistant"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="PlatformActionListItem">
    <xsd:sequence>
     <xsd:element name="actionName" type="xsd:string"/>
     <xsd:element name="actionType" type="tns:PlatformActionType"/>
     <xsd:element name="sortOrder" type="xsd:int"/>
     <xsd:element name="subtype" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="PlatformActionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="QuickAction"/>
     <xsd:enumeration value="StandardButton"/>
     <xsd:enumeration value="CustomButton"/>
     <xsd:enumeration value="ProductivityAction"/>
     <xsd:enumeration value="ActionLink"/>
     <xsd:enumeration value="InvocableAction"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="QuickActionList">
    <xsd:sequence>
     <xsd:element name="quickActionListItems" minOccurs="0" maxOccurs="unbounded" type="tns:QuickActionListItem"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="QuickActionListItem">
    <xsd:sequence>
     <xsd:element name="quickActionName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlexiPageTemplateInstance">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="properties" minOccurs="0" maxOccurs="unbounded" type="tns:ComponentInstanceProperty"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FlexiPageType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AppPage"/>
     <xsd:enumeration value="ObjectPage"/>
     <xsd:enumeration value="RecordPage"/>
     <xsd:enumeration value="HomePage"/>
     <xsd:enumeration value="MailAppAppPage"/>
     <xsd:enumeration value="CommAppPage"/>
     <xsd:enumeration value="CommForgotPasswordPage"/>
     <xsd:enumeration value="CommLoginPage"/>
     <xsd:enumeration value="CommObjectPage"/>
     <xsd:enumeration value="CommQuickActionCreatePage"/>
     <xsd:enumeration value="CommRecordPage"/>
     <xsd:enumeration value="CommRelatedListPage"/>
     <xsd:enumeration value="CommSearchResultPage"/>
     <xsd:enumeration value="CommGlobalSearchResultPage"/>
     <xsd:enumeration value="CommSelfRegisterPage"/>
     <xsd:enumeration value="CommThemeLayoutPage"/>
     <xsd:enumeration value="UtilityBar"/>
     <xsd:enumeration value="RecordPreview"/>
     <xsd:enumeration value="EmbeddedServicePage"/>
     <xsd:enumeration value="CommCheckoutPage"/>
     <xsd:enumeration value="CommOrderConfirmationPage"/>
     <xsd:enumeration value="CommFlowPage"/>
     <xsd:enumeration value="EmailTemplatePage"/>
     <xsd:enumeration value="ApplicationLayout"/>
     <xsd:enumeration value="CommNoSearchResultsPage"/>
     <xsd:enumeration value="EmailContentPage"/>
     <xsd:enumeration value="ServiceDocument"/>
     <xsd:enumeration value="LandingPage"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="Flow">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionCalls" minOccurs="0" maxOccurs="unbounded" type="tns:FlowActionCall"/>
       <xsd:element name="apexPluginCalls" minOccurs="0" maxOccurs="unbounded" type="tns:FlowApexPluginCall"/>
       <xsd:element name="apiVersion" minOccurs="0" type="xsd:double" nillable="true"/>
       <xsd:element name="assignments" minOccurs="0" maxOccurs="unbounded" type="tns:FlowAssignment"/>
       <xsd:element name="choices" minOccurs="0" maxOccurs="unbounded" type="tns:FlowChoice"/>
       <xsd:element name="collectionProcessors" minOccurs="0" maxOccurs="unbounded" type="tns:FlowCollectionProcessor"/>
       <xsd:element name="constants" minOccurs="0" maxOccurs="unbounded" type="tns:FlowConstant"/>
       <xsd:element name="decisions" minOccurs="0" maxOccurs="unbounded" type="tns:FlowDecision"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="dynamicChoiceSets" minOccurs="0" maxOccurs="unbounded" type="tns:FlowDynamicChoiceSet"/>
       <xsd:element name="formulas" minOccurs="0" maxOccurs="unbounded" type="tns:FlowFormula"/>
       <xsd:element name="interviewLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isAdditionalPermissionRequiredToRun" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isTemplate" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="loops" minOccurs="0" maxOccurs="unbounded" type="tns:FlowLoop"/>
       <xsd:element name="orchestratedStages" minOccurs="0" maxOccurs="unbounded" type="tns:FlowOrchestratedStage"/>
       <xsd:element name="processMetadataValues" minOccurs="0" maxOccurs="unbounded" type="tns:FlowMetadataValue"/>
       <xsd:element name="processType" minOccurs="0" type="tns:FlowProcessType"/>
       <xsd:element name="recordCreates" minOccurs="0" maxOccurs="unbounded" type="tns:FlowRecordCreate"/>
       <xsd:element name="recordDeletes" minOccurs="0" maxOccurs="unbounded" type="tns:FlowRecordDelete"/>
       <xsd:element name="recordLookups" minOccurs="0" maxOccurs="unbounded" type="tns:FlowRecordLookup"/>
       <xsd:element name="recordUpdates" minOccurs="0" maxOccurs="unbounded" type="tns:FlowRecordUpdate"/>
       <xsd:element name="runInMode" minOccurs="0" type="tns:FlowRunInMode"/>
       <xsd:element name="screens" minOccurs="0" maxOccurs="unbounded" type="tns:FlowScreen"/>
       <xsd:element name="stages" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStage"/>
       <xsd:element name="start" minOccurs="0" type="tns:FlowStart"/>
       <xsd:element name="startElementReference" minOccurs="0" type="xsd:string"/>
       <xsd:element name="status" minOccurs="0" type="tns:FlowVersionStatus"/>
       <xsd:element name="steps" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStep"/>
       <xsd:element name="subflows" minOccurs="0" maxOccurs="unbounded" type="tns:FlowSubflow"/>
       <xsd:element name="textTemplates" minOccurs="0" maxOccurs="unbounded" type="tns:FlowTextTemplate"/>
       <xsd:element name="variables" minOccurs="0" maxOccurs="unbounded" type="tns:FlowVariable"/>
       <xsd:element name="waits" minOccurs="0" maxOccurs="unbounded" type="tns:FlowWait"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowActionCall">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="actionName" type="xsd:string"/>
       <xsd:element name="actionType" type="tns:InvocableActionType"/>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="dataTypeMappings" minOccurs="0" maxOccurs="unbounded" type="tns:FlowDataTypeMapping"/>
       <xsd:element name="faultConnector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="flowTransactionModel" minOccurs="0" type="tns:FlowTransactionModel"/>
       <xsd:element name="inputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowActionCallInputParameter"/>
       <xsd:element name="outputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowActionCallOutputParameter"/>
       <xsd:element name="storeOutputAutomatically" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowNode">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="elementSubtype" minOccurs="0" type="tns:FlowElementSubtype"/>
       <xsd:element name="label" minOccurs="0" type="xsd:string"/>
       <xsd:element name="locationX" type="xsd:int"/>
       <xsd:element name="locationY" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowElement">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="name" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowBaseElement">
    <xsd:sequence>
     <xsd:element name="processMetadataValues" minOccurs="0" maxOccurs="unbounded" type="tns:FlowMetadataValue"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowMetadataValue">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowElementReferenceOrValue">
    <xsd:sequence>
     <xsd:element name="booleanValue" minOccurs="0" type="xsd:boolean" nillable="true"/>
     <xsd:element name="dateTimeValue" minOccurs="0" type="xsd:dateTime"/>
     <xsd:element name="dateValue" minOccurs="0" type="xsd:date"/>
     <xsd:element name="elementReference" minOccurs="0" type="xsd:string"/>
     <xsd:element name="numberValue" minOccurs="0" type="xsd:double" nillable="true"/>
     <xsd:element name="stringValue" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowActionCallInputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowActionCallOutputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="assignToReference" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowApexPluginCallInputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowApexPluginCallOutputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="assignToReference" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowAssignmentItem">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="assignToReference" type="xsd:string"/>
       <xsd:element name="operator" type="tns:FlowAssignmentOperator"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="FlowAssignmentOperator">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Assign"/>
     <xsd:enumeration value="Add"/>
     <xsd:enumeration value="Subtract"/>
     <xsd:enumeration value="AddItem"/>
     <xsd:enumeration value="RemoveFirst"/>
     <xsd:enumeration value="RemoveBeforeFirst"/>
     <xsd:enumeration value="RemoveAfterFirst"/>
     <xsd:enumeration value="RemoveAll"/>
     <xsd:enumeration value="AddAtStart"/>
     <xsd:enumeration value="RemoveUncommon"/>
     <xsd:enumeration value="AssignCount"/>
     <xsd:enumeration value="RemovePosition"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowChoiceUserInput">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="isRequired" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="promptText" minOccurs="0" type="xsd:string"/>
       <xsd:element name="validationRule" minOccurs="0" type="tns:FlowInputValidationRule"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowInputValidationRule">
    <xsd:sequence>
     <xsd:element name="errorMessage" type="xsd:string"/>
     <xsd:element name="formulaExpression" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowCollectionSortOption">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="doesPutEmptyStringAndNullFirst" type="xsd:boolean"/>
       <xsd:element name="sortField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sortOrder" type="tns:SortOrder"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowCondition">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="leftValueReference" type="xsd:string"/>
       <xsd:element name="operator" type="tns:FlowComparisonOperator"/>
       <xsd:element name="rightValue" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="FlowComparisonOperator">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="EqualTo"/>
     <xsd:enumeration value="NotEqualTo"/>
     <xsd:enumeration value="GreaterThan"/>
     <xsd:enumeration value="LessThan"/>
     <xsd:enumeration value="GreaterThanOrEqualTo"/>
     <xsd:enumeration value="LessThanOrEqualTo"/>
     <xsd:enumeration value="StartsWith"/>
     <xsd:enumeration value="EndsWith"/>
     <xsd:enumeration value="Contains"/>
     <xsd:enumeration value="IsNull"/>
     <xsd:enumeration value="IsChanged"/>
     <xsd:enumeration value="WasSet"/>
     <xsd:enumeration value="WasSelected"/>
     <xsd:enumeration value="WasVisited"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowConnector">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="targetReference" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowDataTypeMapping">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="typeName" type="xsd:string"/>
       <xsd:element name="typeValue" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowInputFieldAssignment">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="field" type="xsd:string"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowOutputFieldAssignment">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="assignToReference" type="xsd:string"/>
       <xsd:element name="field" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowRecordFilter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="field" type="xsd:string"/>
       <xsd:element name="operator" type="tns:FlowRecordFilterOperator"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="FlowRecordFilterOperator">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="EqualTo"/>
     <xsd:enumeration value="NotEqualTo"/>
     <xsd:enumeration value="GreaterThan"/>
     <xsd:enumeration value="LessThan"/>
     <xsd:enumeration value="GreaterThanOrEqualTo"/>
     <xsd:enumeration value="LessThanOrEqualTo"/>
     <xsd:enumeration value="StartsWith"/>
     <xsd:enumeration value="EndsWith"/>
     <xsd:enumeration value="Contains"/>
     <xsd:enumeration value="IsNull"/>
     <xsd:enumeration value="IsChanged"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowScreenFieldInputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowScreenFieldOutputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="assignToReference" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowScreenRule">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="conditionLogic" minOccurs="0" type="xsd:string"/>
       <xsd:element name="conditions" minOccurs="0" maxOccurs="unbounded" type="tns:FlowCondition"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="ruleActions" minOccurs="0" maxOccurs="unbounded" type="tns:FlowScreenRuleAction"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowScreenRuleAction">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="attribute" type="xsd:string"/>
       <xsd:element name="fieldReference" type="xsd:string"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowStageStepAssignee">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="assignee" type="tns:FlowElementReferenceOrValue"/>
       <xsd:element name="assigneeType" type="tns:FlowStageStepAssigneeType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="FlowStageStepAssigneeType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="User"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowStageStepEntryActionInputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowStageStepEntryActionOutputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="assignToReference" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowStageStepExitActionInputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowStageStepExitActionOutputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="assignToReference" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowStageStepInputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowStageStepOutputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="assignToReference" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowSubflowInputAssignment">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowSubflowOutputAssignment">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="assignToReference" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowVisibilityRule">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="conditionLogic" minOccurs="0" type="xsd:string"/>
       <xsd:element name="conditions" minOccurs="0" maxOccurs="unbounded" type="tns:FlowCondition"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowWaitEventInputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowWaitEventOutputParameter">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowBaseElement">
      <xsd:sequence>
       <xsd:element name="assignToReference" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowChoice">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="choiceText" type="xsd:string"/>
       <xsd:element name="dataType" type="tns:FlowDataType"/>
       <xsd:element name="userInput" minOccurs="0" type="tns:FlowChoiceUserInput"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="FlowDataType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Currency"/>
     <xsd:enumeration value="Date"/>
     <xsd:enumeration value="Number"/>
     <xsd:enumeration value="String"/>
     <xsd:enumeration value="Boolean"/>
     <xsd:enumeration value="SObject"/>
     <xsd:enumeration value="DateTime"/>
     <xsd:enumeration value="Picklist"/>
     <xsd:enumeration value="Multipicklist"/>
     <xsd:enumeration value="Apex"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowConstant">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="dataType" type="tns:FlowDataType"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowDynamicChoiceSet">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="dataType" type="tns:FlowDataType"/>
       <xsd:element name="displayField" type="xsd:string"/>
       <xsd:element name="filterLogic" minOccurs="0" type="xsd:string"/>
       <xsd:element name="filters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowRecordFilter"/>
       <xsd:element name="limit" minOccurs="0" type="xsd:int" nillable="true"/>
       <xsd:element name="object" type="xsd:string"/>
       <xsd:element name="outputAssignments" minOccurs="0" maxOccurs="unbounded" type="tns:FlowOutputFieldAssignment"/>
       <xsd:element name="picklistField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="picklistObject" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sortField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sortOrder" minOccurs="0" type="tns:SortOrder"/>
       <xsd:element name="valueField" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowFormula">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="dataType" minOccurs="0" type="tns:FlowDataType"/>
       <xsd:element name="expression" type="xsd:string"/>
       <xsd:element name="scale" minOccurs="0" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowRule">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="conditionLogic" type="xsd:string"/>
       <xsd:element name="conditions" minOccurs="0" maxOccurs="unbounded" type="tns:FlowCondition"/>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="doesRequireRecordChangedToMeetCriteria" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowScheduledPath">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="label" minOccurs="0" type="xsd:string"/>
       <xsd:element name="offsetNumber" type="xsd:int"/>
       <xsd:element name="offsetUnit" type="tns:FlowScheduledPathOffsetUnit"/>
       <xsd:element name="recordField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="timeSource" type="tns:FlowScheduledPathTimeSource"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="FlowScheduledPathOffsetUnit">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Hours"/>
     <xsd:enumeration value="Days"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FlowScheduledPathTimeSource">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="RecordTriggerEvent"/>
     <xsd:enumeration value="RecordField"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowScreenField">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="choiceReferences" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="dataType" minOccurs="0" type="tns:FlowDataType"/>
       <xsd:element name="dataTypeMappings" minOccurs="0" maxOccurs="unbounded" type="tns:FlowDataTypeMapping"/>
       <xsd:element name="defaultSelectedChoiceReference" minOccurs="0" type="xsd:string"/>
       <xsd:element name="defaultValue" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
       <xsd:element name="extensionName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="fieldText" minOccurs="0" type="xsd:string"/>
       <xsd:element name="fieldType" type="tns:FlowScreenFieldType"/>
       <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="tns:FlowScreenField"/>
       <xsd:element name="helpText" minOccurs="0" type="xsd:string"/>
       <xsd:element name="inputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowScreenFieldInputParameter"/>
       <xsd:element name="inputsOnNextNavToAssocScrn" minOccurs="0" type="tns:FlowScreenFieldInputsRevisited"/>
       <xsd:element name="isRequired" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isVisible" minOccurs="0" type="xsd:boolean" nillable="true"/>
       <xsd:element name="objectFieldReference" minOccurs="0" type="xsd:string"/>
       <xsd:element name="outputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowScreenFieldOutputParameter"/>
       <xsd:element name="scale" minOccurs="0" type="xsd:int"/>
       <xsd:element name="storeOutputAutomatically" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="validationRule" minOccurs="0" type="tns:FlowInputValidationRule"/>
       <xsd:element name="visibilityRule" minOccurs="0" type="tns:FlowVisibilityRule"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="FlowScreenFieldType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="DisplayText"/>
     <xsd:enumeration value="InputField"/>
     <xsd:enumeration value="LargeTextArea"/>
     <xsd:enumeration value="PasswordField"/>
     <xsd:enumeration value="RadioButtons"/>
     <xsd:enumeration value="DropdownBox"/>
     <xsd:enumeration value="MultiSelectCheckboxes"/>
     <xsd:enumeration value="MultiSelectPicklist"/>
     <xsd:enumeration value="ComponentInstance"/>
     <xsd:enumeration value="ComponentInput"/>
     <xsd:enumeration value="ComponentChoice"/>
     <xsd:enumeration value="ComponentMultiChoice"/>
     <xsd:enumeration value="ComponentDisplay"/>
     <xsd:enumeration value="RegionContainer"/>
     <xsd:enumeration value="Region"/>
     <xsd:enumeration value="ObjectProvided"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FlowScreenFieldInputsRevisited">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="UseStoredValues"/>
     <xsd:enumeration value="ResetValues"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowStage">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="isActive" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="stageOrder" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowStageStep">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="actionName" type="xsd:string"/>
       <xsd:element name="actionType" type="tns:InvocableActionType"/>
       <xsd:element name="assignees" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStageStepAssignee"/>
       <xsd:element name="entryActionInputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStageStepEntryActionInputParameter"/>
       <xsd:element name="entryActionName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="entryActionOutputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStageStepEntryActionOutputParameter"/>
       <xsd:element name="entryActionType" minOccurs="0" type="tns:InvocableActionType"/>
       <xsd:element name="entryConditionLogic" type="xsd:string"/>
       <xsd:element name="entryConditions" minOccurs="0" maxOccurs="unbounded" type="tns:FlowCondition"/>
       <xsd:element name="exitActionInputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStageStepExitActionInputParameter"/>
       <xsd:element name="exitActionName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="exitActionOutputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStageStepExitActionOutputParameter"/>
       <xsd:element name="exitActionType" minOccurs="0" type="tns:InvocableActionType"/>
       <xsd:element name="inputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStageStepInputParameter"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="outputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStageStepOutputParameter"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="InvocableActionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="apex"/>
     <xsd:enumeration value="chatterPost"/>
     <xsd:enumeration value="contentWorkspaceEnableFolders"/>
     <xsd:enumeration value="emailAlert"/>
     <xsd:enumeration value="emailSimple"/>
     <xsd:enumeration value="externalService"/>
     <xsd:enumeration value="flow"/>
     <xsd:enumeration value="metricRefresh"/>
     <xsd:enumeration value="quickAction"/>
     <xsd:enumeration value="submit"/>
     <xsd:enumeration value="thanks"/>
     <xsd:enumeration value="thunderResponse"/>
     <xsd:enumeration value="createServiceReport"/>
     <xsd:enumeration value="deployOrchestration"/>
     <xsd:enumeration value="createResponseEventAction"/>
     <xsd:enumeration value="sfdcOutputAction"/>
     <xsd:enumeration value="invokeOrchOutputFlow"/>
     <xsd:enumeration value="generateWorkOrders"/>
     <xsd:enumeration value="deactivateSessionPermSet"/>
     <xsd:enumeration value="activateSessionPermSet"/>
     <xsd:enumeration value="aggregateValue"/>
     <xsd:enumeration value="orchestrationTimer"/>
     <xsd:enumeration value="orchestrationDebugLog"/>
     <xsd:enumeration value="choosePricebook"/>
     <xsd:enumeration value="component"/>
     <xsd:enumeration value="liveMessageNotification"/>
     <xsd:enumeration value="scaleCacheAsyncRefresh"/>
     <xsd:enumeration value="skillsBasedRouting"/>
     <xsd:enumeration value="addSkillRequirements"/>
     <xsd:enumeration value="routeWork"/>
     <xsd:enumeration value="createCustomField"/>
     <xsd:enumeration value="assignTrailheadBadge"/>
     <xsd:enumeration value="insightFeedback"/>
     <xsd:enumeration value="publishKnowledgeArticles"/>
     <xsd:enumeration value="routingAddressVerification"/>
     <xsd:enumeration value="assignTargetToSalesCadence"/>
     <xsd:enumeration value="removeTargetFromSalesCadence"/>
     <xsd:enumeration value="modifyCadenceTrackerAttributes"/>
     <xsd:enumeration value="pauseSalesCadenceTracker"/>
     <xsd:enumeration value="resumeSalesCadenceTracker"/>
     <xsd:enumeration value="changeSalesCadenceTargetAssignee"/>
     <xsd:enumeration value="sendSalesCadenceEvent"/>
     <xsd:enumeration value="assignKnowledgeArticles"/>
     <xsd:enumeration value="createDraftFromOnlineKnowledgeArticle"/>
     <xsd:enumeration value="archiveKnowledgeArticles"/>
     <xsd:enumeration value="restoreKnowledgeArticleVersion"/>
     <xsd:enumeration value="customNotificationAction"/>
     <xsd:enumeration value="submitDigitalFormResponse"/>
     <xsd:enumeration value="contactRequestAction"/>
     <xsd:enumeration value="saveAppointment"/>
     <xsd:enumeration value="deleteKnowledgeArticles"/>
     <xsd:enumeration value="submitKnowledgeArticleForTranslation"/>
     <xsd:enumeration value="einsteinEPLitePredictionAction"/>
     <xsd:enumeration value="cartToOrderAction"/>
     <xsd:enumeration value="orderToCartAction"/>
     <xsd:enumeration value="activateOrderAction"/>
     <xsd:enumeration value="refreshActualsCalculation"/>
     <xsd:enumeration value="cancelAppointment"/>
     <xsd:enumeration value="recalculateForecast"/>
     <xsd:enumeration value="getBenefitAndCalculateRebateAmount"/>
     <xsd:enumeration value="upsertCustomRebatePayout"/>
     <xsd:enumeration value="calculateRebateAmountAndUpsertPayout"/>
     <xsd:enumeration value="processRebatesBatchCalculationJob"/>
     <xsd:enumeration value="generateRebatePayoutPeriods"/>
     <xsd:enumeration value="calculateAdvancedAccountForecast"/>
     <xsd:enumeration value="managedContentReleasePublish"/>
     <xsd:enumeration value="editQuipDocument"/>
     <xsd:enumeration value="attachQuipDocumentToRecord"/>
     <xsd:enumeration value="createQuipDocument"/>
     <xsd:enumeration value="createQuipFolder"/>
     <xsd:enumeration value="addUsersToQuipDocument"/>
     <xsd:enumeration value="removeUsersFromQuipDocument"/>
     <xsd:enumeration value="copyQuipDocument"/>
     <xsd:enumeration value="addMessageToQuipDocument"/>
     <xsd:enumeration value="addQuipDocumentToFolder"/>
     <xsd:enumeration value="removeQuipDocumentFromFolder"/>
     <xsd:enumeration value="createQuipChat"/>
     <xsd:enumeration value="addMessageToQuipChat"/>
     <xsd:enumeration value="addUsersToQuipChat"/>
     <xsd:enumeration value="removeUsersFromQuipChat"/>
     <xsd:enumeration value="copyQuipContent"/>
     <xsd:enumeration value="lockQuipDocument"/>
     <xsd:enumeration value="lockQuipSection"/>
     <xsd:enumeration value="quipLivePaste"/>
     <xsd:enumeration value="exportQuipDocumentToPdf"/>
     <xsd:enumeration value="priceCart"/>
     <xsd:enumeration value="cartInitiateAsyncStep"/>
     <xsd:enumeration value="cartCompleteAsyncStep"/>
     <xsd:enumeration value="cancelCartAsyncOperation"/>
     <xsd:enumeration value="cancelFulfillmentOrderItem"/>
     <xsd:enumeration value="createFulfillmentOrder"/>
     <xsd:enumeration value="createInvoiceFromFulfillmentOrder"/>
     <xsd:enumeration value="createFulfillmentOrders"/>
     <xsd:enumeration value="createOrderPaymentSummary"/>
     <xsd:enumeration value="cancelOrderItemSummariesPreview"/>
     <xsd:enumeration value="cancelOrderItemSummariesSubmit"/>
     <xsd:enumeration value="createCreditMemoOrderSummary"/>
     <xsd:enumeration value="ensureFundsOrderSummaryAsync"/>
     <xsd:enumeration value="ensureRefundsOrderSummaryAsync"/>
     <xsd:enumeration value="returnOrderItemSummariesPreview"/>
     <xsd:enumeration value="returnOrderItemSummariesSubmit"/>
     <xsd:enumeration value="createReturnOrder"/>
     <xsd:enumeration value="createOrderSummary"/>
     <xsd:enumeration value="adjustOrderItemSummariesPreview"/>
     <xsd:enumeration value="adjustOrderItemSummariesSubmit"/>
     <xsd:enumeration value="createOrderFromQuote"/>
     <xsd:enumeration value="createOrUpdateAssetFromOrder"/>
     <xsd:enumeration value="createBillingScheduleFromOrderItem"/>
     <xsd:enumeration value="changeFinancePeriodStatus"/>
     <xsd:enumeration value="ociTransferReservation"/>
     <xsd:enumeration value="ociReleaseReservation"/>
     <xsd:enumeration value="ociGetAvailability"/>
     <xsd:enumeration value="ociFulfillReservation"/>
     <xsd:enumeration value="ociCreateReservation"/>
     <xsd:enumeration value="orderRoutingRankByAverageDistance"/>
     <xsd:enumeration value="orderRoutingFindRoutesWithFewestSplits"/>
     <xsd:enumeration value="print"/>
     <xsd:enumeration value="exportSurveyResponses"/>
     <xsd:enumeration value="checkoutSessionAction"/>
     <xsd:enumeration value="checkCartInventoryAction"/>
     <xsd:enumeration value="calcCartTaxesAction"/>
     <xsd:enumeration value="calcCartShipmentAction"/>
     <xsd:enumeration value="calcCartPromotionsAction"/>
     <xsd:enumeration value="sendSurveyInvitation"/>
     <xsd:enumeration value="publishPardotContent"/>
     <xsd:enumeration value="sendAlert"/>
     <xsd:enumeration value="storeReplyRecommendationsFeedback"/>
     <xsd:enumeration value="marketingEmail"/>
     <xsd:enumeration value="updateCheckoutSessionStateAction"/>
     <xsd:enumeration value="massUpdateAccountForecast"/>
     <xsd:enumeration value="massUpdateSalesAgreement"/>
     <xsd:enumeration value="decisionTableAction"/>
     <xsd:enumeration value="createFinancialRecords"/>
     <xsd:enumeration value="addWorkPlans"/>
     <xsd:enumeration value="addWorkSteps"/>
     <xsd:enumeration value="generateWorkPlans"/>
     <xsd:enumeration value="deleteWorkPlans"/>
     <xsd:enumeration value="pardotGetListx"/>
     <xsd:enumeration value="pardotAddToListMembership"/>
     <xsd:enumeration value="getTier"/>
     <xsd:enumeration value="changeTier"/>
     <xsd:enumeration value="changeAllTierOrNone"/>
     <xsd:enumeration value="getPointsBalance"/>
     <xsd:enumeration value="updateAcctMgrTarget"/>
     <xsd:enumeration value="creditPoints"/>
     <xsd:enumeration value="debitPoints"/>
     <xsd:enumeration value="batchJobAction"/>
     <xsd:enumeration value="dataProcessingEngineAction"/>
     <xsd:enumeration value="adjustPointsAction"/>
     <xsd:enumeration value="chat"/>
     <xsd:enumeration value="addMessageToChat"/>
     <xsd:enumeration value="addUsersToChat"/>
     <xsd:enumeration value="cancelRedemption"/>
     <xsd:enumeration value="printServiceDocument"/>
     <xsd:enumeration value="cancelAccrual"/>
     <xsd:enumeration value="addRebateMemberList"/>
     <xsd:enumeration value="saveRecommendationDecision"/>
     <xsd:enumeration value="internalTestAction"/>
     <xsd:enumeration value="getDialerSoftphonePathSuffix"/>
     <xsd:enumeration value="performMultiLevelRollups"/>
     <xsd:enumeration value="rebatesProcessCSV"/>
     <xsd:enumeration value="processMemberBenefitAction"/>
     <xsd:enumeration value="assignMemberTierBenefits"/>
     <xsd:enumeration value="dynamicSendSurveyInvitation"/>
     <xsd:enumeration value="getIntelligentAccountSettingsToken"/>
     <xsd:enumeration value="issueVoucher"/>
     <xsd:enumeration value="setCheckoutDeliveryMethod"/>
     <xsd:enumeration value="refreshDecisionTable"/>
     <xsd:enumeration value="createWorkItem"/>
     <xsd:enumeration value="managedContentVersionPublish"/>
     <xsd:enumeration value="managedContentVersionUnpublish"/>
     <xsd:enumeration value="generateKnowledgeLogData"/>
     <xsd:enumeration value="screenPop"/>
     <xsd:enumeration value="submitFailedRecordsBatchJob"/>
     <xsd:enumeration value="getEligibleProgramRebateTypes"/>
     <xsd:enumeration value="returnReturnOrderItems"/>
     <xsd:enumeration value="slackPostMessage"/>
     <xsd:enumeration value="slackCreateChannel"/>
     <xsd:enumeration value="slackInviteUsersToChannel"/>
     <xsd:enumeration value="slackUserInChannel"/>
     <xsd:enumeration value="slackUserInWorkspace"/>
     <xsd:enumeration value="slackArchiveChannel"/>
     <xsd:enumeration value="slackInviteUserToWorkspace"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowTextTemplate">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="isViewedAsPlainText" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="text" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowVariable">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="apexClass" minOccurs="0" type="xsd:string"/>
       <xsd:element name="dataType" type="tns:FlowDataType"/>
       <xsd:element name="isCollection" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isInput" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isOutput" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="objectType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="scale" minOccurs="0" type="xsd:int"/>
       <xsd:element name="value" minOccurs="0" type="tns:FlowElementReferenceOrValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowWaitEvent">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowElement">
      <xsd:sequence>
       <xsd:element name="conditionLogic" minOccurs="0" type="xsd:string"/>
       <xsd:element name="conditions" minOccurs="0" maxOccurs="unbounded" type="tns:FlowCondition"/>
       <xsd:element name="connector" type="tns:FlowConnector"/>
       <xsd:element name="eventType" type="xsd:string"/>
       <xsd:element name="inputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowWaitEventInputParameter"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="outputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowWaitEventOutputParameter"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="FlowElementSubtype">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="SortCollectionProcessor"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowApexPluginCall">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="apexClass" type="xsd:string"/>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="faultConnector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="inputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowApexPluginCallInputParameter"/>
       <xsd:element name="outputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowApexPluginCallOutputParameter"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowAssignment">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="assignmentItems" minOccurs="0" maxOccurs="unbounded" type="tns:FlowAssignmentItem"/>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowCollectionProcessor">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="collectionProcessorType" type="tns:FlowCollectionProcessorType"/>
       <xsd:element name="collectionReference" type="xsd:string"/>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="limit" minOccurs="0" type="xsd:int" nillable="true"/>
       <xsd:element name="sortOptions" minOccurs="0" maxOccurs="unbounded" type="tns:FlowCollectionSortOption"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="FlowCollectionProcessorType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="SortCollectionProcessor"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowDecision">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="defaultConnector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="defaultConnectorLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="rules" minOccurs="0" maxOccurs="unbounded" type="tns:FlowRule"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowLoop">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="assignNextValueToReference" minOccurs="0" type="xsd:string"/>
       <xsd:element name="collectionReference" type="xsd:string"/>
       <xsd:element name="iterationOrder" minOccurs="0" type="tns:IterationOrder"/>
       <xsd:element name="nextValueConnector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="noMoreValuesConnector" minOccurs="0" type="tns:FlowConnector"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="IterationOrder">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Asc"/>
     <xsd:enumeration value="Desc"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowOrchestratedStage">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="exitActionInputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStageStepExitActionInputParameter"/>
       <xsd:element name="exitActionName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="exitActionOutputParameters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStageStepExitActionOutputParameter"/>
       <xsd:element name="exitActionType" minOccurs="0" type="tns:InvocableActionType"/>
       <xsd:element name="exitConditionLogic" minOccurs="0" type="xsd:string"/>
       <xsd:element name="exitConditions" minOccurs="0" maxOccurs="unbounded" type="tns:FlowCondition"/>
       <xsd:element name="stageSteps" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStageStep"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowRecordCreate">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="assignRecordIdToReference" minOccurs="0" type="xsd:string"/>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="faultConnector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="inputAssignments" minOccurs="0" maxOccurs="unbounded" type="tns:FlowInputFieldAssignment"/>
       <xsd:element name="inputReference" minOccurs="0" type="xsd:string"/>
       <xsd:element name="object" minOccurs="0" type="xsd:string"/>
       <xsd:element name="storeOutputAutomatically" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowRecordDelete">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="faultConnector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="filterLogic" minOccurs="0" type="xsd:string"/>
       <xsd:element name="filters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowRecordFilter"/>
       <xsd:element name="inputReference" minOccurs="0" type="xsd:string"/>
       <xsd:element name="object" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowRecordLookup">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="assignNullValuesIfNoRecordsFound" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="faultConnector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="filterLogic" minOccurs="0" type="xsd:string"/>
       <xsd:element name="filters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowRecordFilter"/>
       <xsd:element name="getFirstRecordOnly" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="object" type="xsd:string"/>
       <xsd:element name="outputAssignments" minOccurs="0" maxOccurs="unbounded" type="tns:FlowOutputFieldAssignment"/>
       <xsd:element name="outputReference" minOccurs="0" type="xsd:string"/>
       <xsd:element name="queriedFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="sortField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sortOrder" minOccurs="0" type="tns:SortOrder"/>
       <xsd:element name="storeOutputAutomatically" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowRecordUpdate">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="faultConnector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="filterLogic" minOccurs="0" type="xsd:string"/>
       <xsd:element name="filters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowRecordFilter"/>
       <xsd:element name="inputAssignments" minOccurs="0" maxOccurs="unbounded" type="tns:FlowInputFieldAssignment"/>
       <xsd:element name="inputReference" minOccurs="0" type="xsd:string"/>
       <xsd:element name="object" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowScreen">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="allowBack" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="allowFinish" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="allowPause" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="tns:FlowScreenField"/>
       <xsd:element name="helpText" minOccurs="0" type="xsd:string"/>
       <xsd:element name="pausedText" minOccurs="0" type="xsd:string"/>
       <xsd:element name="rules" minOccurs="0" maxOccurs="unbounded" type="tns:FlowScreenRule"/>
       <xsd:element name="showFooter" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showHeader" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowStart">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="doesRequireRecordChangedToMeetCriteria" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="filterLogic" minOccurs="0" type="xsd:string"/>
       <xsd:element name="filters" minOccurs="0" maxOccurs="unbounded" type="tns:FlowRecordFilter"/>
       <xsd:element name="object" minOccurs="0" type="xsd:string"/>
       <xsd:element name="objectContainer" minOccurs="0" type="xsd:string"/>
       <xsd:element name="recordTriggerType" minOccurs="0" type="tns:RecordTriggerType"/>
       <xsd:element name="schedule" minOccurs="0" type="tns:FlowSchedule"/>
       <xsd:element name="scheduledPaths" minOccurs="0" maxOccurs="unbounded" type="tns:FlowScheduledPath"/>
       <xsd:element name="triggerType" minOccurs="0" type="tns:FlowTriggerType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="RecordTriggerType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Update"/>
     <xsd:enumeration value="Create"/>
     <xsd:enumeration value="CreateAndUpdate"/>
     <xsd:enumeration value="Delete"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowSchedule">
    <xsd:sequence>
     <xsd:element name="frequency" minOccurs="0" type="tns:FlowStartFrequency"/>
     <xsd:element name="startDate" minOccurs="0" type="xsd:date"/>
     <xsd:element name="startTime" minOccurs="0" type="xsd:time"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FlowStartFrequency">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="OnActivate"/>
     <xsd:enumeration value="Once"/>
     <xsd:enumeration value="Daily"/>
     <xsd:enumeration value="Weekly"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FlowTriggerType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Scheduled"/>
     <xsd:enumeration value="RecordBeforeSave"/>
     <xsd:enumeration value="RecordBeforeDelete"/>
     <xsd:enumeration value="ScheduledJourney"/>
     <xsd:enumeration value="RecordAfterSave"/>
     <xsd:enumeration value="PlatformEvent"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowStep">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="connectors" minOccurs="0" maxOccurs="unbounded" type="tns:FlowConnector"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowSubflow">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="connector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="flowName" type="xsd:string"/>
       <xsd:element name="inputAssignments" minOccurs="0" maxOccurs="unbounded" type="tns:FlowSubflowInputAssignment"/>
       <xsd:element name="outputAssignments" minOccurs="0" maxOccurs="unbounded" type="tns:FlowSubflowOutputAssignment"/>
       <xsd:element name="storeOutputAutomatically" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowWait">
    <xsd:complexContent>
     <xsd:extension base="tns:FlowNode">
      <xsd:sequence>
       <xsd:element name="defaultConnector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="defaultConnectorLabel" type="xsd:string"/>
       <xsd:element name="faultConnector" minOccurs="0" type="tns:FlowConnector"/>
       <xsd:element name="waitEvents" minOccurs="0" maxOccurs="unbounded" type="tns:FlowWaitEvent"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="FlowTransactionModel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Automatic"/>
     <xsd:enumeration value="NewTransaction"/>
     <xsd:enumeration value="CurrentTransaction"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FlowRunInMode">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="DefaultMode"/>
     <xsd:enumeration value="SystemModeWithSharing"/>
     <xsd:enumeration value="SystemModeWithoutSharing"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FlowVersionStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Active"/>
     <xsd:enumeration value="Draft"/>
     <xsd:enumeration value="Obsolete"/>
     <xsd:enumeration value="InvalidDraft"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FlowCategory">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="flowCategoryItems" minOccurs="0" maxOccurs="unbounded" type="tns:FlowCategoryItems"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowCategoryItems">
    <xsd:sequence>
     <xsd:element name="flow" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowDefinition">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="activeVersionNumber" minOccurs="0" type="xsd:int"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FlowSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="canDebugFlowAsAnotherUser" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesEnforceApexCpuTimeLimit" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesFormulaEnforceDataAccess" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesFormulaGenerateHtmlOutput" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFlowBREncodedFixEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFlowCustomPropertyEditor" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFlowDeployAsActiveEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFlowFieldFilterEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFlowFormulasFixEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFlowInterviewSharingEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFlowNullPreviousValueFix" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFlowPauseEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFlowUseApexExceptionEmail" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLightningRuntimeEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isAccessToInvokedApexRequired" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isApexPluginAccessModifierRespected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isEnhancedFlowListViewVisible" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isFlowApexContextRetired" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isManageFlowRequiredForAutomationCharts" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isTimeResumedInSameRunContext" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Folder">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="accessType" minOccurs="0" type="tns:FolderAccessTypes"/>
       <xsd:element name="folderShares" minOccurs="0" maxOccurs="unbounded" type="tns:FolderShare"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="publicFolderAccess" minOccurs="0" type="tns:PublicFolderAccess"/>
       <xsd:element name="sharedTo" minOccurs="0" type="tns:SharedTo"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="FolderAccessTypes">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Shared"/>
     <xsd:enumeration value="Public"/>
     <xsd:enumeration value="Hidden"/>
     <xsd:enumeration value="PublicInternal"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FolderShare">
    <xsd:sequence>
     <xsd:element name="accessLevel" type="tns:FolderShareAccessLevel"/>
     <xsd:element name="sharedTo" type="xsd:string"/>
     <xsd:element name="sharedToType" type="tns:FolderSharedToType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FolderShareAccessLevel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="View"/>
     <xsd:enumeration value="EditAllContents"/>
     <xsd:enumeration value="Manage"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FolderSharedToType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Group"/>
     <xsd:enumeration value="Role"/>
     <xsd:enumeration value="RoleAndSubordinates"/>
     <xsd:enumeration value="RoleAndSubordinatesInternal"/>
     <xsd:enumeration value="Manager"/>
     <xsd:enumeration value="ManagerAndSubordinatesInternal"/>
     <xsd:enumeration value="Organization"/>
     <xsd:enumeration value="Territory"/>
     <xsd:enumeration value="TerritoryAndSubordinates"/>
     <xsd:enumeration value="AllPrmUsers"/>
     <xsd:enumeration value="User"/>
     <xsd:enumeration value="PartnerUser"/>
     <xsd:enumeration value="AllCspUsers"/>
     <xsd:enumeration value="CustomerPortalUser"/>
     <xsd:enumeration value="PortalRole"/>
     <xsd:enumeration value="PortalRoleAndSubordinates"/>
     <xsd:enumeration value="ChannelProgramGroup"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="PublicFolderAccess">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ReadOnly"/>
     <xsd:enumeration value="ReadWrite"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DashboardFolder">
    <xsd:complexContent>
     <xsd:extension base="tns:Folder">
      <xsd:sequence/>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DocumentFolder">
    <xsd:complexContent>
     <xsd:extension base="tns:Folder">
      <xsd:sequence/>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EmailFolder">
    <xsd:complexContent>
     <xsd:extension base="tns:Folder">
      <xsd:sequence/>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EmailTemplateFolder">
    <xsd:complexContent>
     <xsd:extension base="tns:Folder">
      <xsd:sequence/>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ReportFolder">
    <xsd:complexContent>
     <xsd:extension base="tns:Folder">
      <xsd:sequence/>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ForecastingObjectListSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="forecastingTypeObjectListSettings" minOccurs="0" maxOccurs="unbounded" type="tns:ForecastingTypeObjectListSettings"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ForecastingTypeObjectListSettings">
    <xsd:sequence>
     <xsd:element name="forecastingObjectListLabelMappings" minOccurs="0" maxOccurs="unbounded" type="tns:ForecastingObjectListLabelMapping"/>
     <xsd:element name="forecastingObjectListSelectedSettings" type="tns:ForecastingObjectListSelectedSettings"/>
     <xsd:element name="forecastingObjectListUnselectedSettings" type="tns:ForecastingObjectListUnselectedSettings"/>
     <xsd:element name="forecastingTypeDeveloperName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ForecastingObjectListLabelMapping">
    <xsd:sequence>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ForecastingObjectListSelectedSettings">
    <xsd:sequence>
     <xsd:element name="field" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ForecastingObjectListUnselectedSettings">
    <xsd:sequence>
     <xsd:element name="field" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ForecastingSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="defaultToPersonalCurrency" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableForecasts" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="forecastingCategoryMappings" minOccurs="0" maxOccurs="unbounded" type="tns:ForecastingCategoryMapping"/>
       <xsd:element name="forecastingDisplayedFamilySettings" minOccurs="0" maxOccurs="unbounded" type="tns:ForecastingDisplayedFamilySettings"/>
       <xsd:element name="forecastingTypeSettings" minOccurs="0" maxOccurs="unbounded" type="tns:ForecastingTypeSettings"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ForecastingCategoryMapping">
    <xsd:sequence>
     <xsd:element name="forecastingItemCategoryApiName" type="xsd:string"/>
     <xsd:element name="weightedSourceCategories" minOccurs="0" maxOccurs="unbounded" type="tns:WeightedSourceCategory"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WeightedSourceCategory">
    <xsd:sequence>
     <xsd:element name="sourceCategoryApiName" type="xsd:string"/>
     <xsd:element name="weight" type="xsd:double"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ForecastingDisplayedFamilySettings">
    <xsd:sequence>
     <xsd:element name="productFamily" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ForecastingTypeSettings">
    <xsd:sequence>
     <xsd:element name="active" type="xsd:boolean"/>
     <xsd:element name="adjustmentsSettings" type="tns:AdjustmentsSettings"/>
     <xsd:element name="displayedCategoryApiNames" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="forecastRangeSettings" type="tns:ForecastRangeSettings"/>
     <xsd:element name="forecastedCategoryApiNames" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="forecastingDateType" type="tns:ForecastingDateType"/>
     <xsd:element name="hasProductFamily" type="xsd:boolean"/>
     <xsd:element name="isAmount" type="xsd:boolean"/>
     <xsd:element name="isAvailable" type="xsd:boolean"/>
     <xsd:element name="isQuantity" type="xsd:boolean"/>
     <xsd:element name="managerAdjustableCategoryApiNames" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="masterLabel" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="opportunityListFieldsLabelMappings" minOccurs="0" maxOccurs="unbounded" type="tns:OpportunityListFieldsLabelMapping"/>
     <xsd:element name="opportunityListFieldsSelectedSettings" type="tns:OpportunityListFieldsSelectedSettings"/>
     <xsd:element name="opportunityListFieldsUnselectedSettings" type="tns:OpportunityListFieldsUnselectedSettings"/>
     <xsd:element name="opportunitySplitName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="ownerAdjustableCategoryApiNames" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="quotasSettings" type="tns:QuotasSettings"/>
     <xsd:element name="territory2ModelName" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AdjustmentsSettings">
    <xsd:sequence>
     <xsd:element name="enableAdjustments" type="xsd:boolean"/>
     <xsd:element name="enableOwnerAdjustments" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ForecastRangeSettings">
    <xsd:sequence>
     <xsd:element name="beginning" type="xsd:int"/>
     <xsd:element name="displaying" type="xsd:int"/>
     <xsd:element name="periodType" type="tns:PeriodTypes"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="PeriodTypes">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Month"/>
     <xsd:enumeration value="Quarter"/>
     <xsd:enumeration value="Week"/>
     <xsd:enumeration value="Year"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ForecastingDateType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="OpportunityCloseDate"/>
     <xsd:enumeration value="ProductDate"/>
     <xsd:enumeration value="ScheduleDate"/>
     <xsd:enumeration value="OLIMeasureCloseDateOnly"/>
     <xsd:enumeration value="ProductDateOnly"/>
     <xsd:enumeration value="ScheduleDateOnly"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="OpportunityListFieldsLabelMapping">
    <xsd:sequence>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="OpportunityListFieldsSelectedSettings">
    <xsd:sequence>
     <xsd:element name="field" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="OpportunityListFieldsUnselectedSettings">
    <xsd:sequence>
     <xsd:element name="field" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="QuotasSettings">
    <xsd:sequence>
     <xsd:element name="showQuotas" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ForecastingType">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="amount" type="xsd:boolean"/>
       <xsd:element name="dateType" type="xsd:string"/>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="hasProductFamily" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="opportunitySplitType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="quantity" type="xsd:boolean"/>
       <xsd:element name="roleType" type="xsd:string"/>
       <xsd:element name="territory2Model" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FormulaSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableDSTAwareDatevalue" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="GatewayProviderPaymentMethodType">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="comments" minOccurs="0" type="xsd:string"/>
       <xsd:element name="gtwyProviderPaymentMethodType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="paymentGatewayProvider" minOccurs="0" type="xsd:string"/>
       <xsd:element name="paymentMethodType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="recordType" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="GlobalValueSet">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="customValue" minOccurs="0" maxOccurs="unbounded" type="tns:CustomValue"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="sorted" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="GlobalValueSetTranslation">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="valueTranslation" minOccurs="0" maxOccurs="unbounded" type="tns:ValueTranslation"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ValueTranslation">
    <xsd:sequence>
     <xsd:element name="masterLabel" type="xsd:string"/>
     <xsd:element name="translation" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="GoogleAppsSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableGmailButtons" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGmailButtonsAndLinks" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGmailLinks" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGoogleDocs" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGoogleDocsTab" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGoogleTalk" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="googleAppsDomain" minOccurs="0" type="xsd:string"/>
       <xsd:element name="googleAppsDomainLinked" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="googleAppsDomainValidated" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Group">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="doesIncludeBosses" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="name" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="HighVelocitySalesSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableACAutoSendEmail" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableACChangeTargetAssignee" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableACSkipWeekends" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableChgTgtAssigneeUsrPermPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDispositionCategory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEngagementWaveAnalyticsPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHighVelocitySales" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHighVelocitySalesSetup" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOpportunityAttributionPermPref" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="HomePageComponent">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="body" minOccurs="0" type="xsd:string"/>
       <xsd:element name="height" minOccurs="0" type="xsd:int"/>
       <xsd:element name="links" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="page" minOccurs="0" type="xsd:string"/>
       <xsd:element name="pageComponentType" type="tns:PageComponentType"/>
       <xsd:element name="showLabel" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showScrollbars" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="width" minOccurs="0" type="tns:PageComponentWidth"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="PageComponentType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="links"/>
     <xsd:enumeration value="htmlArea"/>
     <xsd:enumeration value="imageOrNote"/>
     <xsd:enumeration value="visualforcePage"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="PageComponentWidth">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="narrow"/>
     <xsd:enumeration value="wide"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="HomePageLayout">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="narrowComponents" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="wideComponents" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="IPAddressRange">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="endIpAddress" type="xsd:string"/>
       <xsd:element name="ipAddressFeature" type="tns:IPAddressFeature"/>
       <xsd:element name="ipAddressUsageScope" type="tns:IPAddressUsageScope"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="startIpAddress" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="IPAddressFeature">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="EmailIpFiltering"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="IPAddressUsageScope">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Exclusion"/>
     <xsd:enumeration value="Inclusion"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="IdeasSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableChatterProfile" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHtmlIdea" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIdeaMultipleCategory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIdeaThemes" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIdeas" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIdeasControllerExtensions" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIdeasReputation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="halfLife" minOccurs="0" type="xsd:double"/>
       <xsd:element name="ideasProfilePage" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="IframeWhiteListUrlSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="iframeWhiteListUrls" minOccurs="0" maxOccurs="unbounded" type="tns:IframeWhiteListUrl"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="IframeWhiteListUrl">
    <xsd:sequence>
     <xsd:element name="context" type="tns:IFrameWhitelistContext"/>
     <xsd:element name="url" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="IFrameWhitelistContext">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="VisualforcePages"/>
     <xsd:enumeration value="Surveys"/>
     <xsd:enumeration value="EmbeddedService"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="InboundNetworkConnection">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="connectionType" type="tns:ExternalConnectionType"/>
       <xsd:element name="description" type="xsd:string"/>
       <xsd:element name="inboundNetworkConnProperties" minOccurs="0" maxOccurs="unbounded" type="tns:InboundNetworkConnProperty"/>
       <xsd:element name="isActive" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="status" type="tns:ExternalConnectionStatus"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ExternalConnectionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AwsPrivateLink"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="InboundNetworkConnProperty">
    <xsd:sequence>
     <xsd:element name="propertyName" type="tns:InboundConnPropertyName"/>
     <xsd:element name="propertyValue" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="InboundConnPropertyName">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Region"/>
     <xsd:enumeration value="AwsVpcEndpointId"/>
     <xsd:enumeration value="SourceIpRanges"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ExternalConnectionStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Unprovisioned"/>
     <xsd:enumeration value="Allocating"/>
     <xsd:enumeration value="PendingAcceptance"/>
     <xsd:enumeration value="PendingActivation"/>
     <xsd:enumeration value="RejectedRemotely"/>
     <xsd:enumeration value="DeletedRemotely"/>
     <xsd:enumeration value="TeardownInProgress"/>
     <xsd:enumeration value="Ready"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="IndustriesManufacturingSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableIndManufacturing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIndustriesMfgAccountForecast" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIndustriesMfgAdvForecast" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIndustriesMfgIAS" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIndustriesMfgTargets" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="IndustriesSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="allowMultipleProducersToWorkOnSamePolicy" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="captureResourceUtilizationOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="createCustomerPropertyFromLAProperty" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="createFSCAssetFromLAAsset" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="createFSCAssetFromLAProperty" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="createFSCLiabilityFromLAFinancial" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="createFSCLiabilityFromLALiability" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="createFinancialAccountFromLAAsset" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="createFinancialAccountFromLALiability" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="createFinancialAccountsFromLAFinancials" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="createFinancialAccountsFromLAProperty" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAccessToMasterListOfCoverageTypes" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAccountScoreEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableBlockResourceAvailabilityOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableBusinessMessenger" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCalculationUsingParentPolicyOnly" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableClaimMgmt" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableClinicalDataModel" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCompliantDataSharingForAccount" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCompliantDataSharingForFinancialDeal" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCompliantDataSharingForInteraction" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCompliantDataSharingForInteractionSummary" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCompliantDataSharingForOpportunity" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDealManagement" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEinsteinDocReader" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEinsteinVisits" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEinsteinVisitsED" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEventManagementOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEventWriteOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFSCInsuranceReport" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFinancialDealRoleHierarchy" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHCReferralScoring" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIndustriesAssessment" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIndustriesRebates" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInteractionRoleHierarchy" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInteractionSummaryPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInteractionSummaryRoleHierarchy" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableManyToManyRelationships" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMedicalDeviceEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMortgageRlaTotalsOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMultiResourceOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMultipleCareProgramEnrolleeOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableObjectDetection" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOverbookingOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePatientAppointmentSchedulingOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePolicyAdministration" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableProviderSearchSyncOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRBLUsingCalcService" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRecordRollup" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableReferralScoring" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSentimentAnalysis" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSmartTags" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTextExtract" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTopicOrTemplate" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTopicTimeSlot" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableVisitCalendarSync" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableVisitInventoryEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="loanApplicantAddressAutoCreation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="loanApplicantAutoCreation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="policyBasedSchedulingOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="transformRBLtoDPE" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="InstalledPackage">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="activateRSS" type="xsd:boolean"/>
       <xsd:element name="password" minOccurs="0" type="xsd:string"/>
       <xsd:element name="versionNumber" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="InventorySettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableOCIB2CIntegration" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOmniChannelInventory" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="InvocableActionSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="isPartialSaveAllowed" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="IoTSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableIoT" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIoTInsightsPilot" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIoTUsageEmail" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="IsvHammerSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableIsvHammerSubIsOptedOut" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="KeywordList">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="keywords" minOccurs="0" maxOccurs="unbounded" type="tns:Keyword"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Keyword">
    <xsd:sequence>
     <xsd:element name="keyword" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="KnowledgeSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="answers" minOccurs="0" type="tns:KnowledgeAnswerSettings"/>
       <xsd:element name="cases" minOccurs="0" type="tns:KnowledgeCaseSettings"/>
       <xsd:element name="defaultLanguage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="enableChatterQuestionKBDeflection" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCreateEditOnArticlesTab" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableExternalMediaContent" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableKbStandardSharing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableKnowledge" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableKnowledgeAgentContribution" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableKnowledgeAnswersPromotion" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableKnowledgeArticleTextHighlights" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableKnowledgeCaseRL" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableKnowledgeKeywordAutoComplete" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableKnowledgeTitleAutoComplete" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLightningKbAutoLoadRichTextField" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLightningKnowledge" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="languages" minOccurs="0" type="tns:KnowledgeLanguageSettings"/>
       <xsd:element name="showArticleSummariesCustomerPortal" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showArticleSummariesInternalApp" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showArticleSummariesPartnerPortal" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showValidationStatusField" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="suggestedArticles" minOccurs="0" type="tns:KnowledgeSuggestedArticlesSettings"/>
       <xsd:element name="votingEnabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="KnowledgeAnswerSettings">
    <xsd:sequence>
     <xsd:element name="assignTo" minOccurs="0" type="xsd:string"/>
     <xsd:element name="defaultArticleType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="enableArticleCreation" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="KnowledgeCaseSettings">
    <xsd:sequence>
     <xsd:element name="articlePDFCreationProfile" minOccurs="0" type="xsd:string"/>
     <xsd:element name="articlePublicSharingCommunities" minOccurs="0" type="tns:KnowledgeCommunitiesSettings"/>
     <xsd:element name="articlePublicSharingSites" minOccurs="0" type="tns:KnowledgeSitesSettings"/>
     <xsd:element name="articlePublicSharingSitesChatterAnswers" minOccurs="0" type="tns:KnowledgeSitesSettings"/>
     <xsd:element name="assignTo" minOccurs="0" type="xsd:string"/>
     <xsd:element name="customizationClass" minOccurs="0" type="xsd:string"/>
     <xsd:element name="defaultContributionArticleType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="editor" minOccurs="0" type="tns:KnowledgeCaseEditor"/>
     <xsd:element name="enableArticleCreation" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableArticlePublicSharingSites" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableCaseDataCategoryMapping" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="useProfileForPDFCreation" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="KnowledgeCommunitiesSettings">
    <xsd:sequence>
     <xsd:element name="community" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="KnowledgeSitesSettings">
    <xsd:sequence>
     <xsd:element name="site" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="KnowledgeCaseEditor">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="simple"/>
     <xsd:enumeration value="standard"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="KnowledgeLanguageSettings">
    <xsd:sequence>
     <xsd:element name="language" minOccurs="0" maxOccurs="unbounded" type="tns:KnowledgeLanguage"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="KnowledgeLanguage">
    <xsd:sequence>
     <xsd:element name="active" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="defaultAssignee" minOccurs="0" type="xsd:string"/>
     <xsd:element name="defaultAssigneeType" minOccurs="0" type="tns:KnowledgeLanguageLookupValueType"/>
     <xsd:element name="defaultReviewer" minOccurs="0" type="xsd:string"/>
     <xsd:element name="defaultReviewerType" minOccurs="0" type="tns:KnowledgeLanguageLookupValueType"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="KnowledgeLanguageLookupValueType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="User"/>
     <xsd:enumeration value="Queue"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="KnowledgeSuggestedArticlesSettings">
    <xsd:sequence>
     <xsd:element name="caseFields" minOccurs="0" type="tns:KnowledgeCaseFieldsSettings"/>
     <xsd:element name="useSuggestedArticlesForCase" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="workOrderFields" minOccurs="0" type="tns:KnowledgeWorkOrderFieldsSettings"/>
     <xsd:element name="workOrderLineItemFields" minOccurs="0" type="tns:KnowledgeWorkOrderLineItemFieldsSettings"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="KnowledgeCaseFieldsSettings">
    <xsd:sequence>
     <xsd:element name="field" minOccurs="0" maxOccurs="unbounded" type="tns:KnowledgeCaseField"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="KnowledgeCaseField">
    <xsd:sequence>
     <xsd:element name="name" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="KnowledgeWorkOrderFieldsSettings">
    <xsd:sequence>
     <xsd:element name="field" minOccurs="0" maxOccurs="unbounded" type="tns:KnowledgeWorkOrderField"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="KnowledgeWorkOrderField">
    <xsd:sequence>
     <xsd:element name="name" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="KnowledgeWorkOrderLineItemFieldsSettings">
    <xsd:sequence>
     <xsd:element name="field" minOccurs="0" maxOccurs="unbounded" type="tns:KnowledgeWorkOrderLineItemField"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="KnowledgeWorkOrderLineItemField">
    <xsd:sequence>
     <xsd:element name="name" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LanguageSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCanadaIcuFormat" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDataTranslation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEndUserLanguages" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableICULocaleDateFormat" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLocalNamesForStdObjects" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePlatformLanguages" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTranslationWorkbench" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="useLanguageFallback" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Layout">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="customButtons" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="customConsoleComponents" minOccurs="0" type="tns:CustomConsoleComponents"/>
       <xsd:element name="emailDefault" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="excludeButtons" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="feedLayout" minOccurs="0" type="tns:FeedLayout"/>
       <xsd:element name="headers" minOccurs="0" maxOccurs="unbounded" type="tns:LayoutHeader"/>
       <xsd:element name="layoutSections" minOccurs="0" maxOccurs="unbounded" type="tns:LayoutSection"/>
       <xsd:element name="miniLayout" minOccurs="0" type="tns:MiniLayout"/>
       <xsd:element name="multilineLayoutFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="platformActionList" minOccurs="0" type="tns:PlatformActionList"/>
       <xsd:element name="quickActionList" minOccurs="0" type="tns:QuickActionList"/>
       <xsd:element name="relatedContent" minOccurs="0" type="tns:RelatedContent"/>
       <xsd:element name="relatedLists" minOccurs="0" maxOccurs="unbounded" type="tns:RelatedListItem"/>
       <xsd:element name="relatedObjects" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="runAssignmentRulesDefault" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showEmailCheckbox" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showHighlightsPanel" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showInteractionLogPanel" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showKnowledgeComponent" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showRunAssignmentRulesCheckbox" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showSolutionSection" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showSubmitAndAttachButton" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="summaryLayout" minOccurs="0" type="tns:SummaryLayout"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomConsoleComponents">
    <xsd:sequence>
     <xsd:element name="primaryTabComponents" minOccurs="0" type="tns:PrimaryTabComponents"/>
     <xsd:element name="subtabComponents" minOccurs="0" type="tns:SubtabComponents"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PrimaryTabComponents">
    <xsd:sequence>
     <xsd:element name="containers" minOccurs="0" maxOccurs="unbounded" type="tns:Container"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Container">
    <xsd:sequence>
     <xsd:element name="height" minOccurs="0" type="xsd:int"/>
     <xsd:element name="isContainerAutoSizeEnabled" type="xsd:boolean"/>
     <xsd:element name="region" type="xsd:string"/>
     <xsd:element name="sidebarComponents" minOccurs="0" maxOccurs="unbounded" type="tns:SidebarComponent"/>
     <xsd:element name="style" type="xsd:string"/>
     <xsd:element name="unit" type="xsd:string"/>
     <xsd:element name="width" minOccurs="0" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SidebarComponent">
    <xsd:sequence>
     <xsd:element name="componentType" type="xsd:string"/>
     <xsd:element name="createAction" minOccurs="0" type="xsd:string"/>
     <xsd:element name="enableLinking" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="height" minOccurs="0" type="xsd:int"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="lookup" minOccurs="0" type="xsd:string"/>
     <xsd:element name="page" minOccurs="0" type="xsd:string"/>
     <xsd:element name="relatedLists" minOccurs="0" maxOccurs="unbounded" type="tns:RelatedList"/>
     <xsd:element name="unit" minOccurs="0" type="xsd:string"/>
     <xsd:element name="updateAction" minOccurs="0" type="xsd:string"/>
     <xsd:element name="width" minOccurs="0" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RelatedList">
    <xsd:sequence>
     <xsd:element name="hideOnDetail" type="xsd:boolean"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SubtabComponents">
    <xsd:sequence>
     <xsd:element name="containers" minOccurs="0" maxOccurs="unbounded" type="tns:Container"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FeedLayout">
    <xsd:sequence>
     <xsd:element name="autocollapsePublisher" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="compactFeed" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="feedFilterPosition" minOccurs="0" type="tns:FeedLayoutFilterPosition"/>
     <xsd:element name="feedFilters" minOccurs="0" maxOccurs="unbounded" type="tns:FeedLayoutFilter"/>
     <xsd:element name="fullWidthFeed" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="hideSidebar" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="highlightExternalFeedItems" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="leftComponents" minOccurs="0" maxOccurs="unbounded" type="tns:FeedLayoutComponent"/>
     <xsd:element name="rightComponents" minOccurs="0" maxOccurs="unbounded" type="tns:FeedLayoutComponent"/>
     <xsd:element name="useInlineFiltersInConsole" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FeedLayoutFilterPosition">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="CenterDropDown"/>
     <xsd:enumeration value="LeftFixed"/>
     <xsd:enumeration value="LeftFloat"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FeedLayoutFilter">
    <xsd:sequence>
     <xsd:element name="feedFilterName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="feedFilterType" type="tns:FeedLayoutFilterType"/>
     <xsd:element name="feedItemType" minOccurs="0" type="tns:FeedItemType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FeedLayoutFilterType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AllUpdates"/>
     <xsd:enumeration value="FeedItemType"/>
     <xsd:enumeration value="Custom"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FeedLayoutComponent">
    <xsd:sequence>
     <xsd:element name="componentType" type="tns:FeedLayoutComponentType"/>
     <xsd:element name="height" minOccurs="0" type="xsd:int"/>
     <xsd:element name="page" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="FeedLayoutComponentType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="HelpAndToolLinks"/>
     <xsd:enumeration value="CustomButtons"/>
     <xsd:enumeration value="Following"/>
     <xsd:enumeration value="Followers"/>
     <xsd:enumeration value="CustomLinks"/>
     <xsd:enumeration value="Milestones"/>
     <xsd:enumeration value="Topics"/>
     <xsd:enumeration value="CaseUnifiedFiles"/>
     <xsd:enumeration value="Visualforce"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="LayoutHeader">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="PersonalTagging"/>
     <xsd:enumeration value="PublicTagging"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="LayoutSection">
    <xsd:sequence>
     <xsd:element name="customLabel" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="detailHeading" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="editHeading" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="layoutColumns" minOccurs="0" maxOccurs="unbounded" type="tns:LayoutColumn"/>
     <xsd:element name="style" type="tns:LayoutSectionStyle"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LayoutColumn">
    <xsd:sequence>
     <xsd:element name="layoutItems" minOccurs="0" maxOccurs="unbounded" type="tns:LayoutItem"/>
     <xsd:element name="reserved" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LayoutItem">
    <xsd:sequence>
     <xsd:element name="analyticsCloudComponent" minOccurs="0" type="tns:AnalyticsCloudComponentLayoutItem"/>
     <xsd:element name="behavior" minOccurs="0" type="tns:UiBehavior"/>
     <xsd:element name="canvas" minOccurs="0" type="xsd:string"/>
     <xsd:element name="component" minOccurs="0" type="xsd:string"/>
     <xsd:element name="customLink" minOccurs="0" type="xsd:string"/>
     <xsd:element name="emptySpace" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="field" minOccurs="0" type="xsd:string"/>
     <xsd:element name="height" minOccurs="0" type="xsd:int"/>
     <xsd:element name="page" minOccurs="0" type="xsd:string"/>
     <xsd:element name="reportChartComponent" minOccurs="0" type="tns:ReportChartComponentLayoutItem"/>
     <xsd:element name="scontrol" minOccurs="0" type="xsd:string"/>
     <xsd:element name="showLabel" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showScrollbars" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="width" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AnalyticsCloudComponentLayoutItem">
    <xsd:sequence>
     <xsd:element name="assetType" type="xsd:string"/>
     <xsd:element name="devName" type="xsd:string"/>
     <xsd:element name="error" minOccurs="0" type="xsd:string"/>
     <xsd:element name="filter" minOccurs="0" type="xsd:string"/>
     <xsd:element name="height" minOccurs="0" type="xsd:int"/>
     <xsd:element name="hideOnError" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showHeader" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showSharing" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showTitle" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="width" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="UiBehavior">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Edit"/>
     <xsd:enumeration value="Required"/>
     <xsd:enumeration value="Readonly"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ReportChartComponentLayoutItem">
    <xsd:sequence>
     <xsd:element name="cacheData" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="contextFilterableField" minOccurs="0" type="xsd:string"/>
     <xsd:element name="error" minOccurs="0" type="xsd:string"/>
     <xsd:element name="hideOnError" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="includeContext" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="reportName" type="xsd:string"/>
     <xsd:element name="showTitle" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="size" minOccurs="0" type="tns:ReportChartComponentSize"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ReportChartComponentSize">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="SMALL"/>
     <xsd:enumeration value="MEDIUM"/>
     <xsd:enumeration value="LARGE"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="LayoutSectionStyle">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="TwoColumnsTopToBottom"/>
     <xsd:enumeration value="TwoColumnsLeftToRight"/>
     <xsd:enumeration value="OneColumn"/>
     <xsd:enumeration value="CustomLinks"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="MiniLayout">
    <xsd:sequence>
     <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="relatedLists" minOccurs="0" maxOccurs="unbounded" type="tns:RelatedListItem"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RelatedListItem">
    <xsd:sequence>
     <xsd:element name="customButtons" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="excludeButtons" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="relatedList" type="xsd:string"/>
     <xsd:element name="sortField" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sortOrder" minOccurs="0" type="tns:SortOrder"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RelatedContent">
    <xsd:sequence>
     <xsd:element name="relatedContentItems" minOccurs="0" maxOccurs="unbounded" type="tns:RelatedContentItem"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RelatedContentItem">
    <xsd:sequence>
     <xsd:element name="layoutItem" type="tns:LayoutItem"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SummaryLayout">
    <xsd:sequence>
     <xsd:element name="masterLabel" type="xsd:string"/>
     <xsd:element name="sizeX" type="xsd:int"/>
     <xsd:element name="sizeY" minOccurs="0" type="xsd:int"/>
     <xsd:element name="sizeZ" minOccurs="0" type="xsd:int"/>
     <xsd:element name="summaryLayoutItems" minOccurs="0" maxOccurs="unbounded" type="tns:SummaryLayoutItem"/>
     <xsd:element name="summaryLayoutStyle" type="tns:SummaryLayoutStyle"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SummaryLayoutItem">
    <xsd:sequence>
     <xsd:element name="customLink" minOccurs="0" type="xsd:string"/>
     <xsd:element name="field" minOccurs="0" type="xsd:string"/>
     <xsd:element name="posX" type="xsd:int"/>
     <xsd:element name="posY" minOccurs="0" type="xsd:int"/>
     <xsd:element name="posZ" minOccurs="0" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="SummaryLayoutStyle">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Default"/>
     <xsd:enumeration value="QuoteTemplate"/>
     <xsd:enumeration value="DefaultQuoteTemplate"/>
     <xsd:enumeration value="ServiceReportTemplate"/>
     <xsd:enumeration value="ChildServiceReportTemplateStyle"/>
     <xsd:enumeration value="DefaultServiceReportTemplate"/>
     <xsd:enumeration value="CaseInteraction"/>
     <xsd:enumeration value="QuickActionLayoutLeftRight"/>
     <xsd:enumeration value="QuickActionLayoutTopDown"/>
     <xsd:enumeration value="PathAssistant"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="LeadConfigSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="doesEnableLeadConvertDefaultSubjectBlankTaskCreation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesHideOpportunityInConvertLeadWindow" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesPreserveLeadStatus" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesSelectNoOpportunityOnConvertLead" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesTrackHistory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableConversionsOnMobile" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOrgWideMergeAndDelete" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="shouldLeadConvertRequireValidation" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="LeadConvertSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="allowOwnerChange" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="objectMapping" minOccurs="0" maxOccurs="unbounded" type="tns:ObjectMapping"/>
       <xsd:element name="opportunityCreationOptions" minOccurs="0" type="tns:VisibleOrRequired"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="VisibleOrRequired">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="VisibleOptional"/>
     <xsd:enumeration value="VisibleRequired"/>
     <xsd:enumeration value="NotVisible"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="Letterhead">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="available" type="xsd:boolean"/>
       <xsd:element name="backgroundColor" type="xsd:string"/>
       <xsd:element name="bodyColor" type="xsd:string"/>
       <xsd:element name="bottomLine" type="tns:LetterheadLine"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="footer" type="tns:LetterheadHeaderFooter"/>
       <xsd:element name="header" type="tns:LetterheadHeaderFooter"/>
       <xsd:element name="middleLine" type="tns:LetterheadLine"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="topLine" type="tns:LetterheadLine"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="LetterheadLine">
    <xsd:sequence>
     <xsd:element name="color" type="xsd:string"/>
     <xsd:element name="height" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LetterheadHeaderFooter">
    <xsd:sequence>
     <xsd:element name="backgroundColor" type="xsd:string"/>
     <xsd:element name="height" type="xsd:int"/>
     <xsd:element name="horizontalAlignment" minOccurs="0" type="tns:LetterheadHorizontalAlignment"/>
     <xsd:element name="logo" minOccurs="0" type="xsd:string"/>
     <xsd:element name="verticalAlignment" minOccurs="0" type="tns:LetterheadVerticalAlignment"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="LetterheadHorizontalAlignment">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="Left"/>
     <xsd:enumeration value="Center"/>
     <xsd:enumeration value="Right"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="LetterheadVerticalAlignment">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="Top"/>
     <xsd:enumeration value="Middle"/>
     <xsd:enumeration value="Bottom"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="LicenseDefinition">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="aggregationGroup" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isPublished" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="licensedCustomPermissions" minOccurs="0" maxOccurs="unbounded" type="tns:LicensedCustomPermissions"/>
       <xsd:element name="licensingAuthority" type="xsd:string"/>
       <xsd:element name="licensingAuthorityProvider" type="xsd:string"/>
       <xsd:element name="minPlatformVersion" type="xsd:int"/>
       <xsd:element name="origin" type="xsd:string"/>
       <xsd:element name="revision" type="xsd:int"/>
       <xsd:element name="trialLicenseDuration" type="xsd:int"/>
       <xsd:element name="trialLicenseQuantity" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="LicensedCustomPermissions">
    <xsd:sequence>
     <xsd:element name="customPermission" type="xsd:string"/>
     <xsd:element name="licenseDefinition" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LightningBolt">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="category" type="tns:LightningBoltCategory"/>
       <xsd:element name="lightningBoltFeatures" minOccurs="0" maxOccurs="unbounded" type="tns:LightningBoltFeatures"/>
       <xsd:element name="lightningBoltImages" minOccurs="0" maxOccurs="unbounded" type="tns:LightningBoltImages"/>
       <xsd:element name="lightningBoltItems" minOccurs="0" maxOccurs="unbounded" type="tns:LightningBoltItems"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="publisher" type="xsd:string"/>
       <xsd:element name="summary" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="LightningBoltCategory">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Communications"/>
     <xsd:enumeration value="Education"/>
     <xsd:enumeration value="FinancialServices"/>
     <xsd:enumeration value="Government"/>
     <xsd:enumeration value="HealthcareLifeSciences"/>
     <xsd:enumeration value="Manufacturing"/>
     <xsd:enumeration value="Media"/>
     <xsd:enumeration value="Nonprofits"/>
     <xsd:enumeration value="ProfessionalServices"/>
     <xsd:enumeration value="RealEstate"/>
     <xsd:enumeration value="Retail"/>
     <xsd:enumeration value="TravelTransportationHospitality"/>
     <xsd:enumeration value="HighTech"/>
     <xsd:enumeration value="GeneralBusiness"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="LightningBoltFeatures">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="order" type="xsd:int"/>
     <xsd:element name="title" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LightningBoltImages">
    <xsd:sequence>
     <xsd:element name="image" type="xsd:string"/>
     <xsd:element name="order" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LightningBoltItems">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="type" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LightningComponentBundle">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="apiVersion" minOccurs="0" type="xsd:double"/>
       <xsd:element name="capabilities" minOccurs="0" type="tns:Capabilities"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isExplicitImport" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isExposed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="lwcResources" minOccurs="0" type="tns:LwcResources"/>
       <xsd:element name="masterLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="runtimeNamespace" minOccurs="0" type="xsd:string"/>
       <xsd:element name="targetConfigs" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="targets" minOccurs="0" type="tns:Targets"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Capabilities">
    <xsd:sequence>
     <xsd:element name="capability" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LwcResources">
    <xsd:sequence>
     <xsd:element name="lwcResource" minOccurs="0" maxOccurs="unbounded" type="tns:LwcResource"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LwcResource">
    <xsd:sequence>
     <xsd:element name="filePath" type="xsd:string"/>
     <xsd:element name="source" type="xsd:base64Binary"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Targets">
    <xsd:sequence>
     <xsd:element name="target" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LightningExperienceSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="activeThemeName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="enableAccessCheckCrucPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableApiUserLtngOutAccessPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAuraCDNPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAuraSecStaticResCRUCPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFeedbackInMobile" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGoogleSheetsForSfdcEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIE11DeprecationMsgHidden" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIE11LEXCrucPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInAppTooltips" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLEXExtensionComponentCustomization" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLEXExtensionDarkMode" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLEXExtensionInlineEditModifier" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLEXExtensionLinkGrabber" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLEXExtensionRelatedLists" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLEXExtensionRequiredFields" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLEXExtensionTrailhead" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLEXOnIpadEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLexEndUsersNoSwitching" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLightningPrintableView" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNavPersonalizationOptOut" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNoBackgroundNavigations" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableQuip" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRemoveThemeBrandBanner" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableS1BannerPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableS1BrowserEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableS1DesktopEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableS1UiLoggingEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSalesforceNext" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSkypeChatEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSparkAllUsers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSparkConversationEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTryLightningOptOut" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUseS1AlohaDesktop" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUsersAreLightningOnly" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWebExEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWebexAllUsers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isLEXExtensionComponentCustomizationOff" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isLEXExtensionDarkModeOff" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isLEXExtensionLinkGrabberOff" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isLEXExtensionOff" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="LightningExperienceTheme">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="defaultBrandingSet" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="shouldOverrideLoadingImage" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="LightningMessageChannel">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isExposed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="lightningMessageFields" minOccurs="0" maxOccurs="unbounded" type="tns:LightningMessageField"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="LightningMessageField">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="fieldName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LightningOnboardingConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="collaborationGroup" type="xsd:string" nillable="true"/>
       <xsd:element name="customQuestion" minOccurs="0" type="xsd:string"/>
       <xsd:element name="feedbackFormDaysFrequency" type="xsd:int" nillable="true"/>
       <xsd:element name="isCustom" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="promptDelayTime" type="xsd:int" nillable="true"/>
       <xsd:element name="sendFeedbackToSalesforce" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="LiveAgentSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableLiveAgent" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableQuickTextEnabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="LiveChatAgentConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="assignments" minOccurs="0" type="tns:AgentConfigAssignments"/>
       <xsd:element name="autoGreeting" minOccurs="0" type="xsd:string"/>
       <xsd:element name="capacity" minOccurs="0" type="xsd:int"/>
       <xsd:element name="criticalWaitTime" minOccurs="0" type="xsd:int"/>
       <xsd:element name="customAgentName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="enableAgentFileTransfer" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAgentSneakPeek" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAssistanceFlag" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAutoAwayOnDecline" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAutoAwayOnPushTimeout" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableChatConferencing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableChatMonitoring" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableChatTransferToAgent" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableChatTransferToButton" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableChatTransferToSkill" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLogoutSound" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNotifications" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRequestSound" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSneakPeek" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableVisitorBlocking" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWhisperMessage" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="supervisorDefaultAgentStatusFilter" minOccurs="0" type="tns:SupervisorAgentStatusFilter"/>
       <xsd:element name="supervisorDefaultButtonFilter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="supervisorDefaultSkillFilter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="supervisorSkills" minOccurs="0" type="tns:SupervisorAgentConfigSkills"/>
       <xsd:element name="transferableButtons" minOccurs="0" type="tns:AgentConfigButtons"/>
       <xsd:element name="transferableSkills" minOccurs="0" type="tns:AgentConfigSkills"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AgentConfigAssignments">
    <xsd:sequence>
     <xsd:element name="profiles" minOccurs="0" type="tns:AgentConfigProfileAssignments"/>
     <xsd:element name="users" minOccurs="0" type="tns:AgentConfigUserAssignments"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AgentConfigProfileAssignments">
    <xsd:sequence>
     <xsd:element name="profile" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AgentConfigUserAssignments">
    <xsd:sequence>
     <xsd:element name="user" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="SupervisorAgentStatusFilter">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Online"/>
     <xsd:enumeration value="Away"/>
     <xsd:enumeration value="Offline"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="SupervisorAgentConfigSkills">
    <xsd:sequence>
     <xsd:element name="skill" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AgentConfigButtons">
    <xsd:sequence>
     <xsd:element name="button" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AgentConfigSkills">
    <xsd:sequence>
     <xsd:element name="skill" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LiveChatButton">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="animation" minOccurs="0" type="tns:LiveChatButtonPresentation"/>
       <xsd:element name="autoGreeting" minOccurs="0" type="xsd:string"/>
       <xsd:element name="chasitorIdleTimeout" minOccurs="0" type="xsd:int"/>
       <xsd:element name="chasitorIdleTimeoutWarning" minOccurs="0" type="xsd:int"/>
       <xsd:element name="chatPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="customAgentName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="deployments" minOccurs="0" type="tns:LiveChatButtonDeployments"/>
       <xsd:element name="enableQueue" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="inviteEndPosition" minOccurs="0" type="tns:LiveChatButtonInviteEndPosition"/>
       <xsd:element name="inviteImage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="inviteStartPosition" minOccurs="0" type="tns:LiveChatButtonInviteStartPosition"/>
       <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="numberOfReroutingAttempts" minOccurs="0" type="xsd:int"/>
       <xsd:element name="offlineImage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="onlineImage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="optionsCustomRoutingIsEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="optionsHasChasitorIdleTimeout" type="xsd:boolean"/>
       <xsd:element name="optionsHasInviteAfterAccept" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="optionsHasInviteAfterReject" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="optionsHasRerouteDeclinedRequest" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="optionsIsAutoAccept" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="optionsIsInviteAutoRemove" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="overallQueueLength" minOccurs="0" type="xsd:int"/>
       <xsd:element name="perAgentQueueLength" minOccurs="0" type="xsd:int"/>
       <xsd:element name="postChatPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="postChatUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="preChatFormPage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="preChatFormUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="pushTimeOut" minOccurs="0" type="xsd:int"/>
       <xsd:element name="routingType" type="tns:LiveChatButtonRoutingType"/>
       <xsd:element name="site" minOccurs="0" type="xsd:string"/>
       <xsd:element name="skills" minOccurs="0" type="tns:LiveChatButtonSkills"/>
       <xsd:element name="timeToRemoveInvite" minOccurs="0" type="xsd:int"/>
       <xsd:element name="type" type="tns:LiveChatButtonType"/>
       <xsd:element name="windowLanguage" minOccurs="0" type="tns:Language"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="LiveChatButtonPresentation">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Slide"/>
     <xsd:enumeration value="Fade"/>
     <xsd:enumeration value="Appear"/>
     <xsd:enumeration value="Custom"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="LiveChatButtonDeployments">
    <xsd:sequence>
     <xsd:element name="deployment" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="LiveChatButtonInviteEndPosition">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="TopLeft"/>
     <xsd:enumeration value="Top"/>
     <xsd:enumeration value="TopRight"/>
     <xsd:enumeration value="Left"/>
     <xsd:enumeration value="Center"/>
     <xsd:enumeration value="Right"/>
     <xsd:enumeration value="BottomLeft"/>
     <xsd:enumeration value="Bottom"/>
     <xsd:enumeration value="BottomRight"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="LiveChatButtonInviteStartPosition">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="TopLeft"/>
     <xsd:enumeration value="TopLeftTop"/>
     <xsd:enumeration value="Top"/>
     <xsd:enumeration value="TopRightTop"/>
     <xsd:enumeration value="TopRight"/>
     <xsd:enumeration value="TopRightRight"/>
     <xsd:enumeration value="Right"/>
     <xsd:enumeration value="BottomRightRight"/>
     <xsd:enumeration value="BottomRight"/>
     <xsd:enumeration value="BottomRightBottom"/>
     <xsd:enumeration value="Bottom"/>
     <xsd:enumeration value="BottomLeftBottom"/>
     <xsd:enumeration value="BottomLeft"/>
     <xsd:enumeration value="BottomLeftLeft"/>
     <xsd:enumeration value="Left"/>
     <xsd:enumeration value="TopLeftLeft"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="LiveChatButtonRoutingType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Choice"/>
     <xsd:enumeration value="LeastActive"/>
     <xsd:enumeration value="MostAvailable"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="LiveChatButtonSkills">
    <xsd:sequence>
     <xsd:element name="skill" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="LiveChatButtonType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Standard"/>
     <xsd:enumeration value="Invite"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="LiveChatDeployment">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="brandingImage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="connectionTimeoutDuration" minOccurs="0" type="xsd:int"/>
       <xsd:element name="connectionWarningDuration" minOccurs="0" type="xsd:int"/>
       <xsd:element name="displayQueuePosition" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="domainWhiteList" minOccurs="0" type="tns:LiveChatDeploymentDomainWhitelist"/>
       <xsd:element name="enablePrechatApi" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTranscriptSave" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="mobileBrandingImage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="site" minOccurs="0" type="xsd:string"/>
       <xsd:element name="windowTitle" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="LiveChatDeploymentDomainWhitelist">
    <xsd:sequence>
     <xsd:element name="domain" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LiveChatSensitiveDataRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionType" type="tns:SensitiveDataActionType"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="enforceOn" type="xsd:int"/>
       <xsd:element name="isEnabled" type="xsd:boolean"/>
       <xsd:element name="pattern" type="xsd:string"/>
       <xsd:element name="priority" type="xsd:int"/>
       <xsd:element name="replacement" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="SensitiveDataActionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Remove"/>
     <xsd:enumeration value="Replace"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="LiveMessageSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCheckCEUserPerm" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLiveMessage" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MLDataDefinition">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="entityDeveloperName" type="xsd:string"/>
       <xsd:element name="excludedFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="includedFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="joinFields" minOccurs="0" maxOccurs="unbounded" type="tns:MLField"/>
       <xsd:element name="parentDefinitionDevName" type="xsd:string"/>
       <xsd:element name="scoringFilter" minOccurs="0" type="tns:MLFilter"/>
       <xsd:element name="segmentFilter" minOccurs="0" type="tns:MLFilter"/>
       <xsd:element name="trainingFilter" minOccurs="0" type="tns:MLFilter"/>
       <xsd:element name="type" type="tns:MLDataDefinitionType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MLField">
    <xsd:sequence>
     <xsd:element name="entity" type="xsd:string"/>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="relatedField" minOccurs="0" type="tns:MLField"/>
     <xsd:element name="relationType" minOccurs="0" type="tns:MLRelationType"/>
     <xsd:element name="type" type="tns:MLFieldType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="MLRelationType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Inner"/>
     <xsd:enumeration value="Leftouter"/>
     <xsd:enumeration value="Leftinner"/>
     <xsd:enumeration value="Full"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="MLFieldType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Prediction"/>
     <xsd:enumeration value="Pushback"/>
     <xsd:enumeration value="Included"/>
     <xsd:enumeration value="Excluded"/>
     <xsd:enumeration value="Join"/>
     <xsd:enumeration value="Related"/>
     <xsd:enumeration value="Expression"/>
     <xsd:enumeration value="SegmentExpression"/>
     <xsd:enumeration value="TrainingExpression"/>
     <xsd:enumeration value="ScoringExpression"/>
     <xsd:enumeration value="PositiveExpression"/>
     <xsd:enumeration value="NegativeExpression"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="MLFilter">
    <xsd:sequence>
     <xsd:element name="filterName" type="xsd:string"/>
     <xsd:element name="lhFilter" minOccurs="0" type="tns:MLFilter"/>
     <xsd:element name="lhPredictionField" minOccurs="0" type="xsd:string"/>
     <xsd:element name="lhType" minOccurs="0" type="tns:AIValueType"/>
     <xsd:element name="lhUnit" minOccurs="0" type="tns:AIFilterUnit"/>
     <xsd:element name="lhValue" minOccurs="0" type="xsd:string"/>
     <xsd:element name="operation" type="tns:AIFilterOperation"/>
     <xsd:element name="rhFilter" minOccurs="0" type="tns:MLFilter"/>
     <xsd:element name="rhPredictionField" minOccurs="0" type="xsd:string"/>
     <xsd:element name="rhType" minOccurs="0" type="tns:AIValueType"/>
     <xsd:element name="rhUnit" minOccurs="0" type="tns:AIFilterUnit"/>
     <xsd:element name="rhValue" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sortOrder" minOccurs="0" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="AIValueType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Number"/>
     <xsd:enumeration value="String"/>
     <xsd:enumeration value="Boolean"/>
     <xsd:enumeration value="Date"/>
     <xsd:enumeration value="DateTime"/>
     <xsd:enumeration value="Supplier"/>
     <xsd:enumeration value="Currency"/>
     <xsd:enumeration value="Varchar"/>
     <xsd:enumeration value="Comparison"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="AIFilterUnit">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Milliseconds"/>
     <xsd:enumeration value="Seconds"/>
     <xsd:enumeration value="Minutes"/>
     <xsd:enumeration value="Hours"/>
     <xsd:enumeration value="Days"/>
     <xsd:enumeration value="Weeks"/>
     <xsd:enumeration value="Months"/>
     <xsd:enumeration value="Years"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="AIFilterOperation">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="And"/>
     <xsd:enumeration value="Or"/>
     <xsd:enumeration value="Not"/>
     <xsd:enumeration value="LessThan"/>
     <xsd:enumeration value="LessThanOrEqual"/>
     <xsd:enumeration value="GreaterThan"/>
     <xsd:enumeration value="GreaterThanOrEqual"/>
     <xsd:enumeration value="Equals"/>
     <xsd:enumeration value="NotEquals"/>
     <xsd:enumeration value="Add"/>
     <xsd:enumeration value="Subtract"/>
     <xsd:enumeration value="Multiply"/>
     <xsd:enumeration value="Divide"/>
     <xsd:enumeration value="IsNull"/>
     <xsd:enumeration value="IsNotNull"/>
     <xsd:enumeration value="StartsWith"/>
     <xsd:enumeration value="EndsWith"/>
     <xsd:enumeration value="Contains"/>
     <xsd:enumeration value="Concat"/>
     <xsd:enumeration value="DoesNotContain"/>
     <xsd:enumeration value="Between"/>
     <xsd:enumeration value="In"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="MLDataDefinitionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Recipient"/>
     <xsd:enumeration value="Candidate"/>
     <xsd:enumeration value="Interaction"/>
     <xsd:enumeration value="Prediction"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="MLPredictionDefinition">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="aiApplicationDeveloperName" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="masterLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="negativeExpression" minOccurs="0" type="tns:MLFilter"/>
       <xsd:element name="positiveExpression" minOccurs="0" type="tns:MLFilter"/>
       <xsd:element name="predictionField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="priority" minOccurs="0" type="xsd:int" nillable="true"/>
       <xsd:element name="pushbackField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="status" type="tns:MLPredictionDefinitionStatus"/>
       <xsd:element name="type" type="tns:AIPredictionType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="MLPredictionDefinitionStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Enabled"/>
     <xsd:enumeration value="Disabled"/>
     <xsd:enumeration value="Draft"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="AIPredictionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ScoringSpecificOutcome"/>
     <xsd:enumeration value="BinaryClassification"/>
     <xsd:enumeration value="MulticlassClassification"/>
     <xsd:enumeration value="Regression"/>
     <xsd:enumeration value="LanguageDetection"/>
     <xsd:enumeration value="DeepLearningIntentClassification"/>
     <xsd:enumeration value="DeepLearningNameEntityRecognition"/>
     <xsd:enumeration value="GlobalDeepLearningIntentClassification"/>
     <xsd:enumeration value="GlobalDeepLearningNameEntityRecognition"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="MacroSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="contextualMacroFiltering" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAdvancedSearch" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="macrosInFolders" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ManagedContentType">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="managedContentNodeTypes" minOccurs="0" maxOccurs="unbounded" type="tns:ManagedContentNodeType"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ManagedContentNodeType">
    <xsd:sequence>
     <xsd:element name="helpText" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isLocalizable" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="isRequired" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="nodeLabel" type="xsd:string"/>
     <xsd:element name="nodeName" type="xsd:string"/>
     <xsd:element name="nodeType" type="tns:MCNodeType"/>
     <xsd:element name="placeholderText" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="MCNodeType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="TEXT"/>
     <xsd:enumeration value="MTEXT"/>
     <xsd:enumeration value="RTE"/>
     <xsd:enumeration value="IMG"/>
     <xsd:enumeration value="NAMEFIELD"/>
     <xsd:enumeration value="URL"/>
     <xsd:enumeration value="DATETIME"/>
     <xsd:enumeration value="DATE"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ManagedTopic">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="managedTopicType" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="parentName" type="xsd:string"/>
       <xsd:element name="position" type="xsd:int"/>
       <xsd:element name="topicDescription" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ManagedTopics">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="managedTopic" minOccurs="0" maxOccurs="unbounded" type="tns:ManagedTopic"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MatchingRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="booleanFilter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="matchingRuleItems" minOccurs="0" maxOccurs="unbounded" type="tns:MatchingRuleItem"/>
       <xsd:element name="ruleStatus" type="tns:MatchingRuleStatus"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MatchingRuleItem">
    <xsd:sequence>
     <xsd:element name="blankValueBehavior" minOccurs="0" type="tns:BlankValueBehavior"/>
     <xsd:element name="fieldName" type="xsd:string"/>
     <xsd:element name="matchingMethod" type="tns:MatchingMethod"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="BlankValueBehavior">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="MatchBlanks"/>
     <xsd:enumeration value="NullNotAllowed"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="MatchingMethod">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Exact"/>
     <xsd:enumeration value="FirstName"/>
     <xsd:enumeration value="LastName"/>
     <xsd:enumeration value="CompanyName"/>
     <xsd:enumeration value="Phone"/>
     <xsd:enumeration value="City"/>
     <xsd:enumeration value="Street"/>
     <xsd:enumeration value="Zip"/>
     <xsd:enumeration value="Title"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="MatchingRuleStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Inactive"/>
     <xsd:enumeration value="DeactivationFailed"/>
     <xsd:enumeration value="Activating"/>
     <xsd:enumeration value="Deactivating"/>
     <xsd:enumeration value="Active"/>
     <xsd:enumeration value="ActivationFailed"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="MatchingRules">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="matchingRules" minOccurs="0" maxOccurs="unbounded" type="tns:MatchingRule"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MeetingsSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableSalesforceMeetings" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSalesforceMeetingsSyncCheck" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableZoomVideoConference" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MetadataWithContent">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="content" minOccurs="0" type="xsd:base64Binary"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AccessControlPolicy">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="deploymentStatus" type="tns:ACPStatus"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="targetEntity" type="xsd:string"/>
       <xsd:element name="version" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ACPStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="New"/>
     <xsd:enumeration value="Pending"/>
     <xsd:enumeration value="Deployed"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ApexClass">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="apiVersion" type="xsd:double"/>
       <xsd:element name="packageVersions" minOccurs="0" maxOccurs="unbounded" type="tns:PackageVersion"/>
       <xsd:element name="status" type="tns:ApexCodeUnitStatus"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ApexCodeUnitStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Inactive"/>
     <xsd:enumeration value="Active"/>
     <xsd:enumeration value="Deleted"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ApexComponent">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="apiVersion" minOccurs="0" type="xsd:double"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="packageVersions" minOccurs="0" maxOccurs="unbounded" type="tns:PackageVersion"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ApexPage">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="apiVersion" type="xsd:double"/>
       <xsd:element name="availableInTouch" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="confirmationTokenRequired" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="packageVersions" minOccurs="0" maxOccurs="unbounded" type="tns:PackageVersion"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ApexTrigger">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="apiVersion" type="xsd:double"/>
       <xsd:element name="packageVersions" minOccurs="0" maxOccurs="unbounded" type="tns:PackageVersion"/>
       <xsd:element name="status" type="tns:ApexCodeUnitStatus"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Certificate">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="caSigned" type="xsd:boolean"/>
       <xsd:element name="encryptedWithPlatformEncryption" minOccurs="0" type="xsd:boolean" nillable="true"/>
       <xsd:element name="expirationDate" minOccurs="0" type="xsd:dateTime" nillable="true"/>
       <xsd:element name="keySize" minOccurs="0" type="xsd:int"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="privateKeyExportable" minOccurs="0" type="xsd:boolean" nillable="true"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ContentAsset">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="format" minOccurs="0" type="tns:ContentAssetFormat"/>
       <xsd:element name="isVisibleByExternalUsers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="language" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="originNetwork" minOccurs="0" type="xsd:string"/>
       <xsd:element name="relationships" minOccurs="0" type="tns:ContentAssetRelationships"/>
       <xsd:element name="versions" type="tns:ContentAssetVersions"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ContentAssetFormat">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Original"/>
     <xsd:enumeration value="ZippedVersions"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ContentAssetRelationships">
    <xsd:sequence>
     <xsd:element name="emailTemplate" minOccurs="0" maxOccurs="unbounded" type="tns:ContentAssetLink"/>
     <xsd:element name="insightsApplication" minOccurs="0" maxOccurs="unbounded" type="tns:ContentAssetLink"/>
     <xsd:element name="network" minOccurs="0" maxOccurs="unbounded" type="tns:ContentAssetLink"/>
     <xsd:element name="organization" minOccurs="0" type="tns:ContentAssetLink"/>
     <xsd:element name="workspace" minOccurs="0" maxOccurs="unbounded" type="tns:ContentAssetLink"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ContentAssetLink">
    <xsd:sequence>
     <xsd:element name="access" type="tns:ContentAssetAccess"/>
     <xsd:element name="isManagingWorkspace" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="name" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ContentAssetAccess">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="VIEWER"/>
     <xsd:enumeration value="COLLABORATOR"/>
     <xsd:enumeration value="INFERRED"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ContentAssetVersions">
    <xsd:sequence>
     <xsd:element name="version" minOccurs="0" maxOccurs="unbounded" type="tns:ContentAssetVersion"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ContentAssetVersion">
    <xsd:sequence>
     <xsd:element name="number" type="xsd:string"/>
     <xsd:element name="pathOnClient" type="xsd:string"/>
     <xsd:element name="zipEntry" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DiscoveryAIModel">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="algorithmType" type="tns:DiscoveryAlgorithmType"/>
       <xsd:element name="classificationThreshold" minOccurs="0" type="xsd:double"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="modelFields" minOccurs="0" maxOccurs="unbounded" type="tns:DiscoveryModelField"/>
       <xsd:element name="modelRuntimeType" type="tns:DiscoveryModelRuntimeType"/>
       <xsd:element name="predictedField" type="xsd:string"/>
       <xsd:element name="predictionType" type="tns:DiscoveryPredictionType"/>
       <xsd:element name="sourceType" type="tns:DiscoveryModelSourceType"/>
       <xsd:element name="status" type="tns:DiscoveryAIModelStatus"/>
       <xsd:element name="trainingMetrics" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="DiscoveryAlgorithmType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Glm"/>
     <xsd:enumeration value="Gbm"/>
     <xsd:enumeration value="Xgboost"/>
     <xsd:enumeration value="Drf"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DiscoveryModelField">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="transformationConfig" minOccurs="0" type="xsd:string"/>
     <xsd:element name="transformationType" minOccurs="0" type="tns:DiscoveryAIModelTransformationType"/>
     <xsd:element name="type" type="tns:DiscoveryModelFieldType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DiscoveryAIModelTransformationType">
    <xsd:restriction base="xsd:string"/>
   </xsd:simpleType>
   <xsd:simpleType name="DiscoveryModelFieldType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Text"/>
     <xsd:enumeration value="Number"/>
     <xsd:enumeration value="Date"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="DiscoveryModelRuntimeType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Discovery"/>
     <xsd:enumeration value="H2O"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="DiscoveryModelSourceType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Discovery"/>
     <xsd:enumeration value="UserUpload"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="DiscoveryAIModelStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Disabled"/>
     <xsd:enumeration value="Enabled"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="Document">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="internalUseOnly" type="xsd:boolean"/>
       <xsd:element name="keywords" minOccurs="0" type="xsd:string"/>
       <xsd:element name="name" minOccurs="0" type="xsd:string"/>
       <xsd:element name="public" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EclairGeoData">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="maps" minOccurs="0" maxOccurs="unbounded" type="tns:EclairMap"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EclairMap">
    <xsd:sequence>
     <xsd:element name="boundingBoxBottom" minOccurs="0" type="xsd:double"/>
     <xsd:element name="boundingBoxLeft" minOccurs="0" type="xsd:double"/>
     <xsd:element name="boundingBoxRight" minOccurs="0" type="xsd:double"/>
     <xsd:element name="boundingBoxTop" minOccurs="0" type="xsd:double"/>
     <xsd:element name="mapLabel" minOccurs="0" type="xsd:string"/>
     <xsd:element name="mapName" type="xsd:string"/>
     <xsd:element name="projection" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="EmailTemplate">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="apiVersion" minOccurs="0" type="xsd:double"/>
       <xsd:element name="attachedDocuments" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="attachments" minOccurs="0" maxOccurs="unbounded" type="tns:Attachment"/>
       <xsd:element name="available" type="xsd:boolean"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="encodingKey" type="tns:Encoding"/>
       <xsd:element name="letterhead" minOccurs="0" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="packageVersions" minOccurs="0" maxOccurs="unbounded" type="tns:PackageVersion"/>
       <xsd:element name="pageDevName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="relatedEntityType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="style" type="tns:EmailTemplateStyle"/>
       <xsd:element name="subject" minOccurs="0" type="xsd:string"/>
       <xsd:element name="textOnly" minOccurs="0" type="xsd:string"/>
       <xsd:element name="type" type="tns:EmailTemplateType"/>
       <xsd:element name="uiType" minOccurs="0" type="tns:EmailTemplateUiType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Attachment">
    <xsd:sequence>
     <xsd:element name="content" type="xsd:base64Binary"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="EmailTemplateStyle">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="none"/>
     <xsd:enumeration value="freeForm"/>
     <xsd:enumeration value="formalLetter"/>
     <xsd:enumeration value="promotionRight"/>
     <xsd:enumeration value="promotionLeft"/>
     <xsd:enumeration value="newsletter"/>
     <xsd:enumeration value="products"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="EmailTemplateType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="text"/>
     <xsd:enumeration value="html"/>
     <xsd:enumeration value="custom"/>
     <xsd:enumeration value="visualforce"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="EmailTemplateUiType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Aloha"/>
     <xsd:enumeration value="SFX"/>
     <xsd:enumeration value="SFX_Sample"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FieldServiceMobileExtension">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="fileName" type="xsd:string"/>
       <xsd:element name="masterLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="size" minOccurs="0" type="xsd:int"/>
       <xsd:element name="version" minOccurs="0" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="InboundCertificate">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="expirationDate" type="xsd:date"/>
       <xsd:element name="issuer" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="serialId" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="NetworkBranding">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="loginBackgroundImageUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="loginFooterText" minOccurs="0" type="xsd:string"/>
       <xsd:element name="loginLogo" minOccurs="0" type="xsd:string"/>
       <xsd:element name="loginLogoName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="loginPrimaryColor" minOccurs="0" type="xsd:string"/>
       <xsd:element name="loginQuaternaryColor" minOccurs="0" type="xsd:string"/>
       <xsd:element name="loginRightFrameUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="network" minOccurs="0" type="xsd:string"/>
       <xsd:element name="pageFooter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="pageHeader" minOccurs="0" type="xsd:string"/>
       <xsd:element name="primaryColor" type="xsd:string"/>
       <xsd:element name="primaryComplementColor" type="xsd:string"/>
       <xsd:element name="quaternaryColor" type="xsd:string"/>
       <xsd:element name="quaternaryComplementColor" type="xsd:string"/>
       <xsd:element name="secondaryColor" type="xsd:string"/>
       <xsd:element name="staticLogoImageUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="tertiaryColor" type="xsd:string"/>
       <xsd:element name="tertiaryComplementColor" type="xsd:string"/>
       <xsd:element name="zeronaryColor" type="xsd:string"/>
       <xsd:element name="zeronaryComplementColor" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Orchestration">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="context" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Scontrol">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="contentSource" type="tns:SControlContentSource"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="encodingKey" type="tns:Encoding"/>
       <xsd:element name="fileContent" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="fileName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="supportsCaching" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="SControlContentSource">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="HTML"/>
     <xsd:enumeration value="URL"/>
     <xsd:enumeration value="Snippet"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="SiteDotCom">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="siteType" type="tns:SiteType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="StaticResource">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="cacheControl" type="tns:StaticResourceCacheControl"/>
       <xsd:element name="contentType" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="StaticResourceCacheControl">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Private"/>
     <xsd:enumeration value="Public"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="UiPlugin">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="extensionPointIdentifier" type="xsd:string"/>
       <xsd:element name="isEnabled" type="xsd:boolean"/>
       <xsd:element name="language" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="UserAuthCertificate">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="expirationDate" minOccurs="0" type="xsd:dateTime"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="serialNumber" type="xsd:string"/>
       <xsd:element name="user" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WaveDashboard">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="application" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="templateAssetSourceName" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WaveComponent">
    <xsd:complexContent>
     <xsd:extension base="tns:WaveDashboard">
      <xsd:sequence/>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WaveDataflow">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="application" minOccurs="0" type="xsd:string"/>
       <xsd:element name="dataflowType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WaveLens">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="application" type="xsd:string"/>
       <xsd:element name="datasets" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="templateAssetSourceName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="visualizationType" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WaveRecipe">
    <xsd:complexContent>
     <xsd:extension base="tns:MetadataWithContent">
      <xsd:sequence>
       <xsd:element name="application" minOccurs="0" type="xsd:string"/>
       <xsd:element name="dataflow" type="xsd:string"/>
       <xsd:element name="format" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="securityPredicate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="targetDatasetAlias" minOccurs="0" type="xsd:string"/>
       <xsd:element name="templateAssetSourceName" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MilestoneType">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="recurrenceType" minOccurs="0" type="tns:MilestoneTypeRecurrenceType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="MilestoneTypeRecurrenceType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="none"/>
     <xsd:enumeration value="recursIndependently"/>
     <xsd:enumeration value="recursChained"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="MlDomain">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="mlIntents" minOccurs="0" maxOccurs="unbounded" type="tns:MlIntent"/>
       <xsd:element name="mlSlotClasses" minOccurs="0" maxOccurs="unbounded" type="tns:MlSlotClass"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MobileApplicationDetail">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="applicationBinaryFile" minOccurs="0" type="xsd:base64Binary"/>
       <xsd:element name="applicationBinaryFileName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="applicationBundleIdentifier" minOccurs="0" type="xsd:string"/>
       <xsd:element name="applicationFileLength" minOccurs="0" type="xsd:int"/>
       <xsd:element name="applicationIconFile" minOccurs="0" type="xsd:string"/>
       <xsd:element name="applicationIconFileName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="applicationInstallUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="devicePlatform" type="tns:DevicePlatformType"/>
       <xsd:element name="deviceType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="minimumOsVersion" minOccurs="0" type="xsd:string"/>
       <xsd:element name="privateApp" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="version" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MobileSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="dashboardMobile" minOccurs="0" type="tns:DashboardMobileSettings"/>
       <xsd:element name="enableImportContactFromDevice" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNewSalesforceMobileAppForTablet" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNewSalesforceMobileAppForTabletWideScreen" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOfflineDraftsEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePopulateNameManuallyInToday" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableS1EncryptedStoragePref2" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableS1OfflinePref" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="DashboardMobileSettings">
    <xsd:sequence>
     <xsd:element name="enableDashboardIPadApp" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ModerationRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="action" type="tns:ModerationRuleAction"/>
       <xsd:element name="actionLimit" minOccurs="0" type="xsd:int"/>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="entitiesAndFields" minOccurs="0" maxOccurs="unbounded" type="tns:ModeratedEntityField"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="notifyLimit" minOccurs="0" type="xsd:int"/>
       <xsd:element name="timePeriod" minOccurs="0" type="tns:RateLimitTimePeriod"/>
       <xsd:element name="type" minOccurs="0" type="tns:ModerationRuleType"/>
       <xsd:element name="userCriteria" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="userMessage" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ModerationRuleAction">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Block"/>
     <xsd:enumeration value="FreezeAndNotify"/>
     <xsd:enumeration value="Review"/>
     <xsd:enumeration value="Replace"/>
     <xsd:enumeration value="Flag"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ModeratedEntityField">
    <xsd:sequence>
     <xsd:element name="entityName" type="xsd:string"/>
     <xsd:element name="fieldName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="keywordList" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="RateLimitTimePeriod">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Short"/>
     <xsd:enumeration value="Medium"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ModerationRuleType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Content"/>
     <xsd:enumeration value="Rate"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="MyDomainDiscoverableLogin">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="apexHandler" type="xsd:string"/>
       <xsd:element name="executeApexHandlerAs" minOccurs="0" type="xsd:string"/>
       <xsd:element name="usernameLabel" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MyDomainSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="canOnlyLoginWithMyDomainUrl" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesApiLoginRequireOrgDomain" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNativeBrowserForAuthOnAndroid" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNativeBrowserForAuthOnIos" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="myDomainName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="myDomainSuffix" minOccurs="0" type="tns:OrgDomainProdSuffix"/>
       <xsd:element name="use3rdPartyCookieBlockingCompatibleHostnames" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="useEdge" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="useStabilizedMyDomainHostnames" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="useStabilizedSandboxMyDomainHostnames" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="OrgDomainProdSuffix">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="MySalesforceLimited"/>
     <xsd:enumeration value="DatabaseLimited"/>
     <xsd:enumeration value="CloudforceLimited"/>
     <xsd:enumeration value="OrgLevelCertificateLimited"/>
     <xsd:enumeration value="Restricted1"/>
     <xsd:enumeration value="MySalesforce"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="NameSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableInformalName" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMiddleName" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNameSuffix" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="NamedCredential">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="allowMergeFieldsInBody" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="allowMergeFieldsInHeader" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="authProvider" minOccurs="0" type="xsd:string"/>
       <xsd:element name="authTokenEndpointUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="awsAccessKey" minOccurs="0" type="xsd:string"/>
       <xsd:element name="awsAccessSecret" minOccurs="0" type="xsd:string"/>
       <xsd:element name="awsRegion" minOccurs="0" type="xsd:string"/>
       <xsd:element name="awsService" minOccurs="0" type="xsd:string"/>
       <xsd:element name="certificate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="endpoint" minOccurs="0" type="xsd:string"/>
       <xsd:element name="generateAuthorizationHeader" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="jwtAudience" minOccurs="0" type="xsd:string"/>
       <xsd:element name="jwtFormulaSubject" minOccurs="0" type="xsd:string"/>
       <xsd:element name="jwtIssuer" minOccurs="0" type="xsd:string"/>
       <xsd:element name="jwtSigningCertificate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="jwtTextSubject" minOccurs="0" type="xsd:string"/>
       <xsd:element name="jwtValidityPeriodSeconds" minOccurs="0" type="xsd:int"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="oauthRefreshToken" minOccurs="0" type="xsd:string"/>
       <xsd:element name="oauthScope" minOccurs="0" type="xsd:string"/>
       <xsd:element name="oauthToken" minOccurs="0" type="xsd:string"/>
       <xsd:element name="outboundNetworkConnection" minOccurs="0" type="xsd:string"/>
       <xsd:element name="password" minOccurs="0" type="xsd:string"/>
       <xsd:element name="principalType" type="tns:ExternalPrincipalType"/>
       <xsd:element name="protocol" type="tns:AuthenticationProtocol"/>
       <xsd:element name="username" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="NavigationMenu">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="container" type="xsd:string"/>
       <xsd:element name="containerType" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="navigationMenuItem" minOccurs="0" maxOccurs="unbounded" type="tns:NavigationMenuItem"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Network">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="allowInternalUserLogin" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="allowMembersToFlag" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="allowedExtensions" minOccurs="0" type="xsd:string"/>
       <xsd:element name="caseCommentEmailTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="changePasswordTemplate" type="xsd:string"/>
       <xsd:element name="chgEmailVerNewTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="chgEmailVerOldTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="communityRoles" minOccurs="0" type="tns:CommunityRoles"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="disableReputationRecordConversations" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="emailFooterLogo" minOccurs="0" type="xsd:string"/>
       <xsd:element name="emailFooterText" minOccurs="0" type="xsd:string"/>
       <xsd:element name="emailSenderAddress" type="xsd:string"/>
       <xsd:element name="emailSenderName" type="xsd:string"/>
       <xsd:element name="enableCustomVFErrorPageOverrides" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDirectMessages" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableExperienceBundleBasedSnaOverrideEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGuestChatter" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGuestFileAccess" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGuestMemberVisibility" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInvitation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableKnowledgeable" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMemberVisibility" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNicknameDisplay" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePrivateMessages" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableReputation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableShowAllNetworkSettings" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSiteAsContainer" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTalkingAboutStats" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTopicAssignmentRules" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTopicSuggestions" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUpDownVote" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="feedChannel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="forgotPasswordTemplate" type="xsd:string"/>
       <xsd:element name="gatherCustomerSentimentData" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="lockoutTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="logoutUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="maxFileSizeKb" minOccurs="0" type="xsd:int"/>
       <xsd:element name="navigationLinkSet" minOccurs="0" type="tns:NavigationLinkSet"/>
       <xsd:element name="networkMemberGroups" minOccurs="0" type="tns:NetworkMemberGroup"/>
       <xsd:element name="networkPageOverrides" minOccurs="0" type="tns:NetworkPageOverride"/>
       <xsd:element name="newSenderAddress" minOccurs="0" type="xsd:string"/>
       <xsd:element name="picassoSite" minOccurs="0" type="xsd:string"/>
       <xsd:element name="recommendationAudience" minOccurs="0" type="tns:RecommendationAudience"/>
       <xsd:element name="recommendationDefinition" minOccurs="0" type="tns:RecommendationDefinition"/>
       <xsd:element name="reputationLevels" minOccurs="0" type="tns:ReputationLevelDefinitions"/>
       <xsd:element name="reputationPointsRules" minOccurs="0" type="tns:ReputationPointsRules"/>
       <xsd:element name="selfRegProfile" minOccurs="0" type="xsd:string"/>
       <xsd:element name="selfRegistration" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="sendWelcomeEmail" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="site" type="xsd:string"/>
       <xsd:element name="status" type="tns:NetworkStatus"/>
       <xsd:element name="tabs" type="tns:NetworkTabSet"/>
       <xsd:element name="urlPathPrefix" minOccurs="0" type="xsd:string"/>
       <xsd:element name="verificationTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="welcomeTemplate" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CommunityRoles">
    <xsd:sequence>
     <xsd:element name="customerUserRole" minOccurs="0" type="xsd:string"/>
     <xsd:element name="employeeUserRole" minOccurs="0" type="xsd:string"/>
     <xsd:element name="partnerUserRole" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="NetworkMemberGroup">
    <xsd:sequence>
     <xsd:element name="permissionSet" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="profile" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="NetworkPageOverride">
    <xsd:sequence>
     <xsd:element name="changePasswordPageOverrideSetting" minOccurs="0" type="tns:NetworkPageOverrideSetting"/>
     <xsd:element name="forgotPasswordPageOverrideSetting" minOccurs="0" type="tns:NetworkPageOverrideSetting"/>
     <xsd:element name="homePageOverrideSetting" minOccurs="0" type="tns:NetworkPageOverrideSetting"/>
     <xsd:element name="loginPageOverrideSetting" minOccurs="0" type="tns:NetworkPageOverrideSetting"/>
     <xsd:element name="selfRegProfilePageOverrideSetting" minOccurs="0" type="tns:NetworkPageOverrideSetting"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="NetworkPageOverrideSetting">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Designer"/>
     <xsd:enumeration value="VisualForce"/>
     <xsd:enumeration value="Standard"/>
     <xsd:enumeration value="Configurable"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="RecommendationAudience">
    <xsd:sequence>
     <xsd:element name="recommendationAudienceDetails" minOccurs="0" maxOccurs="unbounded" type="tns:RecommendationAudienceDetail"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RecommendationAudienceDetail">
    <xsd:sequence>
     <xsd:element name="audienceCriteriaType" minOccurs="0" type="tns:AudienceCriteriaType"/>
     <xsd:element name="audienceCriteriaValue" minOccurs="0" type="xsd:string"/>
     <xsd:element name="setupName" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="AudienceCriteriaType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="CustomList"/>
     <xsd:enumeration value="MaxDaysInCommunity"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="RecommendationDefinition">
    <xsd:sequence>
     <xsd:element name="recommendationDefinitionDetails" minOccurs="0" maxOccurs="unbounded" type="tns:RecommendationDefinitionDetail"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RecommendationDefinitionDetail">
    <xsd:sequence>
     <xsd:element name="actionUrl" minOccurs="0" type="xsd:string"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="linkText" minOccurs="0" type="xsd:string"/>
     <xsd:element name="scheduledRecommendations" minOccurs="0" type="tns:ScheduledRecommendation"/>
     <xsd:element name="setupName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="title" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ScheduledRecommendation">
    <xsd:sequence>
     <xsd:element name="scheduledRecommendationDetails" minOccurs="0" maxOccurs="unbounded" type="tns:ScheduledRecommendationDetail"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ScheduledRecommendationDetail">
    <xsd:sequence>
     <xsd:element name="channel" minOccurs="0" type="tns:RecommendationChannel"/>
     <xsd:element name="enabled" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="rank" minOccurs="0" type="xsd:int"/>
     <xsd:element name="recommendationAudience" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="RecommendationChannel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="DefaultChannel"/>
     <xsd:enumeration value="CustomChannel1"/>
     <xsd:enumeration value="CustomChannel2"/>
     <xsd:enumeration value="CustomChannel3"/>
     <xsd:enumeration value="CustomChannel4"/>
     <xsd:enumeration value="CustomChannel5"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ReputationLevelDefinitions">
    <xsd:sequence>
     <xsd:element name="level" minOccurs="0" maxOccurs="unbounded" type="tns:ReputationLevel"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReputationLevel">
    <xsd:sequence>
     <xsd:element name="branding" minOccurs="0" type="tns:ReputationBranding"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="lowerThreshold" type="xsd:double"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReputationBranding">
    <xsd:sequence>
     <xsd:element name="smallImage" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReputationPointsRules">
    <xsd:sequence>
     <xsd:element name="pointsRule" minOccurs="0" maxOccurs="unbounded" type="tns:ReputationPointsRule"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReputationPointsRule">
    <xsd:sequence>
     <xsd:element name="eventType" type="xsd:string"/>
     <xsd:element name="points" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="NetworkStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="UnderConstruction"/>
     <xsd:enumeration value="Live"/>
     <xsd:enumeration value="DownForMaintenance"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="NetworkTabSet">
    <xsd:sequence>
     <xsd:element name="customTab" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="defaultTab" type="xsd:string"/>
     <xsd:element name="standardTab" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="NotificationTypeConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="notificationTypeSettings" minOccurs="0" maxOccurs="unbounded" type="tns:NotificationTypeSettings"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="NotificationTypeSettings">
    <xsd:sequence>
     <xsd:element name="appSettings" minOccurs="0" maxOccurs="unbounded" type="tns:AppSettings"/>
     <xsd:element name="notificationChannels" minOccurs="0" type="tns:NotificationChannels"/>
     <xsd:element name="notificationType" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="AppSettings">
    <xsd:sequence>
     <xsd:element name="connectedAppName" type="xsd:string"/>
     <xsd:element name="enabled" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="NotificationChannels">
    <xsd:sequence>
     <xsd:element name="desktopEnabled" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="mobileEnabled" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="slackEnabled" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="NotificationsSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableActvityReminderBrowserNotifs" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMobileAppPushNotifications" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNotifications" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="OauthCustomScope">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="assignedTo" minOccurs="0" maxOccurs="unbounded" type="tns:OauthCustomScopeApp"/>
       <xsd:element name="description" type="xsd:string"/>
       <xsd:element name="developerName" type="xsd:string"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isPublic" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="OauthCustomScopeApp">
    <xsd:sequence>
     <xsd:element name="connectedApp" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ObjectLinkingSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableObjectLinking" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="OmniChannelSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableOmniAutoLoginPrompt" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOmniChannel" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOmniSecondaryRoutingPriority" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOmniSkillsRouting" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="OpportunityInsightsSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableOpportunityInsights" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="OpportunityScoreSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableOpportunityScoring" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="OpportunitySettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="autoActivateNewReminders" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="customizableProductSchedulesEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesEnforceStandardOpportunitySaveLogic" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableExpandedPipelineInspectionSetup" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFindSimilarOpportunities" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOpportunityFieldHistoryTracking" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOpportunityInsightsInMobile" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOpportunityTeam" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePipelineInspection" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUpdateReminders" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="findSimilarOppFilter" minOccurs="0" type="tns:FindSimilarOppFilter"/>
       <xsd:element name="oppAmountDealMotionEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="oppCloseDateDealMotionEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="promptToAddProducts" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FindSimilarOppFilter">
    <xsd:sequence>
     <xsd:element name="similarOpportunitiesDisplayColumns" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="similarOpportunitiesMatchFields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="OrchestrationContext">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="datasets" minOccurs="0" maxOccurs="unbounded" type="tns:OrchestrationContextDataset"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="events" minOccurs="0" maxOccurs="unbounded" type="tns:OrchestrationContextEvent"/>
       <xsd:element name="imageFile" type="xsd:string"/>
       <xsd:element name="imageScale" type="xsd:int"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="runtimeType" type="xsd:string"/>
       <xsd:element name="salesforceObject" minOccurs="0" type="xsd:string"/>
       <xsd:element name="salesforceObjectPrimaryKey" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="OrchestrationContextDataset">
    <xsd:sequence>
     <xsd:element name="datasetType" type="xsd:string"/>
     <xsd:element name="orchestrationDataset" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="OrchestrationContextEvent">
    <xsd:sequence>
     <xsd:element name="eventType" type="xsd:string"/>
     <xsd:element name="orchestrationEvent" type="xsd:string"/>
     <xsd:element name="platformEvent" type="xsd:string"/>
     <xsd:element name="platformEventPrimaryKey" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="OrderManagementSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableB2CIntegration" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableB2CSelfService" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOMAutomation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOrderManagement" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePersonAccountsForShoppers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="initOMAutomation" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="OrderSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableEnhancedCommerceOrders" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNegativeQuantity" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOptionalPricebook" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOrderEvents" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOrders" type="xsd:boolean"/>
       <xsd:element name="enableReductionOrders" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableZeroQuantity" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="OutboundNetworkConnection">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="connectionType" type="tns:ExternalConnectionType"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isActive" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="outboundNetworkConnProperties" minOccurs="0" maxOccurs="unbounded" type="tns:OutboundNetworkConnProperty"/>
       <xsd:element name="status" type="tns:ExternalConnectionStatus"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="OutboundNetworkConnProperty">
    <xsd:sequence>
     <xsd:element name="propertyName" type="tns:OutboundConnPropertyName"/>
     <xsd:element name="propertyValue" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="OutboundConnPropertyName">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Region"/>
     <xsd:enumeration value="AwsVpcEndpointId"/>
     <xsd:enumeration value="AwsVpcEndpointServiceName"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="Package">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="apiAccessLevel" minOccurs="0" type="tns:APIAccessLevel"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="namespacePrefix" minOccurs="0" type="xsd:string"/>
       <xsd:element name="objectPermissions" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileObjectPermissions"/>
       <xsd:element name="packageType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="postInstallClass" minOccurs="0" type="xsd:string"/>
       <xsd:element name="setupWeblink" minOccurs="0" type="xsd:string"/>
       <xsd:element name="types" minOccurs="0" maxOccurs="unbounded" type="tns:PackageTypeMembers"/>
       <xsd:element name="uninstallClass" minOccurs="0" type="xsd:string"/>
       <xsd:element name="version" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="APIAccessLevel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Unrestricted"/>
     <xsd:enumeration value="Restricted"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ProfileObjectPermissions">
    <xsd:sequence>
     <xsd:element name="allowCreate" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="allowDelete" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="allowEdit" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="allowRead" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="modifyAllRecords" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="object" type="xsd:string"/>
     <xsd:element name="viewAllRecords" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PackageTypeMembers">
    <xsd:sequence>
     <xsd:element name="members" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PardotEinsteinSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCampaignInsight" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEngagementScore" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PardotSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableAIOptimizedSendTime" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableB2bmaAppEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEngagementHistoryDashboards" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEnhancedProspectCustomFieldsSync" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePardotAppV1Enabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePardotEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePardotObjectSync" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableProspectActivityDataset" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ParticipantRole">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="defaultAccessLevel" type="tns:ParticipantRoleAccessLevel"/>
       <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="parentObject" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ParticipantRoleAccessLevel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="Read"/>
     <xsd:enumeration value="Edit"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="PartyDataModelSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableAutoSelectIndividualOnMerge" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableConsentManagement" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIndividualAutoCreate" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PathAssistant">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="entityName" type="xsd:string"/>
       <xsd:element name="fieldName" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="pathAssistantSteps" minOccurs="0" maxOccurs="unbounded" type="tns:PathAssistantStep"/>
       <xsd:element name="recordTypeName" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PathAssistantStep">
    <xsd:sequence>
     <xsd:element name="fieldNames" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="info" minOccurs="0" type="xsd:string"/>
     <xsd:element name="picklistValueName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PathAssistantSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="canOverrideAutoPathCollapseWithUserPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="pathAssistantEnabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PaymentGatewayProvider">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="apexAdapter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="comments" minOccurs="0" type="xsd:string"/>
       <xsd:element name="idempotencySupported" type="tns:IdempotencySupportStatus"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="IdempotencySupportStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="No"/>
     <xsd:enumeration value="Yes"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="PermissionSet">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="applicationVisibilities" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetApplicationVisibility"/>
       <xsd:element name="classAccesses" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetApexClassAccess"/>
       <xsd:element name="customMetadataTypeAccesses" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetCustomMetadataTypeAccess"/>
       <xsd:element name="customPermissions" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetCustomPermissions"/>
       <xsd:element name="customSettingAccesses" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetCustomSettingAccess"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="externalDataSourceAccesses" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetExternalDataSourceAccess"/>
       <xsd:element name="fieldPermissions" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetFieldPermissions"/>
       <xsd:element name="flowAccesses" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetFlowAccess"/>
       <xsd:element name="hasActivationRequired" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="license" minOccurs="0" type="xsd:string"/>
       <xsd:element name="objectPermissions" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetObjectPermissions"/>
       <xsd:element name="pageAccesses" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetApexPageAccess"/>
       <xsd:element name="recordTypeVisibilities" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetRecordTypeVisibility"/>
       <xsd:element name="tabSettings" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetTabSetting"/>
       <xsd:element name="userPermissions" minOccurs="0" maxOccurs="unbounded" type="tns:PermissionSetUserPermission"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetApplicationVisibility">
    <xsd:sequence>
     <xsd:element name="application" type="xsd:string"/>
     <xsd:element name="visible" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetApexClassAccess">
    <xsd:sequence>
     <xsd:element name="apexClass" type="xsd:string"/>
     <xsd:element name="enabled" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetCustomMetadataTypeAccess">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetCustomPermissions">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetCustomSettingAccess">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetExternalDataSourceAccess">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="externalDataSource" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetFieldPermissions">
    <xsd:sequence>
     <xsd:element name="editable" type="xsd:boolean"/>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="readable" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetFlowAccess">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="flow" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetObjectPermissions">
    <xsd:sequence>
     <xsd:element name="allowCreate" type="xsd:boolean"/>
     <xsd:element name="allowDelete" type="xsd:boolean"/>
     <xsd:element name="allowEdit" type="xsd:boolean"/>
     <xsd:element name="allowRead" type="xsd:boolean"/>
     <xsd:element name="modifyAllRecords" type="xsd:boolean"/>
     <xsd:element name="object" type="xsd:string"/>
     <xsd:element name="viewAllRecords" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetApexPageAccess">
    <xsd:sequence>
     <xsd:element name="apexPage" type="xsd:string"/>
     <xsd:element name="enabled" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetRecordTypeVisibility">
    <xsd:sequence>
     <xsd:element name="recordType" type="xsd:string"/>
     <xsd:element name="visible" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetTabSetting">
    <xsd:sequence>
     <xsd:element name="tab" type="xsd:string"/>
     <xsd:element name="visibility" type="tns:PermissionSetTabVisibility"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="PermissionSetTabVisibility">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="Available"/>
     <xsd:enumeration value="Visible"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="PermissionSetUserPermission">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="MutingPermissionSet">
    <xsd:complexContent>
     <xsd:extension base="tns:PermissionSet">
      <xsd:sequence>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PermissionSetGroup">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="mutingPermissionSets" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="permissionSets" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="status" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PicklistSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="isPicklistApiNameEditDisabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PlatformCachePartition">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isDefaultPartition" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="platformCachePartitionTypes" minOccurs="0" maxOccurs="unbounded" type="tns:PlatformCachePartitionType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PlatformCachePartitionType">
    <xsd:sequence>
     <xsd:element name="allocatedCapacity" type="xsd:int"/>
     <xsd:element name="allocatedPartnerCapacity" type="xsd:int"/>
     <xsd:element name="allocatedPurchasedCapacity" type="xsd:int"/>
     <xsd:element name="allocatedTrialCapacity" type="xsd:int"/>
     <xsd:element name="cacheType" type="tns:PlatformCacheType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="PlatformCacheType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Session"/>
     <xsd:enumeration value="Organization"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="PlatformEncryptionSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="canEncryptManagedPackageFields" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDeterministicEncryption" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEncryptFieldHistory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEncryptionSearchEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEventBusEncryption" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isMEKForEncryptionRequired" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isUseHighAssuranceKeysRequired" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PlatformEventChannel">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="channelType" type="tns:PlatformEventChannelType"/>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="PlatformEventChannelType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="event"/>
     <xsd:enumeration value="data"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="PlatformEventChannelMember">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enrichedFields" minOccurs="0" maxOccurs="unbounded" type="tns:EnrichedField"/>
       <xsd:element name="eventChannel" type="xsd:string"/>
       <xsd:element name="selectedEntity" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="EnrichedField">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Portal">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="admin" minOccurs="0" type="xsd:string"/>
       <xsd:element name="defaultLanguage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="emailSenderAddress" type="xsd:string"/>
       <xsd:element name="emailSenderName" type="xsd:string"/>
       <xsd:element name="enableSelfCloseCase" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="footerDocument" minOccurs="0" type="xsd:string"/>
       <xsd:element name="forgotPassTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="headerDocument" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isSelfRegistrationActivated" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="loginHeaderDocument" minOccurs="0" type="xsd:string"/>
       <xsd:element name="logoDocument" minOccurs="0" type="xsd:string"/>
       <xsd:element name="logoutUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="newCommentTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="newPassTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="newUserTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="ownerNotifyTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="selfRegNewUserUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="selfRegUserDefaultProfile" minOccurs="0" type="xsd:string"/>
       <xsd:element name="selfRegUserDefaultRole" minOccurs="0" type="tns:PortalRoles"/>
       <xsd:element name="selfRegUserTemplate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="showActionConfirmation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="stylesheetDocument" minOccurs="0" type="xsd:string"/>
       <xsd:element name="type" type="tns:PortalType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="PortalRoles">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Executive"/>
     <xsd:enumeration value="Manager"/>
     <xsd:enumeration value="Worker"/>
     <xsd:enumeration value="PersonAccount"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="PortalType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="CustomerSuccess"/>
     <xsd:enumeration value="Partner"/>
     <xsd:enumeration value="Network"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="PortalsSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="clickjackSSPLoginPage" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="redirectPortalLoginToHttps" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PostTemplate">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="default" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PredictionBuilderSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enablePredictionBuilder" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isPredictionBuilderStarted" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PresenceDeclineReason">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PresenceUserConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="assignments" minOccurs="0" type="tns:PresenceConfigAssignments"/>
       <xsd:element name="capacity" type="xsd:int"/>
       <xsd:element name="declineReasons" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="enableAutoAccept" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDecline" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDeclineReason" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDisconnectSound" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRequestSound" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="presenceStatusOnDecline" minOccurs="0" type="xsd:string"/>
       <xsd:element name="presenceStatusOnPushTimeout" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PresenceConfigAssignments">
    <xsd:sequence>
     <xsd:element name="profiles" minOccurs="0" type="tns:PresenceConfigProfileAssignments"/>
     <xsd:element name="users" minOccurs="0" type="tns:PresenceConfigUserAssignments"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PresenceConfigProfileAssignments">
    <xsd:sequence>
     <xsd:element name="profile" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PresenceConfigUserAssignments">
    <xsd:sequence>
     <xsd:element name="user" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PrivacySettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="authorizationCaptureBrowser" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="authorizationCaptureEmail" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="authorizationCaptureIp" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="authorizationCaptureLocation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="authorizationCustomSharing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="authorizationLockingAndVersioning" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableConfigurableUserPIIActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableConsentAuditTrail" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableConsentEventStream" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDefaultMetadataValues" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ProductSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCascadeActivateToRelatedPrices" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableMySettings" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableQuantitySchedule" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRevenueSchedule" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSecureGuestUserRecordAccess" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Profile">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="applicationVisibilities" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileApplicationVisibility"/>
       <xsd:element name="categoryGroupVisibilities" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileCategoryGroupVisibility"/>
       <xsd:element name="classAccesses" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileApexClassAccess"/>
       <xsd:element name="custom" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="customMetadataTypeAccesses" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileCustomMetadataTypeAccess"/>
       <xsd:element name="customPermissions" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileCustomPermissions"/>
       <xsd:element name="customSettingAccesses" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileCustomSettingAccess"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="externalDataSourceAccesses" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileExternalDataSourceAccess"/>
       <xsd:element name="fieldPermissions" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileFieldLevelSecurity"/>
       <xsd:element name="flowAccesses" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileFlowAccess"/>
       <xsd:element name="layoutAssignments" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileLayoutAssignment"/>
       <xsd:element name="loginFlows" minOccurs="0" maxOccurs="unbounded" type="tns:LoginFlow"/>
       <xsd:element name="loginHours" minOccurs="0" type="tns:ProfileLoginHours"/>
       <xsd:element name="loginIpRanges" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileLoginIpRange"/>
       <xsd:element name="objectPermissions" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileObjectPermissions"/>
       <xsd:element name="pageAccesses" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileApexPageAccess"/>
       <xsd:element name="profileActionOverrides" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileActionOverride"/>
       <xsd:element name="recordTypeVisibilities" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileRecordTypeVisibility"/>
       <xsd:element name="tabVisibilities" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileTabVisibility"/>
       <xsd:element name="userLicense" minOccurs="0" type="xsd:string"/>
       <xsd:element name="userPermissions" minOccurs="0" maxOccurs="unbounded" type="tns:ProfileUserPermission"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ProfileApplicationVisibility">
    <xsd:sequence>
     <xsd:element name="application" type="xsd:string"/>
     <xsd:element name="default" type="xsd:boolean"/>
     <xsd:element name="visible" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileCategoryGroupVisibility">
    <xsd:sequence>
     <xsd:element name="dataCategories" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="dataCategoryGroup" type="xsd:string"/>
     <xsd:element name="visibility" type="tns:CategoryGroupVisibility"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="CategoryGroupVisibility">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ALL"/>
     <xsd:enumeration value="NONE"/>
     <xsd:enumeration value="CUSTOM"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ProfileApexClassAccess">
    <xsd:sequence>
     <xsd:element name="apexClass" type="xsd:string"/>
     <xsd:element name="enabled" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileCustomMetadataTypeAccess">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileCustomPermissions">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileCustomSettingAccess">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileExternalDataSourceAccess">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="externalDataSource" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileFieldLevelSecurity">
    <xsd:sequence>
     <xsd:element name="editable" type="xsd:boolean"/>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="readable" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileFlowAccess">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="flow" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileLayoutAssignment">
    <xsd:sequence>
     <xsd:element name="layout" type="xsd:string"/>
     <xsd:element name="recordType" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="LoginFlow">
    <xsd:sequence>
     <xsd:element name="flow" minOccurs="0" type="xsd:string"/>
     <xsd:element name="flowType" type="tns:LoginFlowType"/>
     <xsd:element name="friendlyName" type="xsd:string"/>
     <xsd:element name="uiLoginFlowType" type="tns:UiLoginFlowType"/>
     <xsd:element name="useLightningRuntime" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="vfFlowPage" minOccurs="0" type="xsd:string"/>
     <xsd:element name="vfFlowPageTitle" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="LoginFlowType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="UI"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="UiLoginFlowType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="VisualWorkflow"/>
     <xsd:enumeration value="VisualForce"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ProfileLoginHours">
    <xsd:sequence>
     <xsd:element name="fridayEnd" minOccurs="0" type="xsd:string"/>
     <xsd:element name="fridayStart" minOccurs="0" type="xsd:string"/>
     <xsd:element name="mondayEnd" minOccurs="0" type="xsd:string"/>
     <xsd:element name="mondayStart" minOccurs="0" type="xsd:string"/>
     <xsd:element name="saturdayEnd" minOccurs="0" type="xsd:string"/>
     <xsd:element name="saturdayStart" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sundayEnd" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sundayStart" minOccurs="0" type="xsd:string"/>
     <xsd:element name="thursdayEnd" minOccurs="0" type="xsd:string"/>
     <xsd:element name="thursdayStart" minOccurs="0" type="xsd:string"/>
     <xsd:element name="tuesdayEnd" minOccurs="0" type="xsd:string"/>
     <xsd:element name="tuesdayStart" minOccurs="0" type="xsd:string"/>
     <xsd:element name="wednesdayEnd" minOccurs="0" type="xsd:string"/>
     <xsd:element name="wednesdayStart" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileLoginIpRange">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="endAddress" type="xsd:string"/>
     <xsd:element name="startAddress" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileApexPageAccess">
    <xsd:sequence>
     <xsd:element name="apexPage" type="xsd:string"/>
     <xsd:element name="enabled" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileRecordTypeVisibility">
    <xsd:sequence>
     <xsd:element name="default" type="xsd:boolean"/>
     <xsd:element name="personAccountDefault" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="recordType" type="xsd:string"/>
     <xsd:element name="visible" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfileTabVisibility">
    <xsd:sequence>
     <xsd:element name="tab" type="xsd:string"/>
     <xsd:element name="visibility" type="tns:TabVisibility"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="TabVisibility">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Hidden"/>
     <xsd:enumeration value="DefaultOff"/>
     <xsd:enumeration value="DefaultOn"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ProfileUserPermission">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ProfilePasswordPolicy">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="forgotPasswordRedirect" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="lockoutInterval" type="xsd:int"/>
       <xsd:element name="maxLoginAttempts" type="xsd:int"/>
       <xsd:element name="minimumPasswordLength" type="xsd:int"/>
       <xsd:element name="minimumPasswordLifetime" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="obscure" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="passwordComplexity" type="xsd:int"/>
       <xsd:element name="passwordExpiration" type="xsd:int"/>
       <xsd:element name="passwordHistory" type="xsd:int"/>
       <xsd:element name="passwordQuestion" type="xsd:int"/>
       <xsd:element name="profile" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ProfileSessionSetting">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="externalCommunityUserIdentityVerif" type="xsd:boolean"/>
       <xsd:element name="forceLogout" type="xsd:boolean"/>
       <xsd:element name="profile" type="xsd:string"/>
       <xsd:element name="requiredSessionLevel" minOccurs="0" type="tns:SessionSecurityLevel"/>
       <xsd:element name="sessionPersistence" type="xsd:boolean"/>
       <xsd:element name="sessionTimeout" type="xsd:int"/>
       <xsd:element name="sessionTimeoutWarning" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="SessionSecurityLevel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="LOW"/>
     <xsd:enumeration value="STANDARD"/>
     <xsd:enumeration value="HIGH_ASSURANCE"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="Prompt">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="promptVersions" minOccurs="0" maxOccurs="unbounded" type="tns:PromptVersion"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="PromptVersion">
    <xsd:sequence>
     <xsd:element name="actionButtonLabel" minOccurs="0" type="xsd:string"/>
     <xsd:element name="actionButtonLink" minOccurs="0" type="xsd:string"/>
     <xsd:element name="body" type="xsd:string"/>
     <xsd:element name="customApplication" minOccurs="0" type="xsd:string"/>
     <xsd:element name="delayDays" minOccurs="0" type="xsd:int"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dismissButtonLabel" minOccurs="0" type="xsd:string"/>
     <xsd:element name="displayPosition" minOccurs="0" type="tns:PromptDisplayPosition"/>
     <xsd:element name="displayType" type="tns:PromptDisplayType"/>
     <xsd:element name="elementRelativePosition" minOccurs="0" type="tns:PromptElementRelativePosition"/>
     <xsd:element name="endDate" minOccurs="0" type="xsd:date"/>
     <xsd:element name="header" minOccurs="0" type="xsd:string"/>
     <xsd:element name="image" minOccurs="0" type="xsd:string"/>
     <xsd:element name="imageAltText" minOccurs="0" type="xsd:string"/>
     <xsd:element name="imageLocation" minOccurs="0" type="tns:PromptImageLocation"/>
     <xsd:element name="indexWithIsPublished" minOccurs="0" type="xsd:string"/>
     <xsd:element name="indexWithoutIsPublished" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isPublished" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="masterLabel" type="xsd:string"/>
     <xsd:element name="publishedByUser" minOccurs="0" type="xsd:string"/>
     <xsd:element name="publishedDate" minOccurs="0" type="xsd:date"/>
     <xsd:element name="referenceElementContext" minOccurs="0" type="xsd:string"/>
     <xsd:element name="shouldDisplayActionButton" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="shouldIgnoreGlobalDelay" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="startDate" minOccurs="0" type="xsd:date"/>
     <xsd:element name="stepNumber" minOccurs="0" type="xsd:int"/>
     <xsd:element name="targetAppDeveloperName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="targetAppNamespacePrefix" minOccurs="0" type="xsd:string"/>
     <xsd:element name="targetPageKey1" type="xsd:string"/>
     <xsd:element name="targetPageKey2" minOccurs="0" type="xsd:string"/>
     <xsd:element name="targetPageKey3" minOccurs="0" type="xsd:string"/>
     <xsd:element name="targetPageType" type="xsd:string"/>
     <xsd:element name="themeColor" minOccurs="0" type="tns:PromptThemeColor"/>
     <xsd:element name="themeSaturation" minOccurs="0" type="tns:PromptThemeSaturation"/>
     <xsd:element name="timesToDisplay" minOccurs="0" type="xsd:int"/>
     <xsd:element name="title" type="xsd:string"/>
     <xsd:element name="uiFormulaRule" minOccurs="0" type="tns:UiFormulaRule"/>
     <xsd:element name="userAccess" minOccurs="0" type="tns:PromptUserAccess"/>
     <xsd:element name="userProfileAccess" minOccurs="0" type="tns:PromptUserProfileAccess"/>
     <xsd:element name="versionNumber" type="xsd:int"/>
     <xsd:element name="videoLink" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="PromptDisplayPosition">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="TopLeft"/>
     <xsd:enumeration value="TopCenter"/>
     <xsd:enumeration value="TopRight"/>
     <xsd:enumeration value="BottomLeft"/>
     <xsd:enumeration value="BottomCenter"/>
     <xsd:enumeration value="BottomRight"/>
     <xsd:enumeration value="MiddleLeft"/>
     <xsd:enumeration value="MiddleCenter"/>
     <xsd:enumeration value="MiddleRight"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="PromptDisplayType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="DockedComposer"/>
     <xsd:enumeration value="FloatingPanel"/>
     <xsd:enumeration value="Targeted"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="PromptElementRelativePosition">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="TopLeft"/>
     <xsd:enumeration value="TopCenter"/>
     <xsd:enumeration value="TopRight"/>
     <xsd:enumeration value="LeftTop"/>
     <xsd:enumeration value="LeftCenter"/>
     <xsd:enumeration value="LeftBottom"/>
     <xsd:enumeration value="RightTop"/>
     <xsd:enumeration value="RightCenter"/>
     <xsd:enumeration value="RightBottom"/>
     <xsd:enumeration value="BottomLeft"/>
     <xsd:enumeration value="BottomCenter"/>
     <xsd:enumeration value="BottomRight"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="PromptImageLocation">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Top"/>
     <xsd:enumeration value="Bottom"/>
     <xsd:enumeration value="Left"/>
     <xsd:enumeration value="Right"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="PromptThemeColor">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Theme1"/>
     <xsd:enumeration value="Theme2"/>
     <xsd:enumeration value="Theme3"/>
     <xsd:enumeration value="Theme4"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="PromptThemeSaturation">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Dark"/>
     <xsd:enumeration value="Light"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="PromptUserAccess">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Everyone"/>
     <xsd:enumeration value="SpecificPermissions"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="PromptUserProfileAccess">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Everyone"/>
     <xsd:enumeration value="SpecificProfiles"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="Queue">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="doesSendEmailToMembers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="email" minOccurs="0" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="queueMembers" minOccurs="0" type="tns:QueueMembers"/>
       <xsd:element name="queueRoutingConfig" minOccurs="0" type="xsd:string"/>
       <xsd:element name="queueSobject" minOccurs="0" maxOccurs="unbounded" type="tns:QueueSobject"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="QueueMembers">
    <xsd:sequence>
     <xsd:element name="publicGroups" minOccurs="0" type="tns:PublicGroups"/>
     <xsd:element name="roleAndSubordinates" minOccurs="0" type="tns:RoleAndSubordinates"/>
     <xsd:element name="roleAndSubordinatesInternal" minOccurs="0" type="tns:RoleAndSubordinatesInternal"/>
     <xsd:element name="roles" minOccurs="0" type="tns:Roles"/>
     <xsd:element name="users" minOccurs="0" type="tns:Users"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PublicGroups">
    <xsd:sequence>
     <xsd:element name="publicGroup" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RoleAndSubordinates">
    <xsd:sequence>
     <xsd:element name="roleAndSubordinate" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RoleAndSubordinatesInternal">
    <xsd:sequence>
     <xsd:element name="roleAndSubordinateInternal" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Roles">
    <xsd:sequence>
     <xsd:element name="role" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Users">
    <xsd:sequence>
     <xsd:element name="user" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="QueueSobject">
    <xsd:sequence>
     <xsd:element name="sobjectType" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="QueueRoutingConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="capacityPercentage" minOccurs="0" type="xsd:double"/>
       <xsd:element name="capacityWeight" minOccurs="0" type="xsd:double"/>
       <xsd:element name="dropAdditionalSkillsTimeout" minOccurs="0" type="xsd:int"/>
       <xsd:element name="isAttributeBased" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="pushTimeout" minOccurs="0" type="xsd:int"/>
       <xsd:element name="queueOverflowAssignee" minOccurs="0" type="xsd:string"/>
       <xsd:element name="routingModel" type="tns:RoutingModel"/>
       <xsd:element name="routingPriority" type="xsd:int"/>
       <xsd:element name="skills" minOccurs="0" maxOccurs="unbounded" type="tns:QueueRoutingConfigSkill"/>
       <xsd:element name="userOverflowAssignee" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="RoutingModel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="LEAST_ACTIVE"/>
     <xsd:enumeration value="MOST_AVAILABLE"/>
     <xsd:enumeration value="EXTERNAL_ROUTING"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="QueueRoutingConfigSkill">
    <xsd:sequence>
     <xsd:element name="skill" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="QuickAction">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionSubtype" minOccurs="0" type="tns:ActionSubtype"/>
       <xsd:element name="canvas" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="fieldOverrides" minOccurs="0" maxOccurs="unbounded" type="tns:FieldOverride"/>
       <xsd:element name="flowDefinition" minOccurs="0" type="xsd:string"/>
       <xsd:element name="height" minOccurs="0" type="xsd:int"/>
       <xsd:element name="icon" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" minOccurs="0" type="xsd:string"/>
       <xsd:element name="lightningComponent" minOccurs="0" type="xsd:string"/>
       <xsd:element name="lightningWebComponent" minOccurs="0" type="xsd:string"/>
       <xsd:element name="optionsCreateFeedItem" type="xsd:boolean"/>
       <xsd:element name="page" minOccurs="0" type="xsd:string"/>
       <xsd:element name="quickActionLayout" minOccurs="0" type="tns:QuickActionLayout"/>
       <xsd:element name="quickActionSendEmailOptions" minOccurs="0" type="tns:QuickActionSendEmailOptions"/>
       <xsd:element name="standardLabel" minOccurs="0" type="tns:QuickActionLabel"/>
       <xsd:element name="successMessage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="targetObject" minOccurs="0" type="xsd:string"/>
       <xsd:element name="targetParentField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="targetRecordType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="type" type="tns:QuickActionType"/>
       <xsd:element name="width" minOccurs="0" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ActionSubtype">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ScreenAction"/>
     <xsd:enumeration value="Action"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="FieldOverride">
    <xsd:sequence>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="formula" minOccurs="0" type="xsd:string"/>
     <xsd:element name="literalValue" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="QuickActionLayout">
    <xsd:sequence>
     <xsd:element name="layoutSectionStyle" type="tns:LayoutSectionStyle"/>
     <xsd:element name="quickActionLayoutColumns" minOccurs="0" maxOccurs="unbounded" type="tns:QuickActionLayoutColumn"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="QuickActionLayoutColumn">
    <xsd:sequence>
     <xsd:element name="quickActionLayoutItems" minOccurs="0" maxOccurs="unbounded" type="tns:QuickActionLayoutItem"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="QuickActionLayoutItem">
    <xsd:sequence>
     <xsd:element name="emptySpace" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="field" minOccurs="0" type="xsd:string"/>
     <xsd:element name="uiBehavior" minOccurs="0" type="tns:UiBehavior"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="QuickActionSendEmailOptions">
    <xsd:sequence>
     <xsd:element name="defaultEmailTemplateName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="ignoreDefaultEmailTemplateSubject" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="QuickActionLabel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="LogACall"/>
     <xsd:enumeration value="LogANote"/>
     <xsd:enumeration value="New"/>
     <xsd:enumeration value="NewRecordType"/>
     <xsd:enumeration value="Update"/>
     <xsd:enumeration value="NewChild"/>
     <xsd:enumeration value="NewChildRecordType"/>
     <xsd:enumeration value="CreateNew"/>
     <xsd:enumeration value="CreateNewRecordType"/>
     <xsd:enumeration value="SendEmail"/>
     <xsd:enumeration value="QuickRecordType"/>
     <xsd:enumeration value="Quick"/>
     <xsd:enumeration value="EditDescription"/>
     <xsd:enumeration value="Defer"/>
     <xsd:enumeration value="ChangeDueDate"/>
     <xsd:enumeration value="ChangePriority"/>
     <xsd:enumeration value="ChangeStatus"/>
     <xsd:enumeration value="SocialPost"/>
     <xsd:enumeration value="Escalate"/>
     <xsd:enumeration value="EscalateToRecord"/>
     <xsd:enumeration value="OfferFeedback"/>
     <xsd:enumeration value="RequestFeedback"/>
     <xsd:enumeration value="AddRecord"/>
     <xsd:enumeration value="AddMember"/>
     <xsd:enumeration value="Reply"/>
     <xsd:enumeration value="ReplyAll"/>
     <xsd:enumeration value="Forward"/>
     <xsd:enumeration value="ScheduleAppointment"/>
     <xsd:enumeration value="EnrollInProgram"/>
     <xsd:enumeration value="ModifyAppointment"/>
     <xsd:enumeration value="Quip"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="QuickActionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Create"/>
     <xsd:enumeration value="VisualforcePage"/>
     <xsd:enumeration value="Post"/>
     <xsd:enumeration value="SendEmail"/>
     <xsd:enumeration value="LogACall"/>
     <xsd:enumeration value="SocialPost"/>
     <xsd:enumeration value="Canvas"/>
     <xsd:enumeration value="Update"/>
     <xsd:enumeration value="LightningComponent"/>
     <xsd:enumeration value="LightningWebComponent"/>
     <xsd:enumeration value="Flow"/>
     <xsd:enumeration value="MobileExtension"/>
     <xsd:enumeration value="Quip"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="QuickTextSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="hideQuickTextUiInLtng" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="lightningQuickTextEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="quickTextsInFolders" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="QuoteSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableQuote" type="xsd:boolean"/>
       <xsd:element name="enableQuotesWithoutOppEnabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="RealTimeEventSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="realTimeEvents" minOccurs="0" maxOccurs="unbounded" type="tns:RealTimeEvent"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="RealTimeEvent">
    <xsd:sequence>
     <xsd:element name="entityName" type="xsd:string"/>
     <xsd:element name="isEnabled" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RecommendationBuilderSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableErbEnabledPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableErbStartedPref" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="RecommendationStrategy">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actionContext" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyAction"/>
       <xsd:element name="contextRecordType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="filter" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyNodeFilter"/>
       <xsd:element name="if" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyNodeIf"/>
       <xsd:element name="invocableAction" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyNodeInvocableAction"/>
       <xsd:element name="isTemplate" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="map" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyNodeMap"/>
       <xsd:element name="mutuallyExclusive" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyNodeExclusive"/>
       <xsd:element name="onBehalfOfExpression" minOccurs="0" type="xsd:string"/>
       <xsd:element name="recommendationLimit" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyNodeRecommendationLimit"/>
       <xsd:element name="recommendationLoad" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyNodeRecommendationLoad"/>
       <xsd:element name="sort" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyNodeSort"/>
       <xsd:element name="union" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyNodeUnion"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="StrategyAction">
    <xsd:sequence>
     <xsd:element name="action" type="xsd:string"/>
     <xsd:element name="argument" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyActionArg"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="type" type="tns:InvocableActionType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="StrategyActionArg">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="value" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="StrategyNodeFilter">
    <xsd:complexContent>
     <xsd:extension base="tns:StrategyNodeUnionBase">
      <xsd:sequence>
       <xsd:element name="expression" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="StrategyNodeUnionBase">
    <xsd:complexContent>
     <xsd:extension base="tns:StrategyNodeBase">
      <xsd:sequence>
       <xsd:element name="limit" minOccurs="0" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="StrategyNodeBase">
    <xsd:sequence>
     <xsd:element name="childNode" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="StrategyNodeExclusive">
    <xsd:complexContent>
     <xsd:extension base="tns:StrategyNodeUnionBase">
      <xsd:sequence/>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="StrategyNodeIf">
    <xsd:complexContent>
     <xsd:extension base="tns:StrategyNodeUnionBase">
      <xsd:sequence>
       <xsd:element name="childNodeExpression" minOccurs="0" maxOccurs="unbounded" type="tns:IfExpression"/>
       <xsd:element name="onlyFirstMatch" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="IfExpression">
    <xsd:sequence>
     <xsd:element name="childName" type="xsd:string"/>
     <xsd:element name="expression" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="StrategyNodeInvocableAction">
    <xsd:complexContent>
     <xsd:extension base="tns:StrategyNodeUnionBase">
      <xsd:sequence>
       <xsd:element name="action" type="xsd:string"/>
       <xsd:element name="argument" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyNodeInvocableActionArg"/>
       <xsd:element name="isGenerator" type="xsd:boolean"/>
       <xsd:element name="type" type="tns:InvocableActionType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="StrategyNodeInvocableActionArg">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="value" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="StrategyNodeMap">
    <xsd:complexContent>
     <xsd:extension base="tns:StrategyNodeUnionBase">
      <xsd:sequence>
       <xsd:element name="mapExpression" minOccurs="0" maxOccurs="unbounded" type="tns:MapExpression"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="MapExpression">
    <xsd:sequence>
     <xsd:element name="expression" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="type" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="StrategyNodeRecommendationLimit">
    <xsd:complexContent>
     <xsd:extension base="tns:StrategyNodeUnionBase">
      <xsd:sequence>
       <xsd:element name="filterMode" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyReactionType"/>
       <xsd:element name="lookbackDuration" minOccurs="0" type="xsd:int"/>
       <xsd:element name="maxRecommendationCount" minOccurs="0" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="StrategyReactionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Accepted"/>
     <xsd:enumeration value="Rejected"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="StrategyNodeRecommendationLoad">
    <xsd:complexContent>
     <xsd:extension base="tns:StrategyNodeUnionBase">
      <xsd:sequence>
       <xsd:element name="condition" minOccurs="0" maxOccurs="unbounded" type="tns:RecommendationLoadCondition"/>
       <xsd:element name="conditionLogic" minOccurs="0" type="xsd:string"/>
       <xsd:element name="object" type="xsd:string"/>
       <xsd:element name="sortField" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyNodeSortField"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="RecommendationLoadCondition">
    <xsd:sequence>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="operator" type="tns:RecommendationConditionOperator"/>
     <xsd:element name="value" type="tns:RecommendationConditionValue"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="RecommendationConditionOperator">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="EQUALS"/>
     <xsd:enumeration value="GREATER_THAN"/>
     <xsd:enumeration value="GREATER_THAN_OR_EQUAL_TO"/>
     <xsd:enumeration value="LESS_THAN"/>
     <xsd:enumeration value="LESS_THAN_OR_EQUAL_TO"/>
     <xsd:enumeration value="NOT_EQUALS"/>
     <xsd:enumeration value="LIKE"/>
     <xsd:enumeration value="STARTS_WITH"/>
     <xsd:enumeration value="ENDS_WITH"/>
     <xsd:enumeration value="CONTAINS"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="RecommendationConditionValue">
    <xsd:sequence>
     <xsd:element name="type" type="tns:RecommendationConditionValueType"/>
     <xsd:element name="value" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="RecommendationConditionValueType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="TEXT"/>
     <xsd:enumeration value="NUMBER"/>
     <xsd:enumeration value="BOOLEAN"/>
     <xsd:enumeration value="DATE"/>
     <xsd:enumeration value="DATE_TIME"/>
     <xsd:enumeration value="TIME"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="StrategyNodeSortField">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="nullsFirst" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="order" minOccurs="0" type="tns:SortOrder"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="StrategyNodeSort">
    <xsd:complexContent>
     <xsd:extension base="tns:StrategyNodeUnionBase">
      <xsd:sequence>
       <xsd:element name="field" minOccurs="0" maxOccurs="unbounded" type="tns:StrategyNodeSortField"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="StrategyNodeUnion">
    <xsd:complexContent>
     <xsd:extension base="tns:StrategyNodeUnionBase">
      <xsd:sequence/>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="RecordActionDeployment">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="channelConfigurations" minOccurs="0" maxOccurs="unbounded" type="tns:RecordActionDeploymentChannel"/>
       <xsd:element name="deploymentContexts" minOccurs="0" maxOccurs="unbounded" type="tns:RecordActionDeploymentContext"/>
       <xsd:element name="hasGuidedActions" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="hasRecommendations" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="recommendation" minOccurs="0" type="tns:RecordActionRecommendation"/>
       <xsd:element name="selectableItems" minOccurs="0" maxOccurs="unbounded" type="tns:RecordActionSelectableItem"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="RecordActionDeploymentChannel">
    <xsd:sequence>
     <xsd:element name="channel" type="tns:ChannelSource"/>
     <xsd:element name="channelItems" minOccurs="0" maxOccurs="unbounded" type="tns:RecordActionDefaultItem"/>
     <xsd:element name="isAutopopEnabled" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ChannelSource">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Other"/>
     <xsd:enumeration value="Phone"/>
     <xsd:enumeration value="Chat"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="RecordActionDefaultItem">
    <xsd:sequence>
     <xsd:element name="action" type="xsd:string"/>
     <xsd:element name="isMandatory" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="isUiRemoveHidden" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="pinned" type="tns:PinnedAction"/>
     <xsd:element name="position" type="xsd:int"/>
     <xsd:element name="type" type="tns:RecordActionType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="PinnedAction">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="Top"/>
     <xsd:enumeration value="Bottom"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="RecordActionType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Flow"/>
     <xsd:enumeration value="QuickAction"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="RecordActionDeploymentContext">
    <xsd:sequence>
     <xsd:element name="entityName" type="xsd:string"/>
     <xsd:element name="recommendationStrategy" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RecordActionRecommendation">
    <xsd:sequence>
     <xsd:element name="defaultStrategy" minOccurs="0" type="xsd:string"/>
     <xsd:element name="hasDescription" type="xsd:boolean"/>
     <xsd:element name="hasImage" type="xsd:boolean"/>
     <xsd:element name="hasRejectAction" type="xsd:boolean"/>
     <xsd:element name="hasTitle" type="xsd:boolean"/>
     <xsd:element name="maxDisplayRecommendations" type="xsd:int"/>
     <xsd:element name="shouldLaunchActionOnReject" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RecordActionSelectableItem">
    <xsd:sequence>
     <xsd:element name="action" type="xsd:string"/>
     <xsd:element name="type" type="tns:RecordActionType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RecordPageSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableActivityRelatedList" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableFullRecordView" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="RedirectWhitelistUrl">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="url" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="RemoteSiteSetting">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="disableProtocolSecurity" type="xsd:boolean"/>
       <xsd:element name="isActive" type="xsd:boolean"/>
       <xsd:element name="url" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Report">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="aggregates" minOccurs="0" maxOccurs="unbounded" type="tns:ReportAggregate"/>
       <xsd:element name="block" minOccurs="0" maxOccurs="unbounded" type="tns:Report"/>
       <xsd:element name="blockInfo" minOccurs="0" type="tns:ReportBlockInfo"/>
       <xsd:element name="buckets" minOccurs="0" maxOccurs="unbounded" type="tns:ReportBucketField"/>
       <xsd:element name="chart" minOccurs="0" type="tns:ReportChart"/>
       <xsd:element name="colorRanges" minOccurs="0" maxOccurs="unbounded" type="tns:ReportColorRange"/>
       <xsd:element name="columns" minOccurs="0" maxOccurs="unbounded" type="tns:ReportColumn"/>
       <xsd:element name="crossFilters" minOccurs="0" maxOccurs="unbounded" type="tns:ReportCrossFilter"/>
       <xsd:element name="currency" minOccurs="0" type="tns:CurrencyIsoCode"/>
       <xsd:element name="customDetailFormulas" minOccurs="0" maxOccurs="unbounded" type="tns:ReportCustomDetailFormula"/>
       <xsd:element name="dataCategoryFilters" minOccurs="0" maxOccurs="unbounded" type="tns:ReportDataCategoryFilter"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="division" minOccurs="0" type="xsd:string"/>
       <xsd:element name="filter" minOccurs="0" type="tns:ReportFilter"/>
       <xsd:element name="folderName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="format" type="tns:ReportFormat"/>
       <xsd:element name="formattingRules" minOccurs="0" maxOccurs="unbounded" type="tns:ReportFormattingRule"/>
       <xsd:element name="groupingsAcross" minOccurs="0" maxOccurs="unbounded" type="tns:ReportGrouping"/>
       <xsd:element name="groupingsDown" minOccurs="0" maxOccurs="unbounded" type="tns:ReportGrouping"/>
       <xsd:element name="historicalSelector" minOccurs="0" type="tns:ReportHistoricalSelector"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="numSubscriptions" minOccurs="0" type="xsd:int"/>
       <xsd:element name="params" minOccurs="0" maxOccurs="unbounded" type="tns:ReportParam"/>
       <xsd:element name="reportType" type="xsd:string"/>
       <xsd:element name="reportTypeApiName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="roleHierarchyFilter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="rowLimit" minOccurs="0" type="xsd:int"/>
       <xsd:element name="scope" minOccurs="0" type="xsd:string"/>
       <xsd:element name="showCurrentDate" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showDetails" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showGrandTotal" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="showSubTotals" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="sortColumn" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sortOrder" minOccurs="0" type="tns:SortOrder"/>
       <xsd:element name="territoryHierarchyFilter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="timeFrameFilter" minOccurs="0" type="tns:ReportTimeFrameFilter"/>
       <xsd:element name="userFilter" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ReportAggregate">
    <xsd:sequence>
     <xsd:element name="acrossGroupingContext" minOccurs="0" type="xsd:string"/>
     <xsd:element name="calculatedFormula" type="xsd:string"/>
     <xsd:element name="datatype" type="tns:ReportAggregateDatatype"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="downGroupingContext" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isActive" type="xsd:boolean"/>
     <xsd:element name="isCrossBlock" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="masterLabel" type="xsd:string"/>
     <xsd:element name="reportType" minOccurs="0" type="xsd:string"/>
     <xsd:element name="scale" minOccurs="0" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ReportAggregateDatatype">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="currency"/>
     <xsd:enumeration value="percent"/>
     <xsd:enumeration value="number"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ReportBlockInfo">
    <xsd:sequence>
     <xsd:element name="aggregateReferences" minOccurs="0" maxOccurs="unbounded" type="tns:ReportAggregateReference"/>
     <xsd:element name="blockId" type="xsd:string"/>
     <xsd:element name="joinTable" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportAggregateReference">
    <xsd:sequence>
     <xsd:element name="aggregate" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportBucketField">
    <xsd:sequence>
     <xsd:element name="bucketType" type="tns:ReportBucketFieldType"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="masterLabel" type="xsd:string"/>
     <xsd:element name="nullTreatment" minOccurs="0" type="tns:ReportFormulaNullTreatment"/>
     <xsd:element name="otherBucketLabel" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sourceColumnName" type="xsd:string"/>
     <xsd:element name="useOther" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="values" minOccurs="0" maxOccurs="unbounded" type="tns:ReportBucketFieldValue"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ReportBucketFieldType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="text"/>
     <xsd:enumeration value="number"/>
     <xsd:enumeration value="picklist"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ReportFormulaNullTreatment">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="n"/>
     <xsd:enumeration value="z"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ReportBucketFieldValue">
    <xsd:sequence>
     <xsd:element name="sourceValues" minOccurs="0" maxOccurs="unbounded" type="tns:ReportBucketFieldSourceValue"/>
     <xsd:element name="value" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportBucketFieldSourceValue">
    <xsd:sequence>
     <xsd:element name="from" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sourceValue" minOccurs="0" type="xsd:string"/>
     <xsd:element name="to" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportChart">
    <xsd:sequence>
     <xsd:element name="backgroundColor1" minOccurs="0" type="xsd:string"/>
     <xsd:element name="backgroundColor2" minOccurs="0" type="xsd:string"/>
     <xsd:element name="backgroundFadeDir" minOccurs="0" type="tns:ChartBackgroundDirection"/>
     <xsd:element name="chartSummaries" minOccurs="0" maxOccurs="unbounded" type="tns:ChartSummary"/>
     <xsd:element name="chartType" type="tns:ChartType"/>
     <xsd:element name="enableHoverLabels" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="expandOthers" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="groupingColumn" minOccurs="0" type="xsd:string"/>
     <xsd:element name="legendPosition" minOccurs="0" type="tns:ChartLegendPosition"/>
     <xsd:element name="location" minOccurs="0" type="tns:ChartPosition"/>
     <xsd:element name="secondaryGroupingColumn" minOccurs="0" type="xsd:string"/>
     <xsd:element name="showAxisLabels" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showPercentage" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showTotal" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showValues" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="size" minOccurs="0" type="tns:ReportChartSize"/>
     <xsd:element name="summaryAxisManualRangeEnd" minOccurs="0" type="xsd:double"/>
     <xsd:element name="summaryAxisManualRangeStart" minOccurs="0" type="xsd:double"/>
     <xsd:element name="summaryAxisRange" minOccurs="0" type="tns:ChartRangeType"/>
     <xsd:element name="textColor" minOccurs="0" type="xsd:string"/>
     <xsd:element name="textSize" minOccurs="0" type="xsd:int"/>
     <xsd:element name="title" minOccurs="0" type="xsd:string"/>
     <xsd:element name="titleColor" minOccurs="0" type="xsd:string"/>
     <xsd:element name="titleSize" minOccurs="0" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ChartType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="Scatter"/>
     <xsd:enumeration value="ScatterGrouped"/>
     <xsd:enumeration value="Bubble"/>
     <xsd:enumeration value="BubbleGrouped"/>
     <xsd:enumeration value="HorizontalBar"/>
     <xsd:enumeration value="HorizontalBarGrouped"/>
     <xsd:enumeration value="HorizontalBarStacked"/>
     <xsd:enumeration value="HorizontalBarStackedTo100"/>
     <xsd:enumeration value="VerticalColumn"/>
     <xsd:enumeration value="VerticalColumnGrouped"/>
     <xsd:enumeration value="VerticalColumnStacked"/>
     <xsd:enumeration value="VerticalColumnStackedTo100"/>
     <xsd:enumeration value="Line"/>
     <xsd:enumeration value="LineGrouped"/>
     <xsd:enumeration value="LineCumulative"/>
     <xsd:enumeration value="LineCumulativeGrouped"/>
     <xsd:enumeration value="Pie"/>
     <xsd:enumeration value="Donut"/>
     <xsd:enumeration value="Funnel"/>
     <xsd:enumeration value="VerticalColumnLine"/>
     <xsd:enumeration value="VerticalColumnGroupedLine"/>
     <xsd:enumeration value="VerticalColumnStackedLine"/>
     <xsd:enumeration value="Plugin"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ChartPosition">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="CHART_TOP"/>
     <xsd:enumeration value="CHART_BOTTOM"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ReportChartSize">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Tiny"/>
     <xsd:enumeration value="Small"/>
     <xsd:enumeration value="Medium"/>
     <xsd:enumeration value="Large"/>
     <xsd:enumeration value="Huge"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ReportColorRange">
    <xsd:sequence>
     <xsd:element name="aggregate" minOccurs="0" type="tns:ReportSummaryType"/>
     <xsd:element name="columnName" type="xsd:string"/>
     <xsd:element name="highBreakpoint" minOccurs="0" type="xsd:double"/>
     <xsd:element name="highColor" type="xsd:string"/>
     <xsd:element name="lowBreakpoint" minOccurs="0" type="xsd:double"/>
     <xsd:element name="lowColor" type="xsd:string"/>
     <xsd:element name="midColor" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportColumn">
    <xsd:sequence>
     <xsd:element name="aggregateTypes" minOccurs="0" maxOccurs="unbounded" type="tns:ReportSummaryType"/>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="reverseColors" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showChanges" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportCrossFilter">
    <xsd:sequence>
     <xsd:element name="criteriaItems" minOccurs="0" maxOccurs="unbounded" type="tns:ReportFilterItem"/>
     <xsd:element name="operation" type="tns:ObjectFilterOperator"/>
     <xsd:element name="primaryTableColumn" type="xsd:string"/>
     <xsd:element name="relatedTable" type="xsd:string"/>
     <xsd:element name="relatedTableJoinColumn" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportFilterItem">
    <xsd:sequence>
     <xsd:element name="column" type="xsd:string"/>
     <xsd:element name="columnToColumn" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="isUnlocked" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="operator" type="tns:FilterOperation"/>
     <xsd:element name="snapshot" minOccurs="0" type="xsd:string"/>
     <xsd:element name="value" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ObjectFilterOperator">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="with"/>
     <xsd:enumeration value="without"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="CurrencyIsoCode">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ADP"/>
     <xsd:enumeration value="AED"/>
     <xsd:enumeration value="AFA"/>
     <xsd:enumeration value="AFN"/>
     <xsd:enumeration value="ALL"/>
     <xsd:enumeration value="AMD"/>
     <xsd:enumeration value="ANG"/>
     <xsd:enumeration value="AOA"/>
     <xsd:enumeration value="ARS"/>
     <xsd:enumeration value="ATS"/>
     <xsd:enumeration value="AUD"/>
     <xsd:enumeration value="AWG"/>
     <xsd:enumeration value="AZM"/>
     <xsd:enumeration value="AZN"/>
     <xsd:enumeration value="BAM"/>
     <xsd:enumeration value="BBD"/>
     <xsd:enumeration value="BDT"/>
     <xsd:enumeration value="BEF"/>
     <xsd:enumeration value="BGL"/>
     <xsd:enumeration value="BGN"/>
     <xsd:enumeration value="BHD"/>
     <xsd:enumeration value="BIF"/>
     <xsd:enumeration value="BMD"/>
     <xsd:enumeration value="BND"/>
     <xsd:enumeration value="BOB"/>
     <xsd:enumeration value="BOV"/>
     <xsd:enumeration value="BRB"/>
     <xsd:enumeration value="BRL"/>
     <xsd:enumeration value="BSD"/>
     <xsd:enumeration value="BTN"/>
     <xsd:enumeration value="BWP"/>
     <xsd:enumeration value="BYB"/>
     <xsd:enumeration value="BYN"/>
     <xsd:enumeration value="BYR"/>
     <xsd:enumeration value="BZD"/>
     <xsd:enumeration value="CAD"/>
     <xsd:enumeration value="CDF"/>
     <xsd:enumeration value="CHF"/>
     <xsd:enumeration value="CLF"/>
     <xsd:enumeration value="CLP"/>
     <xsd:enumeration value="CNH"/>
     <xsd:enumeration value="CNY"/>
     <xsd:enumeration value="COP"/>
     <xsd:enumeration value="CRC"/>
     <xsd:enumeration value="CSD"/>
     <xsd:enumeration value="CUC"/>
     <xsd:enumeration value="CUP"/>
     <xsd:enumeration value="CVE"/>
     <xsd:enumeration value="CYP"/>
     <xsd:enumeration value="CZK"/>
     <xsd:enumeration value="DEM"/>
     <xsd:enumeration value="DJF"/>
     <xsd:enumeration value="DKK"/>
     <xsd:enumeration value="DOP"/>
     <xsd:enumeration value="DZD"/>
     <xsd:enumeration value="ECS"/>
     <xsd:enumeration value="EEK"/>
     <xsd:enumeration value="EGP"/>
     <xsd:enumeration value="ERN"/>
     <xsd:enumeration value="ESP"/>
     <xsd:enumeration value="ETB"/>
     <xsd:enumeration value="EUR"/>
     <xsd:enumeration value="FIM"/>
     <xsd:enumeration value="FJD"/>
     <xsd:enumeration value="FKP"/>
     <xsd:enumeration value="FRF"/>
     <xsd:enumeration value="GBP"/>
     <xsd:enumeration value="GEL"/>
     <xsd:enumeration value="GHC"/>
     <xsd:enumeration value="GHS"/>
     <xsd:enumeration value="GIP"/>
     <xsd:enumeration value="GMD"/>
     <xsd:enumeration value="GNF"/>
     <xsd:enumeration value="GRD"/>
     <xsd:enumeration value="GTQ"/>
     <xsd:enumeration value="GWP"/>
     <xsd:enumeration value="GYD"/>
     <xsd:enumeration value="HKD"/>
     <xsd:enumeration value="HNL"/>
     <xsd:enumeration value="HRD"/>
     <xsd:enumeration value="HRK"/>
     <xsd:enumeration value="HTG"/>
     <xsd:enumeration value="HUF"/>
     <xsd:enumeration value="IDR"/>
     <xsd:enumeration value="IEP"/>
     <xsd:enumeration value="ILS"/>
     <xsd:enumeration value="INR"/>
     <xsd:enumeration value="IQD"/>
     <xsd:enumeration value="IRR"/>
     <xsd:enumeration value="ISK"/>
     <xsd:enumeration value="ITL"/>
     <xsd:enumeration value="JMD"/>
     <xsd:enumeration value="JOD"/>
     <xsd:enumeration value="JPY"/>
     <xsd:enumeration value="KES"/>
     <xsd:enumeration value="KGS"/>
     <xsd:enumeration value="KHR"/>
     <xsd:enumeration value="KMF"/>
     <xsd:enumeration value="KPW"/>
     <xsd:enumeration value="KRW"/>
     <xsd:enumeration value="KWD"/>
     <xsd:enumeration value="KYD"/>
     <xsd:enumeration value="KZT"/>
     <xsd:enumeration value="LAK"/>
     <xsd:enumeration value="LBP"/>
     <xsd:enumeration value="LKR"/>
     <xsd:enumeration value="LRD"/>
     <xsd:enumeration value="LSL"/>
     <xsd:enumeration value="LTL"/>
     <xsd:enumeration value="LUF"/>
     <xsd:enumeration value="LVL"/>
     <xsd:enumeration value="LYD"/>
     <xsd:enumeration value="MAD"/>
     <xsd:enumeration value="MDL"/>
     <xsd:enumeration value="MGA"/>
     <xsd:enumeration value="MGF"/>
     <xsd:enumeration value="MKD"/>
     <xsd:enumeration value="MMK"/>
     <xsd:enumeration value="MNT"/>
     <xsd:enumeration value="MOP"/>
     <xsd:enumeration value="MRO"/>
     <xsd:enumeration value="MRU"/>
     <xsd:enumeration value="MTL"/>
     <xsd:enumeration value="MUR"/>
     <xsd:enumeration value="MVR"/>
     <xsd:enumeration value="MWK"/>
     <xsd:enumeration value="MXN"/>
     <xsd:enumeration value="MXV"/>
     <xsd:enumeration value="MYR"/>
     <xsd:enumeration value="MZM"/>
     <xsd:enumeration value="MZN"/>
     <xsd:enumeration value="NAD"/>
     <xsd:enumeration value="NGN"/>
     <xsd:enumeration value="NIO"/>
     <xsd:enumeration value="NLG"/>
     <xsd:enumeration value="NOK"/>
     <xsd:enumeration value="NPR"/>
     <xsd:enumeration value="NZD"/>
     <xsd:enumeration value="OMR"/>
     <xsd:enumeration value="PAB"/>
     <xsd:enumeration value="PEN"/>
     <xsd:enumeration value="PGK"/>
     <xsd:enumeration value="PHP"/>
     <xsd:enumeration value="PKR"/>
     <xsd:enumeration value="PLN"/>
     <xsd:enumeration value="PTE"/>
     <xsd:enumeration value="PYG"/>
     <xsd:enumeration value="QAR"/>
     <xsd:enumeration value="RMB"/>
     <xsd:enumeration value="ROL"/>
     <xsd:enumeration value="RON"/>
     <xsd:enumeration value="RSD"/>
     <xsd:enumeration value="RUB"/>
     <xsd:enumeration value="RUR"/>
     <xsd:enumeration value="RWF"/>
     <xsd:enumeration value="SAR"/>
     <xsd:enumeration value="SBD"/>
     <xsd:enumeration value="SCR"/>
     <xsd:enumeration value="SDD"/>
     <xsd:enumeration value="SDG"/>
     <xsd:enumeration value="SEK"/>
     <xsd:enumeration value="SGD"/>
     <xsd:enumeration value="SHP"/>
     <xsd:enumeration value="SIT"/>
     <xsd:enumeration value="SKK"/>
     <xsd:enumeration value="SLL"/>
     <xsd:enumeration value="SOS"/>
     <xsd:enumeration value="SRD"/>
     <xsd:enumeration value="SRG"/>
     <xsd:enumeration value="SSP"/>
     <xsd:enumeration value="STD"/>
     <xsd:enumeration value="STN"/>
     <xsd:enumeration value="SUR"/>
     <xsd:enumeration value="SVC"/>
     <xsd:enumeration value="SYP"/>
     <xsd:enumeration value="SZL"/>
     <xsd:enumeration value="THB"/>
     <xsd:enumeration value="TJR"/>
     <xsd:enumeration value="TJS"/>
     <xsd:enumeration value="TMM"/>
     <xsd:enumeration value="TMT"/>
     <xsd:enumeration value="TND"/>
     <xsd:enumeration value="TOP"/>
     <xsd:enumeration value="TPE"/>
     <xsd:enumeration value="TRL"/>
     <xsd:enumeration value="TRY"/>
     <xsd:enumeration value="TTD"/>
     <xsd:enumeration value="TWD"/>
     <xsd:enumeration value="TZS"/>
     <xsd:enumeration value="UAH"/>
     <xsd:enumeration value="UGX"/>
     <xsd:enumeration value="USD"/>
     <xsd:enumeration value="UYU"/>
     <xsd:enumeration value="UZS"/>
     <xsd:enumeration value="VEB"/>
     <xsd:enumeration value="VEF"/>
     <xsd:enumeration value="VES"/>
     <xsd:enumeration value="VND"/>
     <xsd:enumeration value="VUV"/>
     <xsd:enumeration value="WST"/>
     <xsd:enumeration value="XAF"/>
     <xsd:enumeration value="XCD"/>
     <xsd:enumeration value="XOF"/>
     <xsd:enumeration value="XPF"/>
     <xsd:enumeration value="YER"/>
     <xsd:enumeration value="YUM"/>
     <xsd:enumeration value="ZAR"/>
     <xsd:enumeration value="ZMK"/>
     <xsd:enumeration value="ZMW"/>
     <xsd:enumeration value="ZWD"/>
     <xsd:enumeration value="ZWL"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ReportCustomDetailFormula">
    <xsd:sequence>
     <xsd:element name="calculatedFormula" type="xsd:string"/>
     <xsd:element name="dataType" type="xsd:string"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="developerName" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="scale" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportDataCategoryFilter">
    <xsd:sequence>
     <xsd:element name="dataCategory" type="xsd:string"/>
     <xsd:element name="dataCategoryGroup" type="xsd:string"/>
     <xsd:element name="operator" type="tns:DataCategoryFilterOperation"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DataCategoryFilterOperation">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="above"/>
     <xsd:enumeration value="below"/>
     <xsd:enumeration value="at"/>
     <xsd:enumeration value="aboveOrBelow"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ReportFilter">
    <xsd:sequence>
     <xsd:element name="booleanFilter" minOccurs="0" type="xsd:string"/>
     <xsd:element name="criteriaItems" minOccurs="0" maxOccurs="unbounded" type="tns:ReportFilterItem"/>
     <xsd:element name="language" minOccurs="0" type="tns:Language"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ReportFormat">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="MultiBlock"/>
     <xsd:enumeration value="Matrix"/>
     <xsd:enumeration value="Summary"/>
     <xsd:enumeration value="Tabular"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ReportFormattingRule">
    <xsd:sequence>
     <xsd:element name="aggregate" minOccurs="0" type="tns:ReportSummaryType"/>
     <xsd:element name="columnName" type="xsd:string"/>
     <xsd:element name="values" minOccurs="0" maxOccurs="unbounded" type="tns:ReportFormattingRuleValue"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportFormattingRuleValue">
    <xsd:sequence>
     <xsd:element name="backgroundColor" minOccurs="0" type="xsd:string"/>
     <xsd:element name="rangeUpperBound" minOccurs="0" type="xsd:double"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportGrouping">
    <xsd:sequence>
     <xsd:element name="aggregateType" minOccurs="0" type="tns:ReportAggrType"/>
     <xsd:element name="dateGranularity" minOccurs="0" type="tns:UserDateGranularity"/>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="sortByName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sortOrder" type="tns:SortOrder"/>
     <xsd:element name="sortType" minOccurs="0" type="tns:ReportSortType"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ReportAggrType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Sum"/>
     <xsd:enumeration value="Average"/>
     <xsd:enumeration value="Maximum"/>
     <xsd:enumeration value="Minimum"/>
     <xsd:enumeration value="Unique"/>
     <xsd:enumeration value="RowCount"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="UserDateGranularity">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="Day"/>
     <xsd:enumeration value="Week"/>
     <xsd:enumeration value="Month"/>
     <xsd:enumeration value="Quarter"/>
     <xsd:enumeration value="Year"/>
     <xsd:enumeration value="FiscalQuarter"/>
     <xsd:enumeration value="FiscalYear"/>
     <xsd:enumeration value="MonthInYear"/>
     <xsd:enumeration value="DayInMonth"/>
     <xsd:enumeration value="FiscalPeriod"/>
     <xsd:enumeration value="FiscalWeek"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ReportSortType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Column"/>
     <xsd:enumeration value="Aggregate"/>
     <xsd:enumeration value="CustomSummaryFormula"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ReportHistoricalSelector">
    <xsd:sequence>
     <xsd:element name="snapshot" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportParam">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="value" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportTimeFrameFilter">
    <xsd:sequence>
     <xsd:element name="dateColumn" type="xsd:string"/>
     <xsd:element name="endDate" minOccurs="0" type="xsd:date"/>
     <xsd:element name="interval" type="tns:UserDateInterval"/>
     <xsd:element name="startDate" minOccurs="0" type="xsd:date"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="UserDateInterval">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="INTERVAL_CURRENT"/>
     <xsd:enumeration value="INTERVAL_CURNEXT1"/>
     <xsd:enumeration value="INTERVAL_CURPREV1"/>
     <xsd:enumeration value="INTERVAL_NEXT1"/>
     <xsd:enumeration value="INTERVAL_PREV1"/>
     <xsd:enumeration value="INTERVAL_CURNEXT3"/>
     <xsd:enumeration value="INTERVAL_CURFY"/>
     <xsd:enumeration value="INTERVAL_PREVFY"/>
     <xsd:enumeration value="INTERVAL_PREV2FY"/>
     <xsd:enumeration value="INTERVAL_AGO2FY"/>
     <xsd:enumeration value="INTERVAL_NEXTFY"/>
     <xsd:enumeration value="INTERVAL_PREVCURFY"/>
     <xsd:enumeration value="INTERVAL_PREVCUR2FY"/>
     <xsd:enumeration value="INTERVAL_CURNEXTFY"/>
     <xsd:enumeration value="INTERVAL_CUSTOM"/>
     <xsd:enumeration value="INTERVAL_YESTERDAY"/>
     <xsd:enumeration value="INTERVAL_TODAY"/>
     <xsd:enumeration value="INTERVAL_TOMORROW"/>
     <xsd:enumeration value="INTERVAL_LASTWEEK"/>
     <xsd:enumeration value="INTERVAL_THISWEEK"/>
     <xsd:enumeration value="INTERVAL_NEXTWEEK"/>
     <xsd:enumeration value="INTERVAL_LASTMONTH"/>
     <xsd:enumeration value="INTERVAL_THISMONTH"/>
     <xsd:enumeration value="INTERVAL_NEXTMONTH"/>
     <xsd:enumeration value="INTERVAL_LASTTHISMONTH"/>
     <xsd:enumeration value="INTERVAL_THISNEXTMONTH"/>
     <xsd:enumeration value="INTERVAL_CURRENTQ"/>
     <xsd:enumeration value="INTERVAL_CURNEXTQ"/>
     <xsd:enumeration value="INTERVAL_CURPREVQ"/>
     <xsd:enumeration value="INTERVAL_NEXTQ"/>
     <xsd:enumeration value="INTERVAL_PREVQ"/>
     <xsd:enumeration value="INTERVAL_CURNEXT3Q"/>
     <xsd:enumeration value="INTERVAL_CURY"/>
     <xsd:enumeration value="INTERVAL_PREVY"/>
     <xsd:enumeration value="INTERVAL_PREV2Y"/>
     <xsd:enumeration value="INTERVAL_AGO2Y"/>
     <xsd:enumeration value="INTERVAL_NEXTY"/>
     <xsd:enumeration value="INTERVAL_PREVCURY"/>
     <xsd:enumeration value="INTERVAL_PREVCUR2Y"/>
     <xsd:enumeration value="INTERVAL_CURNEXTY"/>
     <xsd:enumeration value="INTERVAL_LAST7"/>
     <xsd:enumeration value="INTERVAL_LAST30"/>
     <xsd:enumeration value="INTERVAL_LAST60"/>
     <xsd:enumeration value="INTERVAL_LAST90"/>
     <xsd:enumeration value="INTERVAL_LAST120"/>
     <xsd:enumeration value="INTERVAL_NEXT7"/>
     <xsd:enumeration value="INTERVAL_NEXT30"/>
     <xsd:enumeration value="INTERVAL_NEXT60"/>
     <xsd:enumeration value="INTERVAL_NEXT90"/>
     <xsd:enumeration value="INTERVAL_NEXT120"/>
     <xsd:enumeration value="LAST_FISCALWEEK"/>
     <xsd:enumeration value="THIS_FISCALWEEK"/>
     <xsd:enumeration value="NEXT_FISCALWEEK"/>
     <xsd:enumeration value="LAST_FISCALPERIOD"/>
     <xsd:enumeration value="THIS_FISCALPERIOD"/>
     <xsd:enumeration value="NEXT_FISCALPERIOD"/>
     <xsd:enumeration value="LASTTHIS_FISCALPERIOD"/>
     <xsd:enumeration value="THISNEXT_FISCALPERIOD"/>
     <xsd:enumeration value="CURRENT_ENTITLEMENT_PERIOD"/>
     <xsd:enumeration value="PREVIOUS_ENTITLEMENT_PERIOD"/>
     <xsd:enumeration value="PREVIOUS_TWO_ENTITLEMENT_PERIODS"/>
     <xsd:enumeration value="TWO_ENTITLEMENT_PERIODS_AGO"/>
     <xsd:enumeration value="CURRENT_AND_PREVIOUS_ENTITLEMENT_PERIOD"/>
     <xsd:enumeration value="CURRENT_AND_PREVIOUS_TWO_ENTITLEMENT_PERIODS"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ReportType">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="autogenerated" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="baseObject" type="xsd:string"/>
       <xsd:element name="category" type="tns:ReportTypeCategory"/>
       <xsd:element name="deployed" type="xsd:boolean"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="join" minOccurs="0" type="tns:ObjectRelationship"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="sections" minOccurs="0" maxOccurs="unbounded" type="tns:ReportLayoutSection"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ReportTypeCategory">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="accounts"/>
     <xsd:enumeration value="opportunities"/>
     <xsd:enumeration value="forecasts"/>
     <xsd:enumeration value="cases"/>
     <xsd:enumeration value="leads"/>
     <xsd:enumeration value="campaigns"/>
     <xsd:enumeration value="activities"/>
     <xsd:enumeration value="busop"/>
     <xsd:enumeration value="products"/>
     <xsd:enumeration value="admin"/>
     <xsd:enumeration value="territory"/>
     <xsd:enumeration value="other"/>
     <xsd:enumeration value="content"/>
     <xsd:enumeration value="usage_entitlement"/>
     <xsd:enumeration value="wdc"/>
     <xsd:enumeration value="calibration"/>
     <xsd:enumeration value="territory2"/>
     <xsd:enumeration value="quotes"/>
     <xsd:enumeration value="individual"/>
     <xsd:enumeration value="employee"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ObjectRelationship">
    <xsd:sequence>
     <xsd:element name="join" minOccurs="0" type="tns:ObjectRelationship"/>
     <xsd:element name="outerJoin" type="xsd:boolean"/>
     <xsd:element name="relationship" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportLayoutSection">
    <xsd:sequence>
     <xsd:element name="columns" minOccurs="0" maxOccurs="unbounded" type="tns:ReportTypeColumn"/>
     <xsd:element name="masterLabel" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportTypeColumn">
    <xsd:sequence>
     <xsd:element name="checkedByDefault" type="xsd:boolean"/>
     <xsd:element name="displayNameOverride" minOccurs="0" type="xsd:string"/>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="table" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RestrictionRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="description" type="xsd:string"/>
       <xsd:element name="enforcementType" type="tns:EnforcementType"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="recordFilter" type="xsd:string"/>
       <xsd:element name="targetEntity" type="xsd:string"/>
       <xsd:element name="userCriteria" type="xsd:string"/>
       <xsd:element name="version" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="RetailExecutionSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableProductHierarchy" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRetailExecution" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="RoleOrTerritory">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="caseAccessLevel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="contactAccessLevel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="mayForecastManagerShare" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="opportunityAccessLevel" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Role">
    <xsd:complexContent>
     <xsd:extension base="tns:RoleOrTerritory">
      <xsd:sequence>
       <xsd:element name="parentRole" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Territory">
    <xsd:complexContent>
     <xsd:extension base="tns:RoleOrTerritory">
      <xsd:sequence>
       <xsd:element name="accountAccessLevel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="parentTerritory" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SalesWorkQueueSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="featureName" type="xsd:string"/>
       <xsd:element name="targetEntity" type="xsd:string"/>
       <xsd:element name="targetField" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SamlSsoConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="attributeName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="attributeNameIdFormat" minOccurs="0" type="xsd:string"/>
       <xsd:element name="decryptionCertificate" minOccurs="0" type="xsd:string"/>
       <xsd:element name="errorUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="executionUserId" minOccurs="0" type="xsd:string"/>
       <xsd:element name="identityLocation" type="tns:SamlIdentityLocationType"/>
       <xsd:element name="identityMapping" type="tns:SamlIdentityType"/>
       <xsd:element name="issuer" type="xsd:string"/>
       <xsd:element name="loginUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="logoutUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="oauthTokenEndpoint" minOccurs="0" type="xsd:string"/>
       <xsd:element name="redirectBinding" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="requestSignatureMethod" minOccurs="0" type="xsd:string"/>
       <xsd:element name="requestSigningCertId" minOccurs="0" type="xsd:string"/>
       <xsd:element name="salesforceLoginUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="samlEntityId" type="xsd:string"/>
       <xsd:element name="samlJitHandlerId" minOccurs="0" type="xsd:string"/>
       <xsd:element name="samlVersion" type="tns:SamlType"/>
       <xsd:element name="singleLogoutBinding" minOccurs="0" type="tns:SamlSpSLOBinding"/>
       <xsd:element name="singleLogoutUrl" minOccurs="0" type="xsd:string"/>
       <xsd:element name="useConfigRequestMethod" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="userProvisioning" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="validationCert" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="SamlIdentityLocationType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="SubjectNameId"/>
     <xsd:enumeration value="Attribute"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SamlIdentityType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Username"/>
     <xsd:enumeration value="FederationId"/>
     <xsd:enumeration value="UserId"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SamlType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="SAML1_1"/>
     <xsd:enumeration value="SAML2_0"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="SamlSpSLOBinding">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="RedirectBinding"/>
     <xsd:enumeration value="PostBinding"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="SchemaSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableAdvancedCMTSecurity" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAdvancedCSSecurity" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableListCustomSettingCreation" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSOSLOnCustomSettings" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SearchSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="documentContentSearchEnabled" type="xsd:boolean"/>
       <xsd:element name="enableAdvancedSearchInAlohaSidebar" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEinsteinSearchAssistantDialog" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEinsteinSearchNaturalLanguage" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEinsteinSearchPersonalization" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePersonalTagging" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePublicTagging" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableQuerySuggestionPigOn" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSalesforceGeneratedSynonyms" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSearchTermHistory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSetupSearch" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSuggestArticlesLinksOnly" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUseDefaultSearchEntity" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="optimizeSearchForCJKEnabled" type="xsd:boolean"/>
       <xsd:element name="recentlyViewedUsersForBlankLookupEnabled" type="xsd:boolean"/>
       <xsd:element name="searchSettingsByObject" type="tns:SearchSettingsByObject"/>
       <xsd:element name="sidebarAutoCompleteEnabled" type="xsd:boolean"/>
       <xsd:element name="sidebarDropDownListEnabled" type="xsd:boolean"/>
       <xsd:element name="sidebarLimitToItemsIOwnCheckboxEnabled" type="xsd:boolean"/>
       <xsd:element name="singleSearchResultShortcutEnabled" type="xsd:boolean"/>
       <xsd:element name="spellCorrectKnowledgeSearchEnabled" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SearchSettingsByObject">
    <xsd:sequence>
     <xsd:element name="searchSettingsByObject" minOccurs="0" maxOccurs="unbounded" type="tns:ObjectSearchSetting"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ObjectSearchSetting">
    <xsd:sequence>
     <xsd:element name="enhancedLookupEnabled" type="xsd:boolean"/>
     <xsd:element name="lookupAutoCompleteEnabled" type="xsd:boolean"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="resultsPerPageCount" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SecuritySettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="canUsersGrantLoginAccess" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAdminLoginAsAnyUser" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAuditFieldsInactiveOwner" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAuraSecureEvalPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRequireHttpsConnection" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="networkAccess" minOccurs="0" type="tns:NetworkAccess"/>
       <xsd:element name="passwordPolicies" minOccurs="0" type="tns:PasswordPolicies"/>
       <xsd:element name="sessionSettings" minOccurs="0" type="tns:SessionSettings"/>
       <xsd:element name="singleSignOnSettings" minOccurs="0" type="tns:SingleSignOnSettings"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="NetworkAccess">
    <xsd:sequence>
     <xsd:element name="ipRanges" minOccurs="0" maxOccurs="unbounded" type="tns:IpRange"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="IpRange">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="end" minOccurs="0" type="xsd:string"/>
     <xsd:element name="start" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PasswordPolicies">
    <xsd:sequence>
     <xsd:element name="apiOnlyUserHomePageURL" minOccurs="0" type="xsd:string"/>
     <xsd:element name="complexity" minOccurs="0" type="tns:Complexity"/>
     <xsd:element name="expiration" minOccurs="0" type="tns:Expiration"/>
     <xsd:element name="historyRestriction" minOccurs="0" type="xsd:string"/>
     <xsd:element name="lockoutInterval" minOccurs="0" type="tns:LockoutInterval"/>
     <xsd:element name="maxLoginAttempts" minOccurs="0" type="tns:MaxLoginAttempts"/>
     <xsd:element name="minimumPasswordLength" minOccurs="0" type="xsd:string"/>
     <xsd:element name="minimumPasswordLifetime" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="obscureSecretAnswer" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="passwordAssistanceMessage" minOccurs="0" type="xsd:string"/>
     <xsd:element name="passwordAssistanceURL" minOccurs="0" type="xsd:string"/>
     <xsd:element name="questionRestriction" minOccurs="0" type="tns:QuestionRestriction"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="Complexity">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="NoRestriction"/>
     <xsd:enumeration value="AlphaNumeric"/>
     <xsd:enumeration value="SpecialCharacters"/>
     <xsd:enumeration value="UpperLowerCaseNumeric"/>
     <xsd:enumeration value="UpperLowerCaseNumericSpecialCharacters"/>
     <xsd:enumeration value="Any3UpperLowerCaseNumericSpecialCharacters"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="Expiration">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ThirtyDays"/>
     <xsd:enumeration value="SixtyDays"/>
     <xsd:enumeration value="NinetyDays"/>
     <xsd:enumeration value="SixMonths"/>
     <xsd:enumeration value="OneYear"/>
     <xsd:enumeration value="Never"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="LockoutInterval">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="FifteenMinutes"/>
     <xsd:enumeration value="ThirtyMinutes"/>
     <xsd:enumeration value="SixtyMinutes"/>
     <xsd:enumeration value="Forever"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="MaxLoginAttempts">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ThreeAttempts"/>
     <xsd:enumeration value="FiveAttempts"/>
     <xsd:enumeration value="TenAttempts"/>
     <xsd:enumeration value="NoLimit"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="QuestionRestriction">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="DoesNotContainPassword"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="SessionSettings">
    <xsd:sequence>
     <xsd:element name="allowUserAuthenticationByCertificate" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="canConfirmEmailChangeInLightningCommunities" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="canConfirmIdentityBySmsOnly" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="disableTimeoutWarning" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableCSPOnEmail" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableCSRFOnGet" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableCSRFOnPost" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableCacheAndAutocomplete" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableClickjackNonsetupSFDC" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableClickjackNonsetupUser" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableClickjackNonsetupUserHeaderless" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableClickjackSetup" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableContentSniffingProtection" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableLightningLogin" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableLightningLoginOnlyWithUserPerm" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableOauthCorsPolicy" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enablePostForSessions" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableSMSIdentity" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableU2F" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableUpgradeInsecureRequests" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableXssProtection" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enforceIpRangesEveryRequest" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enforceUserDeviceRevoked" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="forceLogoutOnSessionTimeout" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="forceRelogin" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="hasRetainedLoginHints" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="hasUserSwitching" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="hstsOnForcecomSites" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="identityConfirmationOnEmailChange" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="identityConfirmationOnTwoFactorRegistrationEnabled" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="lockSessionsToDomain" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="lockSessionsToIp" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="lockerServiceAPIVersion" minOccurs="0" type="xsd:string"/>
     <xsd:element name="lockerServiceCSP" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="logoutURL" minOccurs="0" type="xsd:string"/>
     <xsd:element name="redirectionWarning" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="referrerPolicy" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="requireHttpOnly" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="requireHttps" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="sessionTimeout" minOccurs="0" type="tns:SessionTimeout"/>
     <xsd:element name="useLocalStorageForLogoutUrl" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="SessionTimeout">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="TwentyFourHours"/>
     <xsd:enumeration value="TwelveHours"/>
     <xsd:enumeration value="EightHours"/>
     <xsd:enumeration value="FourHours"/>
     <xsd:enumeration value="TwoHours"/>
     <xsd:enumeration value="SixtyMinutes"/>
     <xsd:enumeration value="ThirtyMinutes"/>
     <xsd:enumeration value="FifteenMinutes"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="SingleSignOnSettings">
    <xsd:sequence>
     <xsd:element name="enableCaseInsensitiveFederationID" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableForceDelegatedCallout" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableMultipleSamlConfigs" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableSamlJitProvisioning" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="enableSamlLogin" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="isLoginWithSalesforceCredentialsDisabled" minOccurs="0" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ServiceAISetupDefinition">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="appSourceType" type="tns:ApplicationSourceType"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="setupStatus" type="tns:ServiceAISetupDefStatus"/>
       <xsd:element name="supportedLanguages" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ApplicationSourceType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="REPLY_RECOMMENDATION"/>
     <xsd:enumeration value="ARTICLE_RECOMMENDATION"/>
     <xsd:enumeration value="UTTERANCE_RECOMMENDATION"/>
     <xsd:enumeration value="FAQ"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ServiceAISetupDefStatus">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="FIELDS_SELECTED"/>
     <xsd:enumeration value="TRAINING"/>
     <xsd:enumeration value="READY_TO_ACTIVATE"/>
     <xsd:enumeration value="SERVING"/>
     <xsd:enumeration value="RETIRED"/>
     <xsd:enumeration value="ARCHIVED"/>
     <xsd:enumeration value="READY_FOR_REVIEW"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ServiceAISetupField">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="entity" type="xsd:string"/>
       <xsd:element name="field" type="xsd:string"/>
       <xsd:element name="fieldMappingType" type="tns:ServiceAISetupFieldType"/>
       <xsd:element name="fieldPosition" type="xsd:int"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="setupDefinition" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ServiceAISetupFieldType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="CASE_DESC"/>
     <xsd:enumeration value="CASE_SUBJ"/>
     <xsd:enumeration value="ARTICLE_TITLE"/>
     <xsd:enumeration value="ARTICLE_CONTENT"/>
     <xsd:enumeration value="ARTICLE_SUMMARY"/>
     <xsd:enumeration value="ARTICLE_ANSWER"/>
     <xsd:enumeration value="ARTICLE_QUESTION"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="ServiceChannel">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="doesMinimizeWidgetOnAccept" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="interactionComponent" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="relatedEntityType" type="xsd:string"/>
       <xsd:element name="secondaryRoutingPriorityField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="serviceChannelFieldPriorities" minOccurs="0" maxOccurs="unbounded" type="tns:ServiceChannelFieldPriority"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ServiceChannelFieldPriority">
    <xsd:sequence>
     <xsd:element name="priority" type="xsd:int"/>
     <xsd:element name="value" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ServiceCloudVoiceSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableSCVBYOT" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSCVExternalTelephony" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableServiceCloudVoice" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableVoiceInGovCloudOptIn" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ServicePresenceStatus">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="channels" minOccurs="0" type="tns:ServiceChannelStatus"/>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="ServiceChannelStatus">
    <xsd:sequence>
     <xsd:element name="channel" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ServiceSetupAssistantSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableServiceSetupAssistant" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SharingBaseRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="accessLevel" type="xsd:string"/>
       <xsd:element name="accountSettings" minOccurs="0" type="tns:AccountSharingRuleSettings"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="sharedTo" type="tns:SharedTo"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AccountSharingRuleSettings">
    <xsd:sequence>
     <xsd:element name="caseAccessLevel" type="xsd:string"/>
     <xsd:element name="contactAccessLevel" type="xsd:string"/>
     <xsd:element name="opportunityAccessLevel" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SharingCriteriaRule">
    <xsd:complexContent>
     <xsd:extension base="tns:SharingBaseRule">
      <xsd:sequence>
       <xsd:element name="booleanFilter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="criteriaItems" minOccurs="0" maxOccurs="unbounded" type="tns:FilterItem"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SharingGuestRule">
    <xsd:complexContent>
     <xsd:extension base="tns:SharingBaseRule">
      <xsd:sequence>
       <xsd:element name="booleanFilter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="criteriaItems" minOccurs="0" maxOccurs="unbounded" type="tns:FilterItem"/>
       <xsd:element name="includeHVUOwnedRecords" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SharingOwnerRule">
    <xsd:complexContent>
     <xsd:extension base="tns:SharingBaseRule">
      <xsd:sequence>
       <xsd:element name="sharedFrom" type="tns:SharedTo"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SharingTerritoryRule">
    <xsd:complexContent>
     <xsd:extension base="tns:SharingOwnerRule">
      <xsd:sequence/>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SharingRules">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="sharingCriteriaRules" minOccurs="0" maxOccurs="unbounded" type="tns:SharingCriteriaRule"/>
       <xsd:element name="sharingGuestRules" minOccurs="0" maxOccurs="unbounded" type="tns:SharingGuestRule"/>
       <xsd:element name="sharingOwnerRules" minOccurs="0" maxOccurs="unbounded" type="tns:SharingOwnerRule"/>
       <xsd:element name="sharingTerritoryRules" minOccurs="0" maxOccurs="unbounded" type="tns:SharingTerritoryRule"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SharingSet">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="accessMappings" minOccurs="0" maxOccurs="unbounded" type="tns:AccessMapping"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="profiles" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="AccessMapping">
    <xsd:sequence>
     <xsd:element name="accessLevel" type="xsd:string"/>
     <xsd:element name="object" type="xsd:string"/>
     <xsd:element name="objectField" type="xsd:string"/>
     <xsd:element name="userField" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SharingSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="deferGroupMembership" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="deferSharingRules" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAccountRoleOptimization" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAssetSharing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCaseRuntimeChildImp" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCommunityUserVisibility" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableExternalSharingModel" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableManagerGroups" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableManualUserRecordSharing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePartnerSuperUserAccess" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePortalUserCaseSharing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePortalUserVisibility" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRemoveTMGroupMembership" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRestrictAccessLookupRecords" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSecureGuestAccess" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableShareObjectReportTypes" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableStandardReportVisibility" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTerritoryForecastManager" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SiteSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableProxyLoginICHeader" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSitesRecordReassignOrgPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTopicsInSites" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Skill">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="assignments" minOccurs="0" type="tns:SkillAssignments"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SkillAssignments">
    <xsd:sequence>
     <xsd:element name="profiles" minOccurs="0" type="tns:SkillProfileAssignments"/>
     <xsd:element name="users" minOccurs="0" type="tns:SkillUserAssignments"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SkillProfileAssignments">
    <xsd:sequence>
     <xsd:element name="profile" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SkillUserAssignments">
    <xsd:sequence>
     <xsd:element name="user" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="SocialCustomerServiceSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="caseSubjectOption" type="tns:CaseSubjectOption"/>
       <xsd:element name="enableSocialApprovals" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSocialCaseAssignmentRules" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSocialCustomerService" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSocialPersonaHistoryTracking" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSocialPostHistoryTracking" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSocialReceiveParentPost" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="CaseSubjectOption">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="SocialPostSource"/>
     <xsd:enumeration value="SocialPostContent"/>
     <xsd:enumeration value="BuildCustom"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="SocialProfileSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableSocialProfiles" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isFacebookSocialProfilesDisabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isLinkedInSocialProfilesDisabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isTwitterSocialProfilesDisabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isYouTubeSocialProfilesDisabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="StandardValueSet">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="groupingStringEnum" minOccurs="0" type="xsd:string"/>
       <xsd:element name="sorted" type="xsd:boolean"/>
       <xsd:element name="standardValue" minOccurs="0" maxOccurs="unbounded" type="tns:StandardValue"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="StandardValueSetTranslation">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="valueTranslation" minOccurs="0" maxOccurs="unbounded" type="tns:ValueTranslation"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SurveySettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableIndustriesCxmEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSurvey" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSurveyOwnerCanManageResponse" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SynonymDictionary">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="groups" minOccurs="0" maxOccurs="unbounded" type="tns:SynonymGroup"/>
       <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="label" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="SystemNotificationSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="disableDowntimeNotifications" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="disableMaintenanceNotifications" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Territory2">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="accountAccessLevel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="caseAccessLevel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="contactAccessLevel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="customFields" minOccurs="0" maxOccurs="unbounded" type="tns:FieldValue"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="opportunityAccessLevel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="parentTerritory" minOccurs="0" type="xsd:string"/>
       <xsd:element name="ruleAssociations" minOccurs="0" maxOccurs="unbounded" type="tns:Territory2RuleAssociation"/>
       <xsd:element name="territory2Type" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="FieldValue">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="value" type="xsd:anyType" nillable="true"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Territory2RuleAssociation">
    <xsd:sequence>
     <xsd:element name="inherited" type="xsd:boolean"/>
     <xsd:element name="ruleName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Territory2Model">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="customFields" minOccurs="0" maxOccurs="unbounded" type="tns:FieldValue"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Territory2Rule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="booleanFilter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="objectType" type="xsd:string"/>
       <xsd:element name="ruleItems" minOccurs="0" maxOccurs="unbounded" type="tns:Territory2RuleItem"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Territory2RuleItem">
    <xsd:sequence>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="operation" type="tns:FilterOperation"/>
     <xsd:element name="value" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Territory2Settings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="defaultAccountAccessLevel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="defaultCaseAccessLevel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="defaultContactAccessLevel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="defaultOpportunityAccessLevel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="enableTerritoryManagement2" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="opportunityFilterSettings" minOccurs="0" type="tns:Territory2SettingsOpportunityFilter"/>
       <xsd:element name="showTM2EnabledBanner" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="t2ForecastAccessLevel" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Territory2SettingsOpportunityFilter">
    <xsd:sequence>
     <xsd:element name="apexClassName" type="xsd:string" nillable="true"/>
     <xsd:element name="enableFilter" type="xsd:boolean"/>
     <xsd:element name="runOnCreate" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Territory2Type">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="priority" type="xsd:int"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="TimeSheetTemplate">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="frequency" type="tns:TimeSheetFrequency"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="startDate" type="xsd:date"/>
       <xsd:element name="timeSheetTemplateAssignments" minOccurs="0" maxOccurs="unbounded" type="tns:TimeSheetTemplateAssignment"/>
       <xsd:element name="workWeekEndDay" type="tns:DaysOfWeek"/>
       <xsd:element name="workWeekStartDay" type="tns:DaysOfWeek"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="TimeSheetFrequency">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Daily"/>
     <xsd:enumeration value="Weekly"/>
     <xsd:enumeration value="EveryTwoWeeks"/>
     <xsd:enumeration value="TwiceAMonth"/>
     <xsd:enumeration value="Monthly"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="TimeSheetTemplateAssignment">
    <xsd:sequence>
     <xsd:element name="assignedTo" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="DaysOfWeek">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Sunday"/>
     <xsd:enumeration value="Monday"/>
     <xsd:enumeration value="Tuesday"/>
     <xsd:enumeration value="Wednesday"/>
     <xsd:enumeration value="Thursday"/>
     <xsd:enumeration value="Friday"/>
     <xsd:enumeration value="Saturday"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="TopicsForObjects">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableTopics" type="xsd:boolean"/>
       <xsd:element name="entityApiName" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="TrailheadSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableMyTrailheadPref" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="TransactionSecurityPolicy">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="action" type="tns:TransactionSecurityAction"/>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="apexClass" minOccurs="0" type="xsd:string"/>
       <xsd:element name="blockMessage" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="developerName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="eventName" minOccurs="0" type="tns:TransactionSecurityEventName"/>
       <xsd:element name="eventType" minOccurs="0" type="tns:MonitoredEvents"/>
       <xsd:element name="executionUser" minOccurs="0" type="xsd:string"/>
       <xsd:element name="flow" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" minOccurs="0" type="xsd:string"/>
       <xsd:element name="resourceName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="type" minOccurs="0" type="tns:TxnSecurityPolicyType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="TransactionSecurityAction">
    <xsd:sequence>
     <xsd:element name="block" type="xsd:boolean"/>
     <xsd:element name="endSession" type="xsd:boolean"/>
     <xsd:element name="freezeUser" type="xsd:boolean"/>
     <xsd:element name="notifications" minOccurs="0" maxOccurs="unbounded" type="tns:TransactionSecurityNotification"/>
     <xsd:element name="twoFactorAuthentication" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="TransactionSecurityNotification">
    <xsd:sequence>
     <xsd:element name="inApp" type="xsd:boolean"/>
     <xsd:element name="sendEmail" type="xsd:boolean"/>
     <xsd:element name="user" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="TransactionSecurityEventName">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ReportEvent"/>
     <xsd:enumeration value="ApiEvent"/>
     <xsd:enumeration value="AdminSetupEvent"/>
     <xsd:enumeration value="LoginEvent"/>
     <xsd:enumeration value="ListViewEvent"/>
     <xsd:enumeration value="CredentialStuffingEventStore"/>
     <xsd:enumeration value="ReportAnomalyEventStore"/>
     <xsd:enumeration value="SessionHijackingEventStore"/>
     <xsd:enumeration value="ApiAnomalyEventStore"/>
     <xsd:enumeration value="BulkApiResultEventStore"/>
     <xsd:enumeration value="PermissionSetEventStore"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="MonitoredEvents">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="AuditTrail"/>
     <xsd:enumeration value="Login"/>
     <xsd:enumeration value="Entity"/>
     <xsd:enumeration value="DataExport"/>
     <xsd:enumeration value="AccessResource"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="TxnSecurityPolicyType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="CustomApexPolicy"/>
     <xsd:enumeration value="CustomConditionBuilderPolicy"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="Translations">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="customApplications" minOccurs="0" maxOccurs="unbounded" type="tns:CustomApplicationTranslation"/>
       <xsd:element name="customLabels" minOccurs="0" maxOccurs="unbounded" type="tns:CustomLabelTranslation"/>
       <xsd:element name="customPageWebLinks" minOccurs="0" maxOccurs="unbounded" type="tns:CustomPageWebLinkTranslation"/>
       <xsd:element name="customTabs" minOccurs="0" maxOccurs="unbounded" type="tns:CustomTabTranslation"/>
       <xsd:element name="flowDefinitions" minOccurs="0" maxOccurs="unbounded" type="tns:FlowDefinitionTranslation"/>
       <xsd:element name="prompts" minOccurs="0" maxOccurs="unbounded" type="tns:PromptTranslation"/>
       <xsd:element name="quickActions" minOccurs="0" maxOccurs="unbounded" type="tns:GlobalQuickActionTranslation"/>
       <xsd:element name="reportTypes" minOccurs="0" maxOccurs="unbounded" type="tns:ReportTypeTranslation"/>
       <xsd:element name="scontrols" minOccurs="0" maxOccurs="unbounded" type="tns:ScontrolTranslation"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="CustomApplicationTranslation">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CustomLabelTranslation">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CustomPageWebLinkTranslation">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="CustomTabTranslation">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowDefinitionTranslation">
    <xsd:sequence>
     <xsd:element name="flows" minOccurs="0" maxOccurs="unbounded" type="tns:FlowTranslation"/>
     <xsd:element name="fullName" type="xsd:string"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowTranslation">
    <xsd:sequence>
     <xsd:element name="choices" minOccurs="0" maxOccurs="unbounded" type="tns:FlowChoiceTranslation"/>
     <xsd:element name="fullName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="screens" minOccurs="0" maxOccurs="unbounded" type="tns:FlowScreenTranslation"/>
     <xsd:element name="stages" minOccurs="0" maxOccurs="unbounded" type="tns:FlowStageTranslation"/>
     <xsd:element name="textTemplates" minOccurs="0" maxOccurs="unbounded" type="tns:FlowTextTemplateTranslation"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowChoiceTranslation">
    <xsd:sequence>
     <xsd:element name="choiceText" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="userInput" minOccurs="0" type="tns:FlowChoiceUserInputTranslation"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowChoiceUserInputTranslation">
    <xsd:sequence>
     <xsd:element name="promptText" minOccurs="0" type="xsd:string"/>
     <xsd:element name="validationRule" minOccurs="0" type="tns:FlowInputValidationRuleTranslation"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowInputValidationRuleTranslation">
    <xsd:sequence>
     <xsd:element name="errorMessage" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowScreenTranslation">
    <xsd:sequence>
     <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="tns:FlowScreenFieldTranslation"/>
     <xsd:element name="helpText" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="pausedText" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowScreenFieldTranslation">
    <xsd:sequence>
     <xsd:element name="fieldText" minOccurs="0" type="xsd:string"/>
     <xsd:element name="helpText" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="validationRule" minOccurs="0" type="tns:FlowInputValidationRuleTranslation"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowStageTranslation">
    <xsd:sequence>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="FlowTextTemplateTranslation">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="text" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PromptTranslation">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="promptVersions" minOccurs="0" maxOccurs="unbounded" type="tns:PromptVersionTranslation"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PromptVersionTranslation">
    <xsd:sequence>
     <xsd:element name="actionButtonLabel" minOccurs="0" type="xsd:string"/>
     <xsd:element name="actionButtonLink" minOccurs="0" type="xsd:string"/>
     <xsd:element name="body" minOccurs="0" type="xsd:string"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dismissButtonLabel" minOccurs="0" type="xsd:string"/>
     <xsd:element name="header" minOccurs="0" type="xsd:string"/>
     <xsd:element name="imageAltText" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="stepNumber" minOccurs="0" type="xsd:int"/>
     <xsd:element name="title" minOccurs="0" type="xsd:string"/>
     <xsd:element name="videoLink" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="GlobalQuickActionTranslation">
    <xsd:sequence>
     <xsd:element name="aspect" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportTypeTranslation">
    <xsd:sequence>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="sections" minOccurs="0" maxOccurs="unbounded" type="tns:ReportTypeSectionTranslation"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportTypeSectionTranslation">
    <xsd:sequence>
     <xsd:element name="columns" minOccurs="0" maxOccurs="unbounded" type="tns:ReportTypeColumnTranslation"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReportTypeColumnTranslation">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ScontrolTranslation">
    <xsd:sequence>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="name" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="TrialOrgSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableSampleDataDeleted" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="UIObjectRelationConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="UIObjectRelationFieldConfigs" minOccurs="0" maxOccurs="unbounded" type="tns:UIObjectRelationFieldConfig"/>
       <xsd:element name="contextObject" type="xsd:string"/>
       <xsd:element name="contextObjectRecordType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="directRelationshipField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="indirectObjectContextField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="indirectObjectRelatedField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="indirectRelationshipObject" minOccurs="0" type="xsd:string"/>
       <xsd:element name="isActive" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="relatedObject" type="xsd:string"/>
       <xsd:element name="relatedObjectRecordType" minOccurs="0" type="xsd:string"/>
       <xsd:element name="relationshipType" type="tns:ObjectRelationshipType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="UIObjectRelationFieldConfig">
    <xsd:sequence>
     <xsd:element name="displayLabel" type="xsd:string"/>
     <xsd:element name="queryText" type="xsd:string"/>
     <xsd:element name="rowOrder" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ObjectRelationshipType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Direct"/>
     <xsd:enumeration value="Indirect"/>
     <xsd:enumeration value="Self"/>
     <xsd:enumeration value="InverseDirect"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="UserCriteria">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="creationAgeInSeconds" minOccurs="0" type="xsd:int"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="lastChatterActivityAgeInSeconds" minOccurs="0" type="xsd:int"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="profiles" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="userTypes" minOccurs="0" maxOccurs="unbounded" type="tns:NetworkUserType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="NetworkUserType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Internal"/>
     <xsd:enumeration value="Customer"/>
     <xsd:enumeration value="Partner"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="UserEngagementSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="canGovCloudUseAdoptionApps" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="doesScheduledSwitcherRunDaily" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCustomHelpGlobalSection" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHelpMenuShowFeedback" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHelpMenuShowHelp" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHelpMenuShowNewUser" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHelpMenuShowSearch" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHelpMenuShowSfdcContent" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHelpMenuShowShortcut" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHelpMenuShowSupport" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHelpMenuShowTrailhead" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIBILOptOutDashboards" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIBILOptOutEvents" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIBILOptOutReports" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableIBILOptOutTasks" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableLexToClassicFeedbackEnable" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOrchestrationInSandbox" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableOrgUserAssistEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableScheduledSwitcher" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableSfdcProductFeedbackSurvey" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableShowSalesforceUserAssist" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isAutoTransitionDelayed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isCrucNotificationDisabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isCustomProfileAutoTransitionDelayed" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isLEXWelcomeMatDisabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isMeetTheAssistantDisabledInClassic" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isMeetTheAssistantDisabledInLightning" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="isSmartNudgesDisabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="optimizerAppEnabled" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="UserInterfaceSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="alternateAlohaListView" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="dynamicMruActionsOff" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableAsyncRelatedLists" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableClickjackUserPageHeaderless" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCollapsibleSections" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCollapsibleSideBar" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCustomObjectTruncate" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableCustomeSideBarOnAllPages" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableDeleteFieldHistory" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableExternalObjectAsyncRelatedLists" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableHoverDetails" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableInlineEdit" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNewPageLayoutEditor" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePersonalCanvas" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enablePrintableListViews" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableProfileCustomTabsets" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableQuickCreate" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableRelatedListHovers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableTabOrganizer" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="UserManagementSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCanAnswerContainUsername" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableConcealPersonalInfo" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableContactlessExternalIdentityUsers" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEnhancedPermsetMgmt" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableEnhancedProfileMgmt" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableNewProfileUI" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableProfileFiltering" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableScrambleUserData" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableUserSelfDeactivate" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="psaExpirationUIEnabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="restrictedProfileCloning" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="UserProvisioningConfig">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="approvalRequired" minOccurs="0" type="xsd:string"/>
       <xsd:element name="connectedApp" type="xsd:string"/>
       <xsd:element name="enabled" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enabledOperations" minOccurs="0" type="xsd:string"/>
       <xsd:element name="flow" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="namedCredential" minOccurs="0" type="xsd:string"/>
       <xsd:element name="notes" minOccurs="0" type="xsd:string"/>
       <xsd:element name="onUpdateAttributes" minOccurs="0" type="xsd:string"/>
       <xsd:element name="reconFilter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="userAccountMapping" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="VoiceSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCallDisposition" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableConsentReminder" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableVoiceCallList" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableVoiceCallRecording" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableVoiceCoaching" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableVoiceConferencing" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableVoiceLocalPresence" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableVoiceMail" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableVoiceMailDrop" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WaveApplication">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="assetIcon" minOccurs="0" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="folder" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="shares" minOccurs="0" maxOccurs="unbounded" type="tns:FolderShare"/>
       <xsd:element name="templateOrigin" minOccurs="0" type="xsd:string"/>
       <xsd:element name="templateVersion" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WaveDataset">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="application" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="templateAssetSourceName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="type" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WaveTemplateBundle">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="assetIcon" minOccurs="0" type="xsd:string"/>
       <xsd:element name="assetVersion" minOccurs="0" type="xsd:double"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="templateType" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WaveXmd">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="application" minOccurs="0" type="xsd:string"/>
       <xsd:element name="dataset" type="xsd:string"/>
       <xsd:element name="datasetConnector" minOccurs="0" type="xsd:string"/>
       <xsd:element name="datasetFullyQualifiedName" minOccurs="0" type="xsd:string"/>
       <xsd:element name="dates" minOccurs="0" maxOccurs="unbounded" type="tns:WaveXmdDate"/>
       <xsd:element name="dimensions" minOccurs="0" maxOccurs="unbounded" type="tns:WaveXmdDimension"/>
       <xsd:element name="measures" minOccurs="0" maxOccurs="unbounded" type="tns:WaveXmdMeasure"/>
       <xsd:element name="organizations" minOccurs="0" maxOccurs="unbounded" type="tns:WaveXmdOrganization"/>
       <xsd:element name="origin" minOccurs="0" type="xsd:string"/>
       <xsd:element name="type" minOccurs="0" type="xsd:string"/>
       <xsd:element name="waveVisualization" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WaveXmdDate">
    <xsd:sequence>
     <xsd:element name="alias" type="xsd:string"/>
     <xsd:element name="compact" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="dateFieldDay" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldEpochDay" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldEpochSecond" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldFiscalMonth" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldFiscalQuarter" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldFiscalWeek" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldFiscalYear" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldFullYear" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldHour" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldMinute" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldMonth" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldQuarter" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldSecond" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldWeek" minOccurs="0" type="xsd:string"/>
     <xsd:element name="dateFieldYear" minOccurs="0" type="xsd:string"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="firstDayOfWeek" type="xsd:int"/>
     <xsd:element name="fiscalMonthOffset" type="xsd:int"/>
     <xsd:element name="isYearEndFiscalYear" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="showInExplorer" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="sortIndex" type="xsd:int"/>
     <xsd:element name="type" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WaveXmdDimension">
    <xsd:sequence>
     <xsd:element name="conditionalFormatting" minOccurs="0" maxOccurs="unbounded" type="tns:WaveXmdFormattingProperty"/>
     <xsd:element name="customActions" minOccurs="0" maxOccurs="unbounded" type="tns:WaveXmdDimensionCustomAction"/>
     <xsd:element name="customActionsEnabled" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="dateFormat" minOccurs="0" type="xsd:string"/>
     <xsd:element name="defaultAction" minOccurs="0" type="xsd:string"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="fullyQualifiedName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="imageTemplate" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isDerived" type="xsd:boolean"/>
     <xsd:element name="isMultiValue" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="linkTemplate" minOccurs="0" type="xsd:string"/>
     <xsd:element name="linkTemplateEnabled" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="linkTooltip" minOccurs="0" type="xsd:string"/>
     <xsd:element name="members" minOccurs="0" maxOccurs="unbounded" type="tns:WaveXmdDimensionMember"/>
     <xsd:element name="origin" minOccurs="0" type="xsd:string"/>
     <xsd:element name="recordDisplayFields" minOccurs="0" maxOccurs="unbounded" type="tns:WaveXmdRecordDisplayLookup"/>
     <xsd:element name="recordIdField" minOccurs="0" type="xsd:string"/>
     <xsd:element name="recordOrganizationIdField" minOccurs="0" type="xsd:string"/>
     <xsd:element name="salesforceActions" minOccurs="0" maxOccurs="unbounded" type="tns:WaveXmdDimensionSalesforceAction"/>
     <xsd:element name="salesforceActionsEnabled" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="showDetailsDefaultFieldIndex" minOccurs="0" type="xsd:int"/>
     <xsd:element name="showInExplorer" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="sortIndex" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WaveXmdFormattingProperty">
    <xsd:sequence>
     <xsd:element name="formattingBins" minOccurs="0" maxOccurs="unbounded" type="tns:WaveXmdFormattingBin"/>
     <xsd:element name="formattingPredicates" minOccurs="0" maxOccurs="unbounded" type="tns:WaveXmdFormattingPredicate"/>
     <xsd:element name="property" type="xsd:string"/>
     <xsd:element name="referenceField" type="xsd:string"/>
     <xsd:element name="sortIndex" type="xsd:int"/>
     <xsd:element name="type" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WaveXmdFormattingBin">
    <xsd:sequence>
     <xsd:element name="bin" type="xsd:string"/>
     <xsd:element name="formatValue" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="sortIndex" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WaveXmdFormattingPredicate">
    <xsd:sequence>
     <xsd:element name="formatValue" type="xsd:string"/>
     <xsd:element name="operator" type="xsd:string"/>
     <xsd:element name="sortIndex" type="xsd:int"/>
     <xsd:element name="value" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WaveXmdDimensionCustomAction">
    <xsd:sequence>
     <xsd:element name="customActionName" type="xsd:string"/>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="icon" minOccurs="0" type="xsd:string"/>
     <xsd:element name="method" minOccurs="0" type="xsd:string"/>
     <xsd:element name="sortIndex" type="xsd:int"/>
     <xsd:element name="target" minOccurs="0" type="xsd:string"/>
     <xsd:element name="tooltip" minOccurs="0" type="xsd:string"/>
     <xsd:element name="url" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WaveXmdDimensionMember">
    <xsd:sequence>
     <xsd:element name="color" minOccurs="0" type="xsd:string"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="member" type="xsd:string"/>
     <xsd:element name="sortIndex" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WaveXmdRecordDisplayLookup">
    <xsd:sequence>
     <xsd:element name="recordDisplayField" type="xsd:string"/>
     <xsd:element name="sortIndex" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WaveXmdDimensionSalesforceAction">
    <xsd:sequence>
     <xsd:element name="enabled" type="xsd:boolean"/>
     <xsd:element name="salesforceActionName" type="xsd:string"/>
     <xsd:element name="sortIndex" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WaveXmdMeasure">
    <xsd:sequence>
     <xsd:element name="conditionalFormatting" minOccurs="0" maxOccurs="unbounded" type="tns:WaveXmdFormattingProperty"/>
     <xsd:element name="dateFormat" minOccurs="0" type="xsd:string"/>
     <xsd:element name="description" minOccurs="0" type="xsd:string"/>
     <xsd:element name="field" type="xsd:string"/>
     <xsd:element name="formatCustomFormat" minOccurs="0" type="xsd:string"/>
     <xsd:element name="formatDecimalDigits" minOccurs="0" type="xsd:int"/>
     <xsd:element name="formatDecimalSeparator" minOccurs="0" type="xsd:string"/>
     <xsd:element name="formatIsNegativeParens" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="formatPrefix" minOccurs="0" type="xsd:string"/>
     <xsd:element name="formatSuffix" minOccurs="0" type="xsd:string"/>
     <xsd:element name="formatThousandsSeparator" minOccurs="0" type="xsd:string"/>
     <xsd:element name="formatUnit" minOccurs="0" type="xsd:string"/>
     <xsd:element name="formatUnitMultiplier" minOccurs="0" type="xsd:double"/>
     <xsd:element name="fullyQualifiedName" minOccurs="0" type="xsd:string"/>
     <xsd:element name="isDerived" type="xsd:boolean"/>
     <xsd:element name="label" minOccurs="0" type="xsd:string"/>
     <xsd:element name="origin" minOccurs="0" type="xsd:string"/>
     <xsd:element name="showDetailsDefaultFieldIndex" minOccurs="0" type="xsd:int"/>
     <xsd:element name="showInExplorer" minOccurs="0" type="xsd:boolean"/>
     <xsd:element name="sortIndex" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WaveXmdOrganization">
    <xsd:sequence>
     <xsd:element name="instanceUrl" type="xsd:string"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="organizationIdentifier" type="xsd:string"/>
     <xsd:element name="sortIndex" type="xsd:int"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WebStoreTemplate">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="checkoutTimeToLive" minOccurs="0" type="xsd:int"/>
       <xsd:element name="checkoutValidAfterDate" minOccurs="0" type="xsd:dateTime"/>
       <xsd:element name="defaultCurrency" minOccurs="0" type="xsd:string"/>
       <xsd:element name="defaultLanguage" type="xsd:string"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="guestCartTimeToLive" minOccurs="0" type="xsd:int"/>
       <xsd:element name="masterLabel" type="xsd:string"/>
       <xsd:element name="maxValuesPerFacet" minOccurs="0" type="xsd:int"/>
       <xsd:element name="paginationSize" minOccurs="0" type="xsd:int"/>
       <xsd:element name="pricingStrategy" type="tns:PricingStrategy"/>
       <xsd:element name="productGrouping" minOccurs="0" type="tns:ProductGrouping"/>
       <xsd:element name="supportedCurrencies" minOccurs="0" type="xsd:string"/>
       <xsd:element name="supportedLanguages" type="xsd:string"/>
       <xsd:element name="type" type="tns:WebStoreType"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="PricingStrategy">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="LowestPrice"/>
     <xsd:enumeration value="Priority"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ProductGrouping">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="VariationParent"/>
     <xsd:enumeration value="NoGrouping"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="WebStoreType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="B2B"/>
     <xsd:enumeration value="B2C"/>
     <xsd:enumeration value="OMS"/>
     <xsd:enumeration value="B2CE"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="WebToXSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="webToCaseSpamFilter" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="webToLeadSpamFilter" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WorkDotComSettings">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="enableCoachingManagerGroupAccess" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableGoalManagerGroupAccess" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableProfileSkills" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableProfileSkillsAddFeedPost" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableProfileSkillsAutoSuggest" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableProfileSkillsUsePlatform" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWorkBadgeDefRestrictPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWorkCalibration" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWorkCanvasPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWorkCertification" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWorkCertificationNotification" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWorkRewardsPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWorkThanksPref" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="enableWorkUseObjectivesForGoals" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="Workflow">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="alerts" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowAlert"/>
       <xsd:element name="fieldUpdates" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowFieldUpdate"/>
       <xsd:element name="flowActions" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowFlowAction"/>
       <xsd:element name="knowledgePublishes" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowKnowledgePublish"/>
       <xsd:element name="outboundMessages" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowOutboundMessage"/>
       <xsd:element name="rules" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowRule"/>
       <xsd:element name="send" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowSend"/>
       <xsd:element name="tasks" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowTask"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WorkflowAlert">
    <xsd:complexContent>
     <xsd:extension base="tns:WorkflowAction">
      <xsd:sequence>
       <xsd:element name="ccEmails" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="description" type="xsd:string"/>
       <xsd:element name="protected" type="xsd:boolean"/>
       <xsd:element name="recipients" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowEmailRecipient"/>
       <xsd:element name="senderAddress" minOccurs="0" type="xsd:string"/>
       <xsd:element name="senderType" minOccurs="0" type="tns:ActionEmailSenderType"/>
       <xsd:element name="template" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WorkflowAction">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence/>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WorkflowFieldUpdate">
    <xsd:complexContent>
     <xsd:extension base="tns:WorkflowAction">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="field" type="xsd:string"/>
       <xsd:element name="formula" minOccurs="0" type="xsd:string"/>
       <xsd:element name="literalValue" minOccurs="0" type="xsd:string"/>
       <xsd:element name="lookupValue" minOccurs="0" type="xsd:string"/>
       <xsd:element name="lookupValueType" minOccurs="0" type="tns:LookupValueType"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="notifyAssignee" type="xsd:boolean"/>
       <xsd:element name="operation" type="tns:FieldUpdateOperation"/>
       <xsd:element name="protected" type="xsd:boolean"/>
       <xsd:element name="reevaluateOnChange" minOccurs="0" type="xsd:boolean"/>
       <xsd:element name="targetObject" minOccurs="0" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="LookupValueType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="User"/>
     <xsd:enumeration value="Queue"/>
     <xsd:enumeration value="RecordType"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="FieldUpdateOperation">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Formula"/>
     <xsd:enumeration value="Literal"/>
     <xsd:enumeration value="Null"/>
     <xsd:enumeration value="NextValue"/>
     <xsd:enumeration value="PreviousValue"/>
     <xsd:enumeration value="LookupValue"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="WorkflowFlowAction">
    <xsd:complexContent>
     <xsd:extension base="tns:WorkflowAction">
      <xsd:sequence>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="flow" type="xsd:string"/>
       <xsd:element name="flowInputs" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowFlowActionParameter"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="language" minOccurs="0" type="xsd:string"/>
       <xsd:element name="protected" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WorkflowFlowActionParameter">
    <xsd:sequence>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="value" minOccurs="0" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="WorkflowKnowledgePublish">
    <xsd:complexContent>
     <xsd:extension base="tns:WorkflowAction">
      <xsd:sequence>
       <xsd:element name="action" type="tns:KnowledgeWorkflowAction"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="language" minOccurs="0" type="xsd:string"/>
       <xsd:element name="protected" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="KnowledgeWorkflowAction">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="PublishAsNew"/>
     <xsd:enumeration value="Publish"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="WorkflowOutboundMessage">
    <xsd:complexContent>
     <xsd:extension base="tns:WorkflowAction">
      <xsd:sequence>
       <xsd:element name="apiVersion" type="xsd:double"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="endpointUrl" type="xsd:string"/>
       <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
       <xsd:element name="includeSessionId" type="xsd:boolean"/>
       <xsd:element name="integrationUser" type="xsd:string"/>
       <xsd:element name="name" type="xsd:string"/>
       <xsd:element name="protected" type="xsd:boolean"/>
       <xsd:element name="useDeadLetterQueue" minOccurs="0" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:complexType name="WorkflowSend">
    <xsd:complexContent>
     <xsd:extension base="tns:WorkflowAction">
      <xsd:sequence>
       <xsd:element name="action" type="tns:SendAction"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="label" type="xsd:string"/>
       <xsd:element name="language" minOccurs="0" type="xsd:string"/>
       <xsd:element name="protected" type="xsd:boolean"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="SendAction">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Send"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="WorkflowTask">
    <xsd:complexContent>
     <xsd:extension base="tns:WorkflowAction">
      <xsd:sequence>
       <xsd:element name="assignedTo" minOccurs="0" type="xsd:string"/>
       <xsd:element name="assignedToType" type="tns:ActionTaskAssignedToTypes"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="dueDateOffset" type="xsd:int"/>
       <xsd:element name="notifyAssignee" type="xsd:boolean"/>
       <xsd:element name="offsetFromField" minOccurs="0" type="xsd:string"/>
       <xsd:element name="priority" type="xsd:string"/>
       <xsd:element name="protected" type="xsd:boolean"/>
       <xsd:element name="status" type="xsd:string"/>
       <xsd:element name="subject" type="xsd:string"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="ActionTaskAssignedToTypes">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="user"/>
     <xsd:enumeration value="role"/>
     <xsd:enumeration value="opportunityTeam"/>
     <xsd:enumeration value="accountTeam"/>
     <xsd:enumeration value="owner"/>
     <xsd:enumeration value="accountOwner"/>
     <xsd:enumeration value="creator"/>
     <xsd:enumeration value="accountCreator"/>
     <xsd:enumeration value="partnerUser"/>
     <xsd:enumeration value="portalRole"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="WorkflowEmailRecipient">
    <xsd:sequence>
     <xsd:element name="field" minOccurs="0" type="xsd:string"/>
     <xsd:element name="recipient" minOccurs="0" type="xsd:string"/>
     <xsd:element name="type" type="tns:ActionEmailRecipientTypes"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ActionEmailRecipientTypes">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="group"/>
     <xsd:enumeration value="role"/>
     <xsd:enumeration value="user"/>
     <xsd:enumeration value="opportunityTeam"/>
     <xsd:enumeration value="accountTeam"/>
     <xsd:enumeration value="roleSubordinates"/>
     <xsd:enumeration value="owner"/>
     <xsd:enumeration value="creator"/>
     <xsd:enumeration value="partnerUser"/>
     <xsd:enumeration value="accountOwner"/>
     <xsd:enumeration value="customerPortalUser"/>
     <xsd:enumeration value="portalRole"/>
     <xsd:enumeration value="portalRoleSubordinates"/>
     <xsd:enumeration value="contactLookup"/>
     <xsd:enumeration value="userLookup"/>
     <xsd:enumeration value="roleSubordinatesInternal"/>
     <xsd:enumeration value="email"/>
     <xsd:enumeration value="caseTeam"/>
     <xsd:enumeration value="campaignMemberDerivedOwner"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="ActionEmailSenderType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="CurrentUser"/>
     <xsd:enumeration value="OrgWideEmailAddress"/>
     <xsd:enumeration value="DefaultWorkflowUser"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="WorkflowRule">
    <xsd:complexContent>
     <xsd:extension base="tns:Metadata">
      <xsd:sequence>
       <xsd:element name="actions" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowActionReference"/>
       <xsd:element name="active" type="xsd:boolean"/>
       <xsd:element name="booleanFilter" minOccurs="0" type="xsd:string"/>
       <xsd:element name="criteriaItems" minOccurs="0" maxOccurs="unbounded" type="tns:FilterItem"/>
       <xsd:element name="description" minOccurs="0" type="xsd:string"/>
       <xsd:element name="formula" minOccurs="0" type="xsd:string"/>
       <xsd:element name="triggerType" type="tns:WorkflowTriggerTypes"/>
       <xsd:element name="workflowTimeTriggers" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowTimeTrigger"/>
      </xsd:sequence>
     </xsd:extension>
    </xsd:complexContent>
   </xsd:complexType>
   <xsd:simpleType name="WorkflowTriggerTypes">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="onCreateOnly"/>
     <xsd:enumeration value="onCreateOrTriggeringUpdate"/>
     <xsd:enumeration value="onAllChanges"/>
     <xsd:enumeration value="OnRecursiveUpdate"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="WorkflowTimeTrigger">
    <xsd:sequence>
     <xsd:element name="actions" minOccurs="0" maxOccurs="unbounded" type="tns:WorkflowActionReference"/>
     <xsd:element name="offsetFromField" minOccurs="0" type="xsd:string"/>
     <xsd:element name="timeLength" minOccurs="0" type="xsd:string"/>
     <xsd:element name="workflowTimeTriggerUnit" type="tns:WorkflowTimeUnits"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="WorkflowTimeUnits">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Hours"/>
     <xsd:enumeration value="Days"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="SaveResult">
    <xsd:sequence>
     <xsd:element name="errors" minOccurs="0" maxOccurs="unbounded" type="tns:Error"/>
     <xsd:element name="fullName" type="xsd:string"/>
     <xsd:element name="success" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="Error">
    <xsd:sequence>
     <xsd:element name="extendedErrorDetails" minOccurs="0" maxOccurs="unbounded" type="tns:ExtendedErrorDetails"/>
     <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="message" type="xsd:string"/>
     <xsd:element name="statusCode" type="tns:StatusCode"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="ExtendedErrorCode">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ACTIONCALL_DUPLICATE_INPUT_PARAM">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, actionCallName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTIONCALL_DUPLICATE_OUTPUT_PARAM">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, actionCallName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTIONCALL_INPUT_VALIDATION_FAILED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, cause</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTIONCALL_INVALID_INPUT_PARAM_NAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, actionCallName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTIONCALL_MISSING_NAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTIONCALL_MISSING_REQUIRED_PARAM">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, actionCallName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTIONCALL_MISSING_REQUIRED_TYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, actionCallName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTIONCALL_NOT_FOUND_WITH_NAME_AND_TYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTIONCALL_NOT_SUPPORTED_FOR_PROCESSTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTIONCALL_TRANSACTION_MODEL_NOT_ALLOWED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, actionCallName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTIONCALL_TRANSACTION_MODEL_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTION_CALL_INVALID_CONFIGURATION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, cause</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTION_CALL_INVALID_INPUT_PARAM">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, actionCallName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ACTION_CALL_INVALID_OUTPUT_PARAM">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, actionCallName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ADDING_ATTACHMENT_QUESTIONS_ADDITION_TO_EXISTING_SURVEY">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="APEXCALLOUT_INPUT_DUPLICATE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, apexClassName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="APEXCALLOUT_INPUT_INCOMPATIBLE_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, apexClassName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="APEXCALLOUT_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, apexClassName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="APEXCALLOUT_MISSING_CLASSNAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, apexClassName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="APEXCALLOUT_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, apexClassName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="APEXCALLOUT_OUTPUT_INCOMPATIBLE_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, apexClassName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="APEXCALLOUT_OUTPUT_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, apexClassName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="APEXCALLOUT_REQUIRED_INPUT_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, apexClassName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="APEXCLASS_MISSING_INTERFACE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, apexClassName, parentScreenFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="APEX_CLASS_VARIABLE_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, apexClass</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_ELEMENT_MISSING_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, assignmentName, operatorName, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_ELEMENT_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, assignmentName, elementType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_FIELD_INVALID_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldValue, dataType, incompatibleDataType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_FIELD_INVALID_DATATYPE_WITH_ELEMENT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, acceptedDataType, dataType, fieldValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_INCOMPATIBLE_DATATYPES">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, assignmentName, operatorName, leftElementName, leftElementType, rightElementName, rightElementType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_INVALID_ASSIGNTOREFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, assignmentName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_INVALID_COLLECTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, assignmentName, operatorName, leftElementName, rightElementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_INVALID_DATATYPE_IN_ELEMENT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, dataType, incompatibleDataType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_INVALID_ELEMENTREFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, assignmentName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_INVALID_MERGE_FIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName, operatorName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_INVALID_OPERATOR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, assignmentName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_INVALID_REFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName, operatorName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_INVALID_VALUE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, assignmentName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_LEFT_DATATYPE_INVALID_FOR_OPERATOR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, assignmentName, operatorName, dataType, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_MODIFIES_NONVARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, assignmentName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_NONEXISTENT_REFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName, operatorName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_REQUIRED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, assignmentName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ASSIGNMENTITEM_RIGHT_DATATYPE_INVALID_FOR_OPERATOR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="AUTOLAUNCHED_CHOICELOOKUP_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, choiceLookupName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="AUTOLAUNCHED_CHOICE_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, choiceName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="AUTOLAUNCHED_SCREEN_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="AUTOLAUNCHED_STEP_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="AUTOLAUNCHED_SUBFLOW_INCOMPATIBLE_FLOWTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="AUTOLAUNCHED_WAIT_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="BEFORE_SAVE_FLOW_RECORD_UPDATE_CANNOT_HAVE_FAULT_CONNECTOR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="BEFORE_SAVE_FLOW_RECORD_UPDATE_INVALID_REFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="BEFORE_SAVE_FLOW_RECORD_UPDATE_REQUIRES_INPUTASSIGNMENTS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="BOTH_START_NODE_AND_REFERENCE_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CHOICEFIELD_DEFAULT_CHOICE_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, screenFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CHOICEFIELD_MISSING_CHOICE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, questionName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CHOICELOOKUP_DATATYPE_INCOMPATIBLE_WITH_CHOICEFIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, choiceName, parentScreenFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CHOICE_DATATYPE_INCOMPATIBLE_WITH_CHOICEFIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, choiceName, parentScreenFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CHOICE_NOT_SUPPORTED_FOR_SCREENFIELDTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, screenFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CHOICE_USED_MULTIPLE_TIMES_IN_SAME_FIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, choiceName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="COLLECTION_PROCESSOR_INVALID_COLLECTION_REFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="COLLECTION_PROCESSOR_MAX_SORT_FIELDS_LIMIT_EXCEEDED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="COLLECTION_PROCESSOR_MISSING_SORT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="COLLECTION_PROCESSOR_NOT_SUPPORTED_FOR_API_VERSION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="COLLECTION_PROCESSOR_REQUIRES_PERM">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="COLLECTION_PROCESSOR_SORT_FIELD_INVALID_FOR_OBJECT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="COLLECTION_PROCESSOR_TYPE_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="COLLECTION_PROCESSOR_VARIABLE_NULL">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_BUILDER_MISSING_FLOW_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_BUILDER_MISSING_REQUIRED_PERMISSIONS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_BUILDER_UNSUPPORTED_FLOW_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_INVALID_LEFTOPERAND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementReference, operatorName, ruleName, screenFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_LOGIC_EXCEEDS_LIMIT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, characterLimit</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_LOGIC_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_LOGIC_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_MISSING_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, elementReference, operatorName, ruleName, screenFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_MISSING_OPERATOR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, ruleName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_OPERAND_DATATYPES_INCOMPATIBLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, elementReference, operatorName, ruleName, screenFieldName, elementReferenceOrValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_OPERAND_INCOMPATIBLE_WITH_ELEMENT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, elementReference, ruleName, screenFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_OPERATOR_INCOMPATIBLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, elementReference, operatorName, ruleName, screenFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_REFERENCED_ELEMENT_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, elementReference, ruleName, screenFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONDITION_RIGHTOPERAND_NULL">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, elementReference, elementReferenceOrValue, operatorName, ruleName, screenFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONNECTOR_MISSING_TARGET">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CONSTANT_INCLUDES_REFERENCES">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, constantName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CUSTOMEVENTS_NOT_ENABLED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CUSTOMEVENT_MISSING_PROCESSMETADATAVALUES">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CUSTOMEVENT_OBJECTTYPE_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CUSTOMEVENT_OBJECTTYPE_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CUSTOMEVENT_PROCESSMETADATAVALUES_MISSING_NAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, metadataValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="CUSTOMEVENT_PROCESSMETADATAVALUES_MORE_THAN_ONE_NAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, metadataValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="DATATYPE_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, dataType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="DATATYPE_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="DATA_TYPE_NOT_SUPPORTED_FOR_PROCESSTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType, dataType, elementType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="DECISION_DEFAULT_CONNECTOR_MISSING_LABEL">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, flowDecision</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="DECISION_MISSING_OUTCOME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, flowDecision</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="DYNAMIC_TYPE_MAPPING_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_CONNECTS_TO_SELF">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_COORDINATES_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, coordinateLimit, coordinateName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_INVALID_CONNECTOR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_INVALID_REFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_INVALID_REFERENCE_FOR_CONFLICTING_FIELD_VALUE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, conflictingField, conflictingFieldValue, reference</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_MISSING_CONNECTOR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_MISSING_LABEL">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, characterLimit, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_MISSING_NAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, characterLimit</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_MISSING_REFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_MORE_THAN_ONE_FIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_NAME_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_NEVER_USED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_SCALE_SMALLER_THAN_DEFAULTVALUE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_SUBTYPE_NOT_SUPPORTED_FOR_ELEMENTTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, elementSubtype</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ELEMENT_SUBTYPE_NOT_SUPPORTED_FOR_PROCESSTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType, elementSubtype</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="EXTERNAL_OBJECTS_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="EXTERNAL_OBJECT_FIELDS_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldReference</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="EX_AUTOLAUNCHED_SUBFLOW_INCOMPATIBLE_FLOWTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELDASSIGNMENT_FIELD_INCOMPATIBLE_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELDASSIGNMENT_INVALID_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, elementName, assignmentName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELDASSIGNMENT_INVALID_ELEMENT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, elementName, elementType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELDASSIGNMENT_INVALID_REFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELDASSIGNMENT_MULTIPLE_REFERENCES_SAME_FIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELDASSIGNMENT_PICKLISTFIELD_INCOMPATIBLE_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, dataType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELDASSIGNMENT_REFERENCED_ELEMENT_MISSING_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, elementName, elementType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELDSERVICE_UNSUPPORTED_FIELD_TYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELD_INVALID_VALUE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELD_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELD_RELATIONSHIP_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldRelationshipName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELD_TYPE_NOT_SUPPORTED_AS_CHILD_OF_SCREENFIELD_REGION_OR_REGIONCONTAINER">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELD_TYPE_NOT_SUPPORTED_AS_PARENT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FIELD_VALUE_REQUIRES_PERM">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_COMPONENT_ATTRIBUTE_EXPRESSION_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: componentName, propertyName, propertyType, errorCode, invalidTokens</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_COMPONENT_ATTRIBUTE_GENERIC_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: componentName, propertyName, propertyType, errorIdentifier, errorParams</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_COMPONENT_ATTRIBUTE_MISSING_REQUIRED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: componentName, propertyName, propertyType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_COMPONENT_ATTRIBUTE_TOO_LONG">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: componentName, propertyName, propertyType, maxLength</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_COMPONENT_CUSTOM_VALIDATION_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: componentName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_COMPONENT_DESIGN_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: componentName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_COMPONENT_EVENT_DUPLICATE_TARGET_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: eventName, sourceName, targetName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_COMPONENT_EVENT_EMPTY_TARGET_MAPPING_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: eventName, sourceName, targetName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_COMPONENT_EVENT_INVALID_FORMFACTOR_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: eventName, sourceName, targetName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_COMPONENT_EVENT_SOURCE_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: eventName, sourceName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_COMPONENT_MAX_LIMIT_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: componentCount, maxComponentLimit</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_COMPONENT_RULE_VALIDATION_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: componentName, criterionIndex</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_DUPLICATE_PROPERTY_COMPONENT_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: componentName, propertyName, propertyType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_EVENT_ATTRIBUTE_GENERIC_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: eventName, propertyName, propertyType, sourceName, targetName, errorIdentifier, errorParams</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_INVALID_ITEM_INSTANCE_TYPE_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: regionName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_INVALID_PROPERTY_TYPE_COMPONENT_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: componentName, propertyName, propertyType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_INVALID_PROPERTY_TYPE_EVENT_TARGET_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: eventName, propertyName, propertyType, sourceName, targetName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_ITEM_INSTANCE_CUSTOM_VALIDATION_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: instanceName, pageType, templateName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_MAX_INTERACTIONS_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: maxInteractionLimit</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_PICKLIST_INVALID_VALUE_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: componentName, propertyName, propertyType, invalidValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_RENAMED_COMPONENT_VALIDATION_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: componentName, externalAppVersion, priorComponentName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLEXIPAGE_TEMPLATE_INVALID_SWITCH">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: newTemplate, oldTemplate</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_CONTEXT_RECORD_ASSIGNMENT_VARIABLE_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, flowName, triggerType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_ELEMENT_SCALE_LESS_THAN_ZERO">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_IMMEDIATE_PATH_INCOMPATIBLE_WITH_EXTERNAL_CALLOUTS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_IMMEDIATE_PATH_INCOMPATIBLE_WITH_EXTERNAL_OBJECTS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INCLUDES_STEP">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_BULK_EXECUTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_HANDLED_ERROR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_INPUT_VALIDATION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_INTERACTION_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_INVALID_CHOICE_USER_INPUT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_INVALID_FIELD_VALUE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_INVALID_START_REQUEST">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_LIMIT_EXCEEDED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_MISSING_CHOICE_FOR_REQUIRED_CHOICE_FIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_MISSING_VALUE_FOR_REQUIRED_INPUT_FIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_NAVIGATE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_RANGE_VALIDATION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_REGEX_VALIDATION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_RESUME_INTERVIEW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_SAVE_RESULT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_SET_CHOICE_SELECTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_START_INTERVIEW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INTERVIEW_TYPE_CONVERSION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_INVALID_NAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, maxDevNameLength</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_NAME_USED_IN_OTHER_CLIENT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, flowName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_RECORD_PRIOR_AUTOLAUNCH_UPDATE_ONLY">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_RECORD_PRIOR_INVALID_IN_RECORD_CREATE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_RECORD_PRIOR_INVALID_IN_RECORD_DELETE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_RECORD_PRIOR_INVALID_IN_RECORD_UPDATE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_RECORD_PRIOR_READ_ONLY">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_REFERENCES_APEX_CLASS_NOT_IN_SAME_PACKAGE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_RULE_REQUIRE_RECORD_CHANGED_NEVER_CHECKED_FOR_RECORD_PRIOR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_SCHEDULED_PATH_INCOMPATIBLE_TIME_SOURCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_SCHEDULED_PATH_INCOMPATIBLE_WHEN_DECISION_REQUIRES_RECORD_CHANGED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, ruleName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_SCHEDULED_PATH_INCOMPATIBLE_WITH_FLOW_TRIGGER_TYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_SCHEDULED_PATH_INCOMPATIBLE_WITH_RECORD_PRIOR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, elementType, pathName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_SCHEDULED_PATH_INVALID_OFFSET">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_SCHEDULED_PATH_REQUIRES_DEFAULT_WORKFLOW_USER">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_SCHEDULED_PATH_REQUIRES_RECORD_CHANGED_TO_MEET_CRITERIA">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_SCHEDULE_INFORMATION_INCOMPLETE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType, flowStartFrequency, flowTriggerType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_SOBJECT_VARIABLE_NOT_PERSISTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, variableName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_STAGE_INCLUDES_REFERENCES">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, stageName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_STAGE_ORDER_DUPLICATE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, stageName, stageOrder, stageWithSameOrder</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_STAGE_ORDER_OUT_OF_RANGE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, stageName, invalidStageOrder, maxOrder, minOrder</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_SYSTEM_VARIABLE_NOT_SUPPORTED_FOR_TRIGGERTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType, systemVariable, triggerType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FLOW_TRIGGER_TYPE_INCOMPATIBLE_WITH_RECORD_TRIGGER_TYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, flowTriggerType, recordTriggerType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FORMULA_CMT_LIMIT_EXCEEDED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, formulaExpression</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="FORMULA_EXPRESSION_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, formulaExpression</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="GLOBAL_VARIABLE_NOT_SUPPORTED_FOR_PROCESSTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType, systemVariable</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INCONSISTENT_DYNAMIC_TYPE_MAPPING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INCONSISTENT_VALUE_FOR_DYNAMIC_VALUE_FIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, extensionName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INPUTPARAM_CONFIGURATION_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INPUTPARAM_INCOMPATIBLE_CONFIGURATION_ONLY">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INPUTPARAM_INCOMPATIBLE_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INPUTPARAM_INCOMPATIBLE_WITH_COLLECTION_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INPUTPARAM_INCOMPATIBLE_WITH_NONCOLLECTION_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INPUTPARAM_MISMATCHED_OBJECTTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INVALID_EMAIL_ADDRESS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, actionCallName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INVALID_FLOW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INVALID_FLOW_INTERVIEW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INVALID_REGEX_IN_SURVEY_QUESTIONS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INVALID_SENDER_TYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, actionCallName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="INVALID_SURVEY_VARIABLE_NAME_OR_TYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, surveyName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="LOOP_ASSIGNNEXTVALUETO_MISMATCHED_APEXCLASSTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="LOOP_ASSIGNNEXTVALUETO_MISMATCHED_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="LOOP_ASSIGNNEXTVALUETO_MISMATCHED_OBJECTTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="LOOP_ASSIGNNEXTVALUETO_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="LOOP_ASSIGNNEXTVALUETO_MISSING_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="LOOP_ASSIGNNEXTVALUETO_REFERENCE_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldRelationshipName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="LOOP_COLLECTION_ELEMENT_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="LOOP_COLLECTION_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="LOOP_COLLECTION_NOT_SUPPORTED_FOR_FIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="LOOP_MISSING_COLLECTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="MISSING_EMAIL_RECIPIENTS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="NON_EXPOSED_COMPONENT_IN_FLOW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="NON_GLOBAL_COMPONENT_IN_EXPORTED_FLOW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="NUMBER_OF_SCREENFIELD_REGIONS_EXCEEDS_LIMIT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OBJECTTYPE_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OBJECT_CANNOT_BE_CREATED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OBJECT_CANNOT_BE_DELETED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OBJECT_CANNOT_BE_QUERIED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OBJECT_CANNOT_BE_UPDATED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OBJECT_ENCRYPTED_FIELDS_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OBJECT_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OBJECT_TYPE_DOES_NOT_EXIST">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ORG_WIDE_EMAIL_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, orgWideEmailAddress</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="ORG_WIDE_EMAIL_NOT_USED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OUTPUTPARAM_ASSIGNTOREFERENCE_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OUTPUTPARAM_ASSIGNTOREFERENCE_NOTFOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OUTPUTPARAM_INCOMPATIBLE_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OUTPUTPARAM_MISMATCHED_OBJECTTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OUTPUTPARAM_MISMATCHED_WITH_COLLECTION_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OUTPUTPARAM_MISSING_ASSIGNTOREFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="OUTPUTPARAM_MISTMATCHED_WITH_NONCOLLECTION_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="PARAM_DATATYPE_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="PAST_SCHEDULE_FLOW_WILL_NOT_RUN">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="PROCESSMETADATAVALUES_NOT_SUPPORTED_FOR_PROCESSTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType, metadataValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="PROCESSMETADATAVALUE_NONEXISTENT_ELEMENT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, metadataValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="PROCESSTYPE_COMPONENTTYPE_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType, fieldType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="PROCESSTYPE_ELEMENT_CONFIG_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType, attributeSet, elementType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="PROCESSTYPE_ELEMENT_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType, elementType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="PROCESSTYPE_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="PROCESSTYPE_SCREEN_FIELDTYPE_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType, fieldType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="PROCESS_TYPE_INCOMPATIBLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, currentProcessType, flowName, incompatibleProcessType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECOMMENDATION_STRATEGY_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: errorArguments, errorCode</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECORDFILTER_ENCRYPTED_FIELDS_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECORDFILTER_GEOLOCATION_FIELDS_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECORDFILTER_INVALID_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, elementName, elementType, operatorName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECORDFILTER_INVALID_ELEMENT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, assignmentName, elementName, elementType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECORDFILTER_INVALID_OPERATOR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, operatorName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECORDFILTER_INVALID_REFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, operatorName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECORDFILTER_MISSING_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, elementName, elementType, operatorName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECORDFILTER_MULTIPLE_QUERIES_SAME_FIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECORDFILTER_NON_PRIMITIVE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECORDLOOKUP_IDASSIGNMENT_VARIABLE_INCOMPATIBLE_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECORDLOOKUP_IDASSIGNMENT_VARIABLE_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RECORDUPDATE_MISSING_FILTERS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="REFERENCED_ELEMENT_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, mergeFieldReference</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="REQUIRED_VARIABLE_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="REQUIRED_VARIABLE_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RULE_MISSING_CONDITION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, ruleName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="RULE_REQUIRE_RECORD_CHANGED_NEVER_CHECKED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENCOMPONENT_CONTAINS_VISIBILITY_RULE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_API_VERSION_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_BOOLEAN_ISREQUIRED_IS_FALSE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_CANNOT_HAVE_BOTH_DEFAULTVALUE_AND_DEFAULTSELECTEDCHOICEREFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_DEFAULTVALUE_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_EXTENSION_DUPLICATE_INPUT_PARAM">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, extensionName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_EXTENSION_DUPLICATE_OUTPUT_PARAM">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, extensionName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_EXTENSION_IMPLEMENTATION_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, extensionName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_EXTENSION_INPUT_ATTRIBUTE_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, extensionName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_EXTENSION_NAME_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, extensionName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_EXTENSION_NAME_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, fieldType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_EXTENSION_NAME_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, fieldType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_EXTENSION_OUTPUT_ATTRIBUTE_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, extensionName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_EXTENSION_REQUIRED_INPUT_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, extensionName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_INPUTS_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, fieldType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_INPUTS_ON_NEXT_NAV_TO_ASSOC_SCRN_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, fieldType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_INVALID_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, dataType, fieldType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_MULTISELECTCHOICE_SEMICOLON_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, choiceName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_OBJECTFIELDREFERENCE_INVALID_FORMAT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, objectFieldReference</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_OBJECTPROVIDED_CANNOT_HAVE_DEFAULTVALUE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_OBJECTPROVIDED_CANNOT_HAVE_HELPTEXT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_OBJECTPROVIDED_MISSING_OBJECTFIELDREFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_OUTPUTS_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, fieldType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_REGION_CONTAINS_DUPLICATE_INPUT_PARAMETER_VALUES">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_REGION_INPUT_PARAMETER_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_REGION_MISSING_REQUIRED_PERMISSIONS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_REGION_NOT_IN_CONTAINER">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_REGION_REQUIRED_INPUT_PARAMETER_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_REGION_WIDTH_SUM_EXCEEDS_LIMIT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_REGION_WIDTH_VALUE_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_TYPE_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, fieldType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_TYPE_NOT_SUPPORTED_FOR_API_VERSION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_USERINPUT_NOT_SUPPORTED_FOR_CHOICETYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, choiceName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENFIELD_VALIDATIONRULE_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENRULE_ACTION_INVALID_ATTRIBUTE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, screenRuleName, attributeName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENRULE_ACTION_INVALID_ATTRIBUTE_FOR_API_VERSION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, screenRuleName, attributeName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENRULE_ACTION_INVALID_VALUE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, screenRuleName, acceptedValues, actionValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENRULE_ACTION_MISSING_ATTRIBUTE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, screenRuleName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENRULE_ACTION_MISSING_FIELDREFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, screenRuleName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENRULE_ACTION_MISSING_VALUE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, screenRuleName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENRULE_ATTRIBUTE_NOT_SUPPORTED_FOR_SCREENFIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, screenRuleName, attributeName, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENRULE_FIELD_NOT_FOUND_ON_SCREEN">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, screenRuleName, fieldValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENRULE_MISSING_ACTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, screenRuleName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENRULE_NOT_SUPPORTED_IN_ORG">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENRULE_SCREENFIELD_NOT_VISIBLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREENRULE_VISIBILITY_NOT_SUPPORTED_IN_ORG">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREEN_ALLOWBACK_ALLOWFINISH_BOTH_FALSE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREEN_CONTAINS_LIGHTNING_COMPONENT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREEN_CONTAINS_REGION_CONTAINER_COMPONENT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREEN_MISSING_FOOTER_AND_LIGHTNING_COMPONENT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREEN_MISSING_LABEL">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, characterLimit</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREEN_MULTISELECTFIELD_DOESNT_SUPPORT_CHOICE_WITH_USERINPUT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, choiceName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SCREEN_PAUSEDTEXT_NOT_SHOWN_WHEN_ALLOWPAUSE_IS_FALSE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SETTING_FIELD_MAKES_OTHER_FIELD_REQUIRED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, requiredField</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SETTING_FIELD_MAKES_OTHER_FIELD_UNSUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, otherFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SETTING_FIELD_VALUE_MAKES_OTHER_FIELD_UNSUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, otherFieldName, value</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SETTING_FIELD_VALUE_MAKES_OTHER_FIELD_VALUE_UNSUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, fieldValue, otherFieldName, otherFieldValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SOBJECT_ELEMENT_INCOMPATIBLE_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, fieldValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SOBJECT_ELEMENT_MISMATCHED_OBJECTTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectType, sobjectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SORT_ENCRYPTED_FIELDS_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, objectType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SORT_FIELD_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, sortOrder</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SORT_FIELD_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SORT_GEOLOCATION_FIELDS_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SORT_LIMIT_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, maxLimit</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SORT_ORDER_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SPECIFIC_FIELD_VALUE_MAKES_OTHER_FIELD_REQUIRED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, fieldType, requiedField</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="STAGE_NAME_NOT_FULLY_QUALIFIED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="START_ELEMENT_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_DESKTOP_DESIGNER_FLOWS_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, flowName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_DIFFERENT_RUNMODE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, flowName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INPUT_ELEMENT_INCOMPATIBLE_DATATYPES">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, inputAssignmentNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INPUT_INVALID_VALUE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, inputAssignmentNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INPUT_MISMATCHED_APEX_CLASS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, inputParameterNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INPUT_MISMATCHED_COLLECTIONTYPES">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, inputParameterNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INPUT_MISMATCHED_OBJECTS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, inputParameterNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INPUT_MISSING_NAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INPUT_MULTIPLE_ASSIGNMENTS_TO_ONE_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, inputVariableName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INPUT_REFERENCES_FIELD_ON_SOBJECT_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, inputVariableName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INPUT_VALUE_INCOMPATIBLE_DATATYPES">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, inputAssignmentNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INPUT_VARIABLE_NOT_FOUND_IN_MASTERFLOW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, inputAssignmentNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INPUT_VARIABLE_NOT_FOUND_IN_REFERENCEDFLOW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, inputAssignmentNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INPUT_VARIABLE_NO_INPUT_ACCESS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, inputAssignmentNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INVALID_NAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_INVALID_REFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, flowName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_MASTER_FLOW_TYPE_NOT_AUTOLAUNCHED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parentFlowName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_MISSING_NAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_NO_ACTIVE_VERSION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, flowName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_OUTPUT_INCOMPATIBLE_DATATYPES">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, flowVersion, outputParameterNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_OUTPUT_MISMATCHED_APEX_CLASS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, flowVersion, outputParameterNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_OUTPUT_MISMATCHED_COLLECTIONTYPES">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, flowVersion, outputParameterNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_OUTPUT_MISMATCHED_OBJECTS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, flowVersion, outputParameterNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_OUTPUT_MISSING_ASSIGNTOREFERENCE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, outputAssignment</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_OUTPUT_MISSING_NAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_OUTPUT_MULTIPLE_ASSIGNMENTS_TO_ONE_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, outputVariableName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_OUTPUT_REFERENCES_FIELD_ON_SOBJECT_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, outputAssignment</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_OUTPUT_TARGET_DOES_NOT_EXIST_IN_MASTER_FLOW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, outputAssignmentName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_OUTPUT_VARIABLE_NOT_FOUND_IN_MASTERFLOW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, variableName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_OUTPUT_VARIABLE_NOT_FOUND_IN_REFERENCEDFLOW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, flowVersion, outputParameterNames</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_OUTPUT_VARIABLE_NO_OUTPUT_ACCESS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, variableName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_PROCESSTYPE_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType, subflowElementName, subflowName, subflowProcessType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_PROCESS_TYPE_INCOMPATIBLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, flowName, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SUBFLOW_REFERENCES_MASTERFLOW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_ADVANCED_CONDITION_LOGIC_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_CHOICE_NOT_REFERENCED_BY_A_QUESTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, choiceName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_CHOICE_REFERENCED_BY_MULTIPLE_QUESTIONS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, choiceName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_ELEMENT_NEVER_REACHED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_ENRICH_INVALID_CONFIGURATION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, surveyName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_INACTIVE_SUBFLOWS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_INVALID_ATTACHMENT_QUESTION_CONFIGURATION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_INVALID_CMT_CONFIGURED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_INVALID_LINK_TARGET_IN_QUESTION_LABEL">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_INVALID_MERGE_FIELD_CONFIGURATION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_INVALID_OUTPUT_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, surveyName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_MISSING_QUESTION_OR_SUBFLOW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, surveyName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_MISSING_REQUIRED_VARIABLES">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, surveyName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_MULTIPLE_SCREENS_CANNOT_CONNECT_TO_SAME_DECISION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, flowDecision</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_NESTED_SUBFLOWS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_NONSURVEY_SUBFLOWS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_RULE_INVALID_RIGHT_OPERAND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_SCREENFIELD_TYPE_NOT_SUPPORTED_FOR_QUESTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_START_ELEMENT_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SURVEY_VARIABLE_ACCESS_INVALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, surveyName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="SYSTEM_MODE_NOT_ALLOWED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="TRIGGERED_FLOW_REDUNDANT_QUERY">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="TRIGGERING_RECORD_UPDATE_REQUIRES_INPUTASSIGNMENTS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="TRIGGER_TYPE_CONTEXT_OBJECT_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectName, triggerType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="TRIGGER_TYPE_ELEMENT_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementType, triggerType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="TRIGGER_TYPE_INCOMPATIBLE_WITH_PROCESS_TYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="TRIGGER_TYPE_NOT_ALLOWED_FOR_SUBFLOW">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, subflowName, triggerType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="TYPE_MAPPING_DUPLICATED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="TYPE_MAPPING_NAME_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="TYPE_MAPPING_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="TYPE_MAPPING_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="TYPE_MAPPING_NOT_SUPPORTED_FOR_API_VERSION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="TYPE_MAPPING_NOT_SUPPORTED_FOR_PROCESS_TYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="UNEXPECTED_ERROR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VALIDATION_EXCEPTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: field, message, parentResourceName, resourceName, resourceType, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VALUE_CHAR_LIMIT_EXCEEDED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName, characterLimit</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VARIABLE_FIELD_NOT_SUPPORTED_FOR_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, datatype</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VARIABLE_FIELD_NOT_SUPPORTED_FOR_DATATYPE_AND_COLLECTION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName, datatype</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VARIABLE_FIELD_REQUIRED_FOR_DATATYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, datatype, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VARIABLE_SCALE_EXCEEDS_LIMIT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VARIABLE_SCALE_NEGATIVE_INTEGER">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VARIABLE_SCALE_NULL">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VERSION_NOT_VALID">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, apiVersion</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VISIBILITY_RULE_EXCEEDS_CONDITION_LIMIT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VISIBILITY_RULE_NOT_AVAILABLE_IN_ORG">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VISIBILITY_RULE_NOT_SUPPORTED_FOR_API_VERSION">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VISIBILITY_RULE_NOT_SUPPORTED_FOR_PROCESSTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, processType, screenFieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="VISIBILITY_RULE_NO_CONDITIONS">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, fieldName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_DEFAULT_CONNECTOR_MISSING_LABEL">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_DUPLICATE_INPUT_PARAM">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_INPUT_NOT_SUPPORTED_FOR_EVENTTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName, inputParameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_INPUT_REQUIRES_LITERAL_VALUE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_INVALID_CONDITION_LOGIC">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_MISSING_CONNECTOR">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_MISSING_EVENTTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_OBJECT_NOT_SUPPORTED_FOR_EVENTTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_OUTPUT_NOT_SUPPORTED_FOR_EVENTTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName, outputParameter</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_RELATIVEALARM_INVALID_DATETIME_FIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName, eventParameterName, incompatibleValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_RELATIVEALARM_INVALID_FIELD">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName, eventParameterName, incompatibleValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_RELATIVEALARM_INVALID_OBJECTTYPE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName, inputParameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_RELATIVEALARM_INVALID_OFFSETNUMBER">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName, eventParameterName, incompatibleValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_RELATIVEALARM_INVALID_OFFSETUNIT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName, eventParameterName, incompatibleValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_REQUIRED_INPUT_MISSING">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName, parameterName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WAITEVENT_TYPE_INVALID_OR_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, waitEventName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WORKFLOW_MISSING_PROCESSMETADATAVALUES">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, flowName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WORKFLOW_OBJECTTYPE_NOT_FOUND">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WORKFLOW_OBJECTTYPE_NOT_SUPPORTED">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectType</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WORKFLOW_OBJECTVARIABLE_AND_OLDOBJECTVARIABLE_REFERENCE_SAME_SOBJECT_VARIABLE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectVariableName, oldObjectVariableName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WORKFLOW_OBJECTVARIABLE_DOESNT_SUPPORT_INPUT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectType, objectVariableName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WORKFLOW_OLDOBJECTVARIABLE_DOESNT_SUPPORT_INPUT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, objectType, oldObjectVariableName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WORKFLOW_PROCESSMETADATAVALUES_MORE_THAN_ONE_NAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, metadataValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WORKFLOW_PROCESS_METADATAVALUES_MISSING_NAME">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, metadataValue</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WORKFLOW_RECURSIVECOUNTVARIABLE_DOESNT_SUPPORT_INPUT">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity, elementName</xsd:documentation></xsd:annotation></xsd:enumeration>
     <xsd:enumeration value="WORKFLOW_TRIGGERTYPE_INVALID_VALUE">
      <xsd:annotation>
       <xsd:documentation>Errors with this extended error code have the following properties: erroneousElementApiName, erroneousElementType, erroneousFields, severity</xsd:documentation></xsd:annotation></xsd:enumeration></xsd:restriction></xsd:simpleType>
   <xsd:complexType name="ExtendedErrorDetails">
    <xsd:sequence>
     <xsd:element name="extendedErrorCode" type="tns:ExtendedErrorCode"/>
     <xsd:any namespace="##targetNamespace" minOccurs="0" maxOccurs="unbounded" processContents="lax"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DeleteResult">
    <xsd:sequence>
     <xsd:element name="errors" minOccurs="0" maxOccurs="unbounded" type="tns:Error"/>
     <xsd:element name="fullName" type="xsd:string"/>
     <xsd:element name="success" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DeployOptions">
    <xsd:sequence>
     <xsd:element name="allowMissingFiles" type="xsd:boolean"/>
     <xsd:element name="autoUpdatePackage" type="xsd:boolean"/>
     <xsd:element name="checkOnly" type="xsd:boolean"/>
     <xsd:element name="ignoreWarnings" type="xsd:boolean"/>
     <xsd:element name="performRetrieve" type="xsd:boolean"/>
     <xsd:element name="purgeOnDelete" type="xsd:boolean"/>
     <xsd:element name="rollbackOnError" type="xsd:boolean"/>
     <xsd:element name="runTests" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="singlePackage" type="xsd:boolean"/>
     <xsd:element name="testLevel" type="tns:TestLevel"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="TestLevel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="NoTestRun"/>
     <xsd:enumeration value="RunSpecifiedTests"/>
     <xsd:enumeration value="RunLocalTests"/>
     <xsd:enumeration value="RunAllTestsInOrg"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="AsyncResult">
    <xsd:sequence>
     <xsd:element name="done" type="xsd:boolean"/>
     <xsd:element name="id" type="tns:ID"/>
     <xsd:element name="message" minOccurs="0" type="xsd:string"/>
     <xsd:element name="state" type="tns:AsyncRequestState"/>
     <xsd:element name="statusCode" minOccurs="0" type="tns:StatusCode"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="AsyncRequestState">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Queued"/>
     <xsd:enumeration value="InProgress"/>
     <xsd:enumeration value="Completed"/>
     <xsd:enumeration value="Error"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:complexType name="DescribeMetadataResult">
    <xsd:sequence>
     <xsd:element name="metadataObjects" minOccurs="0" maxOccurs="unbounded" type="tns:DescribeMetadataObject"/>
     <xsd:element name="organizationNamespace" type="xsd:string"/>
     <xsd:element name="partialSaveAllowed" type="xsd:boolean"/>
     <xsd:element name="testRequired" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DescribeMetadataObject">
    <xsd:sequence>
     <xsd:element name="childXmlNames" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="directoryName" type="xsd:string"/>
     <xsd:element name="inFolder" type="xsd:boolean"/>
     <xsd:element name="metaFile" type="xsd:boolean"/>
     <xsd:element name="suffix" minOccurs="0" type="xsd:string"/>
     <xsd:element name="xmlName" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="DescribeValueTypeResult">
    <xsd:sequence>
     <xsd:element name="apiCreatable" type="xsd:boolean"/>
     <xsd:element name="apiDeletable" type="xsd:boolean"/>
     <xsd:element name="apiReadable" type="xsd:boolean"/>
     <xsd:element name="apiUpdatable" type="xsd:boolean"/>
     <xsd:element name="parentField" minOccurs="0" type="tns:ValueTypeField"/>
     <xsd:element name="valueTypeFields" minOccurs="0" maxOccurs="unbounded" type="tns:ValueTypeField"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ValueTypeField">
    <xsd:sequence>
     <xsd:element name="fields" minOccurs="0" maxOccurs="unbounded" type="tns:ValueTypeField"/>
     <xsd:element name="foreignKeyDomain" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="isForeignKey" type="xsd:boolean"/>
     <xsd:element name="isNameField" type="xsd:boolean"/>
     <xsd:element name="minOccurs" type="xsd:int"/>
     <xsd:element name="name" type="xsd:string"/>
     <xsd:element name="picklistValues" minOccurs="0" maxOccurs="unbounded" type="tns:PicklistEntry"/>
     <xsd:element name="soapType" type="xsd:string"/>
     <xsd:element name="valueRequired" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="PicklistEntry">
    <xsd:sequence>
     <xsd:element name="active" type="xsd:boolean"/>
     <xsd:element name="defaultValue" type="xsd:boolean"/>
     <xsd:element name="label" type="xsd:string"/>
     <xsd:element name="validFor" minOccurs="0" type="xsd:string"/>
     <xsd:element name="value" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ListMetadataQuery">
    <xsd:sequence>
     <xsd:element name="folder" minOccurs="0" type="xsd:string"/>
     <xsd:element name="type" type="xsd:string"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="ReadResult">
    <xsd:sequence>
     <xsd:element name="records" minOccurs="0" maxOccurs="unbounded" type="tns:Metadata"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="RetrieveRequest">
    <xsd:sequence>
     <xsd:element name="apiVersion" type="xsd:double"/>
     <xsd:element name="packageNames" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="singlePackage" type="xsd:boolean"/>
     <xsd:element name="specificFiles" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     <xsd:element name="unpackaged" minOccurs="0" type="tns:Package"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:complexType name="UpsertResult">
    <xsd:sequence>
     <xsd:element name="created" type="xsd:boolean"/>
     <xsd:element name="errors" minOccurs="0" maxOccurs="unbounded" type="tns:Error"/>
     <xsd:element name="fullName" type="xsd:string"/>
     <xsd:element name="success" type="xsd:boolean"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:element name="AllOrNoneHeader">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="allOrNone" type="xsd:boolean"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="CallOptions">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="client" type="xsd:string"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="DebuggingHeader">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="categories" minOccurs="0" maxOccurs="unbounded" type="tns:LogInfo"/>
      <xsd:element name="debugLevel" type="tns:LogType"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:complexType name="LogInfo">
    <xsd:sequence>
     <xsd:element name="category" type="tns:LogCategory"/>
     <xsd:element name="level" type="tns:LogCategoryLevel"/>
    </xsd:sequence>
   </xsd:complexType>
   <xsd:simpleType name="LogCategory">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="Db"/>
     <xsd:enumeration value="Workflow"/>
     <xsd:enumeration value="Validation"/>
     <xsd:enumeration value="Callout"/>
     <xsd:enumeration value="Apex_code"/>
     <xsd:enumeration value="Apex_profiling"/>
     <xsd:enumeration value="Visualforce"/>
     <xsd:enumeration value="System"/>
     <xsd:enumeration value="Wave"/>
     <xsd:enumeration value="Nba"/>
     <xsd:enumeration value="All"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="LogCategoryLevel">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="Finest"/>
     <xsd:enumeration value="Finer"/>
     <xsd:enumeration value="Fine"/>
     <xsd:enumeration value="Debug"/>
     <xsd:enumeration value="Info"/>
     <xsd:enumeration value="Warn"/>
     <xsd:enumeration value="Error"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="LogType">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="None"/>
     <xsd:enumeration value="Debugonly"/>
     <xsd:enumeration value="Db"/>
     <xsd:enumeration value="Profiling"/>
     <xsd:enumeration value="Callout"/>
     <xsd:enumeration value="Detail"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:element name="DebuggingInfo">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="debugLog" type="xsd:string"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="SessionHeader">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="sessionId" type="xsd:string"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:simpleType name="ID">
    <xsd:restriction base="xsd:string">
     <xsd:length value="18"/>
     <xsd:pattern value="[a-zA-Z0-9]{18}"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:simpleType name="StatusCode">
    <xsd:restriction base="xsd:string">
     <xsd:enumeration value="ACCESSLIMITED"/>
     <xsd:enumeration value="ACCOUNT_INACTIVE"/>
     <xsd:enumeration value="ALL_OR_NONE_OPERATION_ROLLED_BACK"/>
     <xsd:enumeration value="ALREADY_ARCHIVED"/>
     <xsd:enumeration value="ALREADY_IN_PROCESS"/>
     <xsd:enumeration value="ALREADY_IN_TEAM"/>
     <xsd:enumeration value="ALREADY_IN_TEAM_INVITED_USER"/>
     <xsd:enumeration value="ALREADY_REDEEMED_VOUCHER"/>
     <xsd:enumeration value="APEX_DATA_ACCESS_RESTRICTION"/>
     <xsd:enumeration value="APEX_FAILED"/>
     <xsd:enumeration value="ASSIGNEE_TYPE_REQUIRED"/>
     <xsd:enumeration value="AS_USER_NOT_SUPPORTED"/>
     <xsd:enumeration value="AURA_COMPILE_ERROR"/>
     <xsd:enumeration value="AUTH_PROVIDER_NEEDS_AUTH"/>
     <xsd:enumeration value="AUTH_PROVIDER_NOT_FOUND"/>
     <xsd:enumeration value="B2B_SEARCH_ADMIN_ERROR"/>
     <xsd:enumeration value="BAD_CUSTOM_ENTITY_PARENT_DOMAIN"/>
     <xsd:enumeration value="BCC_NOT_ALLOWED_IF_BCC_COMPLIANCE_ENABLED"/>
     <xsd:enumeration value="CANNOT_CASCADE_PRODUCT_ACTIVE"/>
     <xsd:enumeration value="CANNOT_CHANGE_FIELD_TYPE_OF_APEX_REFERENCED_FIELD"/>
     <xsd:enumeration value="CANNOT_CHANGE_FIELD_TYPE_OF_REFERENCED_FIELD"/>
     <xsd:enumeration value="CANNOT_CREATE_ANOTHER_MANAGED_PACKAGE"/>
     <xsd:enumeration value="CANNOT_DEACTIVATE_DIVISION"/>
     <xsd:enumeration value="CANNOT_DELETE_GLOBAL_ACTION_LIST"/>
     <xsd:enumeration value="CANNOT_DELETE_LAST_DATED_CONVERSION_RATE"/>
     <xsd:enumeration value="CANNOT_DELETE_MANAGED_OBJECT"/>
     <xsd:enumeration value="CANNOT_DISABLE_LAST_ADMIN"/>
     <xsd:enumeration value="CANNOT_ENABLE_IP_RESTRICT_REQUESTS"/>
     <xsd:enumeration value="CANNOT_EXECUTE_FLOW_TRIGGER"/>
     <xsd:enumeration value="CANNOT_FREEZE_SELF"/>
     <xsd:enumeration value="CANNOT_INSERT_UPDATE_ACTIVATE_ENTITY"/>
     <xsd:enumeration value="CANNOT_MODIFY_MANAGED_OBJECT"/>
     <xsd:enumeration value="CANNOT_PASSWORD_LOCKOUT"/>
     <xsd:enumeration value="CANNOT_POST_TO_ARCHIVED_GROUP"/>
     <xsd:enumeration value="CANNOT_RENAME_APEX_REFERENCED_FIELD"/>
     <xsd:enumeration value="CANNOT_RENAME_APEX_REFERENCED_OBJECT"/>
     <xsd:enumeration value="CANNOT_RENAME_REFERENCED_FIELD"/>
     <xsd:enumeration value="CANNOT_RENAME_REFERENCED_OBJECT"/>
     <xsd:enumeration value="CANNOT_REPARENT_RECORD"/>
     <xsd:enumeration value="CANNOT_UPDATE_CONVERTED_LEAD"/>
     <xsd:enumeration value="CANT_ARCHIVE_GENERAL"/>
     <xsd:enumeration value="CANT_DISABLE_CORP_CURRENCY"/>
     <xsd:enumeration value="CANT_UNSET_CORP_CURRENCY"/>
     <xsd:enumeration value="CHANNEL_NOT_FOUND"/>
     <xsd:enumeration value="CHANNEL_TYPE_NOT_SUPPORTED"/>
     <xsd:enumeration value="CHILD_SHARE_FAILS_PARENT"/>
     <xsd:enumeration value="CIRCULAR_DEPENDENCY"/>
     <xsd:enumeration value="CLEAN_SERVICE_ERROR"/>
     <xsd:enumeration value="CLONE_FIELD_INTEGRITY_EXCEPTION"/>
     <xsd:enumeration value="CLONE_NOT_SUPPORTED"/>
     <xsd:enumeration value="CMS_FOLDER_ITEM_MOVE_FAILED"/>
     <xsd:enumeration value="COLLISION_DETECTED"/>
     <xsd:enumeration value="COMMERCIAL_CONTROL_ERROR"/>
     <xsd:enumeration value="COMMUNITY_NOT_ACCESSIBLE"/>
     <xsd:enumeration value="CONFLICTING_ENVIRONMENT_HUB_MEMBER"/>
     <xsd:enumeration value="CONFLICTING_SSO_USER_MAPPING"/>
     <xsd:enumeration value="CONTENT_NOT_FOUND"/>
     <xsd:enumeration value="CONTENT_SEARCH_NOT_ENABLED"/>
     <xsd:enumeration value="CONTENT_TYPE_NOT_FOUND"/>
     <xsd:enumeration value="COULD_NOT_ARCHIVE_CHANNEL"/>
     <xsd:enumeration value="COULD_NOT_CREATE_CHANNEL"/>
     <xsd:enumeration value="CUSTOM_APEX_ERROR"/>
     <xsd:enumeration value="CUSTOM_CLOB_FIELD_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="CUSTOM_ENTITY_OR_FIELD_LIMIT"/>
     <xsd:enumeration value="CUSTOM_FIELD_INDEX_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="CUSTOM_INDEX_EXISTS"/>
     <xsd:enumeration value="CUSTOM_LINK_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="CUSTOM_METADATA_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="CUSTOM_METADATA_REL_FIELD_MANAGEABILITY"/>
     <xsd:enumeration value="CUSTOM_SETTINGS_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="CUSTOM_TAB_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="DATAASSESSMENT_CONFIG_ASSESSMENT_IN_PROGRESS_ERROR"/>
     <xsd:enumeration value="DATAASSESSMENT_CONFIG_SERVICE_ERROR"/>
     <xsd:enumeration value="DATACLOUDADDRESS_NO_RECORDS_FOUND"/>
     <xsd:enumeration value="DATACLOUDADDRESS_PROCESSING_ERROR"/>
     <xsd:enumeration value="DATACLOUDADDRESS_SERVER_ERROR"/>
     <xsd:enumeration value="DATE_OUT_OF_RANGE"/>
     <xsd:enumeration value="DEFAULT_ORG_WIDE_CHANNEL"/>
     <xsd:enumeration value="DELETE_FAILED"/>
     <xsd:enumeration value="DELETE_NOT_ALLOWED"/>
     <xsd:enumeration value="DELETE_OPERATION_TOO_LARGE"/>
     <xsd:enumeration value="DELETE_REQUIRED_ON_CASCADE"/>
     <xsd:enumeration value="DEPENDENCY_EXISTS"/>
     <xsd:enumeration value="DEPRECATED_ENDPOINT"/>
     <xsd:enumeration value="DUPLICATES_DETECTED"/>
     <xsd:enumeration value="DUPLICATE_CASE_SOLUTION"/>
     <xsd:enumeration value="DUPLICATE_CHANNEL_NOT_FOUND"/>
     <xsd:enumeration value="DUPLICATE_COMM_NICKNAME"/>
     <xsd:enumeration value="DUPLICATE_CUSTOM_ENTITY_DEFINITION"/>
     <xsd:enumeration value="DUPLICATE_CUSTOM_TAB_MOTIF"/>
     <xsd:enumeration value="DUPLICATE_DEVELOPER_NAME"/>
     <xsd:enumeration value="DUPLICATE_EXTERNAL_ID"/>
     <xsd:enumeration value="DUPLICATE_MASTER_LABEL"/>
     <xsd:enumeration value="DUPLICATE_MESSAGE_NOT_FOUND"/>
     <xsd:enumeration value="DUPLICATE_SENDER_DISPLAY_NAME"/>
     <xsd:enumeration value="DUPLICATE_USERNAME"/>
     <xsd:enumeration value="DUPLICATE_VALUE"/>
     <xsd:enumeration value="EKM_ACCESS_DENIED"/>
     <xsd:enumeration value="EMAIL_ADDRESS_BOUNCED"/>
     <xsd:enumeration value="EMAIL_EXTERNAL_TRANSPORT_CONNECTION_ERROR"/>
     <xsd:enumeration value="EMAIL_EXTERNAL_TRANSPORT_PERMISSION_ERROR"/>
     <xsd:enumeration value="EMAIL_EXTERNAL_TRANSPORT_TOKEN_ERROR"/>
     <xsd:enumeration value="EMAIL_EXTERNAL_TRANSPORT_TOO_LARGE_ERROR"/>
     <xsd:enumeration value="EMAIL_EXTERNAL_TRANSPORT_TOO_MANY_REQUESTS_ERROR"/>
     <xsd:enumeration value="EMAIL_EXTERNAL_TRANSPORT_UNKNOWN_ERROR"/>
     <xsd:enumeration value="EMAIL_NOT_PROCESSED_DUE_TO_PRIOR_ERROR"/>
     <xsd:enumeration value="EMAIL_OPTED_OUT"/>
     <xsd:enumeration value="EMAIL_TEMPLATE_FORMULA_ERROR"/>
     <xsd:enumeration value="EMAIL_TEMPLATE_MERGEFIELD_ACCESS_ERROR"/>
     <xsd:enumeration value="EMAIL_TEMPLATE_MERGEFIELD_ERROR"/>
     <xsd:enumeration value="EMAIL_TEMPLATE_MERGEFIELD_VALUE_ERROR"/>
     <xsd:enumeration value="EMAIL_TEMPLATE_PROCESSING_ERROR"/>
     <xsd:enumeration value="EMPTY_SCONTROL_FILE_NAME"/>
     <xsd:enumeration value="ENHANCED_EMAIL_TEMPLATE_COMPILATION_ERROR"/>
     <xsd:enumeration value="ENTERPRISE_IS_RESTRICTED"/>
     <xsd:enumeration value="ENTITY_FAILED_IFLASTMODIFIED_ON_UPDATE"/>
     <xsd:enumeration value="ENTITY_IS_ARCHIVED"/>
     <xsd:enumeration value="ENTITY_IS_DELETED"/>
     <xsd:enumeration value="ENTITY_IS_LOCKED"/>
     <xsd:enumeration value="ENTITY_SAVE_ERROR"/>
     <xsd:enumeration value="ENTITY_SAVE_VALIDATION_ERROR"/>
     <xsd:enumeration value="ENVIRONMENT_HUB_MEMBERSHIP_CONFLICT"/>
     <xsd:enumeration value="ENVIRONMENT_HUB_MEMBERSHIP_ERROR_JOINING_HUB"/>
     <xsd:enumeration value="ENVIRONMENT_HUB_MEMBERSHIP_USER_ALREADY_IN_HUB"/>
     <xsd:enumeration value="ENVIRONMENT_HUB_MEMBERSHIP_USER_NOT_ORG_ADMIN"/>
     <xsd:enumeration value="ERROR_CALCULATING_EXPIRY_DATE"/>
     <xsd:enumeration value="ERROR_IN_MAILER"/>
     <xsd:enumeration value="EXCEEDED_MAX_SEMIJOIN_SUBSELECTS_WRITE"/>
     <xsd:enumeration value="EXCHANGE_WEB_SERVICES_URL_INVALID"/>
     <xsd:enumeration value="EXTERNAL_RESOURCE_FORBIDDEN"/>
     <xsd:enumeration value="FAILED_ACTIVATION"/>
     <xsd:enumeration value="FAILED_DUE_TO_OTHER_INPUTS"/>
     <xsd:enumeration value="FAILED_FOR_SOME_USERS"/>
     <xsd:enumeration value="FAILED_LOOKING_UP_USER"/>
     <xsd:enumeration value="FAILED_TO_SEND_INVITE"/>
     <xsd:enumeration value="FAILED_TO_VALIDATE_CALLER"/>
     <xsd:enumeration value="FAILED_TO_VALIDATE_CHANNELS"/>
     <xsd:enumeration value="FAILED_TO_VALIDATE_CUSTOM_MESSAGE"/>
     <xsd:enumeration value="FAILED_TO_VALIDATE_EXPIRATION"/>
     <xsd:enumeration value="FAILED_TO_VALIDATE_TEAM"/>
     <xsd:enumeration value="FATAL_ERROR"/>
     <xsd:enumeration value="FEATURE_NOT_ENABLED"/>
     <xsd:enumeration value="FETCH_MEMBERS_FAILED"/>
     <xsd:enumeration value="FIELD_CUSTOM_VALIDATION_EXCEPTION"/>
     <xsd:enumeration value="FIELD_FILTER_VALIDATION_EXCEPTION"/>
     <xsd:enumeration value="FIELD_INTEGRITY_EXCEPTION"/>
     <xsd:enumeration value="FIELD_KEYWORD_LIST_MATCH_LIMIT"/>
     <xsd:enumeration value="FIELD_MAPPING_ERROR"/>
     <xsd:enumeration value="FIELD_MODERATION_RULE_BLOCK"/>
     <xsd:enumeration value="FIELD_NOT_UPDATABLE"/>
     <xsd:enumeration value="FILE_EXTENSION_NOT_ALLOWED"/>
     <xsd:enumeration value="FILE_SIZE_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="FILTERED_LOOKUP_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="FIND_DUPLICATES_ERROR"/>
     <xsd:enumeration value="FLOW_EXCEPTION"/>
     <xsd:enumeration value="FUNCTIONALITY_NOT_ENABLED"/>
     <xsd:enumeration value="HAS_PUBLIC_REFERENCES"/>
     <xsd:enumeration value="HTML_FILE_UPLOAD_NOT_ALLOWED"/>
     <xsd:enumeration value="IAS_AM_AUTH_BAD_REQUEST"/>
     <xsd:enumeration value="IAS_AM_AUTH_UNAUTHORIZED"/>
     <xsd:enumeration value="IAS_INVALID_AUTH"/>
     <xsd:enumeration value="IAS_INVALID_REQUEST_PARAMETER"/>
     <xsd:enumeration value="IAS_RECORD_DOES_NOT_EXIST"/>
     <xsd:enumeration value="IAS_TENANT_NOT_PROVISIONED"/>
     <xsd:enumeration value="IMAGE_TOO_LARGE"/>
     <xsd:enumeration value="INACTIVE_OWNER_OR_USER"/>
     <xsd:enumeration value="INACTIVE_RULE_ERROR"/>
     <xsd:enumeration value="INSERT_UPDATE_DELETE_NOT_ALLOWED_DURING_MAINTENANCE"/>
     <xsd:enumeration value="INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY"/>
     <xsd:enumeration value="INSUFFICIENT_ACCESS_OR_READONLY"/>
     <xsd:enumeration value="INSUFFICIENT_ACCESS_TO_INSIGHTSEXTERNALDATA"/>
     <xsd:enumeration value="INSUFFICIENT_BALANCE"/>
     <xsd:enumeration value="INSUFFICIENT_CREDITS"/>
     <xsd:enumeration value="INTEGRATION_CANCELLED"/>
     <xsd:enumeration value="INTERNAL_ERROR"/>
     <xsd:enumeration value="INVALID_ACCESS_LEVEL"/>
     <xsd:enumeration value="INVALID_ACCESS_TOKEN"/>
     <xsd:enumeration value="INVALID_API_INPUT"/>
     <xsd:enumeration value="INVALID_ARGUMENTS"/>
     <xsd:enumeration value="INVALID_ARGUMENT_TYPE"/>
     <xsd:enumeration value="INVALID_ARG_NAME"/>
     <xsd:enumeration value="INVALID_ARRAY_ARG"/>
     <xsd:enumeration value="INVALID_ASSIGNEE_TYPE"/>
     <xsd:enumeration value="INVALID_ASSIGNMENT_RULE"/>
     <xsd:enumeration value="INVALID_AUTH"/>
     <xsd:enumeration value="INVALID_AUTH_HEADER"/>
     <xsd:enumeration value="INVALID_BATCH_OPERATION"/>
     <xsd:enumeration value="INVALID_CHARSET"/>
     <xsd:enumeration value="INVALID_CONTENT_TYPE"/>
     <xsd:enumeration value="INVALID_CREDIT_CARD_INFO"/>
     <xsd:enumeration value="INVALID_CROSS_REFERENCE_KEY"/>
     <xsd:enumeration value="INVALID_CROSS_REFERENCE_TYPE_FOR_FIELD"/>
     <xsd:enumeration value="INVALID_CURRENCY_CONV_RATE"/>
     <xsd:enumeration value="INVALID_CURRENCY_CORP_RATE"/>
     <xsd:enumeration value="INVALID_CURRENCY_ISO"/>
     <xsd:enumeration value="INVALID_CURSOR"/>
     <xsd:enumeration value="INVALID_DATASET_REFERENCE_INPUT"/>
     <xsd:enumeration value="INVALID_DATA_CATEGORY_GROUP_REFERENCE"/>
     <xsd:enumeration value="INVALID_DATA_URI"/>
     <xsd:enumeration value="INVALID_EMAIL"/>
     <xsd:enumeration value="INVALID_EMAIL_ADDRESS"/>
     <xsd:enumeration value="INVALID_EMPTY_KEY_OWNER"/>
     <xsd:enumeration value="INVALID_ENTITY_FOR_MATCH_ENGINE_ERROR"/>
     <xsd:enumeration value="INVALID_ENTITY_FOR_MATCH_OPERATION_ERROR"/>
     <xsd:enumeration value="INVALID_ENTITY_FOR_UPSERT"/>
     <xsd:enumeration value="INVALID_ENVIRONMENT_HUB_MEMBER"/>
     <xsd:enumeration value="INVALID_EVENT_DELIVERY"/>
     <xsd:enumeration value="INVALID_EVENT_INPUT"/>
     <xsd:enumeration value="INVALID_EVENT_SUBSCRIPTION"/>
     <xsd:enumeration value="INVALID_EXTENSION_ID"/>
     <xsd:enumeration value="INVALID_FIELD"/>
     <xsd:enumeration value="INVALID_FIELD_FOR_INSERT_UPDATE"/>
     <xsd:enumeration value="INVALID_FIELD_WHEN_USING_TEMPLATE"/>
     <xsd:enumeration value="INVALID_FILTER_ACTION"/>
     <xsd:enumeration value="INVALID_FORM_DATA"/>
     <xsd:enumeration value="INVALID_GOOGLE_DOCS_URL"/>
     <xsd:enumeration value="INVALID_ID_FIELD"/>
     <xsd:enumeration value="INVALID_INET_ADDRESS"/>
     <xsd:enumeration value="INVALID_INPUT"/>
     <xsd:enumeration value="INVALID_INPUT_FORMAT"/>
     <xsd:enumeration value="INVALID_KEY_FIELD_INPUT"/>
     <xsd:enumeration value="INVALID_LIMIT"/>
     <xsd:enumeration value="INVALID_LINEITEM_CLONE_STATE"/>
     <xsd:enumeration value="INVALID_MARKUP"/>
     <xsd:enumeration value="INVALID_MASTER_OR_TRANSLATED_SOLUTION"/>
     <xsd:enumeration value="INVALID_MESSAGE_ID_REFERENCE"/>
     <xsd:enumeration value="INVALID_NAME"/>
     <xsd:enumeration value="INVALID_NAMESPACE_PREFIX"/>
     <xsd:enumeration value="INVALID_OAUTH_URL"/>
     <xsd:enumeration value="INVALID_OPERATION"/>
     <xsd:enumeration value="INVALID_OPERATOR"/>
     <xsd:enumeration value="INVALID_OR_NULL_FOR_RESTRICTED_PICKLIST"/>
     <xsd:enumeration value="INVALID_OWNER"/>
     <xsd:enumeration value="INVALID_PACKAGE_LICENSE"/>
     <xsd:enumeration value="INVALID_PACKAGE_VERSION"/>
     <xsd:enumeration value="INVALID_PARTNER_NETWORK_STATUS"/>
     <xsd:enumeration value="INVALID_PAYLOAD_VERSION"/>
     <xsd:enumeration value="INVALID_PERSON_ACCOUNT_OPERATION"/>
     <xsd:enumeration value="INVALID_POST_TYPE"/>
     <xsd:enumeration value="INVALID_PROVIDER_TYPE"/>
     <xsd:enumeration value="INVALID_QUERY_KEY"/>
     <xsd:enumeration value="INVALID_QUERY_LOCATOR"/>
     <xsd:enumeration value="INVALID_QUERY_VALUE"/>
     <xsd:enumeration value="INVALID_READ_ONLY_USER_DML"/>
     <xsd:enumeration value="INVALID_REFRESH_TOKEN"/>
     <xsd:enumeration value="INVALID_REQUEST_STATE"/>
     <xsd:enumeration value="INVALID_RUNTIME_VALUE"/>
     <xsd:enumeration value="INVALID_SAVE_AS_ACTIVITY_FLAG"/>
     <xsd:enumeration value="INVALID_SCS_INBOUND_USER"/>
     <xsd:enumeration value="INVALID_SESSION_ID"/>
     <xsd:enumeration value="INVALID_SETUP_OWNER"/>
     <xsd:enumeration value="INVALID_SIGNUP_COUNTRY"/>
     <xsd:enumeration value="INVALID_SIGNUP_OPTION"/>
     <xsd:enumeration value="INVALID_SITE_DELETE_EXCEPTION"/>
     <xsd:enumeration value="INVALID_SITE_FILE_IMPORTED_EXCEPTION"/>
     <xsd:enumeration value="INVALID_SITE_FILE_TYPE_EXCEPTION"/>
     <xsd:enumeration value="INVALID_SOURCE_OBJECT_ID"/>
     <xsd:enumeration value="INVALID_STATUS"/>
     <xsd:enumeration value="INVALID_SUBDOMAIN"/>
     <xsd:enumeration value="INVALID_TEAM"/>
     <xsd:enumeration value="INVALID_TEXT_REPRESENTATION"/>
     <xsd:enumeration value="INVALID_TYPE"/>
     <xsd:enumeration value="INVALID_TYPE_FOR_OPERATION"/>
     <xsd:enumeration value="INVALID_TYPE_ON_FIELD_IN_RECORD"/>
     <xsd:enumeration value="INVALID_USERID"/>
     <xsd:enumeration value="IP_RANGE_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="IS_ARCHIVED"/>
     <xsd:enumeration value="IS_BOT"/>
     <xsd:enumeration value="ITEM_NOT_FOUND"/>
     <xsd:enumeration value="JIGSAW_IMPORT_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="LICENSE_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="LIGHT_PORTAL_USER_EXCEPTION"/>
     <xsd:enumeration value="LIMIT_EXCEEDED"/>
     <xsd:enumeration value="LIST_PRICE_NOT_FOUND"/>
     <xsd:enumeration value="MALFORMED_ID"/>
     <xsd:enumeration value="MANAGER_NOT_DEFINED"/>
     <xsd:enumeration value="MASSMAIL_RETRY_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="MASS_MAIL_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="MATCH_DEFINITION_ERROR"/>
     <xsd:enumeration value="MATCH_OPERATION_ERROR"/>
     <xsd:enumeration value="MATCH_OPERATION_INVALID_ENGINE_ERROR"/>
     <xsd:enumeration value="MATCH_OPERATION_INVALID_RULE_ERROR"/>
     <xsd:enumeration value="MATCH_OPERATION_MISSING_ENGINE_ERROR"/>
     <xsd:enumeration value="MATCH_OPERATION_MISSING_OBJECT_TYPE_ERROR"/>
     <xsd:enumeration value="MATCH_OPERATION_MISSING_OPTIONS_ERROR"/>
     <xsd:enumeration value="MATCH_OPERATION_MISSING_RULE_ERROR"/>
     <xsd:enumeration value="MATCH_OPERATION_UNKNOWN_RULE_ERROR"/>
     <xsd:enumeration value="MATCH_OPERATION_UNSUPPORTED_VERSION_ERROR"/>
     <xsd:enumeration value="MATCH_PRECONDITION_FAILED"/>
     <xsd:enumeration value="MATCH_RUNTIME_ERROR"/>
     <xsd:enumeration value="MATCH_SERVICE_ERROR"/>
     <xsd:enumeration value="MATCH_SERVICE_TIMED_OUT"/>
     <xsd:enumeration value="MATCH_SERVICE_UNAVAILABLE_ERROR"/>
     <xsd:enumeration value="MAXIMUM_CCEMAILS_EXCEEDED"/>
     <xsd:enumeration value="MAXIMUM_DASHBOARD_COMPONENTS_EXCEEDED"/>
     <xsd:enumeration value="MAXIMUM_HIERARCHY_CHILDREN_REACHED"/>
     <xsd:enumeration value="MAXIMUM_HIERARCHY_LEVELS_REACHED"/>
     <xsd:enumeration value="MAXIMUM_HIERARCHY_TREE_SIZE_REACHED"/>
     <xsd:enumeration value="MAXIMUM_SIZE_OF_ATTACHMENT"/>
     <xsd:enumeration value="MAXIMUM_SIZE_OF_DOCUMENT"/>
     <xsd:enumeration value="MAX_ACTIONS_PER_RULE_EXCEEDED"/>
     <xsd:enumeration value="MAX_ACTIVE_RULES_EXCEEDED"/>
     <xsd:enumeration value="MAX_APPROVAL_STEPS_EXCEEDED"/>
     <xsd:enumeration value="MAX_DEPTH_IN_FLOW_EXECUTION"/>
     <xsd:enumeration value="MAX_FORMULAS_PER_RULE_EXCEEDED"/>
     <xsd:enumeration value="MAX_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="MAX_RULES_EXCEEDED"/>
     <xsd:enumeration value="MAX_RULE_ENTRIES_EXCEEDED"/>
     <xsd:enumeration value="MAX_TASK_DESCRIPTION_EXCEEEDED"/>
     <xsd:enumeration value="MAX_TM_RULES_EXCEEDED"/>
     <xsd:enumeration value="MAX_TM_RULE_ITEMS_EXCEEDED"/>
     <xsd:enumeration value="MAX_TRIGGERS_EXCEEDED"/>
     <xsd:enumeration value="MERGE_FAILED"/>
     <xsd:enumeration value="METADATA_FIELD_UPDATE_ERROR"/>
     <xsd:enumeration value="METHOD_DEPRECATED"/>
     <xsd:enumeration value="METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE"/>
     <xsd:enumeration value="MISSING_ARGUMENT"/>
     <xsd:enumeration value="MISSING_POST_TYPE"/>
     <xsd:enumeration value="MISSING_RECORD"/>
     <xsd:enumeration value="MISSING_SCOPE"/>
     <xsd:enumeration value="MIXED_DML_OPERATION"/>
     <xsd:enumeration value="MSG_TOO_LONG"/>
     <xsd:enumeration value="MULTIPLE_VOUCHERS"/>
     <xsd:enumeration value="NAME_TAKEN"/>
     <xsd:enumeration value="NONUNIQUE_SHIPPING_ADDRESS"/>
     <xsd:enumeration value="NOT_ALLOWED_TOKEN_TYPE"/>
     <xsd:enumeration value="NOT_AUTHED"/>
     <xsd:enumeration value="NOT_IN_CHANNEL"/>
     <xsd:enumeration value="NO_ACCESS_TOKEN"/>
     <xsd:enumeration value="NO_ACCESS_TOKEN_FROM_REFRESH"/>
     <xsd:enumeration value="NO_APPLICABLE_PROCESS"/>
     <xsd:enumeration value="NO_ATTACHMENT_PERMISSION"/>
     <xsd:enumeration value="NO_AUTH_PROVIDER"/>
     <xsd:enumeration value="NO_INACTIVE_DIVISION_MEMBERS"/>
     <xsd:enumeration value="NO_LOCAL_USER_ON_TEAM"/>
     <xsd:enumeration value="NO_MASS_MAIL_PERMISSION"/>
     <xsd:enumeration value="NO_PARTNER_PERMISSION"/>
     <xsd:enumeration value="NO_PERMISSION"/>
     <xsd:enumeration value="NO_REFRESH_TOKEN"/>
     <xsd:enumeration value="NO_SUCH_USER_EXISTS"/>
     <xsd:enumeration value="NO_TEXT"/>
     <xsd:enumeration value="NO_TOKEN_ENDPOINT"/>
     <xsd:enumeration value="NUMBER_OUTSIDE_VALID_RANGE"/>
     <xsd:enumeration value="NUM_HISTORY_FIELDS_BY_SOBJECT_EXCEEDED"/>
     <xsd:enumeration value="OPERATION_ENQUEUED"/>
     <xsd:enumeration value="OPTED_OUT_OF_MASS_MAIL"/>
     <xsd:enumeration value="OP_WITH_INVALID_USER_TYPE_EXCEPTION"/>
     <xsd:enumeration value="ORCHESTRATION_INVALID"/>
     <xsd:enumeration value="ORDER_MANAGEMENT_ACTION_NOT_ALLOWED"/>
     <xsd:enumeration value="ORDER_MANAGEMENT_INVALID_RECORD"/>
     <xsd:enumeration value="ORDER_MANAGEMENT_RECORD_EXISTS"/>
     <xsd:enumeration value="ORDER_MANAGEMENT_RECORD_NOT_FOUND"/>
     <xsd:enumeration value="ORG_LOGIN_REQUIRED"/>
     <xsd:enumeration value="PACKAGE_DISABLED"/>
     <xsd:enumeration value="PACKAGE_LICENSE_REQUIRED"/>
     <xsd:enumeration value="PACKAGING_API_INSTALL_FAILED"/>
     <xsd:enumeration value="PACKAGING_API_UNINSTALL_FAILED"/>
     <xsd:enumeration value="PALI_INVALID_ACTION_ID"/>
     <xsd:enumeration value="PALI_INVALID_ACTION_NAME"/>
     <xsd:enumeration value="PALI_INVALID_ACTION_TYPE"/>
     <xsd:enumeration value="PAL_INVALID_ASSISTANT_RECOMMENDATION_TYPE_ID"/>
     <xsd:enumeration value="PAL_INVALID_ENTITY_ID"/>
     <xsd:enumeration value="PAL_INVALID_FLEXIPAGE_ID"/>
     <xsd:enumeration value="PAL_INVALID_LAYOUT_ID"/>
     <xsd:enumeration value="PAL_INVALID_PARAMETERS"/>
     <xsd:enumeration value="PARTICIPANT_RELATIONSHIP_EXISTS"/>
     <xsd:enumeration value="PAYLOAD_SIZE_EXCEEDED"/>
     <xsd:enumeration value="PA_API_EXCEPTION"/>
     <xsd:enumeration value="PA_AXIS_FAULT"/>
     <xsd:enumeration value="PA_INVALID_ID_EXCEPTION"/>
     <xsd:enumeration value="PA_NO_ACCESS_EXCEPTION"/>
     <xsd:enumeration value="PA_NO_DATA_FOUND_EXCEPTION"/>
     <xsd:enumeration value="PA_URI_SYNTAX_EXCEPTION"/>
     <xsd:enumeration value="PA_VISIBLE_ACTIONS_FILTER_ORDERING_EXCEPTION"/>
     <xsd:enumeration value="PICKLIST_INACTIVE_VALUES_EXCEEDED"/>
     <xsd:enumeration value="PLATFORM_EVENT_ENCRYPTION_ERROR"/>
     <xsd:enumeration value="PLATFORM_EVENT_PUBLISHING_UNAVAILABLE"/>
     <xsd:enumeration value="PLATFORM_EVENT_PUBLISH_FAILED"/>
     <xsd:enumeration value="PORTAL_NO_ACCESS"/>
     <xsd:enumeration value="PORTAL_USER_ALREADY_EXISTS_FOR_CONTACT"/>
     <xsd:enumeration value="PORTAL_USER_CREATION_RESTRICTED_WITH_ENCRYPTION"/>
     <xsd:enumeration value="PRICE_NOT_FOUND"/>
     <xsd:enumeration value="PRIVATE_CONTACT_ON_ASSET"/>
     <xsd:enumeration value="PROCESSING_HALTED"/>
     <xsd:enumeration value="QA_INVALID_CREATE_FEED_ITEM"/>
     <xsd:enumeration value="QA_INVALID_SUCCESS_MESSAGE"/>
     <xsd:enumeration value="QUERY_TIMEOUT"/>
     <xsd:enumeration value="QUICK_ACTION_LIST_ITEM_NOT_ALLOWED"/>
     <xsd:enumeration value="QUICK_ACTION_LIST_NOT_ALLOWED"/>
     <xsd:enumeration value="RATELIMITED"/>
     <xsd:enumeration value="RATE_LIMITED"/>
     <xsd:enumeration value="RECORD_CREATION_FAILED"/>
     <xsd:enumeration value="RECORD_IN_USE_BY_WORKFLOW"/>
     <xsd:enumeration value="RELATED_ENTITY_FILTER_VALIDATION_EXCEPTION"/>
     <xsd:enumeration value="REL_FIELD_BAD_ACCESSIBILITY"/>
     <xsd:enumeration value="REPUTATION_MINIMUM_NUMBER_NOT_REACHED"/>
     <xsd:enumeration value="REQUEST_RUNNING_TOO_LONG"/>
     <xsd:enumeration value="REQUEST_TIMEOUT"/>
     <xsd:enumeration value="REQUIRED_FEATURE_MISSING"/>
     <xsd:enumeration value="REQUIRED_FIELD_MISSING"/>
     <xsd:enumeration value="REQUIRE_CONNECTED_APP_SCS"/>
     <xsd:enumeration value="REQUIRE_CONNECTED_APP_SESSION_SCS"/>
     <xsd:enumeration value="REQUIRE_RUNAS_USER"/>
     <xsd:enumeration value="RESTRICTED_ACTION"/>
     <xsd:enumeration value="RESTRICTED_ACTION_NON_THREADABLE_CHANNEL"/>
     <xsd:enumeration value="RESTRICTED_ACTION_READ_ONLY_CHANNEL"/>
     <xsd:enumeration value="RESTRICTED_ACTION_THREAD_ONLY_CHANNEL"/>
     <xsd:enumeration value="RETRIEVE_EXCHANGE_ATTACHMENT_FAILED"/>
     <xsd:enumeration value="RETRIEVE_EXCHANGE_EMAIL_FAILED"/>
     <xsd:enumeration value="RETRIEVE_EXCHANGE_EVENT_FAILED"/>
     <xsd:enumeration value="RETRIEVE_GOOGLE_EMAIL_FAILED"/>
     <xsd:enumeration value="RETRIEVE_GOOGLE_EVENT_FAILED"/>
     <xsd:enumeration value="RETRIEVE_USER_CONFIG_ERROR"/>
     <xsd:enumeration value="SALESFORCE_INBOX_TRANSPORT_CONNECTION_ERROR"/>
     <xsd:enumeration value="SALESFORCE_INBOX_TRANSPORT_INVALID_INPUT_ERROR"/>
     <xsd:enumeration value="SALESFORCE_INBOX_TRANSPORT_TOKEN_ERROR"/>
     <xsd:enumeration value="SALESFORCE_INBOX_TRANSPORT_UNKNOWN_ERROR"/>
     <xsd:enumeration value="SELF_REFERENCE_FROM_FLOW"/>
     <xsd:enumeration value="SELF_REFERENCE_FROM_TRIGGER"/>
     <xsd:enumeration value="SERVICE_UNAVAILABLE"/>
     <xsd:enumeration value="SESSION_EXPIRED"/>
     <xsd:enumeration value="SESSION_INVALIDATED"/>
     <xsd:enumeration value="SHARE_NEEDED_FOR_CHILD_OWNER"/>
     <xsd:enumeration value="SINGLE_EMAIL_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="SLACK_CONNECT_FILE_LINK_SHARING_BLOCKED"/>
     <xsd:enumeration value="SLACK_INTERNAL_ERROR"/>
     <xsd:enumeration value="SOCIAL_ACCOUNT_NOT_FOUND"/>
     <xsd:enumeration value="SOCIAL_ACTION_INVALID"/>
     <xsd:enumeration value="SOCIAL_PERSONA_NOT_FOUND"/>
     <xsd:enumeration value="SOCIAL_POST_INVALID"/>
     <xsd:enumeration value="SOCIAL_POST_NOT_FOUND"/>
     <xsd:enumeration value="SPECIFICATION_GENERATION_EXCEPTION"/>
     <xsd:enumeration value="STANDARD_PRICE_NOT_DEFINED"/>
     <xsd:enumeration value="STORAGE_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="STRING_TOO_LONG"/>
     <xsd:enumeration value="SUBDOMAIN_IN_USE"/>
     <xsd:enumeration value="TABSET_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="TEAM_ACCESS_NOT_GRANTED"/>
     <xsd:enumeration value="TEAM_ADDED_TO_ORG"/>
     <xsd:enumeration value="TEAM_ID_OR_ORG_REQUIRED"/>
     <xsd:enumeration value="TEAM_NOT_FOUND"/>
     <xsd:enumeration value="TEMPLATE_NOT_ACTIVE"/>
     <xsd:enumeration value="TEMPLATE_NOT_FOUND"/>
     <xsd:enumeration value="TERMS_OF_SERVICE_UNREAD"/>
     <xsd:enumeration value="TERRITORY_REALIGN_IN_PROGRESS"/>
     <xsd:enumeration value="TEXT_DATA_OUTSIDE_SUPPORTED_CHARSET"/>
     <xsd:enumeration value="TEXT_TO_PICKLIST_VALUES_EXCEEDED"/>
     <xsd:enumeration value="TOKEN_REVOKED"/>
     <xsd:enumeration value="TOO_MANY_APEX_REQUESTS"/>
     <xsd:enumeration value="TOO_MANY_ATTACHMENTS"/>
     <xsd:enumeration value="TOO_MANY_ENUM_VALUE"/>
     <xsd:enumeration value="TOO_MANY_JOBS"/>
     <xsd:enumeration value="TOO_MANY_POSSIBLE_USERS_EXIST"/>
     <xsd:enumeration value="TRANSFER_REQUIRES_READ"/>
     <xsd:enumeration value="TWO_FACTOR_SETUP_REQUIRED"/>
     <xsd:enumeration value="UISF_ENTITY_QUERY_FAILED"/>
     <xsd:enumeration value="UISF_NO_MAPPINGS_FOUND"/>
     <xsd:enumeration value="UISF_TOKEN_NOT_FOUND"/>
     <xsd:enumeration value="UISF_UNKNOWN_EXCEPTION"/>
     <xsd:enumeration value="UISF_USER_MAPPING_FAILED"/>
     <xsd:enumeration value="UNABLE_TO_LOCK_ROW"/>
     <xsd:enumeration value="UNAVAILABLE_RECORDTYPE_EXCEPTION"/>
     <xsd:enumeration value="UNAVAILABLE_REF"/>
     <xsd:enumeration value="UNDEFINED_MAPPING_DEFINITION"/>
     <xsd:enumeration value="UNDELETE_FAILED"/>
     <xsd:enumeration value="UNKNOWN_EXCEPTION"/>
     <xsd:enumeration value="UNKNOWN_TOKEN_ERROR"/>
     <xsd:enumeration value="UNSAFE_HTML_CONTENT"/>
     <xsd:enumeration value="UNSPECIFIED_EMAIL_ADDRESS"/>
     <xsd:enumeration value="UNSUPPORTED_APEX_TRIGGER_OPERATON"/>
     <xsd:enumeration value="UNSUPPORTED_SITE"/>
     <xsd:enumeration value="UNSUPPORTED_SITE_FILE_IMPORTED_EXCEPTION"/>
     <xsd:enumeration value="UNSUPPORTED_SOCIAL_PROVIDER"/>
     <xsd:enumeration value="UNVERIFIED_SENDER_ADDRESS"/>
     <xsd:enumeration value="UPDATE_GOOGLE_EMAIL_LABEL_FAILED"/>
     <xsd:enumeration value="USER_DISABLED"/>
     <xsd:enumeration value="USER_IS_ULTRA_RESTRICTED"/>
     <xsd:enumeration value="USER_MUST_BE_ADMIN"/>
     <xsd:enumeration value="USER_OWNS_PORTAL_ACCOUNT_EXCEPTION"/>
     <xsd:enumeration value="USER_WITH_APEX_SHARES_EXCEPTION"/>
     <xsd:enumeration value="VF_COMPILE_ERROR"/>
     <xsd:enumeration value="WEBLINK_SIZE_LIMIT_EXCEEDED"/>
     <xsd:enumeration value="WEBLINK_URL_INVALID"/>
     <xsd:enumeration value="WORKSPACE_NOT_FOUND"/>
     <xsd:enumeration value="WRONG_CONTROLLER_TYPE"/>
     <xsd:enumeration value="XCLEAN_DJ_MATCH_IGNORABLE_ERROR"/>
     <xsd:enumeration value="XCLEAN_DJ_MATCH_INTERNAL_DJ_ERROR"/>
     <xsd:enumeration value="XCLEAN_DJ_MATCH_NON_RETRIABLE_ERROR"/>
     <xsd:enumeration value="XCLEAN_DJ_MATCH_RETRIABLE_ERROR"/>
     <xsd:enumeration value="XCLEAN_DJ_MATCH_UNKNOWN_ERROR"/>
     <xsd:enumeration value="XCLEAN_UNEXPECTED_ERROR"/>
    </xsd:restriction>
   </xsd:simpleType>
   <xsd:element name="cancelDeploy">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="String" type="tns:ID"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="cancelDeployResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" type="tns:CancelDeployResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="checkDeployStatus">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="asyncProcessId" type="tns:ID"/>
      <xsd:element name="includeDetails" type="xsd:boolean"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="checkDeployStatusResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" type="tns:DeployResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="checkRetrieveStatus">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="asyncProcessId" type="tns:ID"/>
      <xsd:element name="includeZip" type="xsd:boolean"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="checkRetrieveStatusResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" type="tns:RetrieveResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="createMetadata">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="metadata" minOccurs="0" maxOccurs="unbounded" type="tns:Metadata"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="createMetadataResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" minOccurs="0" maxOccurs="unbounded" type="tns:SaveResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="deleteMetadata">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="type" type="xsd:string"/>
      <xsd:element name="fullNames" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="deleteMetadataResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" minOccurs="0" maxOccurs="unbounded" type="tns:DeleteResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="deploy">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="ZipFile" type="xsd:base64Binary"/>
      <xsd:element name="DeployOptions" type="tns:DeployOptions"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="deployResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" type="tns:AsyncResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="deployRecentValidation">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="validationId" type="tns:ID"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="deployRecentValidationResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" type="xsd:string"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="describeMetadata">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="asOfVersion" type="xsd:double"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="describeMetadataResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" type="tns:DescribeMetadataResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="describeValueType">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="type" type="xsd:string"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="describeValueTypeResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" type="tns:DescribeValueTypeResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="listMetadata">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="queries" minOccurs="0" maxOccurs="unbounded" type="tns:ListMetadataQuery"/>
      <xsd:element name="asOfVersion" type="xsd:double"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="listMetadataResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" minOccurs="0" maxOccurs="unbounded" type="tns:FileProperties"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="readMetadata">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="type" type="xsd:string"/>
      <xsd:element name="fullNames" minOccurs="0" maxOccurs="unbounded" type="xsd:string"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="readMetadataResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" type="tns:ReadResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="renameMetadata">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="type" type="xsd:string"/>
      <xsd:element name="oldFullName" type="xsd:string"/>
      <xsd:element name="newFullName" type="xsd:string"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="renameMetadataResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" type="tns:SaveResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="retrieve">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="retrieveRequest" type="tns:RetrieveRequest"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="retrieveResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" type="tns:AsyncResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="updateMetadata">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="metadata" minOccurs="0" maxOccurs="unbounded" type="tns:Metadata"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="updateMetadataResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" minOccurs="0" maxOccurs="unbounded" type="tns:SaveResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="upsertMetadata">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="metadata" minOccurs="0" maxOccurs="unbounded" type="tns:Metadata"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
   <xsd:element name="upsertMetadataResponse">
    <xsd:complexType>
     <xsd:sequence>
      <xsd:element name="result" minOccurs="0" maxOccurs="unbounded" type="tns:UpsertResult"/>
     </xsd:sequence>
    </xsd:complexType>
   </xsd:element>
  </xsd:schema>
 </types>
 <!-- Message for the header parts -->
 <message name="Header">
  <part name="AllOrNoneHeader" element="tns:AllOrNoneHeader"/>
  <part name="CallOptions" element="tns:CallOptions"/>
  <part name="DebuggingHeader" element="tns:DebuggingHeader"/>
  <part name="DebuggingInfo" element="tns:DebuggingInfo"/>
  <part name="SessionHeader" element="tns:SessionHeader"/>
 </message>
 <!-- Operation Messages -->
 <message name="cancelDeployRequest">
  <part element="tns:cancelDeploy" name="parameters"/>
 </message>
 <message name="cancelDeployResponse">
  <part element="tns:cancelDeployResponse" name="parameters"/>
 </message>
 <message name="checkDeployStatusRequest">
  <part element="tns:checkDeployStatus" name="parameters"/>
 </message>
 <message name="checkDeployStatusResponse">
  <part element="tns:checkDeployStatusResponse" name="parameters"/>
 </message>
 <message name="checkRetrieveStatusRequest">
  <part element="tns:checkRetrieveStatus" name="parameters"/>
 </message>
 <message name="checkRetrieveStatusResponse">
  <part element="tns:checkRetrieveStatusResponse" name="parameters"/>
 </message>
 <message name="createMetadataRequest">
  <part element="tns:createMetadata" name="parameters"/>
 </message>
 <message name="createMetadataResponse">
  <part element="tns:createMetadataResponse" name="parameters"/>
 </message>
 <message name="deleteMetadataRequest">
  <part element="tns:deleteMetadata" name="parameters"/>
 </message>
 <message name="deleteMetadataResponse">
  <part element="tns:deleteMetadataResponse" name="parameters"/>
 </message>
 <message name="deployRequest">
  <part element="tns:deploy" name="parameters"/>
 </message>
 <message name="deployResponse">
  <part element="tns:deployResponse" name="parameters"/>
 </message>
 <message name="deployRecentValidationRequest">
  <part element="tns:deployRecentValidation" name="parameters"/>
 </message>
 <message name="deployRecentValidationResponse">
  <part element="tns:deployRecentValidationResponse" name="parameters"/>
 </message>
 <message name="describeMetadataRequest">
  <part element="tns:describeMetadata" name="parameters"/>
 </message>
 <message name="describeMetadataResponse">
  <part element="tns:describeMetadataResponse" name="parameters"/>
 </message>
 <message name="describeValueTypeRequest">
  <part element="tns:describeValueType" name="parameters"/>
 </message>
 <message name="describeValueTypeResponse">
  <part element="tns:describeValueTypeResponse" name="parameters"/>
 </message>
 <message name="listMetadataRequest">
  <part element="tns:listMetadata" name="parameters"/>
 </message>
 <message name="listMetadataResponse">
  <part element="tns:listMetadataResponse" name="parameters"/>
 </message>
 <message name="readMetadataRequest">
  <part element="tns:readMetadata" name="parameters"/>
 </message>
 <message name="readMetadataResponse">
  <part element="tns:readMetadataResponse" name="parameters"/>
 </message>
 <message name="renameMetadataRequest">
  <part element="tns:renameMetadata" name="parameters"/>
 </message>
 <message name="renameMetadataResponse">
  <part element="tns:renameMetadataResponse" name="parameters"/>
 </message>
 <message name="retrieveRequest">
  <part element="tns:retrieve" name="parameters"/>
 </message>
 <message name="retrieveResponse">
  <part element="tns:retrieveResponse" name="parameters"/>
 </message>
 <message name="updateMetadataRequest">
  <part element="tns:updateMetadata" name="parameters"/>
 </message>
 <message name="updateMetadataResponse">
  <part element="tns:updateMetadataResponse" name="parameters"/>
 </message>
 <message name="upsertMetadataRequest">
  <part element="tns:upsertMetadata" name="parameters"/>
 </message>
 <message name="upsertMetadataResponse">
  <part element="tns:upsertMetadataResponse" name="parameters"/>
 </message>
 <portType name="MetadataPortType">
  <operation name="cancelDeploy">
   <documentation>Cancels a metadata deploy.</documentation>
   <input message="tns:cancelDeployRequest"/>
   <output message="tns:cancelDeployResponse"/>
  </operation>
  <operation name="checkDeployStatus">
   <documentation>Check the current status of an asyncronous deploy call.</documentation>
   <input message="tns:checkDeployStatusRequest"/>
   <output message="tns:checkDeployStatusResponse"/>
  </operation>
  <operation name="checkRetrieveStatus">
   <documentation>Check the current status of an asyncronous deploy call.</documentation>
   <input message="tns:checkRetrieveStatusRequest"/>
   <output message="tns:checkRetrieveStatusResponse"/>
  </operation>
  <operation name="createMetadata">
   <documentation>Creates metadata entries synchronously.</documentation>
   <input message="tns:createMetadataRequest"/>
   <output message="tns:createMetadataResponse"/>
  </operation>
  <operation name="deleteMetadata">
   <documentation>Deletes metadata entries synchronously.</documentation>
   <input message="tns:deleteMetadataRequest"/>
   <output message="tns:deleteMetadataResponse"/>
  </operation>
  <operation name="deploy">
   <documentation>Deploys a zipfile full of metadata entries asynchronously.</documentation>
   <input message="tns:deployRequest"/>
   <output message="tns:deployResponse"/>
  </operation>
  <operation name="deployRecentValidation">
   <documentation>Deploys a previously validated payload without running tests.</documentation>
   <input message="tns:deployRecentValidationRequest"/>
   <output message="tns:deployRecentValidationResponse"/>
  </operation>
  <operation name="describeMetadata">
   <documentation>Describes features of the metadata API.</documentation>
   <input message="tns:describeMetadataRequest"/>
   <output message="tns:describeMetadataResponse"/>
  </operation>
  <operation name="describeValueType">
   <documentation>Describe a complex value type</documentation>
   <input message="tns:describeValueTypeRequest"/>
   <output message="tns:describeValueTypeResponse"/>
  </operation>
  <operation name="listMetadata">
   <documentation>Lists the available metadata components.</documentation>
   <input message="tns:listMetadataRequest"/>
   <output message="tns:listMetadataResponse"/>
  </operation>
  <operation name="readMetadata">
   <documentation>Reads metadata entries synchronously.</documentation>
   <input message="tns:readMetadataRequest"/>
   <output message="tns:readMetadataResponse"/>
  </operation>
  <operation name="renameMetadata">
   <documentation>Renames a metadata entry synchronously.</documentation>
   <input message="tns:renameMetadataRequest"/>
   <output message="tns:renameMetadataResponse"/>
  </operation>
  <operation name="retrieve">
   <documentation>Retrieves a set of individually specified metadata entries.</documentation>
   <input message="tns:retrieveRequest"/>
   <output message="tns:retrieveResponse"/>
  </operation>
  <operation name="updateMetadata">
   <documentation>Updates metadata entries synchronously.</documentation>
   <input message="tns:updateMetadataRequest"/>
   <output message="tns:updateMetadataResponse"/>
  </operation>
  <operation name="upsertMetadata">
   <documentation>Upserts metadata entries synchronously.</documentation>
   <input message="tns:upsertMetadataRequest"/>
   <output message="tns:upsertMetadataResponse"/>
  </operation>
 </portType>
 <binding name="MetadataBinding" type="tns:MetadataPortType">
  <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
  <operation name="cancelDeploy">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="checkDeployStatus">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:header use="literal" part="DebuggingInfo" message="tns:Header"/>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="checkRetrieveStatus">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="createMetadata">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:header use="literal" part="AllOrNoneHeader" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="deleteMetadata">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:header use="literal" part="AllOrNoneHeader" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="deploy">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="DebuggingHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="deployRecentValidation">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="DebuggingHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="describeMetadata">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="describeValueType">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="listMetadata">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="readMetadata">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="renameMetadata">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="retrieve">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="updateMetadata">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:header use="literal" part="AllOrNoneHeader" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
  <operation name="upsertMetadata">
   <soap:operation soapAction=""/>
   <input>
    <soap:header use="literal" part="SessionHeader" message="tns:Header"/>
    <soap:header use="literal" part="CallOptions" message="tns:Header"/>
    <soap:header use="literal" part="AllOrNoneHeader" message="tns:Header"/>
    <soap:body use="literal" parts="parameters"/>
   </input>
   <output>
    <soap:body use="literal"/>
   </output>
  </operation>
 </binding>
 <service name="MetadataService">
  <documentation>Manage your Salesforce.com metadata</documentation>
  <port binding="tns:MetadataBinding" name="Metadata">
   <soap:address location="https://test.salesforce.com/services/Soap/m/52.0"/>
  </port>
 </service>
</definitions>