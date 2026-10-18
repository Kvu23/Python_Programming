Specification of Communication AUTOSAR CP Release 4.4.0 



|**Document Title**|Specification of<br>Communication|
|---|---|
|**Document Owner **|AUTOSAR|
|**Document Responsibility**|AUTOSAR|
|**Document Identification No**|015|
|**Document Status**|Final|
|**Part of AUTOSARStandard**<br>**Part of Standard Release**|ClassicPlatform<br>4.4.0|



||**Do**<br>|**cument C**<br>|**hange History**<br>|
|---|---|---|---|
|**Date**|**Release**|**Changed by**|**Change Description**|
|2018-10-31|4.4.0|AUTOSAR<br>Release<br>Management|minor corrections / clarifications /<br>editorial changes; For details please<br>refer to the ChangeDocumentation|
|2017-12-08|4.3.1|AUTOSAR<br>Release<br>Management|reverted I-PDU group control APIs<br>to AUTOSAR Release 3 style<br>minor corrections / clarifications /<br>editorial changes; For details please<br>refer to the ChangeDocumentation|
|2016-11-30|4.3.0|AUTOSAR<br>Release<br>Management|updated TX-confirmation handling<br>revised Signal Based Gateway<br>Com-Stack API harmonization<br>minor corrections / clarifications /<br>editorial changes; For details please<br>refer to the ChangeDocumentation|
|2015-07-31|4.2.2|AUTOSAR<br>Release<br>Management|minor corrections / clarifications /<br>editorial changes; For details please<br>refer to the ChangeDocumentation|
|2014-10-31|4.2.1|AUTOSAR<br>Release<br>Management|added support for Sender/ Receiver<br>Serialization<br>updated to support CAN FD<br>minor corrections|
|2014-03-31|4.1.3|AUTOSAR<br>Release<br>Management|Several correction, clarifications and<br>editioral changes<br>No major functional changes or im-<br>provements|



Document ID 015: AUTOSAR_SWS_COM 

1 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||**Do**<br>|**cument C**<br>|**hange History**<br>|
|---|---|---|---|
|**Date**|**Release**|**Changed by**|**Change Description**|
|2013-10-31|4.1.2|AUTOSAR<br>Release<br>Management|Removed TP-restriction for dynamic<br>length I-PDUs<br>Added parameter to globally enable<br>or disable the cancellation support<br>Many bug fixes, clarifications and<br>harmonization with the other COM-<br>Stack modules<br>Editorial changes<br>Removed chapter(s) on change<br>documentation|
|2013-03-15|4.1.1|AUTOSAR<br>Administration|Reworked according to the new<br>SWS BSW General<br>added support for postbuild<br>loadable configuration<br>harmonization of COM-Stack APIs<br>(TP-APIs & callouts)<br>manycorrections and clarifications|
|2011-12-22|4.0.3|AUTOSAR<br>Administration|Several minor changes and bug-<br>fixes<br>Clarification and minor extensions<br>of transmission mode usage and<br>activation<br>Clarification and extension of trans-<br>fer properties<br>Added retry mechanism for failed<br>transmission requests|
|2010-09-30|3.1.5|AUTOSAR<br>Administration|corrections / clarifications / editorial<br>changes; For details please refer to<br>the ChangeDocumentation|
|2010-02-02|3.1.4|AUTOSAR<br>Administration|Added support for large data types<br>Added support for communication<br>protection<br>Revised mode management inter-<br>face<br>Many clarifications and correc-<br>tions based on SWS improvement,<br>validation and conformance test ac-<br>tivities<br>Legal disclaimer revised|



Document ID 015: AUTOSAR_SWS_COM 

2 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||**Do**|**cument C**|**hange History**|
|---|---|---|---|
|**Date**|**Release**|**Changed by**|**Change Description**|
|2008-08-13|3.1.1|AUTOSAR<br>Administration|Legal disclaimer revised|
|2008-02-01|3.0.2|AUTOSAR<br>Administration|Removed Figure 19, which was in-<br>cluded twice|
|2007-12-21|3.0.1|AUTOSAR<br>Administration|Removal of Internal Communication<br>feature<br>Revision of AUTOSAR COM MOD-<br>ULE configuration<br>Revision of Signal Gateway configu-<br>ration<br>Enhanced maximal<br>I-PDU length for FlexRay<br>Harmonization of callback-interface<br>to RTE<br>Clarifications and bug fixes<br>Document meta information ex-<br>tended<br>Small layout adaptations made|
|2007-01-24|2.1.15|AUTOSAR<br>Administration|Clarifications of requirements<br>throughout the whole document.<br>Chapter 11 contains a detailed list<br>of the made modifications. No new<br>major features were added since re-<br>lease 2.0.<br>“Advice for users” revised<br>“Revision Information” added<br>Legal disclaimer revised|
|2006-05-16|2.0|AUTOSAR<br>Administration|Document structure adapted to<br>common Release 2.0 SWS Tem-<br>plate.<br>Integration of signal gateway<br>Major updates in configuration, error<br>handling, filtering, transmission<br>mode switches, callouts, update-<br>bits, deadline monitoring and initial-<br>ization|
|2005-05-31|1.0|AUTOSAR<br>Administration|Initial release|



Document ID 015: AUTOSAR_SWS_COM 

3 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **Disclaimer** 

This work (specification and/or software implementation) and the material contained in it, as released by AUTOSAR, is for the purpose of information only. AUTOSAR and the companies that have contributed to it shall not be liable for any use of the work. 

The material contained in this work is protected by copyright and other types of intellectual property rights. The commercial exploitation of the material contained in this work requires a license to such intellectual property rights. 

This work may be utilized or reproduced without any modification, in any form or by any means, for informational purposes only. For any other purpose, no part of the work may be utilized or reproduced, in any form or by any means, without permission in writing from the publisher. 

The work has been developed for automotive applications only. It has neither been developed, nor tested for non-automotive applications. 

The word AUTOSAR and the AUTOSAR logo are registered trademarks. 

Document ID 015: AUTOSAR_SWS_COM 

4 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **Table of Contents** 

|1<br>Introduction and Functional Overview ................................................................. 9|
|---|
|2<br>Acronyms, Abbreviations and Definitions .......................................................... 10|
|2.1<br>Acronyms and Abbreviations ...................................................................... 10|
|2.2<br>Definitions ................................................................................................... 10|
|3<br>Related Documentation ..................................................................................... 12|
|3.1<br>Deliverables of AUTOSAR ......................................................................... 12|
|3.2<br>Related Standards and Norms ................................................................... 13|
|3.3<br>Related Specification .................................................................................. 13|
|4<br>Constraints and Assumptions ............................................................................ 14|
|4.1<br>Limitations .................................................................................................. 14|
|4.2<br>Applicability to Car Domains ....................................................................... 14|
|5<br>Dependencies to Other Modules ....................................................................... 15|
|5.1<br>PDU Router ................................................................................................ 15|
|5.2<br>Runtime Environment (RTE) ...................................................................... 16|
|6<br>Requirements Traceability ................................................................................. 17|
|7<br>Functional Specification..................................................................................... 27|
|7.1<br>Introduction ................................................................................................. 27|
|7.2<br>General Functionality .................................................................................. 27|
|7.2.1<br>AUTOSAR COM basis ........................................................................ 27|
|7.2.2<br>Signal Values ...................................................................................... 28<br>|
|7.2.3<br>Endianness Conversion and Sign Extension ...................................... 29|
|7.2.4<br>Filtering ............................................................................................... 31|
|7.2.5<br>Signal Gateway ................................................................................... 33|
|7.3<br>Normal Operation ....................................................................................... 34|
|7.3.1<br>Start-Up Behavior ................................................................................ 34|
|7.3.2<br>De-Initialization .................................................................................... 35|
|7.3.3<br>Communication Modes ....................................................................... 35|
|7.3.4<br>Signal Invalidation ............................................................................... 44|
|7.3.5<br>Handling of I-PDUs ............................................................................. 46|
|7.3.6<br>Deadline Monitoring ............................................................................ 52|
|7.3.7<br>Notification handling ............................................................................ 57|
|7.4<br>Signal Groups - Complex Data Types ........................................................ 58|
|7.4.1<br>Initialization ......................................................................................... 58|
|7.4.2<br>Transmission ....................................................................................... 58|
|7.4.3<br>Reception ............................................................................................ 59|
|7.4.4<br>Notifications......................................................................................... 59|
|7.4.5<br>Attributes of a Signal Group ................................................................ 60|
|7.4.6<br>UINT8-array based access to signal groups ....................................... 60|
|7.5<br>Large Data Types ....................................................................................... 62|
|7.5.1<br>Transmission of Large Signals/ I-PDUs .............................................. 63|
|7.5.2<br>Reception of Large Signals/ I-PDUs .................................................... 64|
|7.6<br>Dynamic Length Signals ............................................................................. 64|
|7.6.1<br>Transmission of Dynamic Length Signals/ I-PDUs .............................. 65|
|7.6.2<br>Reception of Dynamic Length Signals/ I-PDUs ................................... 66|



Document ID 015: AUTOSAR_SWS_COM 

5 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|7.7<br>Int|erface between AUTOSAR COM Module and the PDU Router ............. 66|
|---|---|
|7.8<br>Up|date-Bits ................................................................................................. 67|
|7.8.1|Sender Side ........................................................................................ 67|
|7.8.2|Receiver Side ...................................................................................... 68|
|7.9<br>Da|ta Sequence Control .............................................................................. 69|
|7.9.1|Sender Side ........................................................................................ 69|
|7.9.2|Receiver Side ...................................................................................... 69|
|7.10<br>Co|mmunication Protection ......................................................................... 70|
|7.10.1|Sender Side ........................................................................................ 71|
|7.10.2|Receiver Side ...................................................................................... 71|
|7.10.3|Constraints .......................................................................................... 71|
|7.11<br>Sig|nal Gateway .......................................................................................... 72|
|7.11.1|Dealing with Signals ............................................................................ 73|
|7.11.2|Dealing with Group Signals ................................................................. 73|
|7.11.3|Routing of Out-Timed Signals and Signal Groups ............................... 74|
|7.11.4|Handling of Update-Bits ...................................................................... 74|
|7.11.5|Decoupling Signal Gateway ................................................................ 75|
|7.12<br>Err|or Classification ..................................................................................... 75|
|7.12.1|Development Errors ............................................................................ 75|
|7.12.2|<br>Runtime Errors .................................................................................... 76|
|7.12.3|Transient Faults .................................................................................. 76|
|7.12.4|Production Errors ................................................................................ 76|
|7.12.5|Extended Production Errors ................................................................ 76|
|7.13<br>Err|or Notification ......................................................................................... 76|
|7.14<br>Err|or Handling ............................................................................................ 76|
|7.15<br>AU|TOSAR COM Module’s Interaction Model ............................................. 77|
|8<br>API Sp|ecification ............................................................................................... 81|
|8.1<br>Im|ported Types .......................................................................................... 81|
|8.2<br>Ty|e Definitions .......................................................................................... 81|
|<br>8.2.1|<br>Com_StatusType ................................................................................ 81|
|8.2.2|Com_SignalIdType .............................................................................. 81|
|8.2.3|Com_SignalGroupIdType .................................................................... 81|
|8.2.4|Com_IpduGroupIdType ....................................................................... 82|
|8.2.5|Com_ConfigType ................................................................................ 82|
|8.3<br>Fu|nction Definitions .................................................................................... 82|
|8.3.1|Return Codes ...................................................................................... 82|
|8.3.2|Start-Up and Control Services............................................................. 83|
|8.3.3|Communication Services .................................................................... 87|
|8.4<br>Cal|lback Functions and Notifications .......................................................... 96|
|8.4.1|Com_TriggerTransmit ......................................................................... 96|
|8.4.2|Com_RxIndication ............................................................................... 98|
|8.4.3|Com_TpRxIndication ........................................................................... 98|
|8.4.4|<br>ComTxConfirmation .......................................................................... 98|
|8.4.5|_<br>Com_TpTxConfirmation ...................................................................... 99|
|8.4.6|<br>Com_StartOfReception ....................................................................... 99|
|8.4.7|<br>Com_CopyRxData ............................................................................ 101|
|8.4.8|Com_CopyTxData ............................................................................. 101|
|8.5<br>Sc|heduled Functions ................................................................................ 103|
|8.5.1|Com_MainFunctionRx ....................................................................... 103|



Document ID 015: AUTOSAR_SWS_COM 

6 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|8.5.2|Com_MainFunctionTx ....................................................................... 103|
|---|---|
|8.5.3|Com_MainFunctionRouteSignals ...................................................... 104|
|8.6<br>Exp|<br>ected Interfaces .................................................................................. 104|
|8.6.1|Mandatory Interfaces ........................................................................ 104|
|8.6.2|Optional Interfaces ............................................................................ 104|
|8.6.3|Configurable Interfaces ..................................................................... 105|
|9<br>Sequenc|e Diagrams ........................................................................................ 111|
|9.1<br>Inte|rface between the AUTOSAR COM Module and the PDU Router...... 111|
|9.2<br>Con<br>Mod|firmation Handling between the PDU Router, the AUTOSAR COM<br>ule and the RTE ................................................................................. 113|
|9.3<br>Indi<br>Mod|cation Handling between the PDU Router, the AUTOSAR COM<br>ule and the RTE ................................................................................. 114|
|10 Configur|ation Specification .............................................................................. 115|
|10.1<br>Con|tainers and Configuration Parameters ............................................... 115|
|10.1.1|Configuration of the AUTOSAR COM Module................................... 116|
|10.1.2|<br>Com .................................................................................................. 117|
|10.1.3|ComGeneral ...................................................................................... 117|
|10.1.4|ComConfig ........................................................................................ 120|
|10.1.5|ComTimeBase .................................................................................. 121|
|10.1.6|ComFilter........................................................................................... 123|
|10.1.7|ComIPdu ........................................................................................... 126|
|10.1.8|ComIPduCounter .............................................................................. 131|
|10.1.9|ComIPduReplication ......................................................................... 132|
|10.1.10|ComTxIPdu .................................................................................... 133|
|10.1.11|ComIPduGroup .............................................................................. 135|
|10.1.12|ComSignal ..................................................................................... 136|
|10.1.13|ComSignalGroup ........................................................................... 147|
|10.1.14|ComGroupSignal ........................................................................... 154|
|10.1.15|ComTxMode .................................................................................. 160|
|10.1.16|ComTxModeTrue ........................................................................... 162|
|10.1.17|ComTxModeFalse ......................................................................... 162|
|10.1.18|ComGwMapping ............................................................................ 163|
|10.1.19|ComGwSource .............................................................................. 163|
|10.1.20|ComGwSourceDescription ............................................................ 164|
|10.1.21|ComGwDestination ........................................................................ 167|
|10.1.22|ComGwDestinationDescription ...................................................... 167|
|10.1.23|ComGwSignal ................................................................................ 170|
|10.2<br>Con|figuration Rules .................................................................................. 171|
|10.2.1|General Rules ................................................................................... 171|
|10.2.2|Signal Configuration .......................................................................... 172|
|10.2.3|<br>Signal Group Configuration ............................................................... 173|
|10.2.4|<br>Transmission Mode Configuration ..................................................... 173|
|10.2.5|Signal Gateway Configuration ........................................................... 173|
|10.2.6|<br>Filter Configuration ............................................................................ 174|
|10.2.7|<br>Post Build Configuration .................................................................... 174|
|10.2.8|<br>Dynamic Length I-PDUs .................................................................... 174|
|10.2.9|Replicated I-PDUs ............................................................................. 174|
|10.2.10|I-PDU group ................................................................................... 175|



Document ID 015: AUTOSAR_SWS_COM 

7 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



- 11 Not Applicable Requirements .......................................................................... 176 12 Appendix A ...................................................................................................... 177 

Document ID 015: AUTOSAR_SWS_COM 

8 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **1 Introduction and Functional Overview** 

This specification is the AUTOSAR COM module Software Specification. It is based on the AUTOSAR COM SRS [7]. It specifies how the requirements of the AUTOSAR COM SRS shall be realized. That means that the functionality and the API of the AUTOSAR COM module are described in this document. 

Within the AUTOSAR Layered Architecture the AUTOSAR COM module is placed between RTE and the PDU Router, see [1]. 

The AUTOSAR COM module is derived from [17]. For details, see Chapter 7.2.1. The AUTOSAR COM module provides signal gateway functionality. For details, see Chapter 7.2.5. 

Main Features: 

- Provision of signal oriented data interface for the RTE 

- Packing of AUTOSAR signals to I-PDUs to be transmitted 

- Unpacking of received I-PDUs and provision of received signals to RTE 

- Routing of signals from received I-PDUs into I-PDUs to become transmitted 

- Routing of signal groups from received I-PDUs into I-PDUs to become transmitted 

- Communication transmission control (start/ stop of I-PDU groups) 

- Replications of send requests 

- Guarantee of minimum distances between transmit I-PDUs 

- Monitoring of receive signals (signals timeout) 

- Filter mechanisms for incoming signals 

- Different notification mechanisms 

- Provision of init values and update indications 

- Byte order conversion 

- Sign extension 

- Support of two different transmission modes per I-PDU 

- Signal based gateway 

- Support of large and dynamic length data types 

- Support of I-PDU counters and I-PDU replication 

Document ID 015: AUTOSAR_SWS_COM 

9 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **2 Acronyms, Abbreviations and Definitions** 

## **2.1 Acronyms and Abbreviations** 

|**_Acronym:_**|**_Description:_**|
|---|---|
|AUTOSAR COM|The AUTOSAR COM module is derived from[17]. For details, see Chapter<br>7.2.1.|
|DM|DeadlineMonitoring,fordetails see Chapter 7.3.6|
|I-PDU|Interaction Layer Protocol Data Unit<br>An I-PDU carries signals. It is defined in[17].|
|L-PDU|Data Link Layer Protocol Data Unit. In AUTOSAR, the Data Link Layer is<br>equivalent to the Communication Hardware Abstraction and Microcontroller<br>Abstraction Layer.|
|MDT|A detailed description of the Minimum Delay Timer (MDT) can be found in<br>[17]. See also Chapter 7.3.5.5.|
|PDU Router|The PDU Router is a module transferring I-PDUs from one module to anoth-<br>er module. The PDU Router can be utilized for gateway operations and for<br>internal routing purposes.|
|SDU|Service Data Unit<br>For a description see[1]Chapter 4.|
|TM|Transmission Mode|
|TMC|Transmission Mode Condition, see Chapter 7.3.3.2|
|TMS|Transmission Mode Selector,see Chapter 7.3.3.2|



## **2.2 Definitions** 

|**_Term:_**|**_Description:_**|
|---|---|
|Confirmation|With a Confirmation, the PDU Router reports that a request by the AU-<br>TOSAR COM module has been completed successfully. It is a reaction to a<br>request ofCOM. E.g. whenaPDUhas beensuccessfully transmitted.|
|Data Invalid Value|Value sent by the AUTOSAR COM module to indicate that the sender side<br>AUTOSARSoftware Componentisnot able to provide avalidvalue.|
|Dynamic Length Sig-<br>nal|A dynamic length signal is a signal which length can vary at run-time.|
|Dynamic Length<br>I-PDU|A dynamic length I-PDU is an I-PDU containing a dynamic length signal. It<br>length varies depending onthelengthoftheincluded dynamiclengthsignal.|
|Group signal|Agroup signal is a signalthatis containedina signalgroup.|
|Indication|An Indication is asynchronous information from PDU Router to COM, e.g. to<br>acknowledge that somethinghas been received.|
|Init Value|I-PDUs and signals are set to the Init Value by the AUTOSAR COM module<br>afterstart-up. Thisvalueis used until itis overwritten.|
|I-PDU group|An I-PDU Group is an arbitrary collection of I-PDUs of the same direction<br>(i.e.send or receive)inthe COM module.|
|Inter-ECU –<br>communication|Communication between two or more ECUs for example via a CAN network|
|Intra-ECU –<br>communication|Communication between Software components that reside on the same ECU|
|Large Signal|A large signal is a signal that is too large to fit into a single L-PDU of the<br>underlying communicationprotocol.|
|Large I-PDU|Large I-PDUs are I-Signal-I-PDUs which do not fit into a single L-PDU of the<br>underlyingcommunicationprotocol. Large I-PDUs will be handled like other|



Document ID 015: AUTOSAR_SWS_COM 

10 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Term:_**|**_Description:_**<br>I-PDUs by COM, but are transmitted/received via the TP API.<br>Please note that large I-PDUs can also be handled in a more efficient way by<br>LargeDataCOM if they contain just one signal, or if the signals can be (de-<br>)serialized by the RTE. But if the signals have to be treated separately or<br>have to berouted, thelargeI-PDUshave to behandled by COM.|
|---|---|
|Message|[17]uses always the synonym_message_. In AUTOSAR,_message_is re-<br>placed by _signal_but with the same meaning.|
|Metadata|For some I-PDUs, e.g. J1939 I-PDUs, the payload is extended with addition-<br>al metadata containingforexample the CAN-ID.|
|Notification|Information by the AUTOSAR COM module to RTE, e.g. when new data is<br>available, anerroroccurred.|
|Signal|A signal in the AUTOSAR COM module’s context is equal to a message in<br>[17];see also[7].|
|Signal group|In AUTOSAR, so called complex data types are used. Inside a complex data<br>type, there are one or more data elements (primitive data types), like in a C<br>struct. The data consistency of such complex data types must be ensured.<br>The RTE decomposes the complex data type in single signals and sends<br>them to the AUTOSAR COM module. As these signals altogether need to be<br>treated consistently, they are called_signal group_.<br>See also[7].|
|Update-bit|A mechanism supported by the AUTOSAR COM module with that the re-<br>ceiver of a signal/ signal group could identify whether the sender has updat-<br>ed the data in this signal/ signalgroupbefore sending. See Chapter 7.8.|



Document ID 015: AUTOSAR_SWS_COM 

11 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **3 Related Documentation** 

## **3.1 Deliverables of AUTOSAR** 

- [1] AUTOSAR Layered Architecture AUTOSAR_EXP_LayeredSoftwareArchitecture.pdf 

- [2] Specification of Communication Stack Types AUTOSAR_SWS_CommunicationStackTypes.pdf 

- [3] General Requirements on Basic Software Modules AUTOSAR_SRS_BSWGeneral.pdf 

- [4] Basic Software UML Model AUTOSAR_MOD_BSWUMLModel.eap 

- [5] Specification of Standard Types AUTOSAR_SWS_StandardTypes.pdf 

- [6] Specification of the Virtual Functional Bus AUTOSAR_EXP_VFB.pdf 

- [7] Requirements on Communication AUTOSAR_SRS_COM.pdf 

- [8] Software Component Template AUTOSAR_TPS_SoftwareComponentTemplate.pdf 

- [9] Requirements on Gateway AUTOSAR_SRS_Gateway.pdf 

- [10] Specification of PDU Router AUTOSAR_SWS_PDURouter.pdf 

- [11] Specification of Operating System AUTOSAR_SWS_OS.pdf 

- [12] System Template AUTOSAR_TPS_SystemTemplate.pdf 

- [13] Specification of RTE Software AUTOSAR_SWS_RTE.pdf 

- [14] Specification of ECU Configuration AUTOSAR_TPS_ECUConfiguration.pdf 

Document ID 015: AUTOSAR_SWS_COM 

12 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



- [15] Specification of Communication Manager AUTOSAR_SWS_COMManager.pdf 

- [16] AUTOSAR Basic Software Module Description Template AUTOSAR_TPS_BSWModuleDescriptionTemplate.pdf 

- [19] Specification of CAN Transport Layer AUTOSAR_SWS_CANTransportLayer.pdf 

- [20] Specification of FlexRay Transport Layer AUTOSAR_SWS_FlexRayTransportLayer.pdf 

- [21] List of Basic Software Modules, AUTOSAR_TR_BSWModuleList.pdf 

- [22] Generic Structure Template 

   - AUTOSAR_TPS_GenericStructureTemplate.pdf 

- [23] General Specification of Basic Software Modules AUTOSAR_SWS_BSWGeneral.pdf 

## **3.2 Related Standards and Norms** 

- [17] ISO 17356-4:2005 Road vehicles -- Open interface for embedded automotive applications -- Part 4: OSEK/VDX Communication (COM) 

- [18] ISO 17356-6:2006 Road vehicles -- Open interface for embedded automotive applications -- Part 6: OSEK/VDX Implementation Language (OIL) 

## **3.3 Related Specification** 

AUTOSAR provides a General Specification on Basic Software modules [23] (SWS BSW General), which is also valid for COM. 

Thus, the specification SWS BSW General shall be considered as additional and required specification for COM. 

Document ID 015: AUTOSAR_SWS_COM 

13 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **4 Constraints and Assumptions** 

## **4.1 Limitations** 

The AUTOSAR COM module is based on [17]. Nevertheless not all features of [17] are included and some features are different. See SWS_Com_00013 for a list of not included features. 

## **4.2 Applicability to Car Domains** 

No restrictions. 

Document ID 015: AUTOSAR_SWS_COM 

14 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **5 Dependencies to Other Modules** 

This chapter lists all the features from other modules that are used by the AUTOSAR COM module and functionalities that are provided by the AUTOSAR COM module to other modules. For the placement of the AUTOSAR COM module in the communication stack, see **Figure 1** . 



<!-- Start of picture text -->
«module»<br>Rte<br>«use» «module»<br>ComM<br>«use»<br>Com Rte_Cbk<br>«realize» «use»<br>«module»<br>Com<br>«realize» «module»<br>Det_ReportError «optional» Com_Init BswM<br>«mandatory» «realize»<br>«realize» «optional»<br>PduR_Com Com_Cbk<br>«realize»<br>«use optionally»<br>«module» «module» «module»<br>Det PduR EcuM<br><!-- End of picture text -->

**Figure 1: AUTOSAR COM module’s context view** 

## **5.1 PDU Router** 

<mark>The AUTOSAR COM module uses the union of both sets of PDU Router’s upper layer module APIs. That is the APIs for upper layer modules that uses TP and the</mark> APIs for upper layer modules that do not use TP. This is necessary since the AUTOSAR COM module transports I-PDUs either unfragmented via simple L-PDUs or <mark>fragmented via TP.</mark> 

The following summarizes the functionality of the AUTOSAR COM module needs from the underlying layer PDU Router: 

Document ID 015: AUTOSAR_SWS_COM 

15 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



- <mark>Indication of incoming I-PDUs</mark> 

- <mark>Sending interface for outgoing I-PDUs including the confirmation if an I-PDU has been sent by the communication controller</mark> 

- <mark>Trigger interface to enable the PDU router to cause a transmission from the AUTOSAR COM module</mark> 

- <mark>Buffer handling for TP communication</mark> 

Chapter 7.5 and Chapter 9.1 include a detailed description of the interfaces to the PDU Router. For further information, see [10]. 

## **5.2 Runtime Environment (RTE)** 

The RTE uses the capabilities of the AUTOSAR COM module to send and receive signals. In AUTOSAR, the RTE is the higher layer above the AUTOSAR COM module. For further information, see [13]. 

Document ID 015: AUTOSAR_SWS_COM 

16 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **6 Requirements Traceability** 

The following table references the requirements specified in [3], [7], [17] and [9] and links to the fulfillment of these. Requirements that are not fulfilled by this document are linked to SWS_Com_00999. 

|**Requirement**|**Description**|**Satisfied by**|
|---|---|---|
|SRS_BSW_00003|All software modules shall<br>provide version and identifi-<br>cation information|SWS_Com_00426|
|SRS_BSW_00005|Modules of the µC Abstrac-<br>tion Layer (MCAL) may not<br>have hard coded horizontal<br>interfaces|SWS_Com_00999|
|SRS_BSW_00006|The source code of software<br>modules above the µC<br>Abstraction Layer (MCAL)<br>shall not be processor and<br>compiler dependent.|SWS_Com_00999|
|SRS_BSW_00009|All Basic SW Modules shall<br>be documented according to<br>a common standard.|SWS_Com_00999|
|SRS_BSW_00010|The memory consumption of<br>all Basic SW Modules shall<br>be documented for a defined<br>configuration for all sup-<br>ported platforms.|SWS_Com_00999|
|SRS_BSW_00101|The Basic Software Module<br>shall be able to initialize<br>variables and hardware in a<br>separate initialization func-<br>tion|SWS_Com_00015, SWS_Com_00059,<br>SWS_Com_00098, SWS_Com_00117,<br>SWS_Com_00128, SWS_Com_00217,<br>SWS_Com_00328, SWS_Com_00432,<br>SWS_Com_00484, SWS_Com_00850|
|SRS_BSW_00161|The AUTOSAR Basic Soft-<br>ware shall provide a<br>microcontroller abstraction<br>layer which provides a stan-<br>dardized interface to higher<br>software layers|SWS_Com_00999|
|SRS_BSW_00162|The AUTOSAR Basic Soft-<br>ware shall provide a hard-<br>ware abstraction layer|SWS_Com_00999|
|SRS_BSW_00164|The Implementation of inter-<br>rupt service routines shall be<br>done by the Operating Sys-<br>tem, complex drivers or<br>modules|SWS_Com_00999|
|SRS_BSW_00167|All AUTOSAR Basic Soft-<br>ware Modules shall provide<br>configuration rules and<br>constraints to enable plausi-<br>bility checks|SWS_Com_00497|



Document ID 015: AUTOSAR_SWS_COM 

17 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|SRS_BSW_00168|SW components shall be<br>tested by a function defined<br>in a common API in the<br>Basis-SW|SWS_Com_00999|
|---|---|---|
|SRS_BSW_00170|The AUTOSAR SW Compo-<br>nents shall provide informa-<br>tion about their dependency<br>from faults, signal qualities,<br>driver demands|SWS_Com_00999|
|SRS_BSW_00171|Optional functionality of a<br>Basic-SW component that is<br>not required in the ECU shall<br>be configurable at pre-<br>compile-time|SWS_Com_00999|
|SRS_BSW_00301|All AUTOSAR Basic Soft-<br>ware Modules shall only<br>import the necessary infor-<br>mation|SWS_Com_00609|
|SRS_BSW_00302|All AUTOSAR Basic Soft-<br>ware Modules shall only<br>export information needed<br>by other modules|SWS_Com_00999|
|SRS_BSW_00306|AUTOSAR Basic Software<br>Modules shall be compiler<br>and platform independent|SWS_Com_00999|
|SRS_BSW_00307|Global variables naming<br>convention|SWS_Com_00999|
|SRS_BSW_00308|AUTOSAR Basic Software<br>Modules shall not define<br>global data in their header<br>files, but in the C file|SWS_Com_00999|
|SRS_BSW_00309|All AUTOSAR Basic Soft-<br>ware Modules shall indicate<br>all global data with read-only<br>purposes by explicitly assig-<br>ning the const keyword|SWS_Com_00999|
|SRS_BSW_00312|Shared code shall be re-<br>entrant|SWS_Com_00321|
|SRS_BSW_00314|All internal driver modules<br>shall separate the interrupt<br>frame definition from the<br>service routine|SWS_Com_00999|
|SRS_BSW_00321|The version numbers of<br>AUTOSAR Basic Software<br>Modules shall be enumera-<br>ted according specific rules|SWS_Com_00999|
|SRS_BSW_00325|The runtime of interrupt<br>service routines and func-<br>tions that are running in<br>interrupt context shall be<br>kept short|SWS_Com_00999|
|SRS_BSW_00327|Error values naming conven-<br>tion|SWS_Com_00442|



Document ID 015: AUTOSAR_SWS_COM 

18 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|SRS_BSW_00328|All AUTOSAR Basic Soft-<br>ware Modules shall avoid the<br>duplication of code|SWS_Com_00999|
|---|---|---|
|SRS_BSW_00331|All Basic Software Modules<br>shall strictly separate error<br>and status information|SWS_Com_00194|
|SRS_BSW_00333|For each callback function it<br>shall be specified if it is<br>called from interrupt context<br>or not|SWS_Com_00999|
|SRS_BSW_00334|All Basic Software Modules<br>shall provide an XML file that<br>contains the meta data|SWS_Com_00999|
|SRS_BSW_00335|Status values naming con-<br>vention|SWS_Com_00819|
|SRS_BSW_00336|Basic SW module shall be<br>able to shutdown|SWS_Com_00129, SWS_Com_00130|
|SRS_BSW_00337|Classification of develop-<br>ment errors|SWS_Com_00803, SWS_Com_00804|
|SRS_BSW_00341|Module documentation shall<br>contains all needed informa-<br>tions|SWS_Com_00999|
|SRS_BSW_00344|BSW Modules shall support<br>link-time configuration|SWS_Com_00432|
|SRS_BSW_00347|A Naming seperation of<br>different instances of BSW<br>drivers shall be in place|SWS_Com_00999|
|SRS_BSW_00348|All AUTOSAR standard<br>types and constants shall be<br>placed and organized in a<br>standard type header file|SWS_Com_00865|
|SRS_BSW_00353|All integer type definitions of<br>target and compiler specific<br>scope shall be placed and<br>organized in a single type<br>header|SWS_Com_00999|
|SRS_BSW_00358|The return type of init()<br>functions implemented by<br>AUTOSAR Basic Software<br>Modules shall be void|SWS_Com_00432|
|SRS_BSW_00359|All AUTOSAR Basic Soft-<br>ware Modules callback<br>functions shall avoid return<br>types other than void if pos-<br>sible|SWS_Com_00468, SWS_Com_00491,<br>SWS_Com_00536, SWS_Com_00554,<br>SWS_Com_00555, SWS_Com_00556|
|SRS_BSW_00360|AUTOSAR Basic Software<br>Modules callback functions<br>are allowed to have parame-<br>ters|SWS_Com_00468, SWS_Com_00491,<br>SWS_Com_00536, SWS_Com_00554,<br>SWS_Com_00555, SWS_Com_00556|
|SRS_BSW_00361|All mappings of not standar-<br>dized keywords of compiler<br>specific scope shall be|SWS_Com_00999|



Document ID 015: AUTOSAR_SWS_COM 

19 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||placed and organized in a<br>compiler specific type and<br>keyword header||
|---|---|---|
|SRS_BSW_00369|All AUTOSAR Basic Soft-<br>ware Modules shall not<br>return specific development<br>error codes via the API|SWS_Com_00442|
|SRS_BSW_00375|Basic Software Modules<br>shall report wake-up reasons|SWS_Com_00999|
|SRS_BSW_00377|A Basic Software Module<br>can return a module specific<br>types|SWS_Com_00865|
|SRS_BSW_00378|AUTOSAR shall provide a<br>boolean type|SWS_Com_00999|
|SRS_BSW_00383|The Basic Software Module<br>specifications shall specify<br>which other configuration<br>files from other modules they<br>use at least in the descripti-<br>on|SWS_Com_00999|
|SRS_BSW_00384|The Basic Software Module<br>specifications shall specify at<br>least in the description which<br>other modules they require|SWS_Com_00669, SWS_Com_00670|
|SRS_BSW_00385|List possible error notifica-<br>tions|SWS_Com_00442|
|SRS_BSW_00386|The BSW shall specify the<br>configuration for detecting an<br>error|SWS_Com_00999|
|SRS_BSW_00404|BSW Modules shall support<br>post-build configuration|SWS_Com_00432, SWS_Com_00825|
|SRS_BSW_00405|BSW Modules shall support<br>multiple configuration sets|SWS_Com_00432|
|SRS_BSW_00407|Each BSW module shall<br>provide a function to read<br>out the version information of<br>a dedicated module imple-<br>mentation|SWS_Com_00426|
|SRS_BSW_00409|All production code error ID<br>symbols are defined by the<br>Dem module and shall be<br>retrieved by the other BSW<br>modules from Dem configu-<br>ration|SWS_Com_00999|
|SRS_BSW_00410|Compiler switches shall have<br>defined values|SWS_Com_00999|
|SRS_BSW_00413|An index-based accessing of<br>the instances of BSW mo-<br>dules shall be done|SWS_Com_00999|
|SRS_BSW_00414|Init functions shall have a<br>pointer to a configuration<br>structure as single parame-|SWS_Com_00432, SWS_Com_00805,<br>SWS_Com_00837|



Document ID 015: AUTOSAR_SWS_COM 

20 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||ter||
|---|---|---|
|SRS_BSW_00416|The sequence of modules to<br>be initialized shall be confi-<br>gurable|SWS_Com_00999|
|SRS_BSW_00417|Software which is not part of<br>the SW-C shall report error<br>events only after the DEM is<br>fully operational.|SWS_Com_00999|
|SRS_BSW_00423|BSW modules with AUTO-<br>SAR interfaces shall be<br>describable with the means<br>of the SW-C Template|SWS_Com_00999|
|SRS_BSW_00424|BSW module main proces-<br>sing functions shall not be<br>allowed to enter a wait state|SWS_Com_00999|
|SRS_BSW_00425|The BSW module descripti-<br>on template shall provide<br>means to model the defined<br>trigger conditions of schedu-<br>lable objects|SWS_Com_00359, SWS_Com_00398,<br>SWS_Com_00399, SWS_Com_00400,<br>SWS_Com_00664, SWS_Com_00665,<br>SWS_Com_00666|
|SRS_BSW_00426|BSW Modules shall ensure<br>data consistency of data<br>which is shared between<br>BSW modules|SWS_Com_00999|
|SRS_BSW_00427|ISR functions shall be defi-<br>ned and documented in the<br>BSW module description<br>template|SWS_Com_00999|
|SRS_BSW_00428|A BSW module shall state if<br>its main processing func-<br>tion(s) has to be executed in<br>a specific order or sequence|SWS_Com_00999|
|SRS_BSW_00429|Access to OS is restricted|SWS_Com_00999|
|SRS_BSW_00432|Modules should have sepa-<br>rate main processing func-<br>tions for read/receive and<br>write/transmit data path|SWS_Com_00359, SWS_Com_00398,<br>SWS_Com_00399, SWS_Com_00400,<br>SWS_Com_00466|
|SRS_BSW_00433|Main processing functions<br>are only allowed to be called<br>from task bodies provided by<br>the BSW Scheduler|SWS_Com_00999|
|SRS_BSW_00437|Memory mapping shall pro-<br>vide the possibility to define<br>RAM segments which are<br>not to be initialized during<br>startup|SWS_Com_00999|
|SRS_BSW_00441|Naming convention for type,<br>macro and function|SWS_Com_00820, SWS_Com_00821,<br>SWS_Com_00822, SWS_Com_00825,<br>SWS_Com_00865|
|SRS_BSW_00452|Classification of runtime<br>errors|SWS_Com_00864|
|SRS_Com_00177|AUTOSAR COM and|SWS_Com_00853, SWS_Com_00856|



Document ID 015: AUTOSAR_SWS_COM 

21 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||LargeDataCOM shall sup-<br>port multiple configuration<br>stages|||
|---|---|---|---|
|SRS_Com_00192|The AUTOSAR COM modu-<br>le shall support enabling and<br>disabling reception deadline<br>monitoring of I-PDU groups|<br>SWS_Com_00224,<br>SWS_Com_00486,<br>SWS_Com_00772,<br>SWS_Com_91004|SWS_Com_00225,<br>SWS_Com_00534,<br>SWS_Com_91003,<br>|
|SRS_Com_00218|The AUTOSAR COM modu-<br>le shall support starting and<br>stopping multiple I-PDU<br>groups during runtime|SWS_Com_00114,<br>SWS_Com_00222,<br>SWS_Com_00228,<br>SWS_Com_00334,<br>SWS_Com_00479,<br>SWS_Com_00685,<br>SWS_Com_00714,<br>SWS_Com_00771,<br>SWS_Com_00782,<br>SWS_Com_00787,<br>SWS_Com_00822,<br>SWS_Com_00871,<br>SWS_Com_91001,|SWS_Com_00115,<br>SWS_Com_00223,<br>SWS_Com_00229,<br>SWS_Com_00444,<br>SWS_Com_00684,<br>SWS_Com_00713,<br>SWS_Com_00733,<br>SWS_Com_00777,<br>SWS_Com_00783,<br>SWS_Com_00800,<br>SWS_Com_00840,<br>SWS_Com_00877,<br>SWS_Com_91002|
|SRS_Com_02030|The AUTOSAR COM modu-<br>le shall support to detect if a<br>received signal or signal<br>group was updated by the<br>sender|SWS_Com_00055,<br>SWS_Com_00061,<br>SWS_Com_00067,<br>SWS_Com_00310,<br>SWS_Com_00577,<br>SWS_Com_00702,<br>SWS_Com_00704,<br>SWS_Com_00706,<br>SWS_Com_00802|SWS_Com_00059,<br>SWS_Com_00062,<br>SWS_Com_00117,<br>SWS_Com_00324,<br>SWS_Com_00578,<br>SWS_Com_00703,<br>SWS_Com_00705,<br>SWS_Com_00801,<br>|
|SRS_Com_02037|AUTOSAR COM module<br>shall be based on the functi-<br>onality and APIs of<br>DOC_ISO_COM|SWS_Com_00010,<br>SWS_Com_00012,<br>SWS_Com_00132,<br>SWS_Com_00197,<br>SWS_Com_00231,<br>SWS_Com_00302,<br>SWS_Com_00304,<br>SWS_Com_00346,<br>SWS_Com_00380,<br>SWS_Com_00388,<br>SWS_Com_00396,<br>SWS_Com_00445,<br>SWS_Com_00471,<br>SWS_Com_00492,<br>SWS_Com_00604,<br>SWS_Com_00625,<br>SWS_Com_00694,<br>SWS_Com_00696,<br>SWS_Com_00698,<br>SWS_Com_00719,<br>SWS_Com_00764,<br>SWS_Com_00773,<br>SWS_Com_00775,<br>SWS_Com_00789,<br>SWS_Com_00812,<br>SWS_Com_00820,<br>SWS_Com_00835,<br>SWS_Com_00858,<br>SWS_Com_00862,|SWS_Com_00011,<br>SWS_Com_00013,<br>SWS_Com_00138,<br>SWS_Com_00198,<br>SWS_Com_00273,<br>SWS_Com_00303,<br>SWS_Com_00325,<br>SWS_Com_00348,<br>SWS_Com_00381,<br>SWS_Com_00395,<br>SWS_Com_00439,<br>SWS_Com_00469,<br>SWS_Com_00481,<br>SWS_Com_00603,<br>SWS_Com_00624,<br>SWS_Com_00631,<br>SWS_Com_00695,<br>SWS_Com_00697,<br>SWS_Com_00700,<br>SWS_Com_00762,<br>SWS_Com_00766,<br>SWS_Com_00774,<br>SWS_Com_00776,<br>SWS_Com_00793,<br>SWS_Com_00816,<br>SWS_Com_00828,<br>SWS_Com_00836,<br>SWS_Com_00861,<br>SWS_Com_00866,|



Document ID 015: AUTOSAR_SWS_COM 

22 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|||SWS_Com_00867,<br>SWS_Com_00878,<br>SWS_Com_00880|SWS_Com_00868,<br>SWS_Com_00879,<br>|
|---|---|---|---|
|SRS_Com_02040|AUTOSAR COM and<br>LargeDataCOM shall be<br>configured by using XML as<br>configuration language|SWS_Com_00006||
|SRS_Com_02041|The AUTOSAR module shall<br>handle complex data types<br>as a consistent set of data|SWS_Com_00050,<br>SWS_Com_00200,<br>SWS_Com_00461,<br>SWS_Com_00635,<br>SWS_Com_00638,<br>SWS_Com_00676,<br>SWS_Com_00678,<br>SWS_Com_00821,<br>SWS_Com_00852,<br>SWS_Com_00855,<br>SWS_Com_00882|SWS_Com_00051,<br>SWS_Com_00201,<br>SWS_Com_00513,<br>SWS_Com_00637,<br>SWS_Com_00639,<br>SWS_Com_00677,<br>SWS_Com_00679,<br>SWS_Com_00851,<br>SWS_Com_00854,<br>SWS_Com_00857,<br>|
|SRS_Com_02042|The AUTOSAR COM modu-<br>le shall fill unused areas/ bits<br>within an I-PDU with a confi-<br>gurable value|SWS_Com_00015||
|SRS_Com_02043|AUTOSAR COM and<br>LargeDataCOM shall provide<br>a receive indication function|<br>SWS_Com_00123||
|SRS_Com_02044|AUTOSAR COM and<br>LargeDataCOM shall provide<br>a transmit confirmation<br>function|<br>SWS_Com_00124||
|SRS_Com_02045|AUTOSAR COM and<br>LargeDataCOM shall provide<br>a function to request the<br>transmit buffer data for lower<br>layer triggered transmission|<br>SWS_Com_00001,<br>SWS_Com_00647,|SWS_Com_00475,<br>SWS_Com_00869|
|SRS_Com_02046|The AUTOSAR COM modu-<br>le shall support immediate<br>and deferred signal based<br>notification to the RTE|SWS_Com_00300,<br>SWS_Com_00574,<br>SWS_Com_00794,<br>SWS_Com_00883|SWS_Com_00301,<br>SWS_Com_00575,<br>SWS_Com_00870,<br>|
|SRS_Com_02058|The AUTOSAR COM modu-<br>le shall support deadline<br>monitoring for updated sig-<br>nals/signal groups on recei-<br>ver side|SWS_Com_00117,<br>SWS_Com_00291,<br>SWS_Com_00715,|SWS_Com_00290,<br>SWS_Com_00292,<br>SWS_Com_00716|
|SRS_Com_02067|AUTOSAR COM and<br>LargeDataCOM shall define<br>rules for checking the con-<br>sistency of configuration<br>data|SWS_Com_00102,<br>SWS_Com_00310,<br>SWS_Com_00373,<br>SWS_Com_00401,<br>SWS_Com_00443,<br>SWS_Com_00535,<br>SWS_Com_00732,<br>SWS_Com_00790,|SWS_Com_00105,<br>SWS_Com_00365,<br>SWS_Com_00384,<br>SWS_Com_00402,<br>SWS_Com_00465,<br>SWS_Com_00553,<br>SWS_Com_00785,<br>SWS_Com_00817|
|SRS_Com_02077|The AUTOSAR COM modu-<br>le shall support invalidation<br>of signals at sender side|SWS_Com_00099,<br>SWS_Com_00557,<br>SWS_Com_00643,|SWS_Com_00203,<br>SWS_Com_00642,<br>SWS_Com_00645|



Document ID 015: AUTOSAR_SWS_COM 

23 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|SRS_Com_02078|The AUTOSAR COM modu-<br>le shall support endianness<br>conversion|SWS_Com_00007,<br>SWS_Com_00352,<br>SWS_Com_00580,<br>SWS_Com_00675,|SWS_Com_00221,<br>SWS_Com_00472,<br>SWS_Com_00674,<br>SWS_Com_00810|
|---|---|---|---|
|SRS_Com_02079|The AUTOSAR COM modu-<br>le shall support an optional<br>notification when receiving<br>invalidated data|SWS_Com_00536,<br>SWS_Com_00681,<br>SWS_Com_00717,<br>SWS_Com_00859,|SWS_Com_00680,<br>SWS_Com_00682,<br>SWS_Com_00718,<br>SWS_Com_00860|
|SRS_Com_02080|The AUTOSAR COM modu-<br>le shall cancel outstanding<br>repetitions in case of a new<br>send request|SWS_Com_00279||
|SRS_Com_02082|The AUTOSAR COM modu-<br>le shall support defining two<br>different transmission modes<br>for each I-PDU|<br>SWS_Com_00032,<br>SWS_Com_00239,<br>SWS_Com_00495,<br>SWS_Com_00784,<br>SWS_Com_00881|SWS_Com_00238,<br>SWS_Com_00244,<br>SWS_Com_00582,<br>SWS_Com_00799,<br>|
|SRS_Com_02083|The AUTOSAR COM modu-<br>le shall support multiple<br>transmission modes|SWS_Com_00135,<br>SWS_Com_00308,<br>SWS_Com_00392,<br>SWS_Com_00478,<br>SWS_Com_00602,<br>SWS_Com_00739,<br>SWS_Com_00742,<br>SWS_Com_00767,<br>SWS_Com_00769,|SWS_Com_00305,<br>SWS_Com_00330,<br>SWS_Com_00467,<br>SWS_Com_00494,<br>SWS_Com_00734,<br>SWS_Com_00741,<br>SWS_Com_00743,<br>SWS_Com_00768,<br>SWS_Com_00770|
|SRS_Com_02084|The AUTOSAR COM modu-<br>le shall support a configurab-<br>le signal data based selec-<br>tion mechanism of the two<br>transmission modes|SWS_Com_00032,<br>SWS_Com_00605,<br>SWS_Com_00678,<br>SWS_Com_00763,<br>SWS_Com_00813|SWS_Com_00245,<br>SWS_Com_00677,<br>SWS_Com_00679,<br>SWS_Com_00799,<br>|
|SRS_Com_02086|The AUTOSAR COM modu-<br>le shall support sign-<br>extension|SWS_Com_00008,<br>SWS_Com_00579,<br>SWS_Com_00829|SWS_Com_00352,<br>SWS_Com_00723,<br>|
|SRS_Com_02087|The AUTOSAR COM modu-<br>le shall support an optional<br>substitution of received<br>invalidated data|SWS_Com_00470,<br>SWS_Com_00681,<br>SWS_Com_00859,|SWS_Com_00500,<br>SWS_Com_00683,<br>SWS_Com_00860|
|SRS_Com_02088|The AUTOSAR COM modu-<br>le shall support substituting<br>the last received value by<br>the init value in case of a<br>signal timeout|SWS_Com_00470,<br>SWS_Com_00876|SWS_Com_00875,<br>|
|SRS_Com_02089|The AUTOSAR COM modu-<br>le shall provide two configu-<br>rable options to handle<br>signal timeouts|SWS_Com_00290,<br>SWS_Com_00292,<br>SWS_Com_00738,|SWS_Com_00291,<br>SWS_Com_00333,<br>SWS_Com_00744|
|SRS_Com_02091|AUTOSAR COM and<br>LargeDataCOM shall not<br>support splitting of large<br>signals into different I-PDUs|SWS_Com_00754,<br>SWS_Com_00756|SWS_Com_00755,<br>|
|SRS_Com_02092|The AUTOSAR COM modu-<br>le shall support at most one<br>dynamic length signal per I-|SWS_Com_00690,<br>SWS_Com_00712,<br>SWS_Com_00754|SWS_Com_00711,<br>SWS_Com_00724,<br>|



Document ID 015: AUTOSAR_SWS_COM 

24 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||PDU||
|---|---|---|
|SRS_Com_02093|Dynamic length signal must<br>be placed last in I-PDU|SWS_Com_00755, SWS_Com_00757,<br>SWS_Com_00758, SWS_Com_00832|
|SRS_Com_02094|Dynamic length signals must<br>be of type UINT8n|SWS_Com_00675, SWS_Com_00753|
|SRS_Com_02095|AUTOSAR COM and<br>LargeDataCOM shall use the<br>TP to fragment and reas-<br>semble large signals|<br>SWS_Com_00627, SWS_Com_00628,<br>SWS_Com_00629, SWS_Com_00630,<br>SWS_Com_00650, SWS_Com_00654,<br>SWS_Com_00655, SWS_Com_00657,<br>SWS_Com_00662, SWS_Com_00690,<br>SWS_Com_00691, SWS_Com_00692,<br>SWS_Com_00693, SWS_Com_00720,<br>SWS_Com_00721, SWS_Com_00725,<br>SWS_Com_00818, SWS_Com_00838,<br>SWS_Com_00839, SWS_Com_00863,<br>SWS_Com_00874|
|SRS_Com_02096|The AUTOSAR COM modu-<br>le shall not support fragmen-<br>tation towards the RTE|SWS_Com_00759, SWS_Com_00760|
|SRS_Com_02097|AUTOSAR COM and<br>LargeDataCOM shall sup-<br>port dynamical signals with a<br>static maximum length|SWS_Com_00756|
|SRS_Com_02098|The AUTOSAR COM modu-<br>le shall distinct normal and<br>large signals via its configu-<br>ration|SWS_Com_00753|
|SRS_Com_02099|The AUTOSAR COM modu-<br>le shall provide a mechanism<br>to detect out of sequence<br>received I-PDUs|<br>SWS_Com_00587|
|SRS_Com_02101|The AUTOSAR COM modu-<br>le shall support the incre-<br>menting and checking of the<br>I-PDU Counter|SWS_Com_00588, SWS_Com_00687,<br>SWS_Com_00688|
|SRS_Com_02102|The AUTOSAR COM modu-<br>le shall support the detection<br>of out of sequence I-PDUs|SWS_Com_00590, SWS_Com_00726,<br>SWS_Com_00727, SWS_Com_00834|
|SRS_Com_02103|The AUTOSAR COM modu-<br>le shall provide a mechanism<br>to detect corrupted received<br>I-PDUs and to recover from<br>this failure mode|<br>SWS_Com_00596, SWS_Com_00597|
|SRS_Com_02105|The AUTOSAR COM modu-<br>le shall support transmission<br>and reception of replicated I-<br>PDUs|SWS_Com_00596, SWS_Com_00597|
|SRS_Com_02106|The AUTOSAR COM modu-<br>le shall support the detection<br>of failures when receiving<br>replicated I-PDUs|SWS_Com_00596, SWS_Com_00597|
|SRS_Com_02107|The AUTOSAR COM modu-<br>le shall cancel transmission|SWS_Com_00708|



Document ID 015: AUTOSAR_SWS_COM 

25 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||requests in case of expired<br>transmissions||
|---|---|---|
|SRS_Com_02112|AUTOSAR COM shall provi-<br>de a uint8-array based API<br>for signal groups|SWS_Com_00841, SWS_Com_00842,<br>SWS_Com_00843, SWS_Com_00844,<br>SWS_Com_00845, SWS_Com_00846,<br>SWS_Com_00847, SWS_Com_00848,<br>SWS_Com_00849, SWS_Com_00850,<br>SWS_Com_00851, SWS_Com_00852,<br>SWS_Com_00854, SWS_Com_00855|
|SRS_PduR_06002|The routing configuration<br>shall be updateable at post-<br>build time|SWS_Com_00357, SWS_Com_00361,<br>SWS_Com_00373|
|SRS_PduR_06055|The signal gateway shall<br>provide a mechanism to<br>route individual signals<br>between I-PDUs in a 1:n<br>fashion|SWS_Com_00377, SWS_Com_00539,<br>SWS_Com_00598, SWS_Com_00872,<br>SWS_Com_00873|
|SRS_PduR_06056|Signal Groups shall be rou-<br>ted|SWS_Com_00361, SWS_Com_00383,<br>SWS_Com_00735, SWS_Com_00833|
|SRS_PduR_06061|Routers shall map only<br>signals|SWS_Com_00360, SWS_Com_00361,<br>SWS_Com_00362|
|SRS_PduR_06064|The signal gateway shall be<br>scalable to zero size and<br>zero resource usage when<br>signal routing is not required|SWS_Com_00370|
|SRS_PduR_06089|The timeout of a deadline<br>monitored signal shall be<br>ignored by the SigG|SWS_Com_00377, SWS_Com_00701,<br>SWS_Com_00872, SWS_Com_00873|
|SRS_PduR_06097|A configuration shall be<br>identified by an unique ID<br>number|SWS_Com_00487|
|SRS_PduR_06098|Signal Gateway Error shall<br>be handled with signal rou-<br>ting|SWS_Com_00442|
|SRS_PduR_06099|Signal Gateway Error shall<br>be handled with signal group<br>routing|SWS_Com_00442|



Document ID 015: AUTOSAR_SWS_COM 

26 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **7 Functional Specification** 

## **7.1 Introduction** 

## **7.2 General Functionality** 

### **7.2.1 AUTOSAR COM basis** 

The _ISO 17356-4:2005 Road vehicles -- Open interface for embedded automotive applications -- Part 4: OSEK/VDX Communication (COM)_ is the functional basis of the AUTOSAR COM module. In this document, it is referenced as [17]. 

**[SWS_Com_00010]** ⌈ The AUTOSAR COM module shall implement all the functionality and all the APIs of [17] except the features and APIs mentioned in SWS_Com_00013. ⌋ (SRS_Com_02037) 

**[SWS_Com_00011]** ⌈ If this AUTOSAR COM specification defines functionality in a different way compared to definitions in [17], the AUTOSAR COM module shall implement the functionality defined in this AUTOSAR COM specification. ⌋ (SRS_Com_02037) 

**[SWS_Com_00012]** ⌈ The AUTOSAR COM module shall in addition implement all those features, that are defined in this AUTOSAR COM specification and that are not part of [17]. ⌋ (SRS_Com_02037) 

**[SWS_Com_00013]** ⌈ The AUTOSAR COM module may implement the following features of [17]. If they are implemented in a specific AUTOSAR COM module, the configuration shall disable them by default. This also applies for all other additional features a specific implementation may provide. ⌋ (SRS_Com_02037) 

|**_feature in[17]_**|**_Rationale_**|**_related API in[17]_**|
|---|---|---|
|Mapping of a received network<br>message (within an I-PDU) to more<br>than one message data objects (1:n<br>splittingmechanism)|not required, done by the<br>RTE, see[13]|none|
|Mapping of an internal message to<br>more than one message data ob-<br>jects (1:nsplittingmechanism)|not required, done by the<br>RTE, see[13]|none|
|Mapping an only locally send mes-<br>sage to both an external send mes-<br>sage object and an internal receive<br>message object (1:n splitting mech-<br>anism)|not required, done by the<br>RTE, see[13]|none|
|M:1 sending; mapping of messages<br>from multiple senders to one and the<br>same message object|not required, ensured by RTE,<br>see[13]|SendMessage|
|Queued messages|not required,done bythe|GetMessageStatus|



Document ID 015: AUTOSAR_SWS_COM 

27 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_feature in[17]_**|**_Rationale_**|**_related API in[17]_**|
|---|---|---|
||RTE,see[13]||
|Zero size messages|it is possible to set up com-<br>munication without them<br>functionality is partly covered<br>by Com_TriggerTransmit|SendZeroMessage|
|Notification mechanisms TASK,<br>FLAG and EVENT|not required, done by the<br>RTE,see[13]|none|
|Overlapping messages in an I-PDU|no use case, dangerous con-<br>cept|none|
|Usage of OIL|OIL is not used to configure<br>theAUTOSARCOM module.|None|
|Application modes|notneeded|GetComApplicationMode|
|Start-up behavior|replaced by<br><br>Com_Init<br><br>Com_DeInit<br><br>Com_IpduGroupStart<br><br>Com_IpduGroupStop|StartCOM, StopCOM,<br>StartCOMExtensions,<br>InitMessage|
|Start and stop of periodic messages|no use case, is realized by<br>I-PDU groupmechanism|StartPeriodic, StopPeriodic|
|Reentrancy|Not all of the AUTOSAR API<br>calls are reentrant. See Chap-<br>ter8.3.|See Chapter 8.3.|
|Interface to_indirect NM_|not needed|I_MessageTransfer,<br>I_MessageTimeOut|
|Sender side filtering|no use case, the filter condi-<br>tions are still used in the se-<br>lection of the transmission<br>mode but there is no signal<br>filtering|none|
|Network-order message callout<br>CPU-order message callout|Only I-PDU callouts with a<br>defined AUTOSAR interface<br>are supported by the AU-<br>TOSAR COM module. This is<br>to avoid proprietary solutions.|None|
|Error hook routine|The AUTOSAR COM module<br>defines an own interface for<br>error reporting instead of using<br>error hooks|COMErrorHook<br>COMError_Name1_Name2<br>macros<br>COMErrorGetServiceId|
|Interface for callback routines|The signatures for the used<br>callback function of the AU-<br>TOSAR COM module will be<br>explicitly defined within the<br>AUTOSAR COM module’s<br>specification.|COMCallback|
|Internal communication|not required, ensured by RTE,<br>see[13]|SendMessage,<br>ReceiveMessage|



**Table 1: Excluded features of [17] in the AUTOSAR COM module** 

### **7.2.2 Signal Values** 

The signals sent by the AUTOSAR COM module respectively received by the AUTOSAR COM module could have the values defined in Table 2. 

Document ID 015: AUTOSAR_SWS_COM 

28 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Signal value_**|**_Remark_**|
|---|---|
|initvalue|See Chapter 7.3.1.4 fordetails.|
|Datainvalidvalue|See Chapter 7.3.4 fordetails.|
|<value>|This is the normal case:<br>A valid value after initialization phase, which is sent by the AUTOSAR<br>COM module respectively,received byAUTOSAR COM module.|



**Table 2: Possible signal values** 

### **7.2.3 Endianness Conversion and Sign Extension** 

**[SWS_Com_00675]** ⌈ The AUTOSAR COM module shall support the following data types: 

- boolean 

- uint8 

- uint16 

- uint32 

- uint64 

- sint8 

- sint16 

- sint32 

- sint64 

- uint8[n] 

- float32 

- float64 

The type uint8[n] is mapped to either ComSignalType _UINT8_N or UINT8_DYN_ . ⌋ (SRS_Com_02078, SRS_Com_02094) 

**[SWS_Com_00007]** ⌈ The AUTOSAR COM module shall support endianness conversion for all supported signed and unsigned integer data types (see **SWS_Com_00675** ). ⌋ (SRS_Com_02078) 

**[SWS_Com_00810]** ⌈ The AUTOSAR COM module shall treat non-integer data types (e.g. uint8[n] or float32) either like integer data types of the matching size or leave their contents uninterpreted in case their ComSignalEndianness is configured to _OPAQUE_ . ⌋ (SRS_Com_02078) 

**[SWS_Com_00472]** ⌈ The AUTOSAR COM module shall interpret opaque data as uint8[n] and shall always map it to an n-bytes sized signal. ⌋ (SRS_Com_02078) 

For opaque data endianness, conversion has to be configured to _OPAQUE_ (see ECUC_Com_00157). 

**[SWS_Com_00674]** ⌈ The AUTOSAR COM module shall extend the endianness conversion defined in [17] Chapter 2.4 to signed data types. ⌋ (SRS_Com_02078) 

Document ID 015: AUTOSAR_SWS_COM 

29 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



In [17] Chapter 2.4 defines the endianness conversion for unsigned data types. The associated configurations can be found in Chapter 10. See also ECUC_Com_00127 and ECUC_Com_00157. 

**[SWS_Com_00829]** ⌈ The AUTOSAR COM module shall extend the endianness conversion defined in [17] Chapter 2.4 to signals of signal groups. ⌋ (SRS_Com_02086) 

AUTOSAR COM handles signals and group signals equaly with respect to endianness conversion. 

**[SWS_Com_00008]** ⌈ The AUTOSAR COM module shall extend received data to the size of the ComSignalType of the receive signal (sign extension). ⌋ (SRS_Com_02086) 

The platform specific representation of signed data has to be taken into account. Negative values of signed data will be mapped correctly. 

**Example:** A 10-Bit signed signal is received and copied by Com_ReceiveSignal to a 16-Bit signed integer variable. If (–3)decimal is received, the received 10-Bit signal has a value of 1111111101b. While copying it to the 16-Bit integer variable the value will be extended to 1111111111111101b. 

**[SWS_Com_00723]** ⌈ The AUTOSAR COM module shall extend the init value (ComSignalInitValue) of a signal to the size of its ComSignalType. ⌋ (SRS_Com_02086) 

Note that the AUTOSAR COM module will not need to perform sign extensions on sender side as it is guaranteed that the values to be transmitted will always be signextended. See also SWS_Com_00785. 

**[SWS_Com_00579]** ⌈ The AUTOSAR COM module shall not support sign extension for float32 and float64 data types. ⌋ (SRS_Com_02086) 

**[SWS_Com_00221]** ⌈ The AUTOSAR COM module shall perform endianness conversion before the I-PDU callout on sender side. For an overview, see Chapter 7.15. ⌋ (SRS_Com_02078) 

**[SWS_Com_00352]** ⌈ The AUTOSAR COM module shall perform sign extensions and endianness conversion before performing filtering and notification detection on receiver side. ⌋ (SRS_Com_02078, SRS_Com_02086) 

**[SWS_Com_00580]** ⌈ Beside endianness conversion, the AUTOSAR COM module shall not support further conversions for signals with ComSignalType FLOAT32 or FLOAT64. That is endianness conversion shall be supported but complex conversion or normalizations of fractions, exponents, signs or bias values shall not be supported. ⌋ (SRS_Com_02078) 

Document ID 015: AUTOSAR_SWS_COM 

30 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **7.2.4 Filtering** 

**[SWS_Com_00694]** ⌈ The AUTOSAR COM module shall evaluate each filtering condition to either true or false. ⌋ (SRS_Com_02037) 

**[SWS_Com_00695]** ⌈ The AUTOSAR COM module shall filter out signals only at receiver side. ⌋ (SRS_Com_02037) 

**[SWS_Com_00602]** ⌈ The AUTOSAR COM module shall use filtering mechanisms on sender side for Transmission Mode Conditions (TMC) but it shall not filter out signals on sender side. ⌋ (SRS_Com_02083) 

For Transmission Mode Selection (TMS) see Chapters 7.3.3.2 and 7.3.3.3. 

<mark>The AUTOSAR COM module only provides the following ComFilterAlgorithms of that which are defined in [17], see ECUC_Com_00146:</mark> 

- _<mark>ALWAYS</mark>_ 

- _<mark>NEVER</mark>_ 

- _<mark>MASKED_NEW_EQUALS_X</mark>_ 

- _<mark>MASKED_NEW_DIFFERS_X</mark>_ 

- _<mark>MASKED_NEW_DIFFERS_MASKED_OLD</mark>_ 

- _<mark>NEW_IS_WITHIN</mark>_ 

- _<mark>NEW_IS_OUTSIDE</mark>_ 

- _<mark>ONE_EVERY_N</mark>_ 

To reduce complexity the AUTOSAR COM module does not support all filters defined in [17]. The not supported filters are either obsolete or special cases of other filters. For example, the filter _NEW_IS_DIFFERENT_ is a special case of _MASKED_NEW_DIFFERS_MASKED_OLD_ with a fully set mask. 

**[SWS_Com_00325]** ⌈ The AUTOSAR COM module shall support all filter mechanisms listed in ECUC_Com_00146, considering the exceptions defined in SWS_Com_00380 and SWS_Com_00439. ⌋ (SRS_Com_02037) 

**[SWS_Com_00380]** ⌈ For signals with ComSignalType _FLOAT32_ , _FLOAT64_ , _UINT8_N_ or _UINT8_DYN_ , the AUTOSAR COM module shall only support ComFilterAlgorithm configured to _ALWAYS, NEVER_ or ONE_EVERY_N. ⌋ (SRS_Com_02037) 

**[SWS_Com_00439]** ⌈ For signals with ComSignalType configured to _BOOLEAN_ , the AUTOSAR COM module shall only support ComFilterAlgorithm configured to: 

   - _ALWAYS_ 

   - _NEVER_ 

   - _MASKED_NEW_EQUALS_X_ 

   - _MASKED_NEW_DIFFERS_X_ 

   - _MASKED_NEW_DIFFERS_MASKED_OLD_ 

   - _ONE_EVERY_N_ 

- ⌋ (SRS_Com_02037) 

Document ID 015: AUTOSAR_SWS_COM 

31 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00764]** ⌈ For signals and group signals with ComBitSize configured to 0, the AUTOSAR COM module shall not support the filter algorithm _Masked_New_Differs_Masked_Old._ ⌋ (SRS_Com_02037) 

**[SWS_Com_00866]** ⌈ In case the configured filter condition is MASKED_NEW_DIFFERS_X, MASKED_NEW_EQUALS_X, NEW_IS_OUTSIDE or NEW_IS_WITHIN, the AUTOSAR COM module shall calculate the reception filter by using only the least significant ComBitSize bits of the filter parameters. ⌋ (SRS_Com_02037) 

**[SWS_Com_00273]** ⌈ If the AUTOSAR COM module filters out a signal on receiver side, i.e. filter condition evaluates to false, the AUTOSAR COM module shall discard that signal and shall not process it. See also SWS_Com_00303. ⌋ (SRS_Com_02037) 

**[SWS_Com_00836]** ⌈ If the AUTOSAR COM module filters out a group signal on receiver side, i.e. filter condition evaluates to false, the AUTOSAR COM module shall discard the whole signal group and shall not process it. ⌋ (SRS_Com_02037) 

**[SWS_Com_00132]** ⌈ The AUTOSAR COM module shall support the filtering mechanisms as defined in ECUC_Com_00146 also for signed data types. ⌋ (SRS_Com_02037) 

In the case a filter is evaluated before a send-API has written the corresponding signal, there needs to be a way to determine the filter state of this signal. Some of the filters require a _new_value_ to evaluate the filter. However, this is only available after the signal has been updated using a send-API. Therefore, it is necessary to define the value used by the filter for _new_value_ in the period before the first send takes place. 

**[SWS_Com_00603]** ⌈ The AUTOSAR COM module shall set the _old_value_ of the filtering mechanisms for each signal to the ComSignalInitValue (ECUC_Com_00170) during start-up. See also [17]. ⌋ (SRS_Com_02037) 

**[SWS_Com_00604]** ⌈ Until the application has not updated the _new_value_ of the filtering mechanisms for a signal, the AUTOSAR COM module shall use the ComSignalInitValue as the _new_value_ for that signal. ⌋ (SRS_Com_02037) 

The next two requirements clarify the definitions of [17] according to the update of the _old_value_ of filters. 

**[SWS_Com_00302]** ⌈ If the AUTOSAR COM module evaluates a filter for a signal to true, (value is not filtered out) then the AUTOSAR COM module shall place the value of that signal into _old_value_ (as defined in [17]). ⌋ (SRS_Com_02037) 

**[SWS_Com_00303]** ⌈ When a value is being filtered, if the filter does not allow the passage of the value (i.e. the filter evaluates to false) then the AUTOSAR COM module shall not place that value into _old_value_ (as defined in [17]). ⌋ (SRS_Com_02037) 

**[SWS_Com_00231]** ⌈ In the case of ComFilterAlgorithm is configured to _ONE_EVERY_N_ , the AUTOSAR COM module shall 

Document ID 015: AUTOSAR_SWS_COM 

32 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



   - set OCCURRENCE to zero when OCCURRENCE == PERIOD 

   - set FILTER to true, when OCCURRENCE == OFFSET 

   - increment OCCURRENCE after filter processing 

- ⌋ (SRS_Com_02037) 

For definition of OCCURRENCE, FILTER, OFFSET and PERIOD see [17]. 

Configuring ComFilterAlgorithm to _ONE_EVERY_N_ for a signal has the effect that the signal is passed by the filter (i.e. the filter returns true) once every PERIOD calls of the filter. If the OFFSET parameter is zero then the first time the filter is used the signal is allowed to pass (i.e. filter returns true). If the OFFSET is greater than zero then more than one signal must pass through the filter before it returns true. 

In case the I-PDU is started by Com_IpduGroupStart with parameter initialize set to true, the OCCURRENCE is also set to zero, see SWS_Com_00787. 

This definition exists to clarify the description of the _ONE_EVERY_N_ filter in [17]. 

The associated configuration items can be found in Chapter 10, see ECUC_Com_00339. 

**[SWS_Com_00793]** ⌈ For a signal with a configured reception filter MASKED_NEW_DIFFERS_MASKED_OLD, the AUTOSAR COM module shall treat the first value received for this signal after a reception deadline monitoring timeout occurred for this signal the same way as if the value has passed the filter criteria. ⌋ (SRS_Com_02037) 

Hence, the AUTOSAR COM module will let pass any value for the filter MASKED_NEW_DIFFERS_MASKED_OLD after an RX deadline timeout for the associated I-PDU. 

### **7.2.5 Signal Gateway** 

<mark>The AUTOSAR COM module provides an integrated Signal Gateway for forwarding signals and group signals in a 1:n manner.</mark> 

The routing relations are be statically configured via the ComGwMapping configuration container (see ECUC_Com_00544). 

<mark>As shown in Figure 4 and Figure 5, the integrated Signal Gateway acts as a receiver</mark> for all signals or group signals which are configured as a source for gatewayed signals. 

After the Signal Gateway received signal or group signals for routing, it acts immediately as a sender for these signals or group signals respectively. This is shown in <mark>Figure 3 and Figure 5. The signal processing does not differ if the integrated Signal Gateway forwards a signal/ group signal or if a Software Component sends it.</mark> 

Document ID 015: AUTOSAR_SWS_COM 

33 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



Since the gateway relations are statically configured, an optimized Signal Gateway might skip some processing stages for concrete configurations. For example, the endianness conversion is not necessary in certain cases. Of course, such optimizations should not lead to any different logical behavior or different representations on the target bus. Optimizations may only be introduced to increase the Signal Gateway’s performance. 

As shown in Figure 4 a received signal or group signal might be received on the local ECU and be a source for a gateway action at the same time. 

Figure 3 and Figure 4 show shadow buffers only for group signals that are received by the RTE. The integrated Signal Gateway has of course to ensure to handle group signals consistently but there is no predetermined way in which this must be implemented. 

**[SWS_Com_00370]** ⌈ The Signal Gateway of the AUTOSAR COM module shall scale down to no size if no signal routing functionality is needed. ⌋ (SRS_PduR_06064) 

## **7.3 Normal Operation** 

### **7.3.1 Start-Up Behavior** 

This chapter describes the actions that will be performed during Com_Init. 

**[SWS_Com_00217]** ⌈ The AUTOSAR COM module shall initialize each I-PDU during execution of Com_Init (SWS_Com_00432), firstly byte wise with the ComTxIPduUnusedAreasDefault value and then bit wise according to initial values (ComSignalInitValue) of the contained signals and the update-bits (see SWS_Com_00117). ⌋ (SRS_BSW_00101) 

### **7.3.1.1 Preconditions** 

<mark>The C initialization code, also known as</mark> _<mark>start-up code</mark>_ <mark>, initializes global and static variables with the initial values. It must be executed before any call of an AUTOSAR COM module’s service.</mark> 

### **7.3.1.2 Initialization** 

**[SWS_Com_00128]** ⌈ The AUTOSAR COM module’s initialization function Com_Init (SWS_Com_00432) shall initialize all internal data that is not yet initialized by the _start-up code_ e.g. C-structs. ⌋ (SRS_BSW_00101) 

**[SWS_Com_00328]** ⌈ The AUTOSAR COM module’s initialization function Com_Init (SWS_Com_00432) shall not enable Inter-ECU communication. ⌋ (SRS_BSW_00101) 

This initialization chapter is not complete. Details about initialization of some AUTOSAR COM module’s features are described within the different feature chapters. 

Document ID 015: AUTOSAR_SWS_COM 

34 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**7.3.1.3 Initialization of Not Used Areas of an I-PDU** 

**[SWS_Com_00015]** ⌈ The AUTOSAR COM module shall fill not used areas within an I-PDU with a value determined by configuration parameter ComTxIPduUnusedAreasDefault (ECUC_Com_00017) e.g. 0xFF. ⌋ (SRS_BSW_00101, SRS_Com_02042) 

### **7.3.1.4 Initialization of Signals and Update-Bits** 

**[SWS_Com_00098]** ⌈ The AUTOSAR COM module shall initialize each signal of n-bit sized signal type on sender and receiver side with the lower n-bits of its configuration parameter ComSignalInitValue (ECUC_Com_00170). ⌋ (SRS_BSW_00101) 

The configured ComSignalInitValues (ECUC_Com_00170) are also used for the initialization of the signal in the related I-PDU; see SWS_Com_00217. 

The ComSignalInitValue (ECUC_Com_00170) of a signal can be identical to its ComSignalDataInvalidValue (ECUC_Com_00391). These can be different for each signal. 

**[SWS_Com_00117]** ⌈ The AUTOSAR COM module shall clear all update-bits during initialization. See also SWS_Com_00059. ⌋ (SRS_BSW_00101, SRS_Com_02030, SRS_Com_02058) 

### **7.3.1.5 Initialization of I-PDU Groups** 

**[SWS_Com_00444]** ⌈ By default, all I-PDU groups shall be in the state stopped and they shall not be started automatically by a call to Com_Init (SWS_Com_00432). ⌋ (SRS_Com_00218) 

### **7.3.2 De-Initialization** 

The AUTOSAR COM module provides the API function Com_DeInit (SWS_Com_00130) for de-initialization of the COM layer. This means, after deinitialization of the layer, no communication via the AUTOSAR COM module is possible and all started I-PDU groups are stopped, see also SWS_Com_00129. 

### **7.3.3 Communication Modes** 

This chapter defines the signal flow in the AUTOSAR COM module. It further defines the different transmission modes provided by the AUTOSAR COM module. Chapter 7.3.3.2 defines a mechanism to switch between two transmission modes for one I-PDU. The replication of signals is defined in Chapter 7.3.3.4. 

Explemary communication use cases that the AUTOSAR COM module can deal with are shown in Chapter 12. 

Document ID 015: AUTOSAR_SWS_COM 

35 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **7.3.3.1 Transfer Properties and I-PDU Transmission Mode** 

### 7.3.3.1.1 **Signals** 

The AUTOSAR COM module supports several **_transfer properties_** for signals and several **_transmission modes_** for I-PDUs. The definitions in this chapters are based on and are to be completed with the definitions in [17] Chapter 2.3.3. 

**[SWS_Com_00330]** ⌈ At any send request of a signal with ComTransferProperty _TRIGGERED_ assigned to an I-PDU with ComTxModeMode _DIRECT_ or _MIXED_ , the AUTOSAR COM module shall immediately (within the next main function at the latest) initiate ComTxModeNumberOfRepetitions plus one transmissions of the assigned I-PDU. ⌋ (SRS_Com_02083) 

**[SWS_Com_00767]** ⌈ At any send request of a signal with ComTransferProperty _TRIGGERED_WITHOUT_REPETITION_ assigned to an I-PDU with ComTxModeMode _DIRECT_ or _MIXED_ , the AUTOSAR COM module shall immediately (within the next main function at the latest) initiate one transmission of the assigned I- PDU. ⌋ ( SRS_Com_02083) 

**[SWS_Com_00734]** ⌈ At a send request of a signal with ComTransferProperty _TRIGGERED_ON_CHANGE_ assigned to an I-PDU with ComTxModeMode _DIRECT_ or _MIXED_ , the AUTOSAR COM module shall immediately (within the next main function at the latest) initiate ComTxModeNumberOfRepetitions plus one transmissions of the assigned I-PDU, if the new sent signal differs to the locally stored (last sent or init) in length or value. ⌋ (SRS_Com_02083) 

**[SWS_Com_00768]** ⌈ At a send request of a signal with ComTransferProperty TRIGGERED ON_CHANGE_WITHOUT_REPETITION_ assigned to an I-PDU with ComTxModeMode _DIRECT_ or _MIXED_ , the AUTOSAR COM module shall immediately (within the next main function at the latest) initiate one transmission of the assigned I-PDU, if the new sent signal differs to the locally stored (last sent or init) in length or value. ⌋ (SRS_Com_02083) 

**[SWS_Com_00762]** ⌈ The AUTOSAR COM module shall not support the transfer properties _TRIGGERED_ON_CHANGE_ and _TRIGGERED_ON_CHANGE_WITHOUT_REPETITION_ for signals and group signals with ComBitSize configured to 0. ⌋ (SRS_Com_02037) 

The support of the transfer properties TRIGGERED_ON_CHANGE and TRIGGERED_ON_CHANGE_WITHOUT_REPETITION is not restricted to certain signal types. Hence, they are supported for all possible signal types. This includes even the byte array types, e.g. UINT8_N. 

The details of the transmission replication mechanism are specified in Chapter 7.3.3.4. 

Document ID 015: AUTOSAR_SWS_COM 

36 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00135]** ⌈ The AUTOSAR COM module shall not initiate transmissions for I-PDUs that have the ComTxModeMode (ECUC_Com_00137) _NONE_ . ⌋ (SRS_Com_02083) 

It is possible to request I-PDUs with ComTxModeMode _NONE_ via Com_TriggerTransmit. 

A pending signal associated with an I-PDU is transmitted if the I-PDU’s transmission is triggered for any reason. For example, if a signal with ComTransferProperty _TRIGGERED_ within the same I-PDU is sent or the I-PDU sending is scheduled because of ComTxModeMode _PERIODIC_ or _MIXED_ . 

The bus-timing of I-PDUs can be controlled by send requests of the RTE in combination with the transmission mode and the transfer property as described above. Additionally, the PDU Router, especially in case of FlexRay and LIN, can control it with the service Com_TriggerTransmit. In the latter case, the PDU Router requests I-PDUs to be sent from the AUTOSAR COM module. 

The function Com_TriggerTransmit can be called for any I-PDU regardless of its transmission mode. This allows LIN and FlexRay to use all the available transmission modes, particularly for sporadic communication. The NM also uses this mechanism to send user data. 

### 7.3.3.1.2 **Signal Groups** 

In AUTOSAR COM also signal groups and group signals may have a transfer property, defining in combination with the transmission mode, if the I-PDU is sent out in case of an update of a signal group or group signal, respectively. 

**[SWS_Com_00741]** ⌈ At any send request of a signal group with ComTransferProperty _TRIGGERED_ assigned to an I-PDU with ComTxModeMode _DIRECT_ or _MIXED_ , the AUTOSAR COM module shall immediately (within the next main function at the latest) initiate ComTxModeNumberOfRepetitions plus one transmissions of the assigned I-PDU. ⌋ (SRS_Com_02083) 

**[SWS_Com_00769]** ⌈ At any send request of a signal group with ComTransferProperty _TRIGGERED_WITHOUT_REPETITION_ assigned to an I-PDU with ComTxModeMode _DIRECT_ or _MIXED_ , the AUTOSAR COM module shall initiate one transmission of the assigned I-PDU within the next main function at the latest. ⌋ (SRS_Com_02083) 

**[SWS_Com_00742]** ⌈ Regarding signal groups with ComTransferProperty _TRIGGERED_ON_CHANGE_ which do not contain any signals that have an own ComTransferProperty configured: 

At any send request of such a signal group assigned to an I-PDU with ComTxModeMode _DIRECT_ or _MIXED_ , the AUTOSAR COM module shall immediately (within the next main function at the latest) initiate ComTxModeNumberOfRepetitions plus one transmissions of the assigned I-PDU, if at least one new sent group signal differs to the locally stored (last sent or init) in length or value. ⌋ (SRS_Com_02083) 

Document ID 015: AUTOSAR_SWS_COM 

37 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00743]** ⌈ Regarding signal groups with ComTransferProperty _TRIGGERED_ON_CHANGE_ which contain any signals that have an own ComTransferProperty configured: 

At any send request of such a signal group assigned to an I-PDU with ComTxModeMode _DIRECT_ or _MIXED_ , the AUTOSAR COM module shall immediately (within the next main function at the latest) initiate ComTxModeNumberOfRepetitions plus one transmissions of the assigned I-PDU, if at least one new sent group signal configured with ComTransferProperty _TRIGGERED_ON_CHANGE_ differs to the locally stored (last sent or init) in length or value. ⌋ (SRS_Com_02083) 

**[SWS_Com_00770]** ⌈ At a send request of a signal group with ComTransferProperty _TRIGGERED_ON_CHANGE_WITHOUT_REPETITION_ assigned to an I-PDU with ComTxModeMode _DIRECT_ or _MIXED_ , the AUTOSAR COM module shall immediately (within the next main function at the latest) initiate one transmission of the assigned I-PDU, if at least one new sent group signal differs to the locally stored (last sent or init) in length or value. ⌋ (SRS_Com_02083) 

### **7.3.3.2 Selection of the Transmission Mode for one specific I-PDU** 

I-PDUs carry signals. Because an I-PDU can contain more than one signal, in the following, a method is defined to derive the I-PDU’s transmission mode from the state of the signals that are contained in one specific I-PDU. 

The AUTOSAR COM module allows configuring statically two different transmission modes for each I-PDU (see SWS_Com_00032). The transmission mode of an I-PDU that is valid at a specific point in time is selected using only the values of the signals that are mapped to this I-PDU. 

The signals of one I-PDU that contribute to the selection of one of the two transmission modes as well as the conditions used for the selection of the transmission mode are configured statically, see SWS_Com_00676. 

For the selection of the transmission mode, the AUTOSAR COM module treats group signals like normal signals. 

**[SWS_Com_00676]** ⌈ For the evalutation of a TMS, the AUTOSAR COM module shall take all those (group) signals into account which configuration include a configured ComFilter container. See included containers of ComSignal and ComGroupSignal. ⌋ (SRS_Com_02041) 

If a signal of an I-PDU with ComIPduDirection configured to _SEND_ has a configuration container ComFilter included, the signal is named to **_contribute_** to the TMS of this I-PDU. If the configuration container for that signal has no assigned configuration container ComFilter, then it does **_not contribute_** to a TMS. 

**[SWS_Com_00677]** ⌈ If no signal within an I-PDU contributes to the calculation of the TMS, then the AUTOSAR COM module shall evaluate the TMS of this I-PDU as true. ⌋ (SRS_Com_02084, SRS_Com_02041) 

Document ID 015: AUTOSAR_SWS_COM 

38 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00678]** ⌈ If the AUTOSAR COM module evaluates the TMC of a contributing signal as true, then the AUTOSAR COM module shall evaluate the TMS as true. ⌋ (SRS_Com_02084, SRS_Com_02041) 

**[SWS_Com_00679]** ⌈ If the AUTOSAR COM module evaluates no TMC of a contributing signal as true, then the AUTOSAR COM module shall evaluate the TMS as false. ⌋ (SRS_Com_02084, SRS_Com_02041) 

**[SWS_Com_00605]** ⌈ The AUTOSAR COM module shall define a Transmission Mode Selector, for each I-PDU. See definition of TMS above. ⌋ ( SRS_Com_02084) 

**[SWS_Com_00245]** ⌈ The AUTOSAR COM module shall re-calculate the TMS for an I-PDU, after a contained signal was updated by a call to Com_SendSignal or Com_SendSignalGroup. ⌋ (SRS_Com_02084) 

**[SWS_Com_00763]** ⌈ For the calculation of the transmission mode with the configured condition _MASKED_NEW_DIFFERS_MASKED_OLD_ , the AUTOSAR COM module shall use the least significant ComBitSize bits only. ⌋ (SRS_Com_02084) 

**[SWS_Com_00813]** ⌈ For the calculation of the transmission mode with a configured condition _MASKED_NEW_DIFFERS_X_ , _MASKED_NEW_EQUALS_X_ , _NEW_IS_OUTSIDE_ or _NEW_IS_WITHIN_ , the AUTOSAR COM module shall use all bits of the configured ComSignalType. ⌋ (SRS_Com_02084) 

Note that a signal with ComFilterAlgorithm configured to _ALWAYS,_ will always set the TMS of the respective I-PDU to true. Therefore, care must be taken when defining the signals that contribute to the TMS. 

**[SWS_Com_00032]** ⌈ If the TMS of an I-PDU evaluates to true, then the AUTOSAR COM module shall use the ComTxModeMode defined in configuration container ComTxModeTrue (ECUC_Com_00455) for that I-PDU. ⌋ (SRS_Com_02082, SRS_Com_02084) 

**[SWS_Com_00799]** ⌈ If the TMS for an I-PDU evaluates to false, then the AUTOSAR COM module shall use the ComTxModeMode defined in configuration container ComTxModeFalse (ECUC_Com_00454) for that I-PDU. ⌋ (SRS_Com_02082, SRS_Com_02084) 

**[SWS_Com_00238]** ⌈ In each of the two TMS states, the rules for combination of transfer properties of signals and transmission modes of I-PDUs shall apply as defined in [17] Section 2.3. ⌋ (SRS_Com_02082) 

**[SWS_Com_00239]** ⌈ When the TMS state of an I-PDU changes, the AUTOSAR COM module shall use the now valid transmission mode immediately (within the next main function at the latest). That means, first the AUTOSAR COM module shall perform the mode change and after that, the AUTOSAR COM module shall execute any resulting calls to PduR_ComTransmit caused by mode change. ⌋ (SRS_Com_02082) 

Document ID 015: AUTOSAR_SWS_COM 

39 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00244]** ⌈ If a change of the TMS causes a change of the transmission mode for an I-PDU, then the AUTOSAR COM module shall restart the timer for the cycle time of the transmission mode _PERIODIC_ and _MIXED_ . ⌋ (SRS_Com_02082) 

**[SWS_Com_00495]** ⌈ When a call to Com_SendSignal or Com_SendSignalGroup results into a change of the transmission mode of a started I-PDU to the transmission mode _PERIODIC_ or _MIXED_ , then the AUTOSAR COM module shall start the new transmission cycle with a call to PduR_ComTransmit within the next main function at the latest. The transmission shall be initiated regardless of the transfer property of the signal or signal group that caused the transmission mode switch. The minimum delay time shall still be respected. See also Figure 5 _The AUTOSAR COM module’s interaction model for reception_ . ⌋ (SRS_Com_02082) 

The ComTxModeTimeOffset is not respected. It is only respected by explicit I-PDU transmission mode switches, for example by Com_IpduGroupStart or Com_SwitchIpduTxMode. 

**[SWS_Com_00582]** ⌈ If a change of the TMS causes a change to the transmission mode _DIRECT,_ an immediate (within the next main function at the latest unless shifted due to the MDT) direct/ n-times transmission to the underlying layer shall be initiated. ⌋ (SRS_Com_02082) 

The above requirement clarifies the behavior in case the TMS-switch to ComTxModeMode _DIRECT_ was triggered by a signal with ComTransferProperty _PENDING_ . 

If the ComTxModeMode of an I-PDU is configured to _NONE_ no transmission will be initiated by AUTOSAR COM. This can be used to prevent transmitting an I-PDU, for example in case the TMS evaluates to false. 

**[SWS_Com_00478]** ⌈ The AUTOSAR COM module shall send out an I-PDU at most once within one call of Com_MainFunctionTx. ⌋ (SRS_Com_02083) 

### **7.3.3.3 Signal Flow and Transmission Mode Selection** 

After a send request from the RTE for a specific signal, the signal is written to the appropriate I-PDU buffer as defined by configuration, and the selection of the transmission mode of the I-PDUs is done according to Chapter 7.3.3.2. 

Figure 2 shows the signal flow: 

Document ID 015: AUTOSAR_SWS_COM 

40 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 





<!-- Start of picture text -->
Conditions are the<br>same as Filters in [17] IPDUk<br>true<br>Evaluation of Transmis-<br>sion Mode Condition<br>C(Signal1 , I-PDUk)<br>false<br>update signal in I-PDU<br>Signal 1 Signal 1<br>Conditions are the<br>same as Filters in [17]<br>true<br>Evaluation of Transmis-<br>sion Mode Condition<br>C(Signal 2, I-PDUk)<br>false<br>update signal in I-PDU Signal 2<br>Signal 2<br>Conditions are the<br>From RX side –  same as Filters in [17]<br>after endianness<br>true<br>conversion and<br>sign extension  Evaluation of Transmis-<br>sion Mode Condition<br>Signal C(Signal 3, I-PDUk)<br>based<br>RX gateway TX false<br>Signal 3<br>update signal in I-PDU<br>From RX side –<br>before endianness<br>conversion and<br>sign extension<br>Evaluation of Trans-<br>mission Mode Selec-<br>tor (TMS) for I-PDUk<br><!-- End of picture text -->

**Figure 2: Logical signal flow in the AUTOSAR COM module shown for two signals (Signal1 and Signal2) that are mapped to one I-PDU (IPDUk)** 

Document ID 015: AUTOSAR_SWS_COM 

41 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **7.3.3.4 Replication of Signal Transmission Requests** 

The number of repetitions of transmission requests in the ComTxModeMode _DIRECT_ or _MIXED_ for a send request by the RTE is defined by configuration parameter ComTxModeNumberOfRepetitions (ECUC_Com_00281). 

**[SWS_Com_00467]** ⌈ If ComRetryFailedTransmitRequests is not set to TRUE and an I-PDU with ComTxModeMode DIRECT or MIXED and ComTxModeNumberOfRepetitions set to 0 is triggered for sending, the AUTOSAR COM module shall invoke PduR_ComTransmit for this I-PDU just once, independently of the result of the confirmation. ⌋ (SRS_Com_02083) 

Configuring ComTxModeNumberOfRepetitions to 0 imitates the original direct transmission mode of [17]. 

**[SWS_Com_00279]** ⌈ If a new send request is received from the RTE while sending n transmissions belonging together (e.g. after the 3<sup>rd</sup> of 5 repetitions, see SWS_Com_00305) the AUTOSAR COM module shall cancel the outstanding transmission repetitions and start processing the new request within the next main function at the latest, see Appendix A use-case 4. ⌋ (SRS_Com_02080) 

**[SWS_Com_00305]** ⌈ In case of sending an I-PDU with ComTxModeMode _DIRECT_ or _MIXED_ and ComTxModeNumberOfRepetitions greater than 0, the AUTOSAR COM module shall call PduR_ComTransmit periodically, with period ComTxModeRepetitionPeriod until _ComTxModeNumberOfRepetitions plus one_ successful confirmations for this send-request are received. ⌋ (SRS_Com_02083) 

SWS_Com_00305 assumes that CAN does not have a queue for these I-PDUs. There is a race condition in the interaction between the CAN driver, interface and hardware that may cause an extra transmission to occur in certain unlikely circumstances. 

If the underlying layer returns E_NOT_OK while an N-Times transmission is in progress, this error notification will be ignored, unless ComRetryFailedTransmitRequests is set to true (see also SWS_Com_00773). As SWS_Com_00305 specifies, only confirmed transmissions are counted for the N-Times transmission, erroneous send request can safely be ignored. 

If the N-Times transmission is requested in transmission mode _MIXED_ after a cyclic transmission of the _MIXED_ transmission mode with a pending confirmation, the confirmation of the cyclic transmission will be assigned to the N-Times transmission. In this case, only n-1 transmissions of the new value of the N-Times request are observed. The transmission deadline monitoring timer will then be reset earliest after the N-Times request is completed. This must be respected when configuring the transmission deadline monitoring timer in conjunction with the _MIXED_ transmission mode and N-Times transmission. 

**[SWS_Com_00494]** ⌈ If within the transmission mode _MIXED_ an N-Times transmission request overlaps with the cyclic part of the mixed transmission the cyclic trans- 

Document ID 015: AUTOSAR_SWS_COM 

42 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



mission shall be counted as the corresponding transmission of the N-Times transmission request. ⌋ (SRS_Com_02083) 

**[SWS_Com_00392]** ⌈ If a transmission deadline monitoring timeout occurs before the N-Times transmission is complete, then the AUTOSAR COM module shall not initiate further transmissions for this N-Times transmission. ⌋ (SRS_Com_02083) 

The minimum delay time will always be taken into account as defined in [17] Chapter 2.3.4. 

To avoid bursts in start-up a time offset can be configured per I-PDU. See ECUC_Com_00180 for details. 

The time between two repetitions is configured by configuration parameter ComTxModeRepetitionPeriod (ECUC_Com_00282). 

If the transmission mode change leads to the start of the _MIXED_ transmission mode by sending a triggered signal and ComTxModeNumberOfRepetitions is configured greater than or equal to 1, then there will be at least ComTxModeNumberOfRepetitions plus one transmission requests to the PDU Router at the beginning of the _MIXED_ transmission mode. See also SWS_Com_00305. 

### **7.3.3.5 Retry Failed Transmission Requests** 

**[SWS_Com_00773]** ⌈ If ComRetryFailedTransmitRequests is set to TRUE, the return value of PduR_ComTransmit shall be evaluated. If the return value of PduR_ComTransmit is not equal to E_OK, the AUTOSAR COM Module shall invoke PduR_ComTransmit for the not sent I-PDU again within the next Com_MainFunctionTx. ⌋ (SRS_Com_02037) 

If the I-PDU is updated in between, the new data will be sent. 

SWS_Com_00773 may lead to multiple retries for the same failed transmission request. 

SWS_Com_00773 is not affected by transmission mode changes. 

SWS_Com_00773 has no influence on a potential repetition period. Any repetitions will occur as if no retry had taken place. 

**[SWS_Com_00774]** ⌈ The AUTOSAR COM module shall start the transmission deadline monitoring independently of possible retries. Subsequent retries shall not affect transmission deadline monitoring. ⌋ (SRS_Com_02037) 

**[SWS_Com_00775]** ⌈ If ComRetryFailedTransmitRequests is set to True and a transmission deadline monitoring timeout occurs for an I-PDU, the AUTOSAR COM module shall expire any pending transmission request for this I-PDU. ⌋ (SRS_Com_02037) 

Document ID 015: AUTOSAR_SWS_COM 

43 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00776]** ⌈ The cycle timer for a cyclic transmission shall always start with the first transmit attempt. ⌋ (SRS_Com_02037) 

### **7.3.4 Signal Invalidation** 

The AUTOSAR COM module provides the possibility for the sender to indicate that it is not able to provide a valid value for a corresponding signal, for example in case a sensor is faulty. The AUTOSAR COM module allows defining a ComSignalDataInvalidValue (ECUC_Com_00391) during configuration. 

### **7.3.4.1 Transmission of an Invalidated Signal** 

**[SWS_Com_00099]** ⌈ By a call to Com_InvalidateSignal, the AUTOSAR COM module shall perform internally a Com_SendSignal with the configured ComSignalDataInvalidValue (ECUC_Com_00391). ⌋ (SRS_Com_02077) 

The ComTransferProperty and the transmission mode determine the transmission of the ComSignalDataInvalidValue on the bus. The internally performed Com_SendSignal with the data invalid value leads to data invalid value to be used as current value for filters and TMS. 

The data invalid values are configured per group signal see ECUC_Com_00520. 

The VFB defines only one attribute for a complex data type. Therefore, the best mapping of an invalidated complex data type to an invalidated signal group is to invalidate all group signals of a signal group. Therefore, the RTE can also request to invalidate the complete signal group by a call to Com_InvalidateSignalGroup (SWS_Com_00557). 

### **7.3.4.2 Reception of an Invalidated Signal** 

**[SWS_Com_00680]** ⌈ If the configured ComSignalDataInvalidValue (ECUC_Com_00391) is received for a signal and the ComDataInvalidAction (ECUC_Com_00314) is configured to **_NOTIFY_** for this signal, the AUTOSAR COM module shall notify the RTE via the configured ComInvalidNotification function (ECUC_Com_00315). In this case, no other signal processing like filtering or the normal signal indication shall take place. ⌋ (SRS_Com_02079) 

The reception deadline monitoring timer is also restarted in case of receiving an invalid signal or signal group, see SWS_Com_00738. 

**[SWS_Com_00681]** ⌈ If the configured ComSignalDataInvalidValue (ECUC_Com_00391) is received for a signal and the ComDataInvalidAction (ECUC_Com_00314) is configured to **_REPLACE_** for this signal, the AUTOSAR COM module shall replace the signal’s value by its configured ComSignalInitValue (ECUC_Com_00170). After the replacement, the normal signal processing like filtering and notification shall take place as if the ComSignalInitValue would have been 

Document ID 015: AUTOSAR_SWS_COM 

44 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



received instead of the ComSignalDataInvalidValue. ⌋ (SRS_Com_02079, SRS_Com_02087) 

**[SWS_Com_00682]** ⌈ If the configured ComSignalDataInvalidValue (ECUC_Com_00391) is received for at least one group signal of a signal group and the ComDataInvalidAction (ECUC_Com_00314) is configured to **_NOTIFY_** for this signal group, the AUTOSAR COM module shall notify the RTE via the configured ComInvalidNotification function (ECUC_Com_00315). In this case, no other signal group/ group signal processing like the normal indication shall take place. ⌋ (SRS_Com_02079) 

**[SWS_Com_00683]** ⌈ If the configured ComSignalDataInvalidValue (ECUC_Com_00391) is received for at least one group signal of a signal group and the ComDataInvalidAction (ECUC_Com_00314), is configured to **_REPLACE_** for this signal group, the AUTOSAR COM module shall replace all group signals of this signal group by their configured ComSignalInitValue values. After the replacement, the normal signal group/ group signal processing like reception notification shall take place as if the ComSignalInitValue would have been received for all group signals. ⌋ (SRS_Com_02087) 

**[SWS_Com_00717]** ⌈ If the configured ComSignalDataInvalidValue is received for a signal and its ComDataInvalidAction is configured to **_NOTIFY_** , the AUTOSAR COM module shall not store the received ComSignalDataInvalidValue into the signal object. ⌋ (SRS_Com_02079) 

The next call to Com_ReceiveSignal will return the last valid received signal or the ComSignalInitValue in case no signal was received yet respectively. 

**[SWS_Com_00718]** ⌈ If the configured ComSignalDataInvalidValue is received for at least one group signal of a signal group and its ComDataInvalidAction is configured to **_NOTIFY_** , the AUTOSAR COM module shall not store any of the received group signals into the signal objects. ⌋ (SRS_Com_02079) 

The next call to Com_ReceiveSignalGroup will copy the last valid received group signals or the ComSignalInitValues in case the signal group was not received yet respectively into the shadow buffer. 

Document ID 015: AUTOSAR_SWS_COM 

45 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **7.3.5 Handling of I-PDUs** 

### **7.3.5.1 I-PDU Group Definitions** 

For an I-PDU group the following rules apply: 

1. An I-PDU can belong to any I-PDU group. 

2. An I-PDU is active (started) if it belong to a started I-PDU group (see SWS_Com_00771) or it does not belong to any I-PDU group and it was started implicitly (see SWS_Com_00840). 

3. The maximum number of I-PDU groups is pre-compile configurable. 

4. I-PDU groups may contain only I-PDUs of the same direction (i.e. send or receive), see SWS_Com_00871. 

Rules 1 and 3 are supported by the COM configuration. The maximum number of supported I-PDU groups can be configured via ComSupportedIpduGroups (ECUC_Com_00710). 

**[SWS_Com_00771]** ⌈ An I-PDU is active (started) if at least one I-PDU group is active (started) it belongs to. ⌋ (SRS_Com_00218) 

For the AUTOSAR COM module, the nesting of I-PDU groups is purely conceptual and must be resolved by an appropriate configuration and/ or usage of the AUTOSAR COM module. 

For example, if an I-PDU “BUS1 RX Function1” belongs to I-PDU group “BUS1 RX” and I-PDU group “BUS1 RX” is included in I-PDU group “BUS1” then I-PDU “BUS1 RX Function1” must also be included in I-PDU group “BUS1”.  Such dependencies need to be resolved at configuration time. 

Once again, the COM module does not know or handle any grouping of I-PDUs. Any I-PDU grouping must be handeld either via configuration or by the calling module. 

Further, it is expected that the complete state handling of I-PDU groups is done outside of the AUTOSAR COM module, e.g. within the Basic Software Mode Manager. In case of a state change, the module managing the I-PDU group states consistently starts or stops the I-PDU groups via Com_IpduGroupStart and Com_IpduGroupStop. 

The state of I-PDUs that are not assigned to any I-PDU group cannot be changed, therefore they are started implicitly: 

**[SWS_Com_00840]** ⌈ If an I-PDU is not assigned to any I-PDU group, the AUTOSAR COM shall start this I-PDU within Com_Init as if it would be started by Com_IpduGroupStart with parameter Initialize set to true (see Chapter 7.3.5.2). ⌋ (SRS_Com_00218) 

Since the AUTOSAR COM never stops such an I-PDU implicitely and it is not assigned to any I-PDU group, such an I-PDU can never be stopped. 

Document ID 015: AUTOSAR_SWS_COM 

46 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **7.3.5.2 Starting of I-PDU Groups** 

By default all I-PDU groups are stopped, see SWS_Com_00444. A call to Com_IpduGroupStart starts an I-PDU group if it was previously stopped. 

**[SWS_Com_00114]** ⌈ If an I-PDU is started by Com_IpduGroupStart, the AUTOSAR COM module shall permit to transmit/ receive its signals and signal groups, see also Table 4. ⌋ (SRS_Com_00218) 

**[SWS_Com_00787]** ⌈ If an I-PDU is started by Com_IpduGroupStart, the AUTOSAR COM module shall always initialize the following attributes of this I-PDU: 

- 1) ComMinimumDelayTime of I-PDUs in transmission mode _DIRECT_ or _MIXED_ 

- 2) restart all reception deadline monitoring timers for all signals with a non-zero configured ComFirstTimeout 

- 3) cancel all transmission deadline monitoring timers and use ComFirstTimeout (if configured) as value when a transmission timer is started the first time after the I-PDU activation 

- 4) all included update-bits shall be cleared 

- 5) reset _OCCURRENCE_ of filters with ComFilterAlgorithm _ONE_EVERY_N_ 

- 6) set the I-PDU counter to 0 for I-PDUs with ComIPduDirection configured to SEND 

- 7) accept for I-PDUs with ComIPduDirection configured to _RECEIVED_ any next incoming I-PDU counter ⌋ (SRS_Com_00218) 

**[SWS_Com_00222]** ⌈ If an I-PDU is started by Com_IpduGroupStart with parameter Initialize set to true, the AUTOSAR COM module shall additionally to SWS_Com_00787 initialize the following attributes of this I-PDU: 

- 1) the data of the I-PDU as defined in SWS_Com_00217 

- 2) the shadow buffers of included signal groups 

- 3) old_value of the filtering mechanisms for each signal to the ComSignalInitValue 

- 4) ComTxModeTimePeriod and ComTxModeTimeOffset of I-PDUs in Periodic or MIXED transmission mode ⌋ (SRS_Com_00218) 

**[SWS_Com_00223]** ⌈ If an I-PDU is started by Com_IpduGroupStart, the AUTOSAR COM module shall determine its transmission mode according to its current data content. ⌋ (SRS_Com_00218) 

**[SWS_Com_00228]** ⌈ In some cases, an I-PDU is started by Com_ IpduGroupStart before all its contained signals have been written. In this case, the AUTOSAR COM module shall use the ComSignalInitValue for the missing signal data. ⌋ (SRS_Com_00218) 

**[SWS_Com_00229]** ⌈ When an I-PDU is started and one or more signals in that I-PDU have already been written via one of the send APIs by the upper layer, the AUTOSAR COM module shall use the most recently obtained values to determine the TMS of the I-PDU. ⌋ (SRS_Com_00218) 

**[SWS_Com_00733]** ⌈ If an I-PDU is started by Com_IpduGroupStart and the I-PDU contains signals that have deadline monitoring configured (ECUC_Com_00183, 

Document ID 015: AUTOSAR_SWS_COM 

47 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



ECUC_Com_00263), the AUTOSAR COM module shall start the deadline monitoring for these signals independently of the value of the initialize parameter. ⌋ (SRS_Com_00218) 

Note, in case an I-PDU is started by Com_IpduGroupStart and the parameter initialize is set to false, the internal buffers are not changed and the I-PDU contains the last the last set or init values. Particulary, if the I-PDU is started for the first time and initilaize is set to false, the COM operates on the init-values set by Com_Init. 

**[SWS_Com_00877]** ⌈ If an I-PDU is not part of any I-PDU Group, it is started during the initialization of COM. Its starting transmission mode shall be evaluated according to the ComSignalInitValue of the signals contributing to its TMS. ⌋ (SRS_Com_00218) 

For this case, the evaluation can already be done at configuration time, since the signals cannot be written before the initialization of COM. 

### **7.3.5.3 Stopping of I-PDU Groups** 

A call to Com_IpduGroupStop stops an I-PDU group, if it was previously started. 

In order to disable the transmission of an I-PDU, all I-PDU groups containing this I-PDU needs to be stopped. Hence, to implement **_listen-only-mode_** , all I-PDU groups containing transmission I-PDUs needs to be stopped. Receiving of I-PDUs may also be stopped. 

**[SWS_Com_00334]** ⌈ By a call to the functions: Com_SendSignal, Com_SendSignalGroup, or Com_InvalidateSignal, the AUTOSAR COM module shall update the values of its internal buffers even for stopped I-PDUs. See also Table 3. ⌋ (SRS_Com_00218) 

If a signal written to a stopped I-PDU would trigger the transmission of this I-PDU if it were not stopped, then this trigger is not stored. After re-starting the corresponding I-PDU group, such an old trigger does not lead to an immediate transmission of the I-PDU. 

**[SWS_Com_00777]** ⌈ If an I-PDU is stopped by Com_IpduGroupStop, the AUTOSAR COM module shall cancel any outstanding transmission requests for this I-PDU. This includes cancelling any potential retries with respect to ComRetryFailedTransmitRequests. ⌋ (SRS_Com_00218) 

**[SWS_Com_00115]** ⌈ If an I-PDU is stopped by Com_IpduGroupStop, the AUTOSAR COM module shall cancel the deadline monitoring for all pending confirmations. ⌋ (SRS_Com_00218) 

**[SWS_Com_00800]** ⌈ The AUTOSAR COM module shall ignore any transmit confirmations for a stopped I-PDU. ⌋ (SRS_Com_00218) 

Document ID 015: AUTOSAR_SWS_COM 

48 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



The AUTOSAR COM module cannot prohibit the invocation of the Com_TriggerTransmit function. However, in case of a stopped I-PDU, the function Com_TriggerTransmit returns E_NOT_OK. See SWS_Com_00001. 

**[SWS_Com_00684]** ⌈ If an I-PDU is stopped by Com_IpduGroupStop, the AUTOSAR COM module shall disable its reception processing. ⌋ (SRS_Com_00218) 

**[SWS_Com_00713]** ⌈ If a large I-PDU is stopped by Com_IpduGroupStop, the AUTOSAR COM module shall stop the reception process and ignore the partly received I-PDU. ⌋ (SRS_Com_00218) 

**[SWS_Com_00685]** ⌈ If an I-PDU is stopped by Com_IpduGroupStop, the AUTOSAR COM module shall cancel its deadline monitoring. ⌋ (SRS_Com_00218) 

**[SWS_Com_00479]** ⌈ If an I-PDU is stopped by Com_IpduGroupStop, the AUTOSAR COM module shall immediately invoke the configured ComErrorNotification (ECUC_Com_00499), for outstanding not confirmed transmitted signals/ signal groups of the stopped I-PDU. ⌋ (SRS_Com_00218) 

**[SWS_Com_00714]** ⌈ If a large I-PDU is stopped while its transmission is already in progress, the AUTOSAR COM module shall stop the transmission process immediately. ⌋ (SRS_Com_00218) 

Table 3 gives an overview of the behavior of stopped I-PDUs: 

|**_Behavior of stopped I-PDUs_**||
|---|---|
|**_Receiver side(RX)_**|**_Transmitter side(TX)_**|
|<br>Disable RX deadline monitoring<br><br>No action on a Com_RxIndication to RTE,<br>no storing of the I-PDU|<br>Disable sending<br><br>Disable TX deadline monitoring<br><br>Ignore Com_TxConfirmation:|
|<br>Return code<br>COM_SERVICE_NOT_AVAILABLE on<br>Com_ReceiveSignal and<br>Com_ReceiveSignalGroup and the last<br>known value (or init value) is given back as<br>data|<br>On a call of<br>Com_SendSignal,<br>Com_SendSignalGroup,<br>Com_InvalidateSignal and<br>the values in the AUTOSAR COM module’s in-<br>ternal buffers are still up-dated but the return<br>code COM_SERVICE_NOT_AVAILABLE is re-<br>turned<br><br>Outstanding transmission request (e.g. N-<br>Times) will be cancelled<br><br>Return code E_NOT_OK on<br>Com_TriggerTransmit|
||**_For periodic (TX)_**|
||Do not send anymore|



**Table 3: Behavior of stopped I-PDUs** 

Table 4 gives an overview of the behavior of started I-PDUs: 

Document ID 015: AUTOSAR_SWS_COM 

49 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Behavior of started I-PDUs_**||
|---|---|
|**_Receiver side(RX)_**|**_Transmitter side(TX)_**|
|<br>Reinitialize timeouts if Initialize==true|<br>Normal reaction on|
|(ComSignalFirstTimeout, ComSignal-<br>Timeout)|Com_InvalidateSignal,<br>Com_SendSignal,|
|<br>Normal reaction on Com_RxIndication/<br>Com_TpRxIndication<br><br>Normal reaction on Com_ReceiveSignal,<br>and Com_ReceiveSignalGroup|and Com_SendSignalGroup<br><br>No transmission timeout notification until next<br>send<br><br>Normal reaction on Com_TxConfirmation/<br>Com_TpTxConfirmation<br><br>Normal reaction on Com_TriggerTransmit|
||**_For periodic (TX)_**|
||Start at 0|



**Table 4 Behavior of started I-PDUs** 

### **7.3.5.4 Signal Indication (Unpacking of I-PDUs)** 

In order to support both interrupt-driven and polled systems, it can be configured when the signal indication takes place. There are two configurable signal indication modes _IMMEDIATE_ and _DEFERRED_ configurable via ComIPduSignalProcessing. See ECUC_Com_00119. 

**[SWS_Com_00300]** ⌈ If ComIPduSignalProcessing for an I-PDU is configured to _IMMEDIATE_ , the AUTOSAR COM module shall invoke the configured ComNotifications for the included signals and signal groups within the Com_RxIndication, or Com_TpRxIndication function respectively. ⌋ (SRS_Com_02046) 

**[SWS_Com_00301]** ⌈ If ComIPduSignalProcessing for an I-PDU is configured to _DEFERRED_ , the AUTOSAR COM module shall first copy the I-PDU’s data within the Com_RxIndication function or the related TP reception functions respectively from the PduR into COM. Then the AUTOSAR COM module shall invoke the configured ComNotifications for the included signals and signal groups asynchronously during the next call to Com_MainFunctionRx. ⌋ (SRS_Com_02046) 

If in _DEFERRED_ mode a call to Com_ReceiveSignal is made before the deferred unpacking takes place, the previous not updated values are returned. 

A sequence chart with both indication options can be found in Chapter 9.3. The configuration of these modes is defined in ECUC_Com_00119. 

**[SWS_Com_00574]** ⌈ When unpacking an I-PDU, the AUTOSAR COM module shall check the received data length (PduInfoPtr->SduLength) and unpack and notify only completely received signals via ComNotification. ⌋ (SRS_Com_02046) 

**[SWS_Com_00870]** ⌈ In case of receiving a smaller I-PDU than the length derived via the parameter ComPduIdRef, signals with size 0 shall be received if and only if their configured position is less or equal to the received size of the partially received I-PDU. ⌋ (SRS_Com_02046) 

Document ID 015: AUTOSAR_SWS_COM 

50 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00794]** ⌈ In case of receiving of a smaller I-PDU than expected results into receiving a signal without its configured update-bit, the AUTOSAR COM module shall treat this signal as if its update bit was set and interpret such a signal as updated. ⌋ (SRS_Com_02046) 

If the received I-PDU length is smaller than the configured/ expected I-PDU length, it needs to be prevented that signals are updated partially. On the other hand all completely received signals should be received and notified to the upper layer. 

**[SWS_Com_00575]** ⌈ When unpacking an I-PDU, the AUTOSAR COM module shall check the received data length (PduInfoPtr->SduLength) and in case a signal group is received only partially, such a signal group and all included group signals shall not be unpacked or notified via ComNotification. ⌋ (SRS_Com_02046) 

The above requirement prevents inconsistently received signal groups and therefore inconsistently received complex data types. 

The AUTOSAR COM module does not copy or handle additional received data for not configured signals in case the received data length is greater than expected. 

### **7.3.5.5 Minimum Delay Timer (MDT)** 

The AUTOSAR COM module inherits the minimum delay timer mechanism as defined [17]. This mechanism is clarified and detailed in this chapter. 

When an I-PDU is started, the MDT is re-initialized. Therefore, the MDT can be violated by stopping and starting I-PDUs rapidly. 

The behavior of the transmission deadline monitoring timer is not affected by any transmission delay caused by the minimum delay time supervision. 

**[SWS_Com_00471]** ⌈ No minimum delay time monitoring shall take place, if ComMinimumDelayTime is omitted or configured to 0. ⌋ (SRS_Com_02037) 

**[SWS_Com_00789]** ⌈ If ComEnableMDTForCyclicTransmission (ECUC_Com_00788) is configured to false, the minimum delay timer shall not be (re)started in the following cases: 

   - I-PDUs with ComTxModeMode PERIODIC 

   - the cyclic part of I-PDUs with ComTxModeMode MIXED 

   - repeated transmissions for I-PDUs in case ComTxModeNumberOfRepetitions > 0 

- ⌋ (SRS_Com_02037) 

In case the minimum delay timer is currently not started, there is no way for the minimum delay timer to expire. Thus, optimized implementations might for example omit monitoring the minimum delay time for periodic I-PDUs completely in case ComEnableMDTForCyclicTransmission is configured to false, since the minimum delay timer never gets started. 

Document ID 015: AUTOSAR_SWS_COM 

51 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00698]** ⌈ If ComMinimumDelayTime of an I-PDU is configured greater than 0 and ComRetryFailedTransmitRequests is set to _FALSE_ , the AUTOSAR COM module shall load and start the minimum delay time counter upon transmission of that I-PDU to the PDU Router via PduR_ComTransmit. ⌋ (SRS_Com_02037) 

**[SWS_Com_00828]** ⌈ If ComMinimumDelayTime of an I-PDU is configured greater than 0 and ComRetryFailedTransmitRequests is set to _TRUE_ , the AUTOSAR COM module shall load and start the minimum delay time counter upon transmission of that I-PDU to the PDU Router via PduR_ComTransmit only in case PduR_ComTransmit returns E_OK. ⌋ (SRS_Com_02037) 

**[SWS_Com_00469]** ⌈ If ComMinimumDelayTime of an I-PDU is configured greater than 0, the AUTOSAR COM module shall (re-)load an already running and not yet elapsed minimum delay time counter of that I-PDU with ComMinimumDelayTime on a successful transmit confirmation. ⌋ (SRS_Com_02037) 

The running minimum delay timer is reloaded upon the reception of a successful TXconfirmation of that I-PDU, unless the transmission was already delayed longer than ComMinimumDelayTime at the reception of the confirmation. In normal case, there will be no further transmission of that I-PDU by the AUTOSAR COM module unless the loaded and started minimum delay has expired. See also Figures 2-4, 2-5 and 2- 7 in [17]. However, some exception exists: According to SWS_Com_00475 Com_TriggerTransmit does not interfere with the minimum delay timer. Further, the minimum delay timer is reset if the transmission deadline monitoring timer expires; see Chapter 2.3.4 in [17]. In addition, starting an I-PDU group resets the minimum delay time timer of the included I-PDUs. 

**[SWS_Com_00812]** ⌈ If the minimum delay timer of an I-PDU is reset because the transmission deadline monitoring timer expires and a postponed request for this I-PDU exists, the AUTOSAR COM module shall immediately transmit this I-PDU. ⌋ (SRS_Com_02037) 

### **7.3.6 Deadline Monitoring** 

Deadline monitoring for signals is defined in [17]. 

In the context of deadline monitoring for a signal group, it is handled like a signal. The deadline monitoring parameters ComFirstTimeout and ComTimeout can be defined in the configuration container ComSignal or ComSignalGroup. 

The corresponding timeout notification callback functions can be defined in parameter ComTimeoutNotification in the configuration container ComSignal or ComSignalGroup. 

**[SWS_Com_00333]** ⌈ If the configuration parameter ComTimeout for a signal or signal group is omitted or configured to 0, the AUTOSAR COM module shall not monitor this signal or signal group. It also shall ignore the ComFirstTimeout. ⌋ (SRS_Com_02089) 

Document ID 015: AUTOSAR_SWS_COM 

52 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **7.3.6.1 Reception Deadline Monitoring** 

The reception deadline monitoring can be enabled and disabled by the control of I-PDU groups analogous to Chapter 7.3.5.1. 

**[SWS_Com_00772]** ⌈ The reception deadline monitoring of an I-PDU is enabled if and only if it is contained in an I-PDU group that has reception deadline monitoring enabled. Otherwise, the reception deadline monitoring of the I-PDU is _disabled_ . ⌋ (SRS_Com_00192) 

**[SWS_Com_00292]** ⌈ In the case where reception deadline monitoring is configured for signals with update-bits, the AUTOSAR COM module shall perform a separate reception deadline monitoring for each signal/ signal group with an update-bit. For configuration of ComTimeout, see ECUC_Com_00263. ⌋ (SRS_Com_02089, SRS_Com_02058) 

**[SWS_Com_00290]** ⌈ The AUTOSAR COM module shall perform an I-PDU based reception deadline monitoring for signals without an update-bit. ⌋ (SRS_Com_02089, SRS_Com_02058) 

**[SWS_Com_00291]** ⌈ For all signals and signal groups without update-bits within the same I-PDU, the AUTOSAR COM module shall perform the reception deadline monitoring of the I-PDU using the smallest configured non-zero timeout parameter (ComFirstTimeout, ComTimeout) of all these signals and signal groups which do not have an update-bit configured. ⌋ (SRS_Com_02089, SRS_Com_02058) 

If all signals within an I-PDU with configured reception deadline monitoring have also an update-bit configured, no reception deadline monitoring on I-PDU base needs to be performed. 

In case of an Rx-timeout, the ComRxDataTimeoutAction parameter determines whether the AUTOSAR COM module replaces the signal/ signal group value with the initial value or substitute value or maintains the last received value. See ECUC_Com_00412. 

**[SWS_Com_00470]** ⌈ If ComRxDataTimeoutAction is set to _REPLACE_ (see ECUC_Com_00412), the AUTOSAR COM module shall replace the signal’s value by its ComSignalInitValue (see ECUC_Com_00170) when the reception deadline monitoring timer of a signal expires. ⌋ (SRS_Com_02087, SRS_Com_02088) 

In case the ComSignalInitValue replaces the last received value, the last received value is overwritten and gets lost. Therefore, the AUTOSAR COM module returns the ComSignalInitValue for this signal until a new value is received. 

**[SWS_Com_00875]** ⌈ If ComRxDataTimeoutAction is set to SUBSTITUTE (see ECUC_Com_00412), the AUTOSAR COM module shall replace the signal's value by its ComTimeoutSubstitutionValue (see ECUC_Com_10006) when the reception deadline monitoring timer of a signal expires. ⌋ (SRS_Com_02088) 

Document ID 015: AUTOSAR_SWS_COM 

53 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00500]** ⌈ If the reception deadline monitoring timer of a signal or signal group expires and the configuration parameter ComRxDataTimeoutAction for this signal or signal group is either omitted or configured to _NONE_ , the AUTOSAR COM module shall not replace the signal or the signals of the signal groups respectively. ⌋ (SRS_Com_02087) 

**[SWS_Com_00513]** ⌈ If ComRxDataTimeoutAction is set to _REPLACE_ (see ECUC_Com_00412), the AUTOSAR COM module shall replace the values of all included group signals by their ComSignalInitValues (see ECUC_Com_00170), when the reception deadline monitoring timer of a signal group expires. ⌋ (SRS_Com_02041) 

The Rx-timeout-indication can be combined and configured separately from ECUC_Com_00412. 

**[SWS_Com_00876]** ⌈ If ComRxDataTimeoutAction is set to SUBSTITUTE (see ECUC_Com_00412), the AUTOSAR COM module shall replace the values of all included group signals by their ComTimeoutSubstitutionValue (see ECUC_Com_10006), when the reception deadline monitoring timer of a signal group expires. ⌋ (SRS_Com_02088) 

**[SWS_Com_00715]** ⌈ When a (large) I-PDU with a configured reception deadline monitoring is received successfully, the AUTOSAR COM module shall reset the reception deadline monitoring timer for this (large) I-PDU at invocation of the function Com_RxIndication or Com_TpRxIndication respectively. ⌋ (SRS_Com_02058) 

**[SWS_Com_00716]** ⌈ If the configuration parameter ComFirstTimeout for a signal or signal group is omitted or configured to 0, the AUTOSAR COM module shall not monitor the reception of this signal or signal group respectively from the start of the corresponding I-PDU until the first reception. ⌋ (SRS_Com_02058) 

**[SWS_Com_00738]** ⌈ The I-PDU based reception deadline monitoring mechanism shall not take the values of the signals into account. ⌋ (SRS_Com_02089) 

### 7.3.6.1.1 **En-/Disable Reception Deadline Monitoring** 

When reception deadline monitoring of an I-PDU is disabled and the timer expires, no error indication will be given to the RTE. 

Disabling reception deadline monitoring does not stop the reception of an I-PDU. 

**[SWS_Com_00224]** ⌈ If the reception deadline monitoring of an I-PDU is enabled by Com_EnableReceptionDM, the AUTOSAR COM module shall set the reception deadline monitoring timer for the included signals and signal groups to the configured ComFirstTimeout value. ⌋ (SRS_Com_00192) 

**[SWS_Com_00486]** ⌈ The AUTOSAR COM module shall silently ignore setting the reception deadline monitoring of an I-PDU to enabled by Com_EnableReceptionDM, 

Document ID 015: AUTOSAR_SWS_COM 

54 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



in case the reception deadline monitoring is already enabled for this I-PDU. ⌋ (SRS_Com_00192) 

Enabling reception deadline monitoring implies that timeout notifications of deadline monitoring expiry are notified to the RTE for signals or signal groups with a configured ComTimeoutNotification (ECUC_Com_00552). 

**[SWS_Com_00534]** ⌈ If Com_EnableReceptionDM or Com_DisableReceptionDM is invoked on an I-PDU group containing Tx-I-PDUs, then the AUTOSAR COM module shall silently ignore this request. ⌋ (SRS_Com_00192) 

**[SWS_Com_00225]** ⌈ The AUTOSAR COM module shall silently ignore setting the reception deadline monitoring of an I-PDU to disabled by Com_DisableReceptionDM, in case the reception deadline monitoring is already disabled for this I-PDU. ⌋ (SRS_Com_00192) 

### **7.3.6.2 Transmission Deadline Monitoring** 

The general idea of the AUTOSAR COM transmission deadline monitoring is to supervise the lower layers and the bus but not the COM module itself. Hence, the transmission monitoring timer is generally started, when the COM module sends an I-PDU to the lower layer. This is independent of a transmission mode, a transfer property or update-bits. In generally the transmission monitoring timer is not restarted or reset if it is currently running. 

**[SWS_Com_00481]** ⌈ The AUTOSAR COM module shall perform the transmission deadline monitoring (if configured) for all signals and signal groups independently from the transfer property and independently from the transmission modes of the I-PDU the signal / signal group belongs to. ⌋ (SRS_Com_02037) 

The AUTOSAR COM module makes no distinction between signals with ComTransferProperty _PENDING_ or _TRIGGERED_ with respect to transmission deadline monitoring. 

**[SWS_Com_00445]** ⌈ If different ComTimeout parameters of the associated signals/ signal groups of an I-PDU are configured, the AUTOSAR COM module shall use the smallest value as timeout parameter for the transmission deadline monitoring of the I-PDU. ⌋ (SRS_Com_02037) 

Transmission deadline monitoring should only be configured in the AUTOSAR COM module for busses that support the generation of transmit confirmations. Otherwise, the transmission deadline monitoring would always notify a transmission error. 

**[SWS_Com_00878]** ⌈ The AUTOSAR COM shall start a configured transmission deadline monitoring timer of a signal (group) if it is sent (within an I-PDU) to the lower layer, unless the timer is already running. ⌋ (SRS_Com_02037) 

SWS_Com_00878 does not consider a potential return code, thus the timer is started even if the sent request fails immediately. 

Document ID 015: AUTOSAR_SWS_COM 

55 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



If the timer is already running a new send request does not reset or restart a running timer, but the currently outstanding send request is monitored further on. Unless otherwise specified, the timer is started regardless of the trigger that lead to a potential I-PDU send request. Such triggers are for example a cyclic send request of a signal, a Transmission Mode Switch, or an explicit I-PDU sent request via Com_TriggerIPduSend. 

**[SWS_Com_00879]** ⌈ The transmission deadline monitoring timer shall be started with the configured ComFirstTimeout value if the timer is started for the first time after a (re-)start of the transmission deadline monitoring service for this I-PDU, otherwise the timer shall be started with ComTimeout value. ⌋ (SRS_Com_02037) 

**[SWS_Com_00880]** ⌈ When the AUTOSAR COM receives a transmit confirmation for an I-PDU, it shall cancel all running transmission deadline monitoring timers for all contained signals and signal groups. ⌋ (SRS_Com_02037) 

**[SWS_Com_00696]** ⌈ In case transmission deadline monitoring is configured for an I-PDU with transmission mode _NONE_ only, the AUTOSAR COM module shall start the transmission deadline monitoring timer for this I-PDU upon the start of the I-PDU group to which the I-PDU belongs to. ⌋ (SRS_Com_02037) 

**[SWS_Com_00835]** ⌈ In case transmission deadline monitoring is configured for an I-PDU with transmission mode _NONE_ and another transmission mode, the transmission deadline monitoring shall be disabled whenever the transmission mode _NONE_ is active. ⌋ (SRS_Com_02037) 

**[SWS_Com_00697]** ⌈ In case transmission deadline monitoring is configured for an I-PDU with transmission mode _NONE_ only, the AUTOSAR COM module shall reset the transmission deadline monitoring timer for this I-PDU when a successful transmit confirmation is received. ⌋ (SRS_Com_02037) 

In case of a signal group, it is only possible to configure transmission deadline monitoring for the whole signal group and not for group signals, see ECUC_Com_00345 and ECUC_Com_00520. 

**[SWS_Com_00708]** ⌈ In case the transmission deadline monitoring timer expires for an I-PDU with ComIPduCancellationSupport configured to _TRUE_ , the AUTOSAR COM module shall invoke PduR_ComCancelTransmit for that I-PDU. ⌋ (SRS_Com_02107) 

The invocation of PduR_ComCancelTransmit is done in addition to the normal timeout handling of Com, which notifies the SW-C, if configured. The AUTOSAR COM ignores the return code of PduR_ComCancelTransmit. 

**[SWS_Com_00304]** ⌈ When a transmission deadline monitoring timer elapses, that is there was no successful transmit confirmation for an I-PDU in time,  the AUTOSAR COM module shall notify the RTE by invoking all configured ComTimeoutNotifications for contained signals or signal groups, see ECUC_Com_00552. ⌋ (SRS_Com_02037) 

Document ID 015: AUTOSAR_SWS_COM – AUTOSAR confidential – 

56 of 185 

Specification of Communication AUTOSAR CP Release 4.4.0 



If the transmission deadline monitoring timer runs out, there will be a timeout notification regardless of the reason. For example, the notification will even take place, if the transmission was filtered out by an I-PDU callout. 

### 7.3.6.2.1 **Transmission Deadline Monitoring with N-Times Transmission Mode** 

As defined in [17] the monitoring timer has to be started upon completion of a call to Com_SendSignal or Com_SendSignalGroup respectively if transmission deadline monitoring is configured for the corresponding signal or signal group respectively. 

For the transmission mode _DIRECT_ and _MIXED,_ it should be ensured that all ComTxModeNumberOfRepetitions requests could be made within the configured period (see Chapter 7.3.3.4). 

As defined in [17], if the monitoring timer expires the RTE is notified with the configured notification mechanism about that failure. 

**[SWS_Com_00308]** ⌈ For an I-PDU with ComTxModeMode _DIRECT_ and ComTxModeNumberOfRepetitions > 0, the AUTOSAR COM module shall cancel the transmission deadline monitoring timer after _ComTxModeNumberOfRepetitions plus one_ successfully received transmit confirmations. ⌋ (SRS_Com_02083) 

If the timer is cancelled after _ComTxModeNumberOfRepetitions plus one_ confirmations, the transmission was successful and then the transmission confirmation is sent to the RTE. See also SWS_Com_00305. 

**[SWS_Com_00739]** ⌈ For an I-PDU with ComTxModeMode DIRECT and ComTxModeNumberOfRepetitions > 0, the AUTOSAR COM module shall reset an already running transmission deadline monitoring timer in case another send request for this I-PDU is initiated. ⌋ (SRS_Com_02083) 

### **7.3.7 Notification handling** 

The AUTOSAR COM inherits the notification classes 1,2,3 and 4 of [17]. The notifications are configurable via ComNotification and the definitions of the callbacks are given in Chapter 8.6.3.1. 

**[SWS_Com_00883]** ⌈ If a ComNotification is configured for a signal or signal group, the AUTOSAR COM shall indicate each successful transmission via the configured notification. ⌋ (SRS_Com_02046) 

For example, for periodic transmissions each successful periodic transmission is notified. Note that for n-times transmission multiple transmissions on the bus are necessary before it is considered as successful, see also SWS_Com_00305. 

Document ID 015: AUTOSAR_SWS_COM 

57 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



## **7.4 Signal Groups - Complex Data Types** 

To support the AUTOSAR concept of complex data types the AUTOSAR COM module provides signal groups. The AUTOSAR COM module transmits and receives signal groups consistently to provide the necessary consistency for complex data types. 

Signal groups can be configured statically. For each signal group a symbolic name can be configured. See ECUC_Com_00345 for the configuration details. 

The AUTOSAR COM module achieves the consistency of a signal group by means of a shadow buffer mechanism, i.e. the RTE accesses the group signals in the shadow buffer. If the shadow buffer needs to be synchronized with the I-PDU, the RTE can trigger this explicitly with Com_SendSignalGroup or Com_ReceiveSignalGroup. The synchronization is performed atomically. 

An alternative approach to signal group consistency is to enable the signal group array APIs Com_SendSignalGroupArray (SWS_Com_00851) and Com_ReceiveSignalGroupArray (SWS_Com_00854). The deviations of this approach are described in Chapter 7.4.6. 

### **7.4.1 Initialization** 

**[SWS_Com_00484]** ⌈ By a call to Com_Init, the AUTOSAR COM module shall initialize the shadow buffer of a signal group on sender-side. ⌋ (SRS_BSW_00101) 

Since it is not suspected that a well-formed SWC tries to read a group signal before a call to Com_ReceiveSignalGroup, SWS_Com_00484 applies to the sender side only. 

### **7.4.2 Transmission** 

If Com_SendSignal or Com_InvalidateSignal is called for a signal that belongs to a signal group, then the AUTOSAR COM will only update the shadow buffer of this signal group. There is no need for any further I-PDU processing like TMS evaluation, unless the I-PDU contents changed. 

**[SWS_Com_00050]** ⌈ If Com_SendSignalGroup is called for the signal group, the AUTOSAR COM module shall copy the shadow buffer atomically to the I-PDU buffer. ⌋ (SRS_Com_02041) 

Document ID 015: AUTOSAR_SWS_COM 

58 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



Example with two group signals signal_a and signal_b, which belong to group_x: 

/* copy a to shadow buffer */ Com_SendSignal (signal_a, &a); 

/* copy b to shadow buffer */ Com_SendSignal (signal_b, &b); 

/* copy shadow buffer to I-PDU */ Com_SendSignalGroup (group_x); 

### **7.4.3 Reception** 

A group signal can be received from the shadow buffer by calling the function Com_ReceiveSignal after the signal group data has been copied to the shadow buffer by Com_ReceiveSignalGroup. 

**[SWS_Com_00051]** ⌈ If Com_ReceiveSignalGroup is called for a signal group, the AUTOSAR COM module shall copy the data atomically from the I-PDU buffer to the shadow buffer. ⌋ (SRS_Com_02041) 

Example with two group signals signal_a and signal_b, which belong to group_x: 

/* copy I-PDU to shadow buffer */ Com_ReceiveSignalGroup (group_x); 

/* copy a from shadow buffer */ Com_ReceiveSignal (signal_a, &a); 

/* copy b from shadow buffer */ Com_ReceiveSignal (signal_b, &b); 

### **7.4.4 Notifications** 

Table 5 shows that all notification functions are only configurable for signal groups but not for individual group signals. Chapter 7.3 defines the functional logic of the notification methods for signals and signal groups. The prototypes for the configurable notification functions are defined in Chapter 8.6.3.1. 

Document ID 015: AUTOSAR_SWS_COM 

59 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **7.4.5 Attributes of a Signal Group** 

Table 5 gives an overview of the attributes of a signal group: 

|**_Attribute_**|**_Pergroup signal_**|**_Per signalgroup_**|
|---|---|---|
|Update-bit|No|Yes, associated on the whole<br>group (see Chapter 7.8)|
|Signal Notification (sender<br>side)|No|Yes|
|Signal Notification (receiver<br>side)|No|Yes|
|Error Notification (sender<br>side)|No|Yes|
|Timeout Notification (sender<br>side)|No|Yes|
|Timeout Notification (receiver<br>side)|No|Yes|
|Invalid Notification (receiver<br>side)|No|Yes|
|Data access (receiverside)|Yes|Yes, see SWS_Com_00201|
|Data access (sender side)|Yes|Yes, see SWS_Com_00200,<br>SWS_Com_00557|
|DataFiltering (receiverside)|Yes, see Chapter 7.2.4|No|
|DataFiltering (senderside)|No|No|
|TMS on sender side|Each signal, according to TMS<br>selection definition.<br>(see Chapter 7.3.3.2)|No|



**Table 5: Attributes of signal groups** 

### **7.4.6 UINT8-array based access to signal groups** 

An alternative approach to signal group consistency is to enable the signal group array APIs Com_SendSignalGroupArray (SWS_Com_00851) and Com_ReceiveSignalGroupArray (SWS_Com_00854) via the COM configuration parameter ComSignalGroupArrayAccess (ECUC_Com_10003). The serialization of the composite data is then done outside of the COM module but resulting in the same layout as COM would use to place the group signals in the I-PDU. 

In this approach, no shadow buffer is used. The serialized data is directly provided to the COM module as a uint8-array representation of the signal group. 

**[SWS_Com_00841]** ⌈ The UINT8-array based access to signal groups shall only be used if the following preconditions apply: 

   - uses only fix sized data types for the composite data 

   - signal groups, which are mapped byte aligned to the I-PDU 

   - signal groups, which are not intermitted by other signals (but may contain gaps) 

- ⌋ (SRS_Com_02112) 

[ **SWS_Com_00842** ] ⌈ In case a signal group has ComSignalGroupArrayAccess (ECUC_Com_10003) defined, no shadow buffer shall be allocated for that signal group. ⌋ (SRS_Com_02112) 

Document ID 015: AUTOSAR_SWS_COM 

60 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00843]** ⌈ In case a signal group has ComSignalGroupArrayAccess (ECUC_Com_10003) defined, the call to the following APIs is not supported for that signal group: 

   - Com_SendSignal and Com_ReceiveSignal for any of the group signals of that signal group 

- Com_SendSignalGroup and Com_ReceiveSignalGroup for that signal group 

- ⌋ (SRS_Com_02112) 

The above requirement defines that certain APIs are not supported for signal groups with array access. That is, these APIs must not be called for signal groups with array access. If they are called illegally, the behavior is undefined. 

Since the signal group is provided in the uint8-array representation, reception filtering and transmission mode selection needs to cope with this data representation when evaluating the group signals. 

In order to ease the filter evaluation only a subset of the filters from SWS_Com_00602 is supported. 

For signal group array access the following two filters are excluded from reception filtering and Transmission Mode Selection: 

- _NEW_IS_WITHIN_ 

- _NEW_IS_OUTSIDE_ 

**[SWS_Com_00848]** ⌈ The signal group array processing functions Com_SendSignalGroupArray and Com_ReceiveSignalGroupArray shall support the following filters for reception filtering and Transmission Mode Selection: 

- _ALWAYS_ 

- _NEVER_ 

- _MASKED_NEW_EQUALS_X_ 

- _MASKED_NEW_DIFFERS_X_ 

- _MASKED_NEW_DIFFERS_MASKED_OLD_ 

- _ONE_EVERY_N_ 

⌋ (SRS_Com_02112) 

### **7.4.6.1 Basic functionality** 

In case the AUTOSAR Transformer approach is used the serialization and further data processing is already done in the transformer chain. Since the transformer chain already deals with a uint8-array representation of the communication data, the uint8array based access to signal groups allows to use the already serialized data and to place it into the I-PDU without the need for COM to serialize the data again. 

The AUTOSAR System Template [12] defines which signal group shall be handled in the uint8-array based approach. If the System Template enables the uint8-array based approach the Ecu configuration parameter ComSignalGroupArrayAccess (ECUC_Com_10003) is set to true. 

Document ID 015: AUTOSAR_SWS_COM 

61 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00844]** ⌈ The start position of the uint8-array representation of the communication data shall be the byte offset of the group signal in this signal group with the smallest ComBitPosition. ⌋ (SRS_Com_02112) 

**[SWS_Com_00845]** ⌈ The length of the uint8-array representation of the communication data shall be the number of bytes which all the ComGroupSignals in this ComSignalGroup occupy in the ComIPdu. ⌋ (SRS_Com_02112) 

### **7.4.6.2 Initialization** 

**[SWS_Com_00850]** ⌈ By a call to Com_Init, the AUTOSAR COM module shall initialize the respective I-PDU buffer section of a signal group, that has ComSignalGroupArrayAccess (ECUC_Com_10003) configured _true_ , based on the ComSignalInitValue of all included ComGroupSignals. ⌋ (SRS_Com_02112, SRS_BSW_00101) 

### **7.4.6.3 Transmission** 

**[SWS_Com_00846]** ⌈ When Com_SendSignalGroupArray is called a data pointer to the uint8-array representation of the signal group is provided. The AUTOSAR COM module shall copy the data into the I-PDU based on the start position defined in SWS_Com_00844 and the size defined in SWS_Com_00845. ⌋ (SRS_Com_02112) 

**[SWS_Com_00847]** ⌈ The AUTOSAR COM module shall handle a call of Com_SendSignalGroupArray equally to Com_SendSignalGroup with respect to 

- Chapter 7.3.3.1.2 Signal Groups (Transfer Properties and I-PDU Transmission Mode) 

- Chapter 7.3.3.2 Selection of the Transmission Mode for one specific I-PDU 

- Chapter 7.3.3.3 Signal Flow and Transmission Mode Selection 

⌋ (SRS_Com_02112) 

### **7.4.6.4 Reception** 

**[SWS_Com_00849]** ⌈ When Com_ReceiveSignalGroupArray is called a data pointer to the uint8-array representation of the signal group is provided. The AUTOSAR COM module shall copy the data to the data pointer position of the I-PDU based on the start position defined in SWS_Com_00844 and the size defined in SWS_Com_00845. ⌋ (SRS_Com_02112) 

## **7.5 Large Data Types** 

A **_large signal_** is a signal that is too large to fit into a single L-PDU of the underlying communication protocol. For example, a large signal on CAN would exceed 8 bytes or 64 bytes for CAN FD. For FlexRay the situation is more complex, since one frame can contain several I-PDUs. Hence, a signal may be a large signal for FlexRay even if it does not exceed the size of a FlexRay frame. 

Document ID 015: AUTOSAR_SWS_COM 

62 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



Large signals in AUTOSAR require configuring a **_large I-PDU_** that will be transmitted via the transport protocol of the underlying bus. It is not imperative that a large I-PDU contains one or more large signals. 

Using this concept the I-PDU length and hence the signal size will is limited according to the bus-specific transport protocol, see ECUC_Com_00437. 

UINT8_N is the only signal type that supports signals of a static size larger than 8 bytes. For dynamic length signals see Chapter 7.6. 

Since the AUTOSAR COM module is not aware of the underlying bus properties, it has to be configured if an I-PDU can be transmitted within a single L-PDU, e.g. one CAN frame, or if it needs to be transmitted via TP, see also ECUC_Com_00761. 

The AUTOSAR COM module is not able to prevent or to detect if too large I-PDUs are sent to a specific bus transport protocol, because the AUTOSAR COM module uses the bus-independent PDU Router interface. However, the AUTOSAR COM module allows that the maximum length of the N-SDU of the underlying TPs can be used and therefore the AUTOSAR COM module does not introduce any additional length restrictions. 

### **7.5.1 Transmission of Large Signals/ I-PDUs** 

The AUTOSAR COM module sends large I-PDUs via the generic PduR APIs for upper layer modules that use transport protocol. For details of the AUTOSAR COM module – PDU Router interface see Chapter 7.7. According to [10] the call-sequence is: 

- PduR_ComTransmit: for initiating the send request 

- one or more callbacks to Com_CopyTxData: for copying the data 

- callback to Com_TpTxConfirmation: for confirming the transmission 

**[SWS_Com_00662]** ⌈ After successful initiation of a transmission of a large I-PDU via PduR_ComTransmit, the AUTOSAR COM module shall not modify the data of its internal transmit buffer of this I-PDU unless the AUTOSAR COM module is notified about either the successful transmission or an error indicating that the transmission was aborted. ⌋ (SRS_Com_02095) 

The I-PDUs within the AUTOSAR COM module are statically configured. Therefore, the complete memory of the I-PDU, even for very large I-PDUs, will be allocated. This approach was taken in order to reduce the complexity of the large data type handling. 

If the utilized transportation protocol is also used for diagnosis, or other services, it must support multiple users. This is at least supported by CAN TP and FlexRay TP. 

**[SWS_Com_00863]** ⌈ In case a large I-PDU is currently transmitted and the same I-PDU is triggered for transmission again, the AUTOSAR COM shall skip the additionally send request and report the runtime error COM_E_SKIPPED_TRANSMISSION. ⌋ (SRS_Com_02095) 

Document ID 015: AUTOSAR_SWS_COM 

63 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



This could for example happen in case a large I-PDU is sent out periodically and the transmission is delayed over the next cycle. 

### **7.5.2 Reception of Large Signals/ I-PDUs** 

The AUTOSAR COM module receives large I-PDUs via the generic PDU Router’s APIs for upper layer modules that use transport protocol. For details of the AUTOSAR COM module – PDU Router interface see Chapter 7.8. According to [10] the call-sequence is: 

- call to Com_StartOfReception: for initiating the RX request 

- one or more callbacks to Com_CopyRxData: copying the receive data to the AUTOSAR COM module’s internal receive buffer 

- call to Com_TpRxIndication: indicating the correct, or incorrect, end of the reception process 

**[SWS_Com_00838]** ⌈ In case Com_TpRxIndication is called with value E_NOT_OK for the parameter result, the AUTOSAR COM module shall treat all signals of the received large I-PDU exactly like invalidated signals. That is, the AUTOSAR COM module shall execute all configured ComDataInvalidActions for all included signals and signal groups. ⌋ (SRS_Com_02095) 

When receiving large I-PDUs the internal I-PDU buffer is overwritten gradually. Thus, unless the old signal is not stored somewhere else (for example in a shadow buffer of a signal group), the COM module runs the risk to lose signal data information that might be needed in certain scenarios, for example: 

- receiving a signal with an unset update-bit 

- providing the last value in case the RX-filter is not passed 

- providing the last value in case there is only an invalid notification (but no replacement) is defined and the invalid value is received 

**[SWS_Com_00882]** ⌈ If the AUTOSAR COM module receives signals via large I- PDUs and these signals have features configured that need to keep the old value in certain cases, the AUTOSAR COM module shall correctly provide the old value for signals received via a large I-PDU in the same way as for signals received via normal I-PDUs. ⌋ (SRS_Com_02041) 

It is open to the implementation to find efficient means for providing the old values and to derive from the configuration, which signals or I-PDUs need an additional handling (e.g. buffering). 

This does not mean it is necessary to implement a queue. 

## **7.6 Dynamic Length Signals** 

A **_dynamic length signal_** is a signal which length can vary at run-time. The maximal length of a dynamic length signal needs to be specified at configuration time. A dynamic length signal has to be transmitted in a **_dynamic length I-PDU_** . 

Document ID 015: AUTOSAR_SWS_COM 

64 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00753]** ⌈ For dynamic length signals, the AUTOSAR COM module shall only support the ComSignalType _UINT8_DYN_ . ⌋ (SRS_Com_02094, SRS_Com_02098) 

Restricting the type to a UINT8-array type also restricts the placement of the dynamic length signal to byte boundaries. 

All other signals, potentially including large signals, must be packed in front of the dynamic length signal (see SWS_Com_00754, SWS_Com_00755 and SWS_Com_00756). Therefore, it is not required to encode the length of the dynamic length signal within the I-PDU. On receiver side, the length of the dynamic length signal can be calculated from the length of the received I-PDU. 

It is allowed to configure an update-bit for a dynamic length signal. In this case, the update-bit must be located in front of the dynamic length signal, see also SWS_Com_00755. 

There is no restriction in the AUTOSAR COM module preventing the usage of signal groups in combination with large or dynamic length signals. 

Dynamic length signals are not restricted to be sent via transport protocol. However, the maximum length of the I-PDU containing the dynamic length signal must respect the bus-specifc restrictions. 

In case of I-PDUs with dynamic length signals that shall be sent via CAN FD it is recommended to use the Multi PDU Mapping feature of the IpduM. This avoids misinterpretation of the received length due to the discrete data lengths of CAN FD frames. 

### **7.6.1 Transmission of Dynamic Length Signals/ I-PDUs** 

For sending a dynamic length signal, the RTE needs to specify the actual length at the send call. The corresponding API is Com_SendDynSignal (SWS_Com_00627). 

**[SWS_Com_00757]** ⌈ At a call to Com_SendDynSignal, the AUTOSAR COM module shall set the length of the corresponding dynamic length I-PDU to the smallest length that includes the dynamic length signal. The length of the dynamic signal shall be equal to the value of input parameter “Length” passed in the API Com_SendDynSignal. ⌋ (SRS_Com_02093) 

The AUTOSAR COM module is able to send dynamic length I-PDUs via normal or large I-PDUs. In any case, it needs to pass the length of the dynamic I-PDU to the lower layers. 

**[SWS_Com_00832]** ⌈ When the AUTOSAR COM module invokes PduR_ComTransmit for a dynamic length I-PDU, the SduLength of the PduInfoType shall be set according the last update (or init value if not yet sent) of the included dynamic length signal. ⌋ (SRS_Com_02093) 

Document ID 015: AUTOSAR_SWS_COM 

65 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **7.6.2 Reception of Dynamic Length Signals/ I-PDUs** 

For receiving a dynamic length signal, the RTE needs to be informed about the actual size. 

**[SWS_Com_00758]** ⌈ At reception of a dynamic length I-PDU, the AUTOSAR COM module shall calculate the length of the contained dynamic length signal, by: <dynamic signal length in bytes> = <received I-PDU length in bytes> - <ComBitPosition of dynamic length signal> / 8 

⌋ (SRS_Com_02093) 

Com_ReceiveDynSignal (SWS_Com_00690) returns the length of a dynamic length signal, calculated as defined by SWS_Com_00758. 

Since, the length of a dynamic length signal is derived from the received length of the I-PDU, the AUTOSAR COM module does not support the combination of dynamic length I-PDUs and I-PDUs with metadata, see SWS_Com_00817. 

## **7.7 Interface between AUTOSAR COM Module and the PDU Router** 

[17] leaves the interface between COM and the lower layers undefined. In AUTOSAR, the only lower layer that the AUTOSAR COM module interfaces to is the PDU Router. 

The AUTOSAR COM module uses the PDU Router in two different modes, depending on the type of the I-PDU it will be transported with the bus-specific transport protocol or without. If an I-PDU is supposed to be sent via TP, is configured per configuration parameter ComIPduType. 

**[SWS_Com_00138]** ⌈ The AUTOSAR COM module shall send out I-PDUs by a calling the PduR_ComTransmit function. ⌋ (SRS_Com_02037) 

**[SWS_Com_00759]** ⌈ If the AUTOSAR COM module sends out an I-PDU with ComIPduType configured to _NORMAL_ , the AUTOSAR COM module shall expect to be called by the PDU Router using Com's interfaces for modules that do not use TP. See column _normal I-PDUs_ in **Table 6** . ⌋ (SRS_Com_02096) 

**[SWS_Com_00760]** ⌈ If the AUTOSAR COM module sends out an I-PDU with ComIPduType configured to _TP_ , the AUTOSAR COM module shall expect to be called by the PDU Router using Com's interfaces for modules that use TP. See column _TP I-_ PDUs in **Table 6** . ⌋ (SRS_Com_02096) 

The interaction diagram in Chapter 9.1 shows the interaction between the PDU Router module and the AUTOSAR COM module for normal I-PDUs. 

**Table 6** gives an overview, which API between the AUTOSAR COM module and the PDU Router is used for a concrete I-PDU with respect to the configured value of ComIPduType. The API description itself is specified in Chapter 8. 

Document ID 015: AUTOSAR_SWS_COM 

66 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_API_**|**_normal I-PDUs_**|**_TP I-PDUs_**|
|---|---|---|
|PduR_ComTransmit|**X**|**X**|
|Com_TxConfirmation|**X**|**-**|
|Com_RxIndication|**X**|**-**|
|Com_TriggerTransmit|**X**|**-**|
|Com_TpTxConfirmation|**-**|**X**|
|Com_TpRxIndication|**-**|**X**|
|Com_StartOfReception|**-**|**X**|
|Com_CopyRxData|**-**|**X**|
|Com_CopyTxData|**-**|**X**|



**Table 6: API to PDU Router with respect to ComIPduType** 

## **7.8 Update-Bits** 

To enable the receiver of a signal/ signal group to identify whether the sender has updated the data in this signal/ signal group before sending, the AUTOSAR COM module supports _update-bits_ . 

The update-bits indicate whether the RTE on sender-side has updated a signal value, before the I-PDU, containing that signal, was transmitted to the PDU Router. 

Update-bits are not allowed if transmission mode _DIRECT_ is used with ComTxModeNumberOfRepetitions greater or equal 1 (see SWS_Com_00310). 

By configuration on sender- and on receiver-side, it is possible to add separately for each signal and/or separately for each signal group at most one update-bit. The position of the update-bit is configurable by configuration parameter ComUpdateBitPosition (ECUC_Com_00257). ComUpdateBitPosition is included within the configuration container ComSignal. Hence, it is ensured that the signal/ signal group and the corresponding update-bit are always part of the same I-PDU. 

**[SWS_Com_00055]** ⌈ The AUTOSAR COM module shall handle the update-bit only internally and not as part of the signal or signal group. ⌋ (SRS_Com_02030) 

The update-bits are not directly visible or accessible by AUTOSAR Software Components. 

**[SWS_Com_00059]** ⌈ The AUTOSAR COM module shall interpret the update-bit as defined in Table 7. ⌋ (SRS_BSW_00101, SRS_Com_02030) 

|**_Update-BIT_**||
|---|---|
|0<br>cleared/ data|hasnot beenupdated|
|1<br>set/ data has|been updated|



**Table 7 update-bit interpretation** 

### **7.8.1 Sender Side** 

The initialization of update-bits is defined by SWS_Com_00117. 

Document ID 015: AUTOSAR_SWS_COM 

67 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00061]** ⌈ If the RTE updates the value of a signal by calling Com_SendSignal, the AUTOSAR COM module shall set the update-bit of this signal. ⌋ (SRS_Com_02030) 

**[SWS_Com_00801]** ⌈ If the RTE updates a signal group by calling Com_SendSignalGroup, the AUTOSAR COM module shall set the update-bit of this signal group. ⌋ (SRS_Com_02030) 

**[SWS_Com_00062]** ⌈ If the parameter ComTxIPduClearUpdateBit of an I-PDU is configured to _Transmit_ , the AUTOSAR COM module shall clear all update-bits of all contained signals and signal groups after this I-PDU was sent out via PduR_ComTransmit and PduR_ComTransmit returned E_OK. ⌋ (SRS_Com_02030) 

**[SWS_Com_00577]** ⌈ If the parameter ComTxIPduClearUpdateBit of an I-PDU is configured to Confirmation, the AUTOSAR COM module shall clear all update-bits of all contained signals and signal groups after this I-PDU was sent out via PduR_ComTransmit, PduR_ComTransmit returned E_OK and the I-PDU was successfully confirmed. ⌋ (SRS_Com_02030) 

**[SWS_Com_00578]** ⌈ If the parameter ComTxIPduClearUpdateBit of an I-PDU is configured to _TriggerTransmit_ , the AUTOSAR COM module shall clear all update-bits of all contained signals and signal groups after the contents of this I-PDU was successfully requested by Com_TriggerTransmit. ⌋ (SRS_Com_02030) 

### **7.8.2 Receiver Side** 

**[SWS_Com_00324]** ⌈ If a signal or signal group with an attached update bit is received, the AUTOSAR COM module shall only process this signal, i.e. filter, notification, signal based gateway, byte swapping, if the signal’s update bit is set. ⌋ (SRS_Com_02030) 

**[SWS_Com_00802]** ⌈ If a signal or signal group with an attached update bit is received and the update-bit is not set, the AUTOSAR COM module shall discard this signal. ⌋ (SRS_Com_02030) 

If the signal has not been updated, the signal will not be routed via the signal gateway. It will only be discarded. 

If the RTE reads a signal with an associated cleared update-bit, the init value or the last received value is returned. 

**[SWS_Com_00067]** ⌈ The AUTOSAR COM module shall interpret a signal/ signal group as _updated_ if the signal has an update-bit attached, and the value of the update-bit is set. ⌋ (SRS_Com_02030) 

For the behavior of reception deadline monitoring on signals with update-bits, see Chapter 7.3.6.1. 

Document ID 015: AUTOSAR_SWS_COM 

68 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



## **7.9 Data Sequence Control** 

The AUTOSAR COM module provides mechanisms of data sequence control in the form of I-PDU Counters. _Out of sequence_ I-PDUs, those are repeated I-PDUs or I-PDUs received after missing I-PDUs, will be detected and discarded. 

I-PDU counters are optional and can be configured per I-PDU. For the corresponding configuration container see ECUC_Com_00592. 

### **7.9.1 Sender Side** 

**[SWS_Com_00687]** ⌈ For all I-PDUs with ComIPduDirection configured to _SEND_ that have a configured ComIPduCounter, the AUTOSAR COM module shall set the I-PDU counter to 0, after the I-PDU was initialized by Com_Init or reinitialized by Com_IpduGroupStart. ⌋ (SRS_Com_02101) 

**[SWS_Com_00688]** ⌈ The AUTOSAR COM module shall increase the I-PDU counter of an I-PDU by one, with respect to counter wrap around, directly before the I-PDU is sent out by PduR_ComTransmit. In case the return value of PduR_ComTransmit is not equal to E_OK the update of the I-PDU counter shall be revoked (by decrementing the I-PDU counter by one). ⌋ (SRS_Com_02101) 

If Com_TriggerTransmit fetches an I-PDU containing an I-PDU counter, no incrementation takes place. Hence, care must be taken if I-PDU counters are used on combination with Com_TriggerTransmit. If Com_TriggerTransmit is called multiple times after the corresponding PduR_ComTransmit all I-PDUs will contain the same counter value. Thus, a deferred TriggerTransmit transmission can work, but a pure lower layer driven TriggerTransmit use-case would not work in combination with an I-PDU counter. 

### **7.9.2 Receiver Side** 

**[SWS_Com_00587]** ⌈ For all I-PDUs with ComIPduDirection configured to _RECEIVE_ that have a configured ComIPduCounter, the AUTOSAR COM module shall accept any incoming I-PDU, regardless of the value of the I-PDU counter, after the I-PDU was initialized by Com_Init or reinitialized by Com_IpduGroupStart. ⌋ (SRS_Com_02099) 

**[SWS_Com_00588]** ⌈ At reception of an I-PDU containing an I-PDU counter, the AUTOSAR COM module shall set the next expected value to the value following the received value with respect to counter wrap-around. ⌋ (SRS_Com_02101) 

**Example:** If the I-PDU counter has 4 bits its possible values are 0 – 15. If an I-PDU with a 4-bit sized counter is received and the received counter value is 15 the next expected value is 0. The new expected value needs to be updated regardless if the received value matches the actual expected value or not. 

**[SWS_Com_00590]** ⌈ At reception of an I-PDU containing an I-PDU counter, the AUTOSAR COM module shall discard the I-PDU, after setting the next expected value 

Document ID 015: AUTOSAR_SWS_COM 

69 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



as defined in SWS_Com_00588, if no I-PDU replication for this I-PDU is configured and: 

received I-PDU counter < expected I-PDU counter OR 

received I-PDU counter > expected I-PDU counter + ComIPduCounterThreshold 

with respect to counter wrap-around. ⌋ (SRS_Com_02102) 

**[SWS_Com_00727]** ⌈ In case a mismatch of the expected and the received I-PDU counter is detected, the AUTOSAR COM module shall notify this mismatch by the configured ComIPduCounterErrorNotification (ECUC_Com_00003) notification function. ⌋ (SRS_Com_02102) 

The counter error notification is triggered indepently of the configured ComIPduCounterThreshold. 

The signature of this I-PDU counter error notification function is defined in SWS_Com_00726. 

**Example:** In the example in Table 8, the I-PDU counter is 4-bit wide (values 0-15) and ComIPduCounterThreshold is configured to 1: 

|**_Expected I-PDU counter_**|**_Received counter valu_**|**_e_**<br>**_Action_**|
|---|---|---|
|**_6_**|**_6_**|**_normal reception _**|
|**_6_**|**_7_**|**_normal reception _**|
|**_6_**|**_8_**|**_discarded_**|
|**_6_**|**_1_**|**_discarded_**|
|**_15_**|**_15_**|**_normal reception _**|
|**_15_**|**_0_**|**_normal reception _**|
|**_15_**|**_1_**|**_discarded_**|



**Table 8 Example I-PDU counter handling** 

## **7.10 Communication Protection** 

Safety related I-PDUs might need to be replicated in multiple L-PDUs in order to prevent corruption and loss of data. In AUTOSAR the replication of I-PDUs is realized by the PDU Router. The comparison and voting of replicated I-PDUs is performed in AUTOSAR COM. Since the replicated I-PDUs have no checksum or signature for comparison it is needed to store and compare the complete I-PDUs at the receiver. The AUTOSAR COM allows configuring two additional replicated I-PDUs via ComIPduReplicaRef (ECUC_Com_00601). 

The number of successfully equally received I-PDUs needed for a qualified reception can be configured via ComIPduReplicationQuorum (ECUC_Com_00600) from 1 to 3. The PDU Router module does not support 1:n routing of I-PDUs which are sent or received via a TP module and require multiple frames for transmission. Hence, the AUTOSAR COM stack does currently not support replication of large or dynamic I-PDUs or data types. 

Document ID 015: AUTOSAR_SWS_COM 

70 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **7.10.1 Sender Side** 

Since the replication itself is done by the PduR, there is no special handling on sender side for AUTOSAR COM. However, it must be ensured that replicated I-PDUs have configured an I-PDU counter, see SWS_Com_00834. This is required since the voting at the receiver relies on the I-PDU counter. 

### **7.10.2 Receiver Side** 

At receiver side, the AUTOSAR COM module performs a voting about the multiple replicated I-PDUs. The AUTOSAR COM module passes only signals of successfully confirmed I-PDUs to the RTE. As stated above replicated I-PDUs need to have an I-PDU counter configured. However, the ComIPduCounterThreshold must be configured to 0, see ECUC_Com_00595. There is no use-case of mixing these two features and the voting would be more complex. 

**[SWS_Com_00596]** ⌈ Only when the AUTOSAR COM module has received at least _ComIPduReplicationQuorum_ identical copies of a replicated I-PDU, it shall provide the signals and/ or signal groups out of this I-PDU to the RTE. ⌋ (SRS_Com_02103, SRS_Com_02105, SRS_Com_02106) 

A replicated I-PDU is configured as a normal I-PDU within the AUTOSAR COM module’s configuration. The fan-out on sender-side is configured within the PduR configuration. On reception-side, additionally up to two replicas of PDU-R PDUs (see ECUC_Com_00601 ComIPduReplicaRef) and the necessary number of identically received I-PDUs for successfully voting (see ECUC_Com_00600 ComIPduReplicationQuorum) can be configured within the AUTOSAR COM module’s configuration. 

**[SWS_Com_00597]** ⌈ When the AUTOSAR COM module has received at least _ComIPduReplicationQuorum_ identical copies of a replicated I-PDU, it shall notify the RTE only once with respect to the signals and/or signal groups out of this I-PDU. ⌋ (SRS_Com_02103, SRS_Com_02105, SRS_Com_02106) 

The I-PDU counter will be handled for each replicated I-PDU separately as defined in Chapter 7.9. 

Since the I-PDUs do not contain a special checksum, it is expected, that the comparison is performed by comparing the complete I-PDU byte by byte. 

For I-PDU replication, the ComIPduCounterThreshold needs to be configured to 0, see SWS_Com_00834. Hence, _ComIPduReplicaRef + 1_ buffers are sufficient to store the I-PDUs for a successful voting. 

### **7.10.3 Constraints** 

Due to the approach of reusing already existing functionality, that is using the PduR for the fan out, care must be taken to set up the system correctly. The PduR allows fanning out the replicated I-PDUs on different busses. On the receiver side, these I-PDUs are indicated to COM with the same I-PDU id. However, Com_RxIndication 

Document ID 015: AUTOSAR_SWS_COM 

71 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



(SWS_Com_00123) may not be called reentrant for the same I-PDU id. An easy way to prevent this is to ensure that all I-PDUs are received by the same Interface module, which results in using the same bus for all replicas. For the current AUTOSAR stack, this is the recommend method. However, the system integrator could also synchronize the reception path by other means. 

Furthermore, since there is no mechanism to prevent updates from the upper layer to an I-PDU, this approach of communication protection does not work in combination of decoupled transmission, i.e. I-PDUs requested via Com_TriggerTransmit. 

## **7.11 Signal Gateway** 

The signal gateway is an integrated part of the AUTOSAR COM module. Any external modules, except the cyclic task call, cannot access the signal gateway. 

The AUTOSAR COM module’s signal gateway works with signals and signal groups. 

The AUTOSAR COM module’s signal gateway supports only static routing for the ComGwMapping configuration container (ECUC_Com_00544). It is only possible to configure routes independently of the contents of the routed signals and group signals. 

The destination of a signal or group signal can be configured either per ComGwDestinationDescription container (ECUC_Com_00549), or via ComGwSignal reference (ECUC_Com_00551). The transmission mode will be selected based on the TMCs of other associated signals of the I-PDU. In case no signal contributes to the TMS calculation, the transmission mode ComTxModeTrue (SWS_Com_00677) will be used. 

**[SWS_Com_00377]** ⌈ The AUTOSAR COM module’s signal gateway shall copy the value of routed signals/ group signals to the signals/ group signals for transmission according to configuration, see ECUC_Com_00544. ⌋ (SRS_PduR_06055, SRS_PduR_06089) 

The ComGwMapping configuration allows to configure routing a signal/ group signal from one source signal/ group signal to zero (no signal gateway functionality) or more destinations (1:n). 

The AUTOSAR COM module’s signal gateway does not support to process signals or group signals that are contained within a large I-PDU, see SWS_Com_00598. 

**[SWS_Com_00872]** ⌈ The Signal Gateway shall support the following I-PDU/ signalprocessing stages on the receiver side (see also Figure 5): 

   - 1) reset reception deadline monitoring timer for I-PDU based monitoring 

   - 2) I-PDU callout 

   - 3) check of update–bits 

   - 4) endianness conversion and sign extension 

- ⌋ (SRS_PduR_06055, SRS_PduR_06089) 

Document ID 015: AUTOSAR_SWS_COM 

72 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00873]** ⌈ The Signal Gateway shall support the following I-PDU/ signalprocessing stages on the sender side (see also Figure 5): 

- 1) set of update-bits 

- 2) endianness conversion and sign extension 

- 3) I-PDU transmission mode selection 

- 4) I-PDU callout 

⌋ (SRS_PduR_06055, SRS_PduR_06089) 

### **7.11.1 Dealing with Signals** 

**[SWS_Com_00357]** ⌈ The AUTOSAR COM module shall forward signals to be routed from received I-PDUs to transmit I-PDUs. For configuration, see ECUC_Com_00544 configuration container ComGwMapping. ⌋ (SRS_PduR_06002) 

Stopping the receive I-PDU after the signals to be routed have been forwarded to the transmit I-PDU will not prevent the transmit I-PDU from being transmitted unless it is stopped as well. 

**[SWS_Com_00360]** ⌈ If the endianness of a received signal to be routed differs from the endianness of a related destination signal, the AUTOSAR COM module shall convert its endianness to the endianness of the destination signal. ⌋ (SRS_PduR_06061) 

### **7.11.2 Dealing with Group Signals** 

**[SWS_Com_00361]** ⌈ The AUTOSAR COM module shall forward routed group signals from received I-PDUs to transmit I-PDUs. See also configuration container ComGwMapping (ECUC_Com_00544). ⌋ (SRS_PduR_06002, SRS_PduR_06056, SRS_PduR_06061) 

Stopping the receive I-PDU after the group signals to be routed have been forwarded to the transmit I-PDU will not prevent the transmit I-PDU from being transmitted unless it is stopped as well. 

**[SWS_Com_00383]** ⌈ The AUTOSAR COM module shall route all group signals belonging to the same signal group in a consistent manner. Therefore, the AUTOSAR COM module shall transfer the data of a signal group as one consistent (sub-)set of data during a routing operation. ⌋ (SRS_PduR_06056) 

**[SWS_Com_00735]** ⌈ The AUTOSAR COM module shall support routing consistently a subset of group signals of a source signal group into a reduced target signal group. ⌋ (SRS_PduR_06056) 

**[SWS_Com_00833]** ⌈ The AUTOSAR COM module shall support routing of individual group signals of a source signal group to a individual target signals (which are not part of signal group). ⌋ (SRS_PduR_06056) 

**[SWS_Com_00362]** ⌈ If the endianness of a received group signal to be routed differs from the endianness of a related destination (group) signal, the AUTOSAR COM 

Document ID 015: AUTOSAR_SWS_COM 

73 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



module shall convert its endianness to the endianness of the destination (group) signal. ⌋ (SRS_PduR_06061) 

### **7.11.3 Routing of Out-Timed Signals and Signal Groups** 

**[SWS_Com_00701]** ⌈ The AUTOSAR COM module’s signal gateway shall route signal and group signals even if any configured reception deadline monitoring timeout expired. ⌋ (SRS_PduR_06089) 

In case of a not in time received signal or group signal the AUTOSAR COM module’s signal gateway will route these signal or group signal anyway. 

### **7.11.4 Handling of Update-Bits** 

The routing relations for signal groups are solely defined on the group signals. However, with respect to the update-bit the integrated signal gateway has to respect the update-bits of the enclosing signal groups. Hence, when update-bits of signal groups are referenced within this chapter the signal groups that include the configured group signals are meant. 

**[SWS_Com_00702]** ⌈ If both, the received signal/ signal group and the destination signal/ signal group have an update-bit (ComUpdateBitPosition) configured and the update-bit of the received signal/ signal group is set, the AUTOSAR COM module shall route the signal/ signal group with the set update-bit and clear the update-bit of the destination signal/ signal group after it was sent. ⌋ (SRS_Com_02030) 

**[SWS_Com_00703]** ⌈ If the received signal/ signal group and the destination signal/ signal group have an update-bit (ComUpdateBitPosition) configured, and the updatebit of the received signal/ signal group is not set, the AUTOSAR COM module shall not route this signal/ signal group. ⌋ (SRS_Com_02030) 

**[SWS_Com_00704]** ⌈ If the received signal/ signal group has an update-bit (ComUpdateBitPosition) configured, but the destination signal has no update-bit configured, and the update-bit is set, the AUTOSAR COM module shall route this signal/ signal group without the update-bit. ⌋ (SRS_Com_02030) 

**[SWS_Com_00705]** ⌈ If the received signal/ signal group has an update-bit (ComUpdateBitPosition) configured, but the destination signal has no update-bit configured, and the update-bit is not set, the AUTOSAR COM module shall not route this signal/ signal group. ⌋ (SRS_Com_02030) 

**[SWS_Com_00706]** ⌈ If the received signal/ signal group has no update-bit (ComUpdateBitPosition) configured and the destination signal/ signal group has an update-bit configured, the AUTOSAR COM module shall set the update-bit of the destination signal when a new signal/ signal group was received and clear it after sending of the destination signal/ signal group. ⌋ (SRS_Com_02030) 

Document ID 015: AUTOSAR_SWS_COM 

74 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **7.11.5 Decoupling Signal Gateway** 

To protect interrupt routines used for I-PDU reception from incalculable and perhaps expensive time usage, it is necessary to decouple the AUTOSAR COM module’s signal gateway from interrupt routines. 

**[SWS_Com_00359]** ⌈ The AUTOSAR COM module shall execute all functions of its signal gateway during the function call Com_MainFunctionRouteSignals (SWS_Com_00400). During this function call, the AUTOSAR COM module’s signal gateway shall check received routed signals and group signals and copy them from the related receive I-PDUs to the related transmit I-PDUs. ⌋ (SRS_BSW_00425, SRS_BSW_00432) 

**[SWS_Com_00466]** ⌈ Within Com_MainFunctionRouteSignals, the AUTOSAR COM module shall evaluate the transfer properties and transmission modes and perform its routing actions in the following sequence, see also Figure 2: 

   1. copy all gated signals from the source to the target I-PDUs 

   2. evaluate the TMC of all gated signals 

   3. evaluate the TMS for the target I-PDUs 

- ⌋ (SRS_BSW_00432) 

In the case, that a target I-PDU contains gated signals with ComTransferProperty TRIGGERED that are newly received, the sending may be performed in either Com_MainFunctionTx or Com_MainFunctionRouteSignals. 

**[SWS_Com_00539]** ⌈ The AUTOSAR COM module shall sent out an I-PDU at most once while one call to Com_MainFunctionRouteSignals. ⌋ (SRS_PduR_06055) 

## **7.12 Error Classification** 

### **7.12.1 Development Errors** 

**[SWS_Com_00803]** ⌈ API service called with wrong parameter: 

- error code: COM_E_PARAM  value [hex]: 0x01 

⌋ (SRS_BSW_00337) 

**[SWS_Com_00804]** ⌈ Error code if any API service (except Com_GetStatus, Com_GetVersionInfo, Com_MainFunctionRx, Com_MainFunctionTx and Com_MainFunctionRouteSignals) is called before the AUTOSAR COM module was initialized with Com_Init or after a call to Com_DeInit: 

 error code: COM_E_UNINIT  value [hex]: 0x02 

⌋ (SRS_BSW_00337) 

**[SWS_Com_00805]** ⌈ NULL pointer checking: 

Document ID 015: AUTOSAR_SWS_COM 

75 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



 error code: COM_E_PARAM_POINTER  value [hex]: 0x03 

⌋ (SRS_BSW_00414) 

**[SWS_Com_00837]** ⌈ Invalid configuration set selection: 

- error code: COM_E_INIT_FAILED 

- value [hex]: 

0x04 

- ⌋ (SRS_BSW_00414) 

### **7.12.2 Runtime Errors** 

**[SWS_Com_00864]** ⌈ Transmission request was skipped:  error code: COM_E_SKIPPED_TRANSMISSION  value [hex]: 0x05 

⌋ (SRS_BSW_00452) 

### **7.12.3 Transient Faults** 

There are no transient faults. 

### **7.12.4 Production Errors** 

There are no production errors. 

### **7.12.5 Extended Production Errors** 

There are no extended production errors. 

## **7.13 Error Notification** 

**[SWS_Com_00442]** ⌈ When a development error is detected, the function Det_ReportError of the Default Error Tracer shall be called with: 

- 50 as the AUTOSAR COM’s ModuleId 

- 0 as InstanceId 

- the service ID of the AUTOSAR COM module’s API in which the error was detected as ApiId 

- the error ID as defined in Chapter 7.12.1as ErrorId 

⌋ (SRS_BSW_00369, SRS_BSW_00385, SRS_BSW_00327, SRS_PduR_06098, SRS_PduR_06099) 

## **7.14 Error Handling** 

AUTOSAR COM supports supervision of the communication with deadline monitoring, see Chapter 7.3.6. Further, the AUTOSAR COM supports data sequence control see Chapter 7.9 and communication protection see Chapter 7.10. 

Document ID 015: AUTOSAR_SWS_COM 

76 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



The concrete reaction of the AUTOSAR COM module with respect to error and return values of called APIs is stated within the corresponding functional requirements. 

## **7.15 AUTOSAR COM Module’s Interaction Model** 

This chapter corresponds to the chapter _Functional Model of Interaction Layer_ of [17]. The following figures illustrate the behavior of the Interaction layer for external reception and external transmission. The complete functionality is shown but it depends on the configuration what parts are present/ used in a concrete implementation. 

**[SWS_Com_00396]** ⌈ A received signal or signal group can be configured for various processing steps. The AUTOSAR COM module shall execute the configured processing steps in the following order: 

   - 1) reset reception deadline monitoring timer for I-PDU based monitoring 

   - 2) check update-bits 

   - 3) endianness conversion and sign extension 

   - 4) data invalidation 

   - 5) reception filtering 

   - 6) reset reception deadline monitoring timer for signal based monitoring 

   - 7) notification 

- ⌋ (SRS_Com_02037) 

**[SWS_Com_00744]** ⌈ In case both a ComRxDataTimeoutAction and a ComTimeoutNotification is configured for a ComSignal or a ComSignalGroup, the AUTOSAR COM module shall first call the configured ComRxDataTimeoutAction and then call the configured ComTimeoutNotification. ⌋ (SRS_Com_02089) 

Document ID 015: AUTOSAR_SWS_COM 

77 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 





<!-- Start of picture text -->
Upper  RTE<br>Layer<br>Com_SendSignal Com_SendSignal Com_SendSignalGroup Com_CbkTxTOut Com_CbkTxAck<br>From Rx side<br>Notification<br>Signal Based<br>Gateway TX<br>set update bits<br>AUTOSAR<br>endianness conversion and COM<br>sign extension<br>Transmission<br>Deadline Monitoring<br>Signal<br>Transfer<br>I-PDU Minimum Delay<br>Properties<br>Time Monitoring<br>I-PDU Transmission<br>I-PDU Callout Mode Selection<br>PduR_ComTransmit Com_TriggerTransmit Com_TxConfirmation<br>Lower  PDU<br>Layer Router<br>signal internal representation signal network representation shadow buffer<br>signal group internal representation signal group network representation I-PDU<br><!-- End of picture text -->

**Figure 3 The AUTOSAR COM module’s interaction model for transmission** 

Document ID 015: AUTOSAR_SWS_COM 

78 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 





<!-- Start of picture text -->
Upper  RTE<br>Layer<br>Com_Receive Com_Cbk Com_Cbk Com_Cbk<br>Com_ReceiveSignal SignalGroup RxAck Inv RxTOut<br>Notification<br>To Tx side<br>notification detection<br>reset reception deadline monitoring timer<br>Signal Based<br>for signal based monitoring Reception<br>Gateway TX<br>Deadline  AUTOSAR<br>reception filtering Monitoring COM<br>data invalidation<br>endianness conversion and sign extension<br>check update bits<br>I-PDU Callout<br>reset reception deadline monitoring timer for I-PDU based monitoring<br>Com_RxIndication<br>Lower  PDU<br>Layer Router<br>signal internal representation signal network representation shadow buffer<br>signal group internal representation signal group network representation I-PDU<br><!-- End of picture text -->

**Figure 4 The AUTOSAR COM module’s interaction model for reception** 

Document ID 015: AUTOSAR_SWS_COM 

79 of 185 

– AUTOSAR confidential – 



<!-- Start of picture text -->
Specification of Communication<br>AUTOSAR CP Release 4.4.0<br>Upper  RTE<br>Layer<br>Com_ReceiveSignal Com_ReceiveSignalGroup Com_SendSignal<br>notification detection<br>reset reception deadline<br>monitoring timer<br>for signal based monitoring<br>reception filtering AUTOSAR<br>data invalidation Transmission  COM<br>Signal Deadline<br>Based Monitoring<br>endianness conversion Gateway<br>and sign extension<br>check Update Bits Depending on the concrete configuration an optimized  set update bits I-PDU Transmission Mode Selection<br>gateway signal flow may<br>endianness conversion<br>skip one or more processing<br>I-PDU Callout stages. and sign extension I-PDU<br>Minimum<br>reset reception deadline<br>monitoring timer Delay Time<br>for I-PDU based monitoring  I-PDU Callout Monitoring<br>Com_RxIndication PduR_ComTransmit<br>Lower  PDU<br>Layer Router<br>signal/ signal group signal/ signal group shadow buffer<br>internal representation network representation I-PDU<br><!-- End of picture text -->

**Figure 5: The AUTOSAR COM module’s interaction model for integrated Signal Gateway** 

The endianness conversion and sign extension on receiver side are needed to feed the TMS with a correct data format. This endianness conversion is only necessary if the endianness of the Rx-bus differs from the endianness of the CPU. The endianness conversion on the sender side is only necessary if the endianness of the Rx-bus differs from the endianness of the Tx-bus. 

Document ID 015: AUTOSAR_SWS_COM 

80 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **8 API Specification** 

## **8.1 Imported Types** 

In this chapter, all types included from the following files are listed: 

### **<u>[SWS_Com_00609]</u>** <u>⌈</u> 

|**_Module_**|**_Header File_**|**_Imported Type_**|
|---|---|---|
|ComStack_Types|ComStackTypes.h|BufReq_ReturnType|
||ComStackTypes.h|PduIdType|
||ComStackTypes.h|PduInfoType|
||ComStackTypes.h|PduLengthType|
||ComStackTypes.h|RetryInfoType|
|Std_Types|StandardTypes.h|Std_ReturnType|
||StandardTypes.h|Std_VersionInfoType|



⌋ (SRS_BSW_00301) 

## **8.2 Type Definitions** 

### **8.2.1 Com_StatusType** 

### **<u>[SWS_Com_00819]</u>** <u>⌈</u> 

|**_Name: _**|Com_StatusType||
|---|---|---|
|**_Type: _**|Enumeration||
|**_Range:_**|COM_INIT|--<br>TheAUTOSARCOM moduleisinitialized and usable.|
||COM_UNINIT|0x00 The AUTOSAR COM module is not initialized or not<br>usable.<br>This shall be the default value after reset. This status<br>shall have thevalue 0.|
|**_Description:_**|This is a status v|alue returned bythe API service Com_GetStatus().|
|**_Available via: _**|Com.h||



⌋ (SRS_BSW_00335) 

### **8.2.2 Com_SignalIdType** 

### **<u>[SWS_Com_00820]</u>** <u>⌈</u> 

|**_Name: _**|Com_SignalIdType|
|---|---|
|**_Type: _**|uint16|
|**_Range: _**|0..<SignalIdmax><br>-- Zero-basedinteger number|
|**_Description:_**|TheAUTOSARCOM module's signalobjectidentifier.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_02037, SRS_BSW_00441) 

### **8.2.3 Com_SignalGroupIdType** 

**[SWS_Com_00821]** ⌈ 

Document ID 015: AUTOSAR_SWS_COM 

81 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Name: _**|Com_SignalGroupIdType|
|---|---|
|**_Type: _**|uint16|
|**_Range: _**|0..<SignalGroupIdmax> -- Zero-basedinteger number|
|**_Description:_**|TheAUTOSARCOM module's signalgroup objectidentifier.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_02041, SRS_BSW_00441) 

### **8.2.4 Com_IpduGroupIdType** 

### **<u>[SWS_Com_00822]</u>** <u>⌈</u> 

|**_Name: _**|Com_IpduGroupIdType|
|---|---|
|**_Type: _**|uint16|
|**_Range:_**|0..<IpduGroupId-<br>max><br>--Zero-based integer number; where IpduGroupId-max <<br>ComSupportedIPduGroups|
|**_Description:_**|TheAUTOSARCOM I-PDUmodule's group objectidentifier.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_00218, SRS_BSW_00441) 

### **8.2.5 Com_ConfigType** 

### **<u>[SWS_Com_00825]</u>** <u>⌈</u> 

|**_Name: _**|Com_ConfigType|
|---|---|
|**_Type: _**|Structure|
|**_Range:_**|implementation<br>specific<br>The content of the initialization data structure is<br>implementationspecific|
|**_Description:_**|Thisis the type ofthe data structure containing theinitializationdataforCOM.|
|**_Available via: _**|Com.h|



⌋ (SRS_BSW_00404, SRS_BSW_00441) 

## **8.3 Function Definitions** 

**[SWS_Com_00321]** ⌈ Non-reentrant functions do not have to check if they are called reentrant. ⌋ (SRS_BSW_00312) 

Most of the COM functions are non-reentrant with respect to a concrete object. E.g. Com_SendSignal is not reentrant for the same signal, but reentrant for different signals. Hence, if there are multiple callers of the AUTOSAR COM module they need to be synchronized on a system level, for example by using disjoint sets of signals and I-PDU groups. 

### **8.3.1 Return Codes** 

The AUTOSAR COM module does not define a special COM return type. The API services return errors either by using the Std_ReturnType as defined in [5] or via a uint8 value mapped according to Table 9. 

Return codes of the AUTOSAR COM module are defined in Table 9. 

Document ID 015: AUTOSAR_SWS_COM 

82 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **<u>[SWS_Com_00865]</u>** <u>⌈</u> 

|**_Name_**|**_Description_**|**_Type_**|**_Value_**|**_Defined in_**|
|---|---|---|---|---|
|E_OK|the service has been accepted|#define|0x00|Stan-<br>dardTypes.h|
|E_NOT_OK|invocation of service failed|#define|0x01|Stan-<br>dardTypes.h|
|COM_SERVICE_<br>NOT_AVAILABLE|the service is currently not available e.g.<br>the corresponding I-PDU group is stopped<br>(or a development error has been detect-<br>ed)|#define|0x80|Com.h|
|COM_BUSY|Successful execution of this function is<br>currently not possible, because a resource<br>is currently in use. For example, the buffer<br>of a large I-PDU is locked.<br>COM_BUSY might, but must not, be re-<br>turned whenever a signal of a large I-PDU<br>is accessed.|#define|0x81|Com.h|



⌋ (SRS_BSW_00348, SRS_BSW_00377, SRS_BSW_00441) 

**Table 9: Mapping of AUTOSAR COM module’s return codes** 

### **8.3.2 Start-Up and Control Services** 

### **8.3.2.1 Com_Init** 

### **<u>[SWS_Com_00432]</u>** <u>⌈</u> 

|**_Service name: _**|Com_Init|
|---|---|
|**_Syntax:_**|void Com_Init(<br>const Com_ConfigType* config<br>)|
|**_Service ID[hex]: _**|0x01|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|Non Reentrant|
|**_Parameters (in): _**|config<br>Pointerto theAUTOSARCOM module's configurationdata.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value:_**|None|
|**_Description:_**|This service initializes internal and external interfaces and variables of the<br>AUTOSAR COM module layer for the further processing.<br>After callingthis function the inter-ECU communication is still disabled.|
|**_Available via: _**|Com.h|



⌋ (SRS_BSW_00344, SRS_BSW_00404, SRS_BSW_00405, SRS_BSW_00101, SRS_BSW_00358, SRS_BSW_00414) 

The behavior of the AUTOSAR COM module is unspecified until a correct call to Com_Init is made. 

**Caveats of Com_Init:** It is not foreseen that Com_Init pre-empts any other AUTOSAR COM module’s function. The AUTOSAR COM module can relies on the rest of the system that Com_Init is not called in such a way. 

Document ID 015: AUTOSAR_SWS_COM 

83 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **8.3.2.2 Com_DeInit** 

### **<u>[SWS_Com_00130]</u>** <u>⌈</u> 

|**_Service name:_**|Com_DeInit|
|---|---|
|**_Syntax:_**|void Com_DeInit(<br>void<br>)|
|**_Service ID[hex]: _**|0x02|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|Non Reentrant|
|**_Parameters (in): _**|None|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|This service stops the inter-ECU communication. All started I-PDU groups are<br>stopped and have to be started again, if needed, after Com_Init is called.<br>By a call to Com_DeInit the AUTOSAR COM module is put into an not initialized<br>state.|
|**_Available via: _**|Com.h|



⌋ (SRS_BSW_00336) 

**[SWS_Com_00129]** ⌈ The AUTOSAR COM module’s function Com_DeInit shall stop all started I-PDU groups. ⌋ (SRS_BSW_00336) 

**Caveats of Com_DeInit:** It is not foreseen that Com_DeInit pre-empts any AUTOSAR COM module’s function. The AUTOSAR COM module can relies on the rest of the system that Com_DeInit is not called in such a way. 

### **8.3.2.3 Com_IpduGroupStart** 

### **<u>[SWS_Com_91001]</u>** <u>⌈</u> 

|**_Service name: _**|Com_IpduGroupStart|
|---|---|
|**_Syntax:_**|void Com_IpduGroupStart(<br>Com_IpduGroupIdType IpduGroupId,<br>boolean initialize<br>)|
|**_Service ID[hex]: _**|0x03|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|ReentrantfordifferentI-PDU groups. Non reentrantforthe sameI-PDU group.|
||IpduGroupId<br>Id of I-PDUgroupto be started|
|**_Parameters (in):_**|initialize<br>flag to request initialization of the data in the I-PDUs of this I-<br>PDU group|
|**_Parameters_**<br>**_(in-_**<br>**_out): _**|None|
|**_Parameters (out): _**|None|
|**_Return value:_**|None|
|**_Description:_**|Starts a preconfigured I-PDU group. For example, cyclic I-PDUs will be sent out<br>cyclically after the call of Com_IpduGroupStart(). If Initialize is true all I-PDUs of<br>the I-PDU group shall be (re-)initialized before the I-PDU group is started. That is<br>they shall behave like after a start-up of COM, for example the old_value of the<br>filterobjects and shadowbuffers ofsignalgroupshave to be (re-)initialized.|
|**_Available via: _**|Com.h|



Document ID 015: AUTOSAR_SWS_COM 

84 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### ⌋ (SRS_Com_00218) 

### **8.3.2.4 Com_IpduGroupStop** 

### **<u>[SWS_Com_91002]</u>** <u>⌈</u> 

|**_Service name: _**|Com_IpduGroupStop|
|---|---|
|**_Syntax:_**|void Com_IpduGroupStop(<br>Com_IpduGroupIdType IpduGroupId<br>)|
|**_Service ID[hex]: _**|0x04|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|ReentrantfordifferentI-PDU groups. Non reentrantforthe sameI-PDU group.|
|**_Parameters (in): _**|IpduGroupId<br>Id of I-PDU group to be stopped|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters(out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|Stops a preconfigured I-PDU group. For example, cyclic I-PDUs will be stopped<br>afterthe callofCom_IpduGroupStop().|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_00218) 

### **8.3.2.5 Com_EnableReceptionDM** 

### **<u>[SWS_Com_91004]</u>** <u>⌈</u> 

|**_Service name: _**|Com_EnableReceptionDM|
|---|---|
|**_Syntax:_**|void Com_EnableReceptionDM(<br>Com_IpduGroupIdType IpduGroupId<br>)|
|**_Service ID[hex]: _**|0x06|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|ReentrantfordifferentI-PDU groups. Non reentrantforthe sameI-PDU group.|
|**_Parameters (in): _**|IpduGroupId<br>Id of I-PDU groupwherereception DMshallbe enabled.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|Enables the reception deadline monitoring for the I-PDUs within the given I-PDU<br>group.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_00192) 

### **8.3.2.6 Com_DisableReceptionDM** 

### **<u>[SWS_Com_91003]</u>** <u>⌈</u> 

|**_Service name: _**|Com_DisableReceptionDM|
|---|---|
|**_Syntax:_**|void Com_DisableReceptionDM(<br>Com_IpduGroupIdType IpduGroupId<br>)|
|**_Service ID[hex]: _**|0x05|



Document ID 015: AUTOSAR_SWS_COM 

85 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Sync/Async: _**|Synchronous|
|---|---|
|**_Reentrancy: _**|ReentrantfordifferentI-PDU groups. Non reentrantforthe sameI-PDU group.|
|**_Parameters (in): _**|IpduGroupId<br>Id of I-PDU groupwherereception DMshallbe disabled.|
|**_Parameters_**<br>**_(in-_**<br>**_out): _**|None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|Disables the reception deadline monitoring for the I-PDUs within the given I-PDU<br>group.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_00192) 

### **8.3.2.7 Com_GetStatus** 

### **<u>[SWS_Com_00194]</u>** <u>⌈</u> 

|**_Service name:_**|Com_GetStatus|
|---|---|
|**_Syntax:_**|Com_StatusType Com_GetStatus(<br>void<br>)|
|**_Service ID[hex]: _**|0x07|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|Reentrant|
|**_Parameters (in): _**|None|
|**_Parameters_**<br>**_(in-_**<br>**_out): _**|None|
|**_Parameters (out): _**|None|
|**_Return value:_**|Com_StatusType COM_UNINIT: the AUTOSAR COM module is not initialized and<br>not usable<br>COM_INIT:theAUTOSARCOM moduleisinitialized and usable|
|**_Description:_**|Returns the status oftheAUTOSARCOM module.|
|**_Available via: _**|Com.h|



⌋ (SRS_BSW_00331) 

### **8.3.2.8 Com_GetVersionInfo** 

### **<u>[SWS_Com_00426]</u>** <u>⌈</u> 

|**_Service name: _**|Com_GetVersionInfo|
|---|---|
|**_Syntax:_**|void Com_GetVersionInfo(<br>Std_VersionInfoType* versioninfo<br>)|
|**_Service ID[hex]: _**|0x09|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|Reentrant|
|**_Parameters (in): _**|None|
|**_Parameters_**<br>**_(in-_**<br>**_out): _**|None|
|**_Parameters (out): _**|versioninfoPointertowhere to store theversion informationofthismodule.|
|**_Return value: _**|None|
|**_Description:_**|Returns theversion informationofthismodule.|
|**_Available via: _**|Com.h|



⌋ (SRS_BSW_00407, SRS_BSW_00003) 

Document ID 015: AUTOSAR_SWS_COM 

86 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



For configuration of Com_GetVersionInfo see SWS_Com_00026. 

### **8.3.3 Communication Services** 

### **8.3.3.1 Com_SendSignal** 

### **<u>[SWS_Com_00197]</u>** <u>⌈</u> 

|**_Service name:_**|Com_SendSi|gnal|
|---|---|---|
|**_Syntax:_**|uint8 Com_S<br>Com_Sign<br>const void*<br>)|endSignal(<br>alIdType SignalId,<br>SignalDataPtr|
|**_Service ID[hex]: _**|0x0a||
|**_Sync/Async: _**|Asynchronou|s|
|**_Reentrancy: _**|Non Reentran|tforthe same signal. Reentrantfordifferent signals.|
|**_Parameters (in):_**|SignalId|Id ofsignalto be sent.|
||SignalDataPtr|Reference to the signaldata to be transmitted.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None||
|**_Parameters (out): _**|None||
|**_Return value:_**|uint8|E_OK: service has been accepted<br>COM_SERVICE_NOT_AVAILABLE: corresponding I-PDU group<br>was stopped (or service failed due to development error)<br>COM_BUSY: in case the TP-Buffer is locked for large data types<br>handling|
|**_Description:_**|The service C<br>the signal refe|om_SendSignal updates the signal object identified by SignalId with<br>renced by the SignalDataPtrparameter.|
|**_Available via: _**|Com.h||



⌋ (SRS_Com_02037) 

**[SWS_Com_00624]** ⌈ The service Com_SendSignal shall update the signal object identified by SignalId with the signal referenced by the SignalDataPtr parameter. ⌋ (SRS_Com_02037) 

**[SWS_Com_00625]** ⌈ If the updated signal has the ComTransferProperty TRIGGERED and it is assigned to an I-PDU with ComTxModeMode DIRECT or MIXED, then Com_SendSignal shall perform an immediate transmission (within the next main function at the latest) of that I-PDU, unless the sending is delayed or prevented by other COM mechanisms. ⌋ (SRS_Com_02037) 

A related mechanism is for example the minimum delay timer (ComMinimumDelayTime). 

### **8.3.3.2 Com_SendDynSignal** 

### **<u>[SWS_Com_00627]</u>** <u>⌈</u> 

|**_Service name: _**|Com_SendDynSignal|
|---|---|
|**_Syntax:_**|uint8 Com_SendDynSignal(<br>Com_SignalIdType SignalId,<br>const void* SignalDataPtr,<br> uint16Length|



Document ID 015: AUTOSAR_SWS_COM 

87 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Service ID[hex]: _**|)<br>0x21||
|---|---|---|
|**_Sync/Async: _**|Asynchron|ous|
|**_Reentrancy: _**|Non Reent|rantforthe same signal. Reentrantfordifferent signals.|
||SignalId|Id ofsignalto be sent.|
|**_Parameters (in):_**|SignalData|Ptr Reference to the signaldata to be transmitted.|
||Length|Lengthofthe dynamiclengthsignal|
|**_Parameters_**<br>**_(in-_**<br>**_out): _**|None||
|**_Parameters (out): _**|None||
|**_Return value:_**|uint8|E_OK: service has been accepted<br>E_NOT_OK: in case the Length is greater than the configured<br>ComSignalLength of this sent signal<br>COM_SERVICE_NOT_AVAILABLE: corresponding I-PDU group<br>was stopped (or service failed due to development error)<br>COM_BUSY: incase theTP-Buffer islocked|
|**_Description:_**|The service<br>withthe sig|Com_SendDynSignal updates the signal object identified by SignalId<br>nal referenced by the SignalDataPtrparameter.|
|**_Available via: _**|Com.h||



⌋ (SRS_Com_02095) 

**[SWS_Com_00628]** ⌈ The service Com_SendDynSignal shall update the signal object identified by SignalId with the signal referenced by the SignalDataPtr parameter. ⌋ (SRS_Com_02095) 

**[SWS_Com_00629]** ⌈ If the updated signal (see SWS_Com_00628) has the ComTransferProperty _TRIGGERED_ , then the function Com_SendDynSignal shall perform an immediate transmission (within the next main function at the latest) of the I-PDU associated with the signal except when the signal is packed into an I-PDU with Periodic transmission mode. ⌋ (SRS_Com_02095) 

**[SWS_Com_00630]** ⌈ If the updated signal, see SWS_Com_00628, has the ComTransferProperty _PENDING_ , then the function Com_SendDynSignal shall not perform a transmission of the I-PDU associated with the signal. ⌋ (SRS_Com_02095) 

There is no restriction regarding the minimal length of a dynamic length signal. Hence, it is allowed that a dynamic length signal has zero length. 

### **8.3.3.3 Com_ReceiveSignal** 

### **<u>[SWS_Com_00198]</u>** <u>⌈</u> 

|**_Service name: _**|Com_ReceiveSignal|
|---|---|
|**_Syntax:_**<br>**_Service ID[hex]: _**|uint8 Com_ReceiveSignal(<br>Com_SignalIdType SignalId,<br>void* SignalDataPtr<br>)<br>0x0b|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|Non Reentrantforthe same signal. Reentrantfordifferent signals.|
|**_Parameters (in): _**|SignalId<br>Id ofsignalto bereceived.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|



Document ID 015: AUTOSAR_SWS_COM 

88 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Parameters (out):_**|<sup>SignalDataPt</sup>|<sup>r Reference to the location where the received signal data shall be</sup><br>stored|
|---|---|---|
|**_Return value:_**|uint8|E_OK: service has been accepted<br>COM_SERVICE_NOT_AVAILABLE: corresponding I-PDU group<br>was stopped (or service failed due to development error)<br>COM_BUSY: in case the TP-Buffer is locked for large data types<br>handling|
|**_Description:_**|Com_Receiv<br>locationspec|eSignal copies the data of the signal identified by SignalId to the<br>ified by SignalDataPtr.|
|**_Available via: _**|Com.h||



⌋ (SRS_Com_02037) 

**[SWS_Com_00631]** ⌈ The service Com_ReceiveSignal shall copy the data of the signal object identified by SignalId to the position referenced by SignalDataPtr. ⌋ (SRS_Com_02037) 

**Caveats of Com_ReceiveSignal:** The AUTOSAR COM module relies on the fact the SignalDataPtr is properly aligned with respect to the data type of the signal with the given SignalId. The caller of Com_ReceiveSignal has to ensure this. 

### **8.3.3.4 Com_ReceiveDynSignal** 

### **<u>[SWS_Com_00690]</u>** <u>⌈</u> 

|**_Service name: _**|Com_ReceiveD|ynSignal|
|---|---|---|
|**_Syntax:_**|uint8 Com_Rec<br>Com_Signal<br>void* Signal<br>uint16* Leng<br>)|eiveDynSignal(<br>IdType SignalId,<br>DataPtr,<br>th|
|**_Service ID[hex]: _**|0x22||
|**_Sync/Async: _**|Synchronous||
|**_Reentrancy: _**|Non Reentrant|for the same signal. Reentrant for different signals.|
|**_Parameters (in): _**|SignalId|Id ofsignalto bereceived.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>Length|in: maximum length that could be received<br>out: lengthofthe dynamiclengthsignal|
|**_Parameters (out):_**|<sup>SignalDataPtr</sup>|<sup>reference to the location where the received signal data shall be</sup><br>stored|
|**_Return value:_**|uint8|E_OK: service has been accepted<br>E_NOT_OK: in case the Length (as in-parameter) is smaller than<br>the received length of the dynamic length signal<br>COM_SERVICE_NOT_AVAILABLE: corresponding I-PDU group<br>was stopped (or service failed due to development error)<br>COM_BUSY: incase theTP-Buffer islocked|
|**_Description:_**|Com_ReceiveD<br>location specifi<br>signalat the po|ynSignal copies the data of the signal identified by SignalId to the<br>ed by SignalDataPtr and stores the length of the dynamical length<br>sitiongivenby theLengthparameter.|
|**_Available via: _**|Com.h||



⌋ (SRS_Com_02092, SRS_Com_02095) 

**[SWS_Com_00711]** ⌈ The service Com_ReceiveDynSignal shall copy the data of the signal object identified by SignalId to the position referenced by SignalDataPtr. ⌋ (SRS_Com_02092) 

Document ID 015: AUTOSAR_SWS_COM 

89 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00712]** ⌈ The service Com_ReceiveDynSignal shall return the calculated length (see SWS_Com_00758) of the dynamic length signal identified by SignalId in parameter Length. ⌋ (SRS_Com_02092) 

**[SWS_Com_00724]** ⌈ In case, the Length (as in-parameter) is smaller than the received length of the dynamic length signal, Com_ReceiveDynSignal shall not copy any data to the position referenced by SignalDataPtr. ⌋ (SRS_Com_02092) 

### **8.3.3.5 Com_SendSignalGroup** 

### **<u>[SWS_Com_00200]</u>** <u>⌈</u> 

|**_Service name: _**|Com_SendSignalGroup|
|---|---|
|**_Syntax:_**|uint8 Com_SendSignalGroup(<br>Com_SignalGroupIdType SignalGroupId<br>)|
|**_Service ID[hex]: _**|0x0d|
|**_Sync/Async: _**|Asynchronous|
|**_Reentrancy: _**|Non Reentrantforthe same group signal. Reentrantfordifferent group signals.|
|**_Parameters (in): _**|SignalGroupIdId ofsignalgroup to be sent.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value:_**|uint8<br>E_OK: service has been accepted<br>COM_SERVICE_NOT_AVAILABLE: corresponding I-PDU group<br>was stopped (or service failed due to development error)<br>COM_BUSY: in case the TP-Buffer is locked for large data types<br>handling|
|**_Description:_**|The service Com_SendSignalGroup copies the content of the associated shadow<br>bufferto the associatedI-PDU.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_02041) 

**[SWS_Com_00635]** ⌈ The service Com_SendSignalGroup shall copy the content of the shadow buffer referenced by parameter SignalGroupId to the associated I-PDU. ⌋ (SRS_Com_02041) 

**[SWS_Com_00637]** ⌈ Configuration of Com_SendSignalGroup: A signal group must be configured before this call. See ECUC_Com_00345 for details. ⌋ (SRS_Com_02041) 

### **8.3.3.6 Com_ReceiveSignalGroup** 

### **<u>[SWS_Com_00201]</u>** <u>⌈</u> 

|**_Service name:_**|Com_ReceiveSignalGroup|
|---|---|
|**_Syntax:_**|uint8 Com_ReceiveSignalGroup(<br>Com_SignalGroupIdType SignalGroupId<br>)|
|**_Service ID[hex]: _**|0x0e|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|Non Reentrantforthe same group signal. Reentrantfordifferent group signals.|
|**_Parameters (in): _**|SignalGroupIdId ofsignalgroup to bereceived.|



Document ID 015: AUTOSAR_SWS_COM 

90 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None||
|---|---|---|
|**_Parameters (out): _**|None||
|**_Return value:_**|uint8|E_OK: service has been accepted<br>COM_SERVICE_NOT_AVAILABLE: corresponding I-PDU group<br>was stopped (or service failed due to development error)<br>COM_BUSY: in case the TP-Buffer is locked for large data types<br>handling|
|**_Description:_**|The servic<br>I-PDU to th|e Com_ReceiveSignalGroup copies the received signal group from the<br>e shadowbuffer.|
|**_Available via: _**|Com.h||



⌋ (SRS_Com_02041) 

**[SWS_Com_00638]** ⌈ The service Com_ReceiveSignalGroup shall copy the received signal group from the I-PDU to the shadow buffer. ⌋ (SRS_Com_02041) 

After this call, the group signals could be copied from the shadow buffer to the RTE by calling Com_ReceiveSignal. 

**[SWS_Com_00639]** ⌈ Configuration of Com_ReceiveSignalGroup: A signal group must be configured before this call. See ECUC_Com_00345 for details. ⌋ (SRS_Com_02041) 

**[SWS_Com_00461]** ⌈ The AUTOSAR COM module shall always copy the last known data, or the ComSignalInitValue(s) if not yet written, of the I-PDU to the shadow buffer by a call to Com_ReceiveSignalGroup even if the I-PDU is stopped and COM_SERVICE_NOT_AVAILABLE is returned. ⌋ (SRS_Com_02041) 

### **8.3.3.7 Com_SendSignalGroupArray** 

### **<u>[SWS_Com_00851]</u>** <u>⌈</u> 

|**_Service name: _**|Com_SendSignalGro|upArray|
|---|---|---|
|**_Syntax:_**|uint8 Com_SendSign<br>Com_SignalGroupI<br>const uint8* Signal<br>)|alGroupArray(<br>dType SignalGroupId,<br>GroupArrayPtr|
|**_Service ID[hex]: _**|0x23||
|**_Sync/Async: _**|Asynchronous||
|**_Reentrancy: _**|Non Reentrantforthe|same signalgroup. Reentrantfordifferent signalgroups.|
|**_Pt i_**|SignalGroupId|Id ofsignalgroup to be sent.|
|**_arameers (n):_**|SignalGroupArrayPtr|Reference to the signalgroup array.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None||
|**_Parameters (out): _**|None||
|**_Return value:_**|uint8|E_OK: service has been accepted<br>COM_SERVICE_NOT_AVAILABLE: corresponding I-PDU<br>group was stopped (or service failed due to development<br>error)<br>COM_BUSY: in case the TP-Buffer is locked for large data<br>types handling|
|**_Description:_**|The service Com_Sen<br>SignalGroupArrayPtr<br>to the arrayrepresent|dSignalGroupArray copies the content of the provided<br>to the associated I-PDU. The provided data shall correspond<br>ationofthe signalgroup.|



Document ID 015: AUTOSAR_SWS_COM 

91 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**_<mark>Available via:</mark>_** <u>Com.h</u> 

⌋ (SRS_Com_02112, SRS_Com_02041) 

**[SWS_Com_00852]** ⌈ The service Com_SendSignalGroupArray shall copy the content designated by the SignalGroupArrayPtr to the associated I-PDU. ⌋ (SRS_Com_02112, SRS_Com_02041) 

**[SWS_Com_00853]** ⌈ The Com_SendSignalGroupArray API shall only be available when the configuration switch ComEnableSignalGroupArrayApi is enabled. ⌋ (SRS_Com_00177) 

### **8.3.3.8 Com_ReceiveSignalGroupArray** 

### **<u>[SWS_Com_00854]</u>** <u>⌈</u> 

|**_Service name:_**|Com_ReceiveSignalG|roupArray|
|---|---|---|
|**_Syntax:_**|uint8 Com_ReceiveS<br>Com_SignalGroup<br>uint8* SignalGroup<br>)|ignalGroupArray(<br>IdType SignalGroupId,<br>ArrayPtr|
|**_Service ID[hex]: _**|0x24||
|**_Sync/Async: _**|Synchronous||
|**_Reentrancy: _**|Non Reentrantforthe|same signalgroup. Reentrantfordifferent signalgroups.|
|**_Parameters (in): _**|SignalGroupId|Id ofsignalgroup to bereceived.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None||
|**_Parameters (out):_**|<sup>SignalGroupArrayPtr</sup>|<sup>reference to the location where the received signal group</sup><br>array shallbe stored|
|**_Return value:_**|uint8|E_OK: service has been accepted<br>COM_SERVICE_NOT_AVAILABLE: corresponding I-PDU<br>group was stopped (or service failed due to development<br>error)<br>COM_BUSY: in case the TP-Buffer is locked for large data<br>types<br>handling|
|**_Description:_**|The service Com_Re<br>array representation f<br>rayPtr.|ceiveSignalGroupArray copies the received signal group<br>rom the PDU to the location designated by SignalGroupAr-|
|**_Available via: _**|Com.h||



⌋ (SRS_Com_02112, SRS_Com_02041) 

**[SWS_Com_00855]** ⌈ The service Com_ReceiveSignalGroupArray shall copy the array representation of the received signal group from the I-PDU to the location designated by SignalGroupArrayPtr. ⌋ (SRS_Com_02112, SRS_Com_02041) 

**[SWS_Com_00856]** ⌈ The Com_ReceiveSignalGroupArray API shall only be available when the configuration switch ComEnableSignalGroupArrayApi is enabled. ⌋ (SRS_Com_00177) 

**[SWS_Com_00857]** ⌈ The AUTOSAR COM module shall always copy the last known data, or the ComSignalInitValues if not yet written, of the I-PDU to the SignalGroupArrayPtr by a call to Com_ReceiveSignalGroupArray even if the I-PDU is stopped and COM_SERVICE_NOT_AVAILABLE is returned. ⌋ (SRS_Com_02041) 

92 of 185 

Document ID 015: AUTOSAR_SWS_COM 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **8.3.3.9 Com_InvalidateSignal** 

### **<u>[SWS_Com_00203]</u>** <u>⌈</u> 

|**_Service name:_**|Com_InvalidateSignal|
|---|---|
|**_Syntax:_**|uint8 Com_InvalidateSignal(<br>Com_SignalIdType SignalId<br>)|
|**_Service ID[hex]: _**|0x10|
|**_Sync/Async: _**|Asynchronous|
|**_Reentrancy: _**|Non Reentrant for the same signal. Reentrant for different signals.|
|**_Parameters (in): _**|SignalIdId ofsignalto beinvalidated.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value:_**|uint8<br>E_OK: service has been accepted<br>COM_SERVICE_NOT_AVAILABLE: corresponding I-PDU group is<br>stopped, no ComSignalDataInvalidValue is configured for the given<br>signalId or service fails due to development error<br>COM_BUSY: incase theTP-Buffer islocked|
|**_Description:_**|The service Com_InvalidateSignal invalidates the signal with the given SignalId by<br>settingitsvalue toits configured ComSignalDataInvalidValue.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_02077) 

See Chapter 7.4.4 for further information about the signal invalidation mechanism. 

**[SWS_Com_00642]** ⌈ After invaliding the signal data, the function Com_InvalidateSignal shall perform a call of Com_SendSignal internally, for details see SWS_Com_00099. ⌋ (SRS_Com_02077) 

**[SWS_Com_00643]** ⌈ Com_InvalidateSignal shall return COM_SERVICE_NOT_AVAILABLE in case no ComSignalDataInvalidValue (ECUC_Com_00391) is configured for the signal with the given SignalId. ⌋ (SRS_Com_02077) 

### **8.3.3.10 Com_InvalidateSignalGroup** 

### **<u>[SWS_Com_00557]</u>** <u>⌈</u> 

|**_Service name: _**|Com_InvalidateSignalGroup|
|---|---|
|**_Syntax:_**|uint8 Com_InvalidateSignalGroup(<br>Com_SignalGroupIdType SignalGroupId<br>)|
|**_Service ID[hex]: _**|0x1b|
|**_Sync/Async: _**|Asynchronous|
|**_Reentrancy: _**|Non Reentrant for the same signalgroup. Reentrant for different signalgroups.|
|**_Parameters (in): _**|SignalGroupIdId ofsignalgroup to beinvalidated.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value:_**|uint8<br>E_OK: service has been accepted<br>COM_SERVICE_NOT_AVAILABLE: corresponding I-PDU group is<br>stopped, no ComSignalDataInvalidValue is configured for any of the<br>group signals or service fails due to development error<br>COM_BUSY: incase theTP-Buffer islocked|



93 of 185 

Document ID 015: AUTOSAR_SWS_COM 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Description:_**|The service Com_InvalidateSignalGroup invalidates all group signals of the signal<br>group with the given SignalGroupId by setting their values to their configured|
|---|---|
||ComSignalDataInvalidValues.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_02077) 

For further information about the signal invalidation mechanism, see Chapter 7.4.4. 

**[SWS_Com_00645]** ⌈ After invaliding the signal group data, the function Com_InvalidateSignalGroup shall perform a call of Com_SendSignalGroup internally. ⌋ (SRS_Com_02077) 

### **8.3.3.11 Com_TriggerIPDUSend** 

### **<u>[SWS_Com_00348]</u>** <u>⌈</u> 

|**_Service name: _**|Com_TriggerIPDUSend|
|---|---|
|**_Syntax:_**|Std_ReturnType Com_TriggerIPDUSend(<br>PduIdType PduId<br>)|
|**_Service ID[hex]: _**|0x17|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|Non Reentrant|
|**_Parameters (in): _**|PduId<br>TheI-PDU-IDoftheI-PDU that shallbe triggeredforsending|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value:_**|Std_ReturnType E_OK: I-PDU was triggered for transmission<br>E_NOT_OK: I-PDU is stopped, the transmission could not be<br>triggered|
|**_Description:_**|By a call to Com_TriggerIPDUSend the I-PDU with the given ID is triggered for<br>transmission.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_02037) 

**[SWS_Com_00861]** ⌈ By a call to Com_TriggerIPDUSend, the AUTOSAR COM shall trigger the I-PDU with the given ID for transmission only if the I-PDU is started. ⌋ (SRS_Com_02037) 

In case a stopped I-PDU is triggered for transmission, just E_NOT_OK is returned. For stopped I-PDUs no triggers are stored for a later execution after a potential (re-) starting of the I-PDU. 

**[SWS_Com_00388]** ⌈ When an I-PDU is transmitted because of the function Com_TriggerIPDUSend or Com_TriggerIPDUSendWithMetaData, the AUTOSAR COM module shall only take the minimum delay time into account. That is the AUTOSAR COM module shall postpone transmissions if necessary and reset the minimum delay timer in case of transmissions. The AUTOSAR COM module shall not take into account all other transmission mode related parameters like ComTxModeNumberOfRepetitions. ⌋ (SRS_Com_02037) 

Document ID 015: AUTOSAR_SWS_COM 

94 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00492]** ⌈ If an I-PDU triggered by Com_TriggerIPDUSend or Com_TriggerIPDUSendWithMetaData has a configured I-PDU-callout, see ECUC_Com_00387, then the function Com_TriggerIPDUSend or Com_TriggerIPDUSendWithMetaData repectively shall also call this I-PDU-Callout. ⌋ (SRS_Com_02037) 

If within the Com_TriggerIPDUSend function, another call to Com_TriggerIPDUSend is invoked the application programmer must take care to not create infinite recursions. Both, direct recursions by invoking Com_TriggerIPDUSend with the same ComPduId again and indirect recursions with longer recursion paths are theoretically possible. 

The previous paragraph is also true for Com_TriggerIPDUSendWithMetaData as well as for combinations of these two I-PDU triggering functions. 

**[SWS_Com_00867]** ⌈ In case a large I-PDU is triggered for transmission by Com_TriggerIPDUSend and the buffer of the large I-PDU is currently locked, the AUTOSAR COM shall store the transmit request and transmit the I-PDU when the buffer is available again. ⌋ (SRS_Com_02037) 

### **8.3.3.12  Com_TriggerIPDUSendWithMetaData** 

### **<u>[SWS_Com_00858]</u>** <u>⌈</u> 

|**_Service name: _**|Com_TriggerIPDUSendWithMetaData|
|---|---|
|**_Syntax:_**|Std_ReturnType Com_TriggerIPDUSendWithMetaData(<br>PduIdType PduId,<br>const uint8* MetaData<br>)|
|**_Service ID[hex]: _**|0x28|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|Non Reentrant|
|**_Parameters (in):_**|PduId<br>The I-PDU-ID of the I-PDU that shall be triggered for<br>sending|
||MetaData<br>Apointerto themetadataforthe triggered send-request|
|**_Parameters_**<br>**_(in-_**<br>**_out): _**|None|
|**_Parameters (out): _**|None|
|**_Return value:_**|Std_ReturnType<br>E_OK: I-PDU was triggered for transmission<br>E_NOT_OK: I-PDU is stopped, the transmission could not<br>be triggered|
|**_Description:_**|By a call to Com_TriggerIPDUSendWithMetaData the AUTOSAR COM module<br>updates its internal metadata for the I-PDU with the given ID by copying the<br>metadata from the given position and with respect to length of the globally<br>configured MetaDataType of this I-PDU. Then the I-PDU is triggered for<br>transmission.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_02037) 

**[SWS_Com_00862]** ⌈ By a call to Com_TriggerIPDUSendWithMetaData, the AUTOSAR COM shall trigger the I-PDU with the given ID for transmission only if the I- PDU is started. ⌋ (SRS_Com_02037) 

Document ID 015: AUTOSAR_SWS_COM 

95 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



In case a stopped I-PDU is triggered for transmission, just E_NOT_OK is returned. There is no mechanism in COM to store the triggering and to execute it after a potential (re-)starting of the I-PDU. 

**[SWS_Com_00868]** ⌈ In case a large I-PDU is triggered for transmission by Com_TriggerIPDUSendWithMetaData and the buffer of the large I-PDU is currently locked, the AUTOSAR COM shall store the transmit request with the given MetaData and transmit the I-PDU when the buffer is available again. ⌋ (SRS_Com_02037) 

### **8.3.3.13 Com_SwitchIpduTxMode** 

### **<u>[SWS_Com_00784]</u>** <u>⌈</u> 

|**_Service name: _**|Com_SwitchIpduTxMode|
|---|---|
|**_Syntax:_**|void Com_SwitchIpduTxMode(<br>PduIdType PduId,<br>boolean Mode<br>)|
|**_Service ID[hex]: _**|0x27|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|ReentrantfordifferentPduIds. Non reentrantforthe samePduId.|
|**_Pt i_**|PduId<br>Id oftheI-PDU of whichthe transmission mode shallbe changed.|
|**_arameers (n):_**|Mode<br>the transmission mode that shallbe set.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|The service Com_SwitchIpduTxMode sets the transmission mode of the I-PDU<br>referenced by PduId to Mode.<br>In case the transmission mode changes, the new mode shall immediately be<br>effective (see SWS_Com_00239).<br>In case the requested transmission mode was already active for this I-PDU, the<br>call will haveno effect.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_02082) 

**[SWS_Com_00881]** ⌈ When the transmission mode of an I-PDU is explicitly set by Com_SwitchIpduTxMode, the AUTOSAR COM shall defer the cyclic transmissions of this I-PDU by ComTxModeTimeOffset. ⌋ (SRS_Com_02082) 

By mixing the signal based TMS and explicit TMS by Com_SwitchIpduTxMode for the same I-PDU, it must be noted that the signal base TMS might switch back the manual set mode during a call to Com_SendSignal or Com_SendSignalGroup for this I-PDU. Therefore, mixing explicit and manual TMS for one I-PDU must be carefully designed, if used at all. 

## **8.4 Callback Functions and Notifications** 

### **8.4.1 Com_TriggerTransmit** 

**[SWS_Com_00001]** ⌈ 

Document ID 015: AUTOSAR_SWS_COM 

96 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Service name: _**|Com_TriggerTra|nsmit|
|---|---|---|
|**_Syntax:_**|Std_ReturnType<br>PduIdType Tx<br>PduInfoType*<br>)|Com_TriggerTransmit(<br>PduId,<br>PduInfoPtr|
|**_Service ID[hex]: _**|0x41||
|**_Sync/Async: _**|Synchronous||
|**_Reentrancy: _**|Reentrantfordiff|erentPduIds. Non reentrantforthe samePduId.|
|**_Parameters (in): _**|TxPduId|IDofthe SDU thatisrequested to be transmitted.|
|**_Parameters_**<br>**_(in-_**<br>**_out):_**|PduInfoPtr|Contains a pointer to a buffer (SduDataPtr) to where the SDU<br>data shall be copied, and the available buffer size in SduLengh.<br>On return, the service will indicate the length of the copied SDU<br>datainSduLength.|
|**_Parameters(out): _**|None||
|**_Return value:_**|Std_ReturnType|E_OK: SDU has been copied and SduLength indicates the<br>number of copied bytes.<br>E_NOT_OK: No SDU data has been copied. PduInfoPtr must not<br>be used since it may contain a NULL pointer or point to invalid<br>data.|
|**_Description:_**|Within this API, t<br>available data fit<br>If it fits, it shall co<br>and update the l<br>If not,itreturnsE|he upper layer module (called module) shall check whether the<br>s into the buffer size reported by PduInfoPtr->SduLength.<br>py its data into the buffer provided by PduInfoPtr->SduDataPtr<br>ength of the actual copied data in PduInfoPtr->SduLength.<br> _NOT_OK without changingPduInfoPtr.|
|**_Available via: _**|Com.h||



⌋ (SRS_Com_02045) 

**[SWS_Com_00647]** ⌈ Within the function Com_TriggerTransmit, the AUTOSAR COM module shall copy the contents of its I-PDU transmit buffer to the L-PDU buffer given by PduInfoPtr->SduDataPtr and update PduInfoPtr->SduLength with length of the copied data accordingly. ⌋ (SRS_Com_02045) 

**[SWS_Com_00869]** ⌈ In case the given PduInfoPtr->SduLength is smaller than the actual PDU-length, Com_TriggerTransmit shall not copy any data and return E_NOT_OK. ⌋ (SRS_Com_02045) 

**[SWS_Com_00475]** ⌈ Com_TriggerTransmit is not interfered by the I-PDU minimum delay time and shall not reset the minimum delay timer, see ECUC_Com_00181. ⌋ (SRS_Com_02045) 

The function Com_TriggerTransmit behaves independent of the configured transmission mode. 

**Use case:** This function is used e.g. by the LIN Master for sending out a LIN frame. In this case, the trigger transmit can be initiated by the Master schedule table itself or a received LIN header. The FlexRay Interface for requesting PDUs to be sent in static part (synchronous to the FlexRay global time) also uses this function. 

Once the PDU Router has successfully sent the I-PDU, the PDU Router will call Com_TxConfirmation. 

**Caveats of Com_TriggerTransmit:** This function might be called in interrupt context. 

Document ID 015: AUTOSAR_SWS_COM 

97 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **8.4.2 Com_RxIndication** 

### **<u>[SWS_Com_00123]</u>** <u>⌈</u> 

|**_Service name:_**|Com_RxIndication|
|---|---|
|**_Syntax:_**|void Com_RxIndication(<br>PduIdType RxPduId,<br>const PduInfoType* PduInfoPtr<br>)|
|**_Service ID[hex]: _**|0x42|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|ReentrantfordifferentPduIds. Non reentrantforthe samePduId.|
||RxPduIdIDofthereceivedPDU.|
|**_Parameters (in):_**|PduInfoPtr Contains the length (SduLength) of the received PDU, a pointer to a<br>buffer (SduDataPtr) containing the PDU, and the MetaData related to<br>thisPDU.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|IndicationofareceivedPDUfromalower layercommunication interfacemodule.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_02043) 

**Caveats of Com_RxIndication:** This function might be called in interrupt context. 

### **8.4.3 Com_TpRxIndication** 

### **<u>[SWS_Com_00650]</u>** <u>⌈</u> 

|**_Service name: _**|Com_TpRxIndication|
|---|---|
|**_Syntax:_**|void Com_TpRxIndication(<br>PduIdType id,<br>Std_ReturnType result<br>)|
|**_Service ID[hex]: _**|0x45|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|Reentrant|
|**_Prmtr in_**|id<br>IdentificationofthereceivedI-PDU.|
|**_aaees ():_**|result<br>Result ofthereception.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|Called after an I-PDU has been received via the TP API, the result indicates<br>whetherthe transmission was successfulor not.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_02095) 

**Caveats of Com_TpRxIndication:** This function might be called in interrupt context. 

### **8.4.4 Com_TxConfirmation** 

### **[SWS_Com_00124]** ⌈ 

Document ID 015: AUTOSAR_SWS_COM 

98 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Service name: _**|Com_TxConfirmation|
|---|---|
|**_Syntax:_**|void Com_TxConfirmation(<br>PduIdType TxPduId,<br>Std_ReturnType result<br>)|
|**_Service ID[hex]: _**|0x40|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|ReentrantfordifferentPduIds. Non reentrantforthe samePduId.|
||TxPduId<br>IDofthePDU thathas beentransmitted.|
|**_Parameters (in):_**|result<br>E_OK: The PDU was transmitted.<br>E_NOT_OK: TransmissionofthePDUfailed.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|The lower layer communication interface module confirms the transmission of a<br>PDU,or the failure to transmit a PDU.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_02044) 

**Caveats of Com_TxConfirmation:** This function might be called in interrupt context, e.g. from transmit interrupt. 

### **8.4.5 Com_TpTxConfirmation** 

### **<u>[SWS_Com_00725]</u>** <u>⌈</u> 

|**_Service name: _**|Com_TpTxConfirmation|
|---|---|
|**_Syntax:_**|void Com_TpTxConfirmation(<br>PduIdType id,<br>Std_ReturnType result<br>)|
|**_Service ID[hex]: _**|0x48|
|**_Sync/Async:_**|Synchronous|
|**_Reentrancy: _**|Reentrant|
|**_Parameters (in):_**|id<br>Identificationofthe transmittedI-PDU.|
||result<br>Result of the transmission of the I-PDU.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|This function is called after the I-PDU has been transmitted on its network, the<br>resultindicateswhetherthe transmission was successfulor not.|
|**_Available via: _**|Com.h|



⌋ (SRS_Com_02095) 

### **8.4.6 Com_StartOfReception** 

### **<u>[SWS_Com_00691]</u>** <u>⌈</u> 

|**_Service name: _**|Com_StartOfReception|
|---|---|
|**_Syntax:_**|BufReq_ReturnType Com_StartOfReception(<br>PduIdType id,|
||constPduInfoType* info,|



Document ID 015: AUTOSAR_SWS_COM 

99 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||PduLengthType T<br>PduLengthType*<br>)|pSduLength,<br>bufferSizePtr|
|---|---|---|
|**_Service ID[hex]: _**|0x46||
|**_Sync/Async: _**|Synchronous||
|**_Reentrancy: _**|Reentrant||
||id|IdentificationoftheI-PDU.|
|**_Parameters (in):_**|info|Pointer to a PduInfoType structure containing the payload<br>data (without protocol information) and payload length of the<br>first frame or single frame of a transport protocol I-PDU<br>reception, and the MetaData related to this PDU. If neither<br>first/single frame data nor MetaData are available, this<br>parameter is set toNULL_PTR.|
||TpSduLength|Total lengthoftheN-SDU to bereceived.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None||
|**_Parameters (out):_**|bufferSizePtr|Available receive buffer in the receiving module. This<br>parameter will be used to compute the Block Size (BS) in the<br>transport protocol module.|
|**_Return value:_**|BufReq_ReturnTyp|e BUFREQ_OK: Connection has been accepted. bufferSizePtr<br>indicates the available receive buffer; reception is continued.<br>If no buffer of the requested size is available, a receive buffer<br>size of 0 shall be indicated by bufferSizePtr.<br>BUFREQ_E_NOT_OK: Connection has been rejected;<br>reception is aborted. bufferSizePtr remains unchanged.<br>BUFREQ_E_OVFL: No buffer of the required length can be<br>provided; reception is aborted. bufferSizePtr remains<br>unchanged.|
|**_Description:_**<br>**_Available via: _**|This function is calle<br>fragmented into mul<br>consist of a single N<br>maximumbuffersiz<br>Com.h|d at the start of receiving an N-SDU. The N-SDU might be<br>tiple N-PDUs (FF with one or more following CFs) or might<br>-PDU (SF). The service shall provide the currently available<br>ewhen invokedwith TpSduLengthequalto 0.|



⌋ (SRS_Com_02095) 

**[SWS_Com_00654]** ⌈ If ComRxPduId corresponds to a large I-PDU and TpSduLength is greater than the configured length of this I-PDU then the function Com_StartOfReception shall return BUFREQ_E_OVFL. ⌋ (SRS_Com_02095) 

**[SWS_Com_00655]** ⌈ If ComRxPduId corresponds to a dynamic length I-PDU and TpSduLength is greater than the configured maximum length of this I-PDU then the function Com_StartOfReception shall return BUFREQ_E_OVFL. ⌋ (SRS_Com_02095) 

**[SWS_Com_00657]** ⌈ If the internal AUTOSAR COM module’s buffer is currently not locked and the parameter TpSduLength does not exceed the (maximum) expected length, the function Com_StartOfReception shall write the complete size of the AUTOSAR COM module’s internal I-PDU buffer of the I-PDU with handle ComRxPduId to the position given by RxBufferSizePtr. ⌋ (SRS_Com_02095) 

**[SWS_Com_00721]** ⌈ Com_StartOfReception shall return BUFREQ_E_NOT_OK, in case ComRxPduId refers to a stopped I-PDU. ⌋ (SRS_Com_02095) 

Document ID 015: AUTOSAR_SWS_COM 

100 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00818]** ⌈ In case Com_StartOfReception returnes BUFREQ_E_NOT_OK or BUFREQ_E_OVFL, the AUTOSAR COM module shall not expect a call to Com_TpRxIndication and hence shall not lock its internal buffer. ⌋ (SRS_Com_02095) 

**[SWS_Com_00874]** ⌈ In case Com_StartOfReception is called with TpSduLength equal to 0, the AUTOSAR COM module shall return the configured (maximum) length of this I-PDU via the bufferSizePtr. ⌋ (SRS_Com_02095) 

A TpSduLength equal to 0 indicates an unknown message length. 

### **8.4.7 Com_CopyRxData** 

### **<u>[SWS_Com_00692]</u>** <u>⌈</u> 

|**_Service name: _**|Com_CopyRxData||
|---|---|---|
|**_Syntax:_**|BufReq_ReturnTyp<br>PduIdType id,<br>const PduInfoTyp<br>PduLengthType*<br>)|e Com_CopyRxData(<br>e* info,<br>bufferSizePtr|
|**_Service ID[hex]: _**|0x44||
|**_Sync/Async: _**|Synchronous||
|**_Reentrancy: _**|Reentrant||
||id|IdentificationofthereceivedI-PDU.|
|**_Parameters (in):_**|info|Provides the source buffer (SduDataPtr) and the number of<br>bytes to be copied (SduLength).<br>An SduLength of 0 can be used to query the current amount<br>of available buffer in the upper layer module. In this case, the<br>SduDataPtr may be aNULL_PTR.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None||
|**_Parameters (out): _**|bufferSizePtr|Availablereceive bufferafterdatahas beencopied.|
|**_Return value:_**|BufReq_ReturnTyp|e BUFREQ_OK: Data copied successfully<br>BUFREQ_E_NOT_OK: Data was not copied because an<br>erroroccurred.|
|**_Description:_**|This function is calle<br>to the upper layer.<br>Each call to this fun<br>The size of the rem<br>bufferSizePtr.|d to provide the received data of an I-PDU segment (N-PDU)<br>ction provides the next part of the I-PDU data.<br>aining buffer is written to the position indicated by|
|**_Available via: _**|Com.h||



⌋ (SRS_Com_02095) 

**Caveats of Com_CopyRxData:** This function might be called in interrupt context. Therefore, data consistency must be ensured. 

**[SWS_Com_00782]** ⌈ Com_CopyRxData shall copy no data and return BUFREQ_E_NOT_OK in case the given PduId refers to a stopped I-PDU. ⌋ (SRS_Com_00218) 

### **8.4.8 Com_CopyTxData** 

### **[SWS_Com_00693]** ⌈ 

Document ID 015: AUTOSAR_SWS_COM 

101 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Service name: _**<br>|Com_CopyTxData<br>||
|---|---|---|
|**_Syntax:_**|BufReq_ReturnType<br>PduIdType id,<br>const PduInfoType<br>const RetryInfoTyp<br>PduLengthType* a<br>)|Com_CopyTxData(<br>* info,<br>e* retry,<br>vailableDataPtr|
|**_Service ID[hex]: _**<br>|0x43<br>||
|**_Sync/Async: _**|Synchronous||
|**_Reentrancy: _**|Reentrant||
||id|Identificationofthe transmittedI-PDU.|
||info|Provides the destination buffer (SduDataPtr) and the number<br>of bytes to be copied (SduLength).<br>If not enough transmit data is available, no data is copied by<br>the upper layer module and BUFREQ_E_BUSY is returned.<br>The lower layer module may retry the call.<br>An SduLength of 0 can be used to indicate state changes in<br>the retry parameter or to query the current amount of<br>available data in the upper layer module. In this case, the<br>SduDataPtr may be aNULL_PTR.|
||retry|This parameter is used to acknowledge transmitted data or<br>to retransmit data after transmission problems.|
|**_Parameters (in):_**||If the retry parameter is a NULL_PTR, it indicates that the<br>transmit data can be removed from the buffer immediately<br>after it has been copied. Otherwise, the retry parameter<br>must point to a valid RetryInfoType element.<br>If TpDataState indicates TP_CONFPENDING, the previously<br>copied data must remain in the TP buffer to be available for<br>error recovery.<br>TP_DATACONF indicates that all data that has been copied<br>before this call is confirmed and can be removed from the<br>TP buffer. Data copied by this API call is excluded and will<br>be confirmed later.<br>TP_DATARETRY indicates that this API call shall copy<br>previously copied data in order to recover from an error. In<br>this case TxTpDataCnt specifies the offset in bytes from the<br>current data copy position.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None||
|**_Parameters (out):_**|availableDataPtr|Indicates the remaining number of bytes that are available in<br>the upper layer module's Tx buffer. availableDataPtr can be<br>used by TP modules that support dynamic payload lengths<br>(e.g. FrIsoTp) to determine the size ofthefollowing CFs.|
|**_Return value:_**|BufReq_ReturnType|BUFREQ_OK: Data has been copied to the transmit buffer<br>completely as requested.<br>BUFREQ_E_BUSY: Request could not be fulfilled, because<br>the required amount of Tx data is not available. The lower<br>layer module may retry this call later on. No data has been<br>copied.<br>BUFREQ_E_NOT_OK: Data has not been copied. Request<br>failed.|
|**_Description:_**|This function is called<br>Each call to this funct<br>>TpDataState is TP_<br>data beginning at the<br>>TxTpDataCnt. The s<br>by availableDataPtr.|to acquire the transmit data of an I-PDU segment (N-PDU).<br>ion provides the next part of the I-PDU data unless retry-<br>DATARETRY. In this case the function restarts to copy the<br>offset from the current position indicated by retry-<br>ize of the remaining data is written to the position indicated|



Document ID 015: AUTOSAR_SWS_COM 

102 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**_<mark>Available via:</mark>_** <u>Com.h</u> 

⌋ (SRS_Com_02095) 

**Caveats of Com_CopyTxData:** This function might be called in interrupt context. 

**[SWS_Com_00783]** ⌈ Com_CopyTxData shall copy no data and return BUFREQ_E_NOT_OK in case the given PduId refers to a stopped I-PDU. ⌋ (SRS_Com_00218) 

## **8.5 Scheduled Functions** 

### **8.5.1 Com_MainFunctionRx** 

### **<u>[SWS_Com_00398]</u>** <u>⌈</u> 

|**_Service name: _**|Com_MainFunctionRx|
|---|---|
|**_Syntax:_**|void Com_MainFunctionRx(<br>void<br>)|
|**_Service ID[hex]: _**|0x18|
|**_Description:_**|This function performs the processing of the AUTOSAR COM module's receive<br>processing that are not directly handled within the COM's functions invoked by the<br>PDU-R,forexample Com_RxIndication.|
|**_Available via: _**|SchM_Com.h|



⌋ (SRS_BSW_00425, SRS_BSW_00432) 

**[SWS_Com_00664]** ⌈ A call to Com_MainFunctionRx shall simply return if the AUTOSAR COM module was not previously initialized with a call to Com_Init. ⌋ (SRS_BSW_00425) 

Configuration of Com_MainFunctionRx: see ECUC_Com_00186. 

### **8.5.2 Com_MainFunctionTx** 

### **<u>[SWS_Com_00399]</u>** <u>⌈</u> 

|**_Service name:_**|Com_MainFunctionTx|
|---|---|
|**_Syntax:_**|void Com_MainFunctionTx(<br>void<br>)|
|**_Service ID[hex]: _**|0x19|
|**_Description:_**|This function performs the processing of the AUTOSAR COM module's<br>transmission activities that are not directly handled within the COM's function<br>invoked by theRTE,forexample Com_SendSignal.|
|**_Available via: _**|SchM_Com.h|



⌋ (SRS_BSW_00425, SRS_BSW_00432) 

**[SWS_Com_00665]** ⌈ A call to Com_MainFunctionTx shall simply return if the AUTOSAR COM module was not previously initialized with a call to Com_Init. ⌋ (SRS_BSW_00425) 

Document ID 015: AUTOSAR_SWS_COM 

103 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**Configuration:** see ECUC_Com_00186. 

### **8.5.3 Com_MainFunctionRouteSignals** 

### **<u>[SWS_Com_00400]</u>** <u>⌈</u> 

|**_Service name:_**|Com_MainFunctionRouteSignals|
|---|---|
|**_Syntax:_**|void Com_MainFunctionRouteSignals(<br>void<br>)|
|**_Service ID[hex]: _**|0x1a|
|**_Description:_**|Calls the signal gateway part of the AUTOSAR COM module to forward received<br>signals to berouted.|
|**_Available via: _**|SchM_Com.h|



⌋ (SRS_BSW_00425, SRS_BSW_00432) 

**[SWS_Com_00666]** ⌈ A call to Com_MainFunctionRouteSignals shall simply return if the AUTOSAR COM module was not previously initialized with a call to Com_Init. ⌋ (SRS_BSW_00425) 

### **Caveats of Com_MainFunctionRouteSignals:** 

- The time between two consecutive calls (perhaps the related task/thread cycle) affects directly the signal gateway latency. 

- The insertion of this call is necessary for decoupling receive interrupts and signal gateway tasks. 

- Normally a cyclic task/ thread to call this function is configured. The cycle of this task/thread directly affects the latency of the signal gateway. 

## **8.6 Expected Interfaces** 

### **8.6.1 Mandatory Interfaces** 

This chapter defines all interfaces, which are required to fulfill the core functionality of the module. 

### **<u>[SWS_Com_00669]</u>** <u>⌈</u> 

|**_API function _**|**_Header File_**|**_Description _**|
|---|---|---|
|PduR_ComTransmit|PduR_Com.h|Requests transmissionofaPDU.|



⌋ (SRS_BSW_00384) 

### **8.6.2 Optional Interfaces** 

This chapter defines all interfaces that are required to fulfill an optional functionality of the module. 

### **<u>[SWS_Com_00670]</u>** <u>⌈</u> 

|**_API function _**|**_Header File_**|**_Description _**|
|---|---|---|
|Det_ReportError|Det.h|Service toreport development errors.|
|Det_ReportRuntimeError|Det.h|Service toreportruntime errors. Ifa callouthas been|



Document ID 015: AUTOSAR_SWS_COM 

104 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



<u>configured then this callout shall be called.</u> PduR_ComCancelTransmit PduR_Com.h Requests cancellation of an ongoing transmission of a PDU in a lower layer communication module. 

⌋ (SRS_BSW_00384) 

The associated configuration parameter for API function Det_ReportError is ComConfigurationUseDet (ECUC_Com_00141). 

The API function PduR_ComCancelTransmit must be included if at least one I-PDU has configured ComIPduCancellationSupport to TRUE, see ECUC_Com_00709. 

### **8.6.3 Configurable Interfaces** 

### **8.6.3.1 Callback/ Notification Functions** 

**Caveats of configurable interfaces:** A callback routine runs either on interrupt level or on task level. Thus, the OS restrictions of usage of system functions for interrupt service routines as well as for tasks apply. 

### **<u>[SWS_Com_00468]</u>** <u>⌈</u> 

|**_Service name: _**|Com_CbkTxAck|
|---|---|
|**_Syntax:_**|void Com_CbkTxAck(<br>void<br>)|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|don't care|
|**_Parameters (in): _**|None|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|This callback represents notification class 2 of [17]. It is called immediately after<br>successful transmission of the I-PDU containingthe message.|
|**_Available via: _**|configurable|



⌋ (SRS_BSW_00359, SRS_BSW_00360) 

Com_CbkTxAck is called on sender side only. It can be configured for signals and signal groups. 

Com_CbkTxAck corresponds to Rte_COMCbkTAck_<sn> or Rte_COMCbkTAck_<sg> respectively. 

The callback function name must be configured by ComNotification (ECUC_Com_00498). 

### **<u>[SWS_Com_00491]</u>** <u>⌈</u> 

|**_Service name: _**|Com_CbkTxErr|
|---|---|
|**_Syntax:_**|void Com_CbkTxErr(|



Document ID 015: AUTOSAR_SWS_COM 

105 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||void<br>)|
|---|---|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|don't care|
|**_Parameters (in): _**|None|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|This callback corresponds to notification class 4 of [17]. It is called in case the<br>transmission isnot possible because the correspondingI-PDU groupis stopped.|
|**_Available via: _**|configurable|



⌋ (SRS_BSW_00359, SRS_BSW_00360) 

Com_CbkTxErr is called on sender side only. This callback function corresponds to Rte_COMCbkTErr_<sn> or Rte_COMCbkTErr_<sg> respectively. 

The callback function name must be configured by ComErrorNotification (ECUC_Com_00499). 

### **<u>[SWS_Com_00554]</u>** <u>⌈</u> 

|**_Service name: _**|Com_CbkTxTOut|
|---|---|
|**_Syntax:_**|void Com_CbkTxTOut(<br>void<br>)|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|don't care|
|**_Parameters (in): _**|None|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|This callback corresponds to notification class 4 of [17]. It is called immediately<br>after a message transmission error has been detected by the deadline monitoring<br>mechanism.|
|**_Available via: _**|configurable|



⌋ (SRS_BSW_00359, SRS_BSW_00360) 

Com_CbkTxTOut is called on sender side only. It can be configured for signals and signal groups. 

This callback function corresponds to Rte_COMCbkTxTOut_<sn> or Rte_COMCbkTxTOut_<sg> respectively. 

The callback function name must be configured by ComTimeoutNotification (ECUC_Com_00552). 

### **<u>[SWS_Com_00555]</u>** <u>⌈</u> 

|**_Service name: _**|Com_CbkRxAck|
|---|---|
|**_Syntax:_**|void Com_CbkRxAck(<br>void<br>)|
|**_Sync/Async: _**|Synchronous|



Document ID 015: AUTOSAR_SWS_COM 

106 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Reentrancy: _**|don't care|
|---|---|
|**_Parameters (in): _**|None|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|This callback represents notification class 1 of [17]. It is called immediately after<br>themessagehas beenstoredinthereceivingmessage object.|
|**_Available via: _**|configurable|



⌋ (SRS_BSW_00359, SRS_BSW_00360) 

Com_CbkRxAck is called on receiver side only. It can be configured for signals and signal groups. 

Com_CbkRxAck corresponds to Rte_COMCbk_<sn> or Rte_COMCbk_<sg> respectively. 

The callback function name must be configured by ComNotification (ECUC_Com_00498). 

### **<u>[SWS_Com_00556]</u>** <u>⌈</u> 

|**_Service name: _**|Com_CbkRxTOut|
|---|---|
|**_Syntax:_**|void Com_CbkRxTOut(<br>void<br>)|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|don't care|
|**_Parameters (in): _**|None|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters(out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|This callback corresponds to notification class 3 of [17]. It is called immediately<br>after a message reception error has been detected by the deadline monitoring<br>mechanism.|
|**_Available via: _**|configurable|



⌋ (SRS_BSW_00359, SRS_BSW_00360) 

Com_CbkRxTOut is called on receiver side only. It can be configured for signals and signal groups. 

This callback function corresponds to Rte_COMCbkRxTOut_<sn> or Rte_COMCbkRxTOut_<sg> respectively. 

The callback function name must be configured by ComTimeoutNotification (see ECUC_Com_00552). 

### **<u>[SWS_Com_00536]</u>** <u>⌈</u> 

|**_Service name: _**|Com_CbkInv|
|---|---|
|**_Syntax:_**|void Com_CbkInv(<br>void<br>)|



Document ID 015: AUTOSAR_SWS_COM 

107 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Sync/Async: _**|Synchronous|
|---|---|
|**_Reentrancy: _**|don't care|
|**_Parameters (in): _**|None|
|**_Parameters_**<br>**_(in-_**<br>**_out): _**|None|
|**_Parameters (out): _**|None|
|**_Return value: _**|None|
|**_Description:_**|This callback function corresponds to SWS_Com_00680. It is called after<br>receptionofan invalid signalorsignalgrouprespectively.|
|**_Available via: _**|configurable|



⌋ (SRS_BSW_00359, SRS_BSW_00360, SRS_Com_02079) 

Com_CbkInv is called on receiver side only. It can be configured for signals, group signals and signal groups. 

This callback function corresponds to Rte_COMCbkInv_<sn> (for signals and group signals) and Rte_COMCbkInv_<sg> respectively. 

The callback function name must be configured by ComInvalidNotification (ECUC_Com_00315). 

### **<u>[SWS_Com_00726]</u>** <u>⌈</u> 

|**_Service name: _**|Com_CbkCounterErr|
|---|---|
|**_Syntax:_**|void Com_CbkCounterErr(<br>PduIdType ComPduId,<br>uint8 ExpectedCounter,<br>uint8 ReceivedCounter<br>)|
|**_Sync/Async: _**|Synchronous|
|**_Reentrancy: _**|don't care|
||ComPduId<br>Id oftheI-PDUforthat a counter mismatch was detected|
|**_Parameters (in):_**|ExpectedCounter<br>The expected counter value|
||ReceivedCounter<br>Thereceived counter value|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>None|
|**_Parameters (out): _**|None|
|**_Return value:_**|None|
|**_Description:_**|This function is called immediately, if the AUTOSAR COM module receives an I-<br>PDU counterthat differsfromthe expected one.|
|**_Available via: _**|configurable|



⌋ (SRS_Com_02102) 

Com_CbkCounterErr is called on receiver side only. It can be configured per I-PDU counter. The callback function name must be configured by ComIPduCounterErrorNotification (ECUC_Com_00003). 

### **8.6.3.2 I-PDU Callout Functions** 

As stated in SWS_Com_00013 _Network-order message callout_ and _CPU-order message callout_ are not supported by the AUTOSAR COM module. The only callout method supported by the AUTOSAR COM module therefore is the I-PDU callout. The AUTOSAR COM module supports I-PDU callouts on sender and on receiver side. 

Document ID 015: AUTOSAR_SWS_COM 

108 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



As specified in [17], if the I-PDU callout returns false the I-PDU will not be processed any further. 

### **<u>[SWS_Com_00700]</u>** <u>⌈</u> 

|**_Service name:_**|Com_RxI|pduCallout|
|---|---|---|
|**_Syntax:_**|boolean C<br>PduIdT<br>const P<br>)|om_RxIpduCallout(<br>ype PduId,<br>duInfoType* PduInfoPtr|
|**_Service ID[hex]: _**|0x2A||
|**_Sync/Async: _**|Synchron|ous|
|**_Reentrancy: _**|don't care||
||PduId|IDofthereceivedI-PDU.|
|**_Parameters (in):_**|PduInfoP|tr Contains the length (SduLength) of the received I-PDU and a pointer to<br>the data oftheI-PDU (SduDataPtr).|
|**_Parameters_**<br>**_(in-_**<br>**_out): _**|None||
|**_Parameters (out): _**|None||
|**_Return value:_**|boolean|true: I-PDU will be processed normal<br>false: I-PDUwill not be processed anyfurther|
|**_Description:_**|The I-PD<br>receive fil|U callout on receiver side can be configured to implement user-defined<br>teringmechanisms.|
|**_Available via: _**|configura|ble|



⌋ (SRS_Com_02037) 

The callout function name must be configured by ComIPduCallout (ECUC_Com_00387). 

**[SWS_Com_00816]** ⌈ The AUTOSAR COM module shall forward all data of the received I-PDU (i.e. the complete I-PDU as provided by the PduR) in the Com_RxIpduCallout. ⌋ (SRS_Com_02037) 

### **<u>[SWS_Com_00346]</u>** <u>⌈</u> 

|**_Service name: _**|Com_TxIpdu|Callout|
|---|---|---|
|**_Syntax:_**|boolean Co<br>PduIdTyp<br>PduInfoTy<br>)|m_TxIpduCallout(<br>e PduId,<br>pe* PduInfoPtr|
|**_Service ID[hex]: _**|0x29||
|**_Sync/Async: _**|Synchronou|s|
|**_Reentrancy: _**|don't care||
|**_Parameters (in): _**|PduId|IDofthe transmittedI-PDU.|
|**_Parameters_**<br>**_(in_**<br>**_out): _**|**_-_**<br>PduInfoPtr|Contains the length (SduLength) of the transmitted I-PDU and a<br>pointerto the data oftheI-PDU (SduDataPtr).|
|**_Parameters (out): _**|None||
|**_Return value:_**|boolean|true: I-PDU will be processed normal<br>false: I-PDUwill not be processed anyfurther|
|**_Description:_**|The I-PDU c<br>user-defined<br>the outgoing|allout on sender side can be configured for example to implement<br>transmission filtering or user-defined pre-transmission-processing of<br>I-PDU.|
|**_Available via: _**|configurable||



⌋ (SRS_Com_02037) 

Document ID 015: AUTOSAR_SWS_COM 

109 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



The callout function name must be configured either by ComIPduCallout (ECUC_Com_00387) or by ComIPduTriggerTransmitCallout (ECUC_Com_00765). 

The AUTOSAR COM module implements no means to detect or prevent possible recursions that may occur when I-PDUs are triggered by actions within an I-PDU callout. It is solely in the responsibility of the implementer of an I-PDU callout and the system integrator that unwanted or endless chains of I-PDU callouts are avoided. 

**[SWS_Com_00381]** ⌈ The AUTOSAR COM module shall not support that other AUTOSAR COM module’s APIs than Com_TriggerIPDUSend, Com_TriggerIPDUSendWithMetaData, Com_SendSignal and Com_SendSignalGroup can be called out of an I-PDU callout. ⌋ (SRS_Com_02037) 

**[SWS_Com_00766]** ⌈ In case a ComIPduTriggerTransmitCallout is configured for an I-PDU and the I-PDU is started, the AUTOSAR COM module shall invoke this I-PDU callout within every execution of Com_TriggerTransmit for this I-PDU. ⌋ (SRS_Com_02037) 

**[SWS_Com_00395]** ⌈ When Com_TriggerTransmit is called, the AUTOSAR COM module shall ignore the return value from the ComIPduTriggerTransmitCallout. ⌋ (SRS_Com_02037) 

**[SWS_Com_00719]** ⌈ In case a ComIPduCallout is configured for an I-PDU with ComIPduDirection configured to _SEND_ , the AUTOSAR COM module shall invoke this I-PDU callout diretly before the I-PDU is transmitted via PduR_ComTransmit. ⌋ (SRS_Com_02037) 

For TP I-PDUs, the I-PDU callout functions are handled similar to the I-PDU callout functions of normal I-PDUs and are supported both on transmitter and receiver side. Note that for example the requirement SWS_Com_00719 does not consider the configured ComIPduType. 

**[SWS_Com_00720]** ⌈ When a large I-PDU is received successfully via the TP interface, the I-PDU callout shall take place within the invocation of Com_TpRxIndication. ⌋ (SRS_Com_02095) 

**[SWS_Com_00839]** ⌈ When the I-PDU callout in context of Com_TpRxIndication returns false, the I-PDU shall be considered as incorrectly received and therefore all included signals shall be treated exactly like invalidated signals. That is, the AUTOSAR COM module shall execute all configured ComDataInvalidActions for all included signals and signal groups. ⌋ (SRS_Com_02095) 

Document ID 015: AUTOSAR_SWS_COM 

110 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **9 Sequence Diagrams** 

A sequence diagram of the underlying communication stack can be found in [17]. 

## **9.1 Interface between the AUTOSAR COM Module and the PDU Router** 

The following chart shows the communication between the AUTOSAR COM module and the PDU Router. 

Document ID 015: AUTOSAR_SWS_COM 

111 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 





<!-- Start of picture text -->
«module» «module»<br>Com PduR<br>seq Reception CAN, LIN, FlexRay<br>Com_RxIndication(PduIdType, const PduInfoType*)<br>Internal<br>processing()<br>seq Transmission LIN, FlexRay<br>PduR_ComTransmit(Std_ReturnType, PduIdType, const PduInfoType*):<br>Std_ReturnType<br>internal<br>processing()<br>E_OK()<br>internal<br>processing()<br>Com_TriggerTransmit(Std_ReturnType, PduIdType, PduInfoType*)<br>Internal<br>processing()<br>Com_TxConfirmation(PduIdType, Std_ReturnType)<br>Internal<br>processing()<br>seq Transmission CAN<br>PduR_ComTransmit(Std_ReturnType, PduIdType, const PduInfoType*):<br>Std_ReturnType<br>E_OK()<br>Com_TxConfirmation(PduIdType, Std_ReturnType)<br>Internal<br>processing()<br><!-- End of picture text -->

**Figure 6: Interactions between the AUTOSAR COM module and the PDU router** 

Document ID 015: AUTOSAR_SWS_COM 

112 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



## **9.2 Confirmation Handling between the PDU Router, the AUTOSAR COM Module and the RTE** 

The following chart shows the confirmation handling with respect to the two different IPDU-processing modes. (See also Chapter 7.3.5.4.) 



<!-- Start of picture text -->
«module» «module» «module»<br>Rte Com PduR<br>alt Unpacking<br>[Unpack.Immediate] Com_TxConfirmation(PduIdType, Std_ReturnType)<br>Rte_COMCbkTAck_signalX()<br>internal processing<br>()<br>Rte_COMCbkTAck_signalY()<br>internal processing<br>()<br>[Unpack.Deferred]<br>Com_TxConfirmation(PduIdType, Std_ReturnType)<br>set<br>flag<br>()<br>check<br>flag()<br>alt check flag<br>[flag set]<br>Rte_COMCbkTAck_signalX()<br>internal processing<br>()<br>Rte_COMCbkTAck_signalY()<br>internal processing<br>()<br>[flag not set]<br><!-- End of picture text -->

**Figure 7: Confirmation handling between the PDU Router, the AUTOSAR COM module and the RTE** 

Document ID 015: AUTOSAR_SWS_COM 

113 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



## **9.3 Indication Handling between the PDU Router, the AUTOSAR COM Module and the RTE** 

The following chart shows the indication handling with respect to the two different unpacking modes. (See also Chapter 7.3.5.4.) 



<!-- Start of picture text -->
«module» «module» «module»<br>Rte Com PduR<br>alt Unpacking<br>[Unpack.Immediate] Com_RxIndication(PduIdType, PduInfoType*)<br>Rte_COMCbk_signalX()<br>internal processing<br>()<br>Rte_COMCbk_signalY()<br>internal processing<br>()<br>[Unpack.Deferred]<br>Com_RxIndication(PduIdType, PduInfoType*)<br>set flag, copy data<br>()<br>check flag<br>()<br>alt check flag<br>[flag set]<br>Rte_COMCbk_signalX()<br>internal processing<br>()<br>Rte_COMCbk_signalY()<br>internal processing<br>()<br>[flag not set]<br><!-- End of picture text -->

**Figure 8: Indication handling between the PDU Router, the AUTOSAR COM module and the RTE** 

Document ID 015: AUTOSAR_SWS_COM 

114 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **10 Configuration Specification** 

## **10.1 Containers and Configuration Parameters** 

The following chapters summarize all configuration parameters. The detailed meanings of the parameters are described in Chapter 7 and Chapter 8. 

**[SWS_Com_00006]** ⌈ The configuration parameters are based on [18]. All parameters shall be stored in an XML format. ⌋ (SRS_Com_02040) 

Document ID 015: AUTOSAR_SWS_COM 

115 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **10.1.1 Configuration of the AUTOSAR COM Module** 

For an overview of the AUTOSAR COM module’s configuration, see Figure 9. 



<!-- Start of picture text -->
EcucIntegerParamDefComMaxIPduCnt : EcucIntegerParamDefComDataMemSize : Com :EcucModuleDef +container EcucParamConfContainerDefComGeneral :<br>lowerMultiplicity = 0upperMultiplicity = 1 lowerMultiplicity = 0upperMultiplicity = 1 upperMultiplicity = 1lowerMultiplicity = 0 upperMultiplicity = 1lowerMultiplicity = 1<br>+parameter +parameter<br>+container<br>ComConfig :EcucParamConfContainerDef<br>+subContainer +subContainer +subContainer +subContainer<br>ComIPdu : ComSignalGroup : ComSignal : ComIPduGroup :<br>EcucParamConfContainerDef +destination EcucParamConfContainerDef EcucParamConfContainerDef EcucParamConfContainerDef<br>lowerMultiplicity = 0 lowerMultiplicity = 0 lowerMultiplicity = 0 lowerMultiplicity = 0<br>+destination upperMultiplicity = * upperMultiplicity = * upperMultiplicity = * upperMultiplicity = * +subContainer<br>+subContainer +subContainer +destination ComTimeBase :EcucParamConfContainerDef<br>ComTxIPdu : ComGroupSignal :<br>EcucParamConfContainerDef EcucParamConfContainerDef<br>upperMultiplicity = 1 lowerMultiplicity = 0<br>lowerMultiplicity = 0 upperMultiplicity = * +parameter +parameter<br>+subContainer +subContainer +destination +subContainer +subContainer EcucFloatParamDefComGwTimeBase : EcucFloatParamDefComRxTimeBase :<br>ComTxModeTrue : ComTxModeFalse : ComFilter : min = 0 min = 0<br>EcucParamConfContainerDef EcucParamConfContainerDef EcucParamConfContainerDef max = INF max = INF<br>lowerMultiplicity = 0 lowerMultiplicity = 0<br>upperMultiplicity = 1 upperMultiplicity = 1 upperMultiplicity = 1 upperMultiplicity = 1 upperMultiplicity = 1<br>lowerMultiplicity = 0 lowerMultiplicity = 0 lowerMultiplicity = 0 +subContainer +parameter<br>+subContainer<br>+subContainer +subContainer ComGwMapping :EcucParamConfContainerDef EcucFloatParamDefComTxTimeBase :<br>ComTxMode :<br>EcucParamConfContainerDef lowerMultiplicity = 0upperMultiplicity = * min = 0max = INF<br>lowerMultiplicity = 0<br>+subContainer +subContainer upperMultiplicity = 1<br>ComGwSignalRef : ComGwSource : ComGwDestination :<br>EcucChoiceReferenceDef EcucChoiceContainerDef EcucChoiceContainerDef<br>lowerMultiplicity = 1<br>+reference upperMultiplicity = *<br>ComGwIPduRef :EcucReferenceDef +choice +choice<br>ComGwSignal :<br>+reference +reference EcucParamConfContainerDef<br>upperMultiplicity = 1<br>lowerMultiplicity = 0<br>+choice<br>ComGwSourceDescription :<br>EcucParamConfContainerDef<br>upperMultiplicity = 1 +choice<br>lowerMultiplicity = 0<br>ComGwDestinationDescription :<br>EcucParamConfContainerDef<br>upperMultiplicity = 1<br>lowerMultiplicity = 0<br><!-- End of picture text -->

**Figure 9: The AUTOSAR COM module’s Configuration Overview** 

Document ID 015: AUTOSAR_SWS_COM 

116 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **10.1.2 Com** 

|**_SWS Item_**|**ECUC_Com_00540 :**|
|---|---|
|**_Module Name_**|_Com_|
|**_Module Description_**|Configuration of the AUTOSAR COM module.|
|**_Post-Build Variant Support_**|true|
|**_Supported Config Variants  _**|VARIANT-LINK-TIME,VARIANT-POST-BUILD,VARIANT-PRE-COMPILE|



|**_Included Containers_**||
|---|---|
|**_Container Name_**|**_Multiplicity_**<br>**_Scope / Dependency_**|
|ComConfig|1<br>This container contains the configuration parameters and sub<br>containers oftheAUTOSARCOM module.|
|ComGeneral|1<br>Contains the general configuration parameters of the<br>AUTOSAR COM module.|



### **10.1.3 ComGeneral** 

|**_SWS Item_**|**ECUC_Com_00541 :**||
|---|---|---|
|**_Container Name_**|ComGeneral||
|**_Description_**|Contains thegeneral config|urationparameters of the module.|
|**_Configuration Parameters_**|||
|**_SWS Item_**|**ECUC_Com_10000 :**||
|**_Name_**|ComCancellationSupport||
|**_Parent Container_**|ComGeneral||
|**_Description_**|This parameter enables/dis<br>true: enabled<br>false: disabled|ables the cancellation feature:|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucBooleanParamDef||
|**_Default value_**|true||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false||
|**_Post-Build Variant Value_**|false||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  All Variants|
|**_Class_**|**_Link time_**|--|
||**_Post-build time_**|--|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X  All Variants|
||**_Link time_**|--|
||**_Post-build time_**|--|
|**_Scope / Dependency_**|scope: local||
|**_SWS Item_**|**ECUC_Com_00141 :**||
|**_Name_**|ComConfigurationUseDet||
|**_Parent Container_**|ComGeneral||
|**_Description_**|The error hook shall contain<br>If this parameter is configur<br>to ON as output of the confi|code to call the Det.<br>ed COM_DEV_ERROR_DETECT shall be set<br>guration tool.(as input for the source code).|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucBooleanParamDef||
|**_Default value_**|--||



117 of 185 

Document ID 015: AUTOSAR_SWS_COM 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|---|---|---|---|
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**<br>|**_Pre-compile time_**|X|All Variants|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**<br>|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00788 :**|||
|**_Name_**|ComEnableMDTForCyclic|Transm|ission|
|**_Parent Container_**|ComGeneral|||
|**_Description_**|Enables globally for the wh<br>monitoring for cyclic and re<br>(ComTxModeMode=PERI<br>cyclic transmissions, Com<br>transmissions).|ole Co<br>peated<br>ODIC or<br>TxMode|m module the minimum delay time<br>transmissions<br>ComTxModeMode=MIXED for the<br>NumberOfRepetitions > 0 for repeated|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucBooleanParamDef|||
|**_Default value_**|true|||
|**_Post-Build Variant Multipli-_**|<br>|||
|<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|All Variants|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br> <br>**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_10002 :**|||
|**_Name_**|ComEnableSignalGroupAr|rayApi||
|**_Parent Container_**|ComGeneral|||
|**_Description_**|Activate/Deactivate the sig<br>(Com_SendSignalGroupAr<br>true: signal group array ac|nal gro<br>ray, Co<br>cess AP|up array access APIs<br>m_ReceiveSignalGroupArray).<br>Is activated|
||false: signalgrouparraya<br>|ccess A|PIs deactivated|
|**_Multiplicity_**|1|||
|**_Type_**|EcucBooleanParamDef|||
|**_Default value_**|false|||
|**_Post-Build Variant Value_**|false|||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_10004 :**|||
|**_Name_**|ComMetaDataSupport|||
|<br>**_Parent Container_**|<br>ComGeneral|||
|**_Description_**|This parameter enables/di<br>including the API Com_Tri<br>true:enabled|sables t<br>ggerIPD|he support of meta-data feature<br>USendWithMetaData.|



Document ID 015: AUTOSAR_SWS_COM 

118 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Multiplicity_**|false: disabled<br>0..1|||
|---|---|---|---|
|**_Type_**|EcucBooleanParamDef|||
|**_Default value_**|false|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X|All Variants|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00780 :**|||
|**_Name_**|ComRetryFailedTransmitRe|quests||
|**_Parent Container_**|ComGeneral|||
|**_Description_**|If this Parameter is set to tru<br>|e, retr<br>|y of failed transmission requests is<br>|
||enabled. If this Parameter is|notpr|esent,the default value is assumed.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucBooleanParamDef|||
|**_Default value_**|false|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|All Variants|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUCCom00710 :**|||
|**_Name_**|**__**<br>ComSupportedIPduGroups|||
|**_Parent Container_**|ComGeneral|||
|**_Description_**|Defines the maximum numb|er of s|upported I-PDUgroups.|
|**_Multiplicity_**|1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|0 .. 65535|||
|**_Default value_**|--|||
|**_Post-Build Variant Value_**|false|||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_10001 :**|||
|**_Name_**|ComUserCbkHeaderFile|||
|<br>**_Parent Container_**|<br>ComGeneral|||
|**_Description_**|Defines the header files for<br>the COM module.|callbac|k functions which shall be included by|
|**_Multiplicity_**|0..*|||
|**_Type_**<br>**_Default value_**|EcucStringParamDef<br>--|||



119 of 185 

Document ID 015: AUTOSAR_SWS_COM 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_maxLength_**|32|||
|---|---|---|---|
|**_minLength_**|1|||
|**_regularExpression_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|All Variants|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00438 :**|||
|**_Name_**|ComVersionInfoApi|||
|**_Parent Container_**|ComGeneral|||
|**_Description_**|Activate/Deactivate the ver<br>True: version information A<br>False: version information|sion in<br>PI acti<br>API de|formation API (Com_GetVersionInfo).<br>vated<br>activated|
|**_Multiplicity_**|1|||
|**_Type_**|EcucBooleanParamDef|||
|**_Default value_**|false|||
|**_Post-Build Variant Value_**|false|||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||



#### **_<mark>No Included Containers</mark>_** 

### **10.1.4 ComConfig** 

|**_SWS Item_**|**ECUC_Com_00337 :**|
|---|---|
|**_Container Name_**|ComConfig|
|**_Description_**|This container contains the configuration parameters and sub containers of<br>the AUTOSAR COM module.|
|**_Configuration Parameters_**||
|**_SWS Item_**|**ECUC_Com_00783 :**|
|**_Name_**|ComDataMemSize|
|**_Parent Container_**|ComConfig|
|**_Description_**|Size of internal Com data in units of bytes (static memory allocation) -<br>memory required by post-build configuration must be smaller than this<br>constant. This parameter is needed only in case of post-build loadable<br>implementation usingstatic memoryallocation.|
|**_Multiplicity_**|0..1|
|**_Type_**|EcucIntegerParamDef|
|**_Range_**|0 ..<br>18446744073709551615|
|**_Default value_**|--|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|



Document ID 015: AUTOSAR_SWS_COM 

120 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Post-Build Variant Value_**|false|||
|---|---|---|---|
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00782 :**|||
|**_Name_**|ComMaxIPduCnt|||
|**_Parent Container_**|ComConfig|||
|**_Description_**|Maximum number of IPdus.<br>build loadable implementati|This<br>on usi|parameter is needed only in case of post-<br>ngstatic memoryallocation.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|0 ..<br>18446744073709551615|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||



|**_Included Containers_**|||
|---|---|---|
|**_Container Name_**|**_Multiplicit_**|**_y_**<br>**_Scope / Dependency_**|
|ComGwMapping|0..*|Each instance of this container defines one mapping of the<br>integrated Signal Gateway.|
|ComIPdu|0..*|See ECUC_Com_00340, if there is no ComIpdu container<br>included no IPDUs are defined. In this case no communication<br>via the AUTOSAR COM module ispossible.|
|ComIPduGroup|0..*|See ECUC_Com_00341, if there is no ComIPduGroup<br>container included then no IPDU group is defined. In this case<br>no communication via the AUTOSAR COM module ispossible.|
|ComSignal|0..*|See ECUC_Com_00344, if there is no ComSignal container<br>included no single signals are defined.|
|ComSignalGroup|0..*|See ECUC_Com_00345, if there is no ComSignalGroup<br>container included no signalgroups are defined.|
|ComTimeBase|1|Contains the timebaseparameters for Tx,Rx and routing.|



### **10.1.5 ComTimeBase** 

|**_SWS Item_**|**ECUC_Com_00730 :**|
|---|---|



Document ID 015: AUTOSAR_SWS_COM 

121 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Container Name_**<br>|ComTimeBase<br>|||
|---|---|---|---|
|**_Description_**|Contains the timebasepar|ameter|s for Tx,Rx and routing.|
|**_Configuration Parameters_**||||
|**_SWS Item_**|**ECUC_Com_00729 :**|||
|**_Name_**<br>|ComGwTimeBase<br>|||
|**_Parent Container_**|ComTimeBase|||
|**_Description_**|The period between succe<br>in seconds. This paramete<br>transform the values of the<br>parameters of the COM m<br>or tick values. The COM m<br>implementation specific.<br>The COM module (generat<br>Com_MainFunctionRouteS<br>configured here.|ssive c<br>r may b<br>signal<br>odule to<br>odule's<br>or) mig<br>ignals|alls to Com_MainFunctionRouteSignals<br>e used by the COM generator to<br>gateway related timing configuration<br>internal implementation specific counter<br>internal timing handling is<br>ht rely on the fact that<br>is scheduled according to the value|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucFloatParamDef|||
|**_Range_**|]0 .. INF[|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**|<br>false|||
|**_city_**||||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME VARIANT-POST-|
||||,<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-|
||||<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: ECU|||
|**_SWS Item_**|**ECUC_Com_00728 :**|||
|**_Name_**|ComRxTimeBase|||
|**_Parent Container_**|ComTimeBase|||
|**_Description_**|The period between succe<br>This parameter may be us<br>values of the reception rela<br>module to internal impleme<br>COM module's internal tim<br>The COM module (generat<br>Com_MainFunctionRx is s<br>|ssive c<br>ed by th<br>ted tim<br>ntation<br>ing han<br>or) ma<br>chedule|alls to Com_MainFunctionRx in seconds.<br>e COM generator to transform the<br>ing configuration parameters of the COM<br>specific counter or tick values. The<br>dling is implementation specific.<br>y rely on the fact that<br>d according to the value configured|
||here.|||
|**_Multiplicity_**|0..1|||
|**_Type_**<br>|EcucFloatParamDef<br>|||
|**_Range_**|]0 .. INF[|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_cit_**|<br>false|||
|**_y_**<br>**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|<br><br>**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-|
||||BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||<br><br>**_Link time_**|X|VARIANT-LINK-TIME,VARIANT-POST-|



122 of 185 

Document ID 015: AUTOSAR_SWS_COM 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||||BUILD|
|---|---|---|---|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: ECU|||
|**_SWS Item_**|**ECUC_Com_00186 :**|||
|**_Name_**|ComTxTimeBase|||
|**_Parent Container_**|ComTimeBase|||
|**_Description_**|The period between succe<br>This parameter may be us<br>values of the transmission<br>COM module to internal im<br>The COM module's intern<br>The COM module (genera<br>Com_MainFunctionTx is s|ssive c<br>ed by t<br>related<br>pleme<br>al timing<br>tor) ma<br>chedule|alls to Com_MainFunctionTx in seconds.<br>he COM generator to transform the<br>timing configuration parameters of the<br>ntation specific counter or tick values.<br>handling is implementation specific.<br>y rely on the fact that<br>d accordingto the value configured here.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucFloatParamDef|||
|**_Range_**|]0 .. INF[|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||<br><br>**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: ECU|||



**_<mark>No Included Containers</mark>_** 

### **10.1.6 ComFilter** 

|**_SWS Item_**|**ECUC_Com_00339 :**|
|---|---|
|**_Container Name_**|ComFilter|
|**_Description_**|This container contains the configuration parameters of the AUTOSAR<br>COM module's Filters.<br>Note: On sender side the container is used to specify the transmission<br>mode conditions.|
|**_Configuration Parameters_**||



|**_SWS Item_**|**ECUC_Com_00146 :**|
|---|---|
|**_Name_**|ComFilterAlgorithm|
|**_Parent Container_**|ComFilter|
|**_Description_**|The range of values is specified in the [17] specification, chapter 2.2.2, Reception<br>Filtering.|
|**_Multiplicity_**|1|
|**_Type_**|EcucEnumerationParamDef|
|**_Range_**|ALWAYS<br>--|
||MASKED_NEW_DIFFERS_MASKED_OLD<br>--|
||MASKED_NEW_DIFFERS_X<br>--|



123 of 185 

Document ID 015: AUTOSAR_SWS_COM 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||MASKED<br>NEVER|_NEW_EQUALS_X||--<br>--|
|---|---|---|---|---|
||NEW_IS_|OUTSIDE||--|
||NEW_IS_|WITHIN||--|
|<br>|ONE_EV<br>|ERY_N||--|
|**_Post-Build_**<br>**_Vari-_**<br>**_ant Value_**|false||||
|**_Value Configura-_**<br>|<br>**_Pre-comp_**|**_ile time_**||X  VARIANT-PRE-COMPILE|
|**_tion Class_**|**_Link time_**|||X  VARIANT-LINK-TIME,<br>VARIANT-POST-BUILD|
||**_Post-buil_**|**_d time_**||<br>--|
|**_Scope / Depen-_**|<br>scope: loc|al|||
|**_dency_**|||||
|**_SWS Item_**||**ECUC_Com_00235 :**|||
|**_Name_**||ComFilterMask|||
|**_Parent Container_**||ComFilter|||
|**_Description_**<br>||The name of this attribute<br>specification of Reception<br>|corresp<br>Filtering|onds to the parameter name in the [17]<br>.|
|**_Multiplicity_**||0..1|||
|**_Type_**||EcucIntegerParamDef|||
|**_Range_**||-2147483648 ..|||
|||4294967295|||
|**_Default value_**||--|||
|**_Post-Build Varian_**|**_t Multipli-_**|<br>fl|||
|**_city_**||ase|||
|**_Post-Build Varian_**<br> <br>|**_t Value_**<br>|false<br><br>|||
|**_Multiplicity_**<br>**_Con_**|**_figuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|<br><br>**_Class_**||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-|
|||||<br>BUILD|
|||**_Post-build time_**|--||
|**_Value Configurati_**|**_on Class_**|**_Pre-compile time_**<br>|X<br>|VARIANT-PRE-COMPILE<br>|
|||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-|
|||||<br>BUILD|
|||**_Post-build time_**|--||
|**_Scope / Dependen_**|**_cy_**|scope: local|||
|**_SWS Item_**||**ECUC_Com_00317 :**|||
|**_Name_**||ComFilterMax|||
|**_Parent Container_**||ComFilter|||
|**_Description_**||The name of this attribute<br>specification of Reception|corresp<br>Filtering|onds to the parameter name in the [17]<br>.|
|**_Multiplicity_**||0..1|||
|**_Type_**||EcucIntegerParamDef|||
|**_Range_**||-2147483648 ..<br>|||
|||4294967295|||
|**_Default value_**||--|||
|**_Post-Build Varian_**|**_t Multipli-_**|<br>false|||
|**_city_**|||||
|**_Post-Build Varian_**|**_t Value_**|false|||
|**_Multiplicity_**<br>**_Con_**|**_figuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|<br><br>**_Class_**||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-|
|||||BUILD|
|||**_Post-build time_**<br>|--<br>|<br>|
|**_Value Configurati_**|**_on Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|||**_Linktime_**|X|VARIANT-LINK-TIME,VARIANT-POST-|



Document ID 015: AUTOSAR_SWS_COM 

124 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||**_Post-build time_**|--|BUILD<br>|
|---|---|---|---|
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00318 :**|||
|**_Name_**|ComFilterMin|||
|**_Parent Container_**|ComFilter|||
|**_Description_**|The name of this attribute<br>specification of Reception|corresp<br>Filtering|onds to the parameter name in the [17]<br>.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|-2147483648 ..|||
||4294967295|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>|
||||BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>|
||||BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00313 :**|||
|**_Name_**|ComFilterOffset|||
|**_Parent Container_**|ComFilter|||
|**_Description_**|The name of this attribute<br>specification of Reception<br>Range = 0..(ComFilterPeri|corresp<br>Filtering<br>od-1)|onds to the parameter name in the [17]<br>.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|0 .. 4294967294|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>|
||||BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
||dependency: ECUC_Com|_00312||
|**_SWS Item_**|**ECUC_Com_00312 :**|||
|**_Name_**|ComFilterPeriod|||
|**_Parent Container_**|ComFilter|||
|**_Description_**|This parameter defines the<br>ONE_EVERY_N.|period|of the ComFilterAlgorithm|



Document ID 015: AUTOSAR_SWS_COM 

125 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Multiplicity_**|0..1|||
|---|---|---|---|
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|2 .. 4294967295|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true|||
|**_Post-Build Variant Value_**|true|||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|<br> <br>**_Class_**|<br><br>**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00147 :**|||
|**_Name_**|ComFilterX|||
|**_Parent Container_**|ComFilter|||
|**_Description_**|The name of this attribute<br>specification of Reception|corresp<br>Filterin|onds to the parameter name in the [17]<br>g.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|-2147483648 ..<br>4294967295|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||



**_<mark>No Included Containers</mark>_** 

### **10.1.7 ComIPdu** 

|**_SWS Item_**|**ECUC_Com_00340 :**||
|---|---|---|
|**_Container Name_**|ComIPdu||
|**_Description_**|Contains the configuration<br>PDUs.|parameters of the AUTOSAR COM module's I-|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Configuration Parameters_**|||



Document ID 015: AUTOSAR_SWS_COM 

126 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_SWS Item_**|**ECUC_Com_00387 :**|||
|---|---|---|---|
|**_Name_**|ComIPduCallout|||
|**_Parent Container_**|ComIPdu|||
|**_Description_**|This parameter defines the<br>the corresponding I-PDU. I<br>shall takeplace for the cor|existe<br>f this p<br>respon|nce and the name of a callout function for<br>arameter is omitted no I-PDU callout<br>dingI-PDU.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucFunctionNameDef|||
|**_Default value_**|--|||
|**_maxLength_**|--|||
|**_minLength_**|--|||
|**_regularExpression_**|--|||
|**_Post-Build Variant Multipli-_**|<br>fl|||
|**_city_**|ase|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X|All Variants|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00709 :**|||
|**_Name_**|ComIPduCancellationSupp|ort||
|**_Parent Container_**|ComIPdu|||
|**_Description_**|Defines for I-PDUs with Co<br>modul supports cancellatio<br>Defines for I-PDUs with Co<br>supports RX and TX cance|mIPdu<br>n of tra<br>mIPdu<br>llation|Type NORMAL: If the underlying IF-<br>nsmit requests.<br>Type TP: If the underlying TP-module<br>of ongoingrequests.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucBooleanParamDef|||
|**_Default value_**|false|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true|||
|**_Post-Build Variant Value_**|true|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|--||
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: ECU<br>dependency: This paramet<br>ComCancellationSupport i|er shal<br>s set to|l not be set to true if<br>false|



|**_SWS Item_**|**ECUC_Com_00493 :**|
|---|---|
|**_Name_**|ComIPduDirection|
|**_Parent Container_**|ComIPdu|
|**_Description_**|The direction defines if this I-PDU, and therefore the contributing signals and signal<br>groups,shall be sent or received.|
|**_Multiplicity_**|1|
|**_Type_**|EcucEnumerationParamDef|
|**_Range_**|RECEIVE<br>--|
||SEND<br>--|
|**_Post-Build_**<br>**_Varian_**|**_t_**false|



Document ID 015: AUTOSAR_SWS_COM 

127 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Value_**<br>**_Value_**<br>**_Configurati-_**|**_Pre-co_**|**_mpile time_**|X  VARIANT-PRE-COMPILE|
|---|---|---|---|
|**_on Class_**|**_Link tim_**|**_e_**|X  VARIANT-LINK-TIME, VARIANT-|
||||POST-BUILD|
||**_Post-bu_**|**_ild time_**|--|
|**_Scope_**<br>**_/_**<br>**_Depen-_**|scope: l|ocal||
|<br> <br><br>**_dency_**|<br>depend<br>see EC|<br>ency: If configured to Sent also a C<br>UC_Com_00496|omTxIpdu container shall be included,|
|**_SWS Item_**||**ECUC_Com_00175 :**||
|**_Name_**||ComIPduHandleId||
|**_Parent Container_**||ComIPdu||
|**_Description_**||The numerical value used as the I<br>is required by the API calls Com_<br>Com_StartOfReception and Com<br>PduR (ComIP-duDirection: Receiv<br>Rx-I-PDU-callout. For Tx-I-PDUs<br>is used for the APIs calls Com_Tx<br>Com_TriggerIPDUSend or Com_<br>Com_CopyTxData and Com_TpT<br>confirm transmissions of I-PDUs,<br>PDU-callout configured with ComI<br>ComIPduTriggerTransmitCallout.|D of this I-PDU. The ComIPduHandleId<br>RxIndication, Com_TpRxIndication,<br>_CopyRxData to receive I-PDUs from the<br>e), as well as the PduId passed to an<br>(ComIPduDirection: Send), this handle Id<br>Confirmation, Com_TriggerTransmit,<br>TriggerIPDUSendWithMetaData,<br>xConfirmation to transmit respectively<br>as well as the PduId passed to the Tx-I-<br>PduCallout and/or|
|**_Multiplicity_**||0..1||
|**_Type_**||EcucIntegerParamDef(Symbolic|Namegenerated for thisparameter)|
|**_Range_**||0 .. 65535||
|**_Default value_**||--||
|**_Post-Build Variant_**<br>**_city_**|**_Multipli-_**|<br>false||
|**_Post-Build Variant V_**|**_alue_**|false||
|**_Multiplicity_**<br>**_Confi_**|**_guration_**|**_Pre-compile time_**<br>X|All Variants|
|**_Class_**||**_Link time_**<br>--||
|||**_Post-build time_**<br>--||
|**_Value Configuration_**|**_Class_**|**_Pre-compile time_**<br>X|All Variants|
|||**_Link time_**<br>--||
|||**_Post-build time_**<br>--||
|**_Scope / Dependenc_**|**_y_**|scope: ECU||
|**_SWS Item_**|**ECUC_**|**Com_00119 :**||
|**_Name_**|ComIPd|uSignalProcessing||
|**_Parent Container_**|ComIPd|u||
|**_Description_**|For the|definition of the two modes Immed|iate and Deferred.|
|**_Multiplicity_**|1|||
|**_Type_**|EcucEn|umerationParamDef||
|**_Range_**|DEFER|RED<br>sig<br>de|nal indication / confirmations are<br>ferred for example to a cyclic task|
||IMMEDI|ATE<br>the<br>pe<br>Co|signal indications / confirmations are<br>rformed in Com_RxIndication/<br>m_TxConfirmation|
|**_Post-Build Variant_**|<br>|||
|<br>**_Value_**|<br>true|||
|**_Value Configurati-_**|**_Pre-com_**|**_pile time_**<br>X|VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link tim_**|**_e_**<br>X|VARIANT-LINK-TIME|
||**_Post-bu_**|**_ild time_**<br>X|VARIANT-POST-BUILD|
|**_Scope_**<br>**_/_**<br>**_Depen-_**|scope: l|cal||
|<br> <br><br>**_dency_**||||



Document ID 015: AUTOSAR_SWS_COM 

128 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_SWS Item_**|**ECUC_Com_00765 :**|||
|---|---|---|---|
|**_Name_**|ComIPduTriggerTransmitC|allout||
|**_Parent Container_**|ComIPdu|||
|**_Description_**|If there is a trigger transmit<br>contains the name of the c|callou<br>allout f|t defined for this I-PDU this parameter<br>unction.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucFunctionNameDef|||
|**_Default value_**|--|||
|**_maxLength_**|--|||
|**_minLength_**|--|||
|**_regularExpression_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|All Variants|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||



|**_SWS Item_**|**ECUC_Com_00761 :**||
|---|---|---|
|**_Name_**|ComIPduType||
|**_Parent Container_**|ComIPdu||
|**_Description_**|Defines if this I-PDU is a normal I-<br>large I-PDU that shall be sent via t|PDU that can be sent unfragmented or if this is a<br>he Transport Protocol of the underlyingbus.|
|**_Multiplicity_**|1||
|**_Type_**|EcucEnumerationParamDef||
|**_Range_**|NORMAL|sent or received via normal L-PDU|
||TP|sent or received via TP|
|**_Post-Build_**<br>**_Variant_**<br>**_Value_**|<br>true||
|**_Value_**<br>**_Configurati-_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope_**<br>**_/_**<br>**_Depen-_**<br>**_dency_**|scope: local||



|**_SWS Item_**|**ECUC_Com_00206 :**|||
|---|---|---|---|
|**_Name_**|ComIPduGroupRef|||
|**_Parent Container_**|ComIPdu|||
|**_Description_**|Reference to the I-PDUg|roups th|is I-PDU belongs to.|
|**_Multiplicity_**|0..*|||
|**_Type_**|Reference to[ComIPdu|Group ]||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true|||
|**_Post-Build Variant Value_**|true|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|||



Document ID 015: AUTOSAR_SWS_COM 

129 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_SWS Item_**<br>|**ECUC_Com_00519 :**<br>||
|---|---|---|
|**_Name_**|ComIPduSignalGroupRef||
|**_Parent Container_**|ComIPdu||
|**_Description_**|References to all signalgroups co|ntained in this I-Pdu|
|**_Multiplicity_**<br>|0..*<br>||
|**_Type_**|Reference to[ComSignalGroup ]||
|**_Post-Build Variant Multipli-_**|<br>||
|<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**<br>X|VARIANT-LINK-TIME|
||**_Post-build time_**<br>X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
||**_Link time_**<br>X|VARIANT-LINK-TIME|
||**_Post-build time_**<br>X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local||
|**_SWS Item_**|**ECUC_Com_00518 :**||
|**_Name_**|ComIPduSignalRef||
|**_Parent Container_**|ComIPdu||
|**_Description_**|References to all signals containe|d in this I-PDU.|
|**_Multiplicity_**|0..*||
|**_Type_**|Reference to[ComSignal]||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**<br>X|VARIANT-LINK-TIME|
||**_Post-build time_**<br>X<br> <br>|VARIANT-POST-BUILD<br>|
|**_Value Configuration Class_**|**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
||**_Link time_**<br>X|VARIANT-LINK-TIME|
||**_Post-build time_**<br>X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local||
|**_SWS Item_**|**ECUC_Com_00711 :**||
|**_Name_**|ComPduIdRef||
|**_Parent Container_**|ComIPdu||
|**_Description_**|Reference to the "global" Pdu stru<br>IDs in the COM-Stack.|cture to allow harmonization of handle|
|**_Multiplicity_**|1||
|**_Type_**|Reference to[Pdu]||
|**_Post-Build Variant Value_**<br>|false<br> <br>||
|**_Value Configuration Class_**|**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
||**_Link time_**<br>X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**<br>--||
|**_Scope / Dependency_**|||
|**_Included Containers_**|||
|**_Container Name_**|**_Multiplicity_**<br>**_Scope / Dependency_**||
|ComIPduCounter|0..1<br>This optional containe<br>of PDU Counter.|r contains the configuration parameters|
|ComIPduReplication|0..1<br>This optional containe<br>each I-PDU replicated|r contains the information needed for<br>.|
|ComTxIPdu|0..1<br>This container must b<br>configured to SEND.|e included if COM_IPDU_DIRECTION is|



Document ID 015: AUTOSAR_SWS_COM 

130 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00497]** ⌈ A ComTxIPdu container must be included if ComIPduDirection is configured to SEND. ⌋ (SRS_BSW_00167) 

### **10.1.8 ComIPduCounter** 

|**_SWS Item_**|**ECUC_Com_00592 :**|||
|---|---|---|---|
|**_Container Name_**|ComIPduCounter|||
|**_Description_**|This optional container co<br>Counter.|ntains th|e configuration parameters of PDU|
|**_Configuration Parameters_**||||
|**_SWS Item_**<br>|**ECUC_Com_00003 :**<br>|||
|**_Name_**|ComIPduCounterErrorNoti|fication||
|**_Parent Container_**|ComIPduCounter|||
|**_Description_**|Name of Com_CbkCounte<br>parameter is omitted no I-<br>place.|rErr cal<br>PDU co|lback function to be called. If this<br>unter mismatch notification shall take|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucFunctionNameDef|||
|**_Default value_**|--|||
|**_maxLength_**|--|||
|**_minLength_**|--|||
|**_regularExpression_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**<br>|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00593 :**|||
|**_Name_**|ComIPduCounterSize|||
|**_Parent Container_**|ComIPduCounter|||
|**_Description_**|Size of PDU Counter expr|essed in|bits|
|**_Multiplicity_**|1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**<br>|1 .. 8|||
|**_Default value_**|--|||
|**_Post-Build Variant Value_**|false|||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00594 :**|||
|**_Name_**|ComIPduCounterStartPos|ition||
|**_Parent Container_**|ComIPduCounter|||



131 of 185 

Document ID 015: AUTOSAR_SWS_COM 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Description_**<br>**_Multiplicity_**|Position of PDU counter e<br>content<br>of I-PDU (SDU). Note that<br>border.<br>The parameter ComIPduC<br>first<br>byte like in little endian byt<br>1|xpressed in bits from start position of data<br>PDU counter is not allowed to cross a byte<br>ounterStartPosition shall define the bit0 of the<br>e order.|
|---|---|---|
|**_Type_**|EcucIntegerParamDef||
|**_Range_**|0 .. 4294967295||
|**_Default value_**|--||
|**_Post-Build Variant Value_**|false||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X  All Variants|
||**_Link time_**|--|
||**_Post-build time_**|--|
|**_Scope / Dependency_**|scope: local||



|**_SWS Item_**|**ECUC_Com_00595 :**|||
|---|---|---|---|
|**_Name_**|ComIPduCounterThresho|ld||
|**_Parent Container_**|ComIPduCounter|||
|**_Description_**|Threshold value of I-PDU|counter|algorithm,see ECUC_Com_00590.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|0 .. 255|||
|**_Default value_**|0|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|All Variants|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|--||
|**_Value Configuration Class_**|**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||



#### **_<mark>No Included Containers</mark>_** 

### **10.1.9 ComIPduReplication** 

|**_SWS Item_**|**ECUC_Com_00599 :**|
|---|---|
|**_Container Name_**|ComIPduReplication|
|**_Description_**|This optional container contains the information needed for each I-PDU<br>replicated.|
|**_Configuration Parameters_**||
|**_SWS Item_**|**ECUC_Com_00600 :**|
|**_Name_**|ComIPduReplicationQuorum|
|**_Parent Container_**|ComIPduReplication|
|**_Description_**|The number of identical I-PDUs needed for successful voting.|
|**_Multiplicity_**|1|
|**_Type_**|EcucIntegerParamDef|
|**_Range_**|1 .. 3|



132 of 185 

Document ID 015: AUTOSAR_SWS_COM 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Default value_**|--||
|---|---|---|
|**_Post-Build Variant Value_**|false||
|**_Value Configuration Class_**|**_Pre-compile time_**<br>X|All Variants|
||**_Link time_**<br>--||
||**_Post-build time_**<br>--||
|**_Scope / Dependency_**|scope: local<br>dependency: This value must be l<br>ComIPduReplicaRef + 1).|ess or equal to the multiplicity of (|
|**_SWS Item_**|**ECUC_Com_00601 :**||
|**_Name_**|ComIPduReplicaRef||
|**_Parent Container_**|ComIPduReplication||
|**_Description_**|Reference to replicas PduR PDU|s of this IPDU.|
|**_Multiplicity_**|1..2||
|**_Type_**|Reference to[Pdu]||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false||
|**_Post-Build Variant Value_**|false||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**<br>X|All Variants|
|<br><br>**_Class_**|**_Link time_**<br>--||
||**_Post-build time_**<br>--||
|**_Value Configuration Class_**|**_Pre-compile time_**<br>X|All Variants|
||**_Link time_**<br>--||
||**_Post-build time_**<br>--||
|**_Scope / Dependency_**|scope: ECU||
|**_No Included Containers_**|||



### **10.1.10 ComTxIPdu** 

|**_SWS Item_**|**ECUC_Com_00496 :**|
|---|---|
|**_Container Name_**|ComTxIPdu|
|**_Description_**|This container contains additional transmission related configuration<br>parameters of the AUTOSAR COM module's I-PDUs.|
|**_Configuration Parameters_**||



|**_SWS Item_**|**ECUC_Com_10005 :**|
|---|---|
|**_Name_**|ComMetaDataDefault|
|**_Parent Container_**|ComTxIPdu|
|**_Description_**|In case an I-PDU refers to a globally configured MetaDataType and no<br>explicit meta data is given for a send request (e.g. by using<br>Com_TriggerIPDUSendWithMetaData ), the AUTOSAR COM module uses<br>this configured default meta data for sending.<br>The configured string shall be interpreted as a decimal representation of<br>the characters separated by blanks, e.g. "97 98 100" means a string "abd",<br>where the char "a" is in byte 0(lowest address), "b" is in byte 1, and "d" is<br>in byte 2 and(highest address).|
|**_Multiplicity_**|0..1|
|**_Type_**|EcucStringParamDef|
|**_Default value_**|--|
|**_maxLength_**|--|
|**_minLength_**|--|
|**_regularExpression_**|--|



Document ID 015: AUTOSAR_SWS_COM 

133 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|---|---|---|---|
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|All Variants|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|--||
|**_Value Configuration Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: ECU<br>dependency: This parameter<br>ComMetaDataSupport is en<br>match thegloballyconfigure|shall<br>abled.<br>d Met|only be used in case<br>The length of the default meta data shall<br>aDataLength of this I-PDU.|
|**_SWS Item_**|**ECUC_Com_00181 :**|||
|**_Name_**|ComMinimumDelayTime|||
|**_Parent Container_**|ComTxIPdu|||
|**_Description_**|Defines the Minimum Delay<br>transmissions of this I-PDU i<br>possible different transmissi<br>time parameter for one I-PD<br>changing the transmission m<br>minimum delay time by trans<br>monitor the minimum delay t<br>Com_TriggerTransmit API.|Time<br>n sec<br>on mo<br>U. Th<br>ode.<br>missi<br>ime fo|(MDT) between successive<br>onds. The MDT is independent of the<br>des. There is only one minimum delay<br>e minimum delay timer is not reset by<br>Hence, it is not allowed to violate the<br>on mode changes. It is not possible to<br>r I-PDUs that are requested using the|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucFloatParamDef|||
|**_Range_**|[0 .. 3600]|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true|||
|**_Post-Build Variant Value_**|true|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|<br><br>**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|||



|**_SWS Item_**|**ECUC_Com_00576 :**||
|---|---|---|
|**_Name_**|ComTxIPduClearUpdateBit||
|**_Parent Container_**|ComTxIPdu||
|**_Description_**|Defines when the update-bits of si<br>will be cleared.|gnals or signal groups, contained in this I-PDU,|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucEnumerationParamDef||
|**_Range_**|Confirmation|The update-bits are cleared when the<br>transmission of the I-PDU was confirmed.<br>In case of Direct/N-Times transmission<br>mode the update bits will be cleared with<br>respect to the confirmation behaviour of<br>SWS_Com_00305.|
||Transmit|The update-bits are cleared directly after<br>the invocation of PduR_ComTransmit.|
||TriggerTransmit|The update-bits are cleared after the I-PDU|



Document ID 015: AUTOSAR_SWS_COM 

134 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|||was fetched via Com_TriggerTransmit.|
|---|---|---|
|**_Post-Build Variant_**<br>**_Multiplicity_**|<br>true||
|**_Post-Build Variant_**<br>**_Value_**|<br>true||
|**_Multiplicity Confi-_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_guration Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Value Configurati-_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope_**<br>**_/_**<br>**_Depen-_**<br>**_dency_**|scope: local||



|**_SWS Item_**|**ECUC_Com_00017 :**|||
|---|---|---|---|
|**_Name_**|ComTxIPduUnusedAreasD|efault||
|**_Parent Container_**|ComTxIPdu|||
|**_Description_**|The AUTOSAR COM mod<br>pattern. This attribute is ma<br>byte-pattern will be repeate<br>or update-bits were set.|ule fills<br>ndator<br>d thro|not used areas of an I-PDU with this byte<br>y to avoid undefined behaviour. This<br>ughout the I-PDU before any init-values|
|**_Multiplicity_**|1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|0 .. 255|||
|**_Default value_**|--|||
|**_Post-Build Variant Value_**|false|||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||



|**_Included Containers_**<br>|||
|---|---|---|
|**_Container Name_**|**_Multiplici_**|**_y_**<br>**_Scope / Dependency_**|
|ComTxModeFalse|0..1|The referenced transmission mode object that is used when<br>the filtering state for this I-PDU evaluates to false.<br>The default is transmission mode None.|
|ComTxModeTrue|0..1|The referenced transmission mode object that is used when<br>the filteringstate for this I-PDU evaluates to true.|



### **10.1.11 ComIPduGroup** 

|**_SWS Item_**|**ECUC_Com_00341 :**||
|---|---|---|
|**_Container Name_**|ComIPduGroup||
|**_Description_**|Contains the configuration<br>PDUgroups.|parameters of the AUTOSAR COM module's I-|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Configuration Parameters_**|||



Document ID 015: AUTOSAR_SWS_COM 

135 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_SWS Item_**|**ECUC_Com_00184 :**||
|---|---|---|
|**_Name_**|ComIPduGroupHandleId||
|**_Parent Container_**|ComIPduGroup||
|**_Description_**|The numerical value used as the<br>The ComIPduGroupHandleId is r<br>I-PDU Groups.<br>Range: 0 ..(ComSupportedIPduG|ID of this I-PDU Group .<br>equired by the API calls to start and stop<br>roups-1)|
|**_Multiplicity_**|1||
|**_Type_**|EcucIntegerParamDef(Symbolic|Namegenerated for thisparameter)|
|**_Range_**|0 .. 65535||
|**_Default value_**|--||
|**_Post-Build Variant Value_**|false||
|**_Value Configuration Class_**|**_Pre-compile time_**<br>X|All Variants|
||**_Link time_**<br>--||
||**_Post-build time_**<br>--||
|**_Scope / Dependency_**|scope: ECU||
|**_SWS Item_**|**ECUC_Com_00185 :**||
|**_Name_**|ComIPduGroupGroupRef||
|**_Parent Container_**|ComIPduGroup||
|**_Description_**|References to all I-PDU groups th<br>reference is omitted this I-PDU gr<br>group.|at includes this I-PDU group. If this<br>oup does not belong to another I-PDU|
|**_Multiplicity_**|0..*||
|**_Type_**|Reference to[ComIPduGroup ]||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**<br>X|VARIANT-LINK-TIME|
||**_Post-build time_**<br>X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
||**_Link time_**<br>X|VARIANT-LINK-TIME|
||**_Post-build time_**<br>X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local||
|**_No Included Containers_**|||



### **10.1.12 ComSignal** 

|**_SWS Item_**|**ECUC_Com_00344 :**||
|---|---|---|
|**_Container Name_**|ComSignal||
|**_Description_**|Contains the configuration<br>signals.|parameters of the AUTOSAR COM module's|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Configuration Parameters_**|||
|**_SWS Item_**|**ECUC_Com_00259 :**||



Document ID 015: AUTOSAR_SWS_COM 

136 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Name_**<br>||ComBitPosition<br>||
|---|---|---|---|
|**_Parent Container_**||ComSignal||
|**_Description_**||Starting position within the<br>the I-PDU and not in the s<br>configured to Opaque the<br>of the first byte like in little|I-PDU. This parameter refers to the position in<br>hadow buffer. If the endianness conversion is<br>parameter ComBitPosition shall define the bit0<br>endian byte order|
|**_Multiplicity_**<br>||1<br>||
|**_Type_**||EcucIntegerParamDef||
|**_Range_**||0 .. 4294967295||
|**_Default value_**||--||
|**_Post-Build Variant_**|**_Value_**|true||
|**_Value Configuration_**|**_Class_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|||**_Link time_**|X  VARIANT-LINK-TIME|
|||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependenc_**|**_y_**|scope: local||
|**_SWS Item_**||**ECUC_Com_00158 :**||
|**_Name_**||ComBitSize||
|**_Parent Container_**||ComSignal||
|**_Description_**||Size in bits, for integer sig<br>UINT8_DYN<br>the size shall be configure<br>FLOAT32 and<br>FLOAT64 the size is alrea<br>be omitted.|nal types. For ComSignalType UINT8_N and<br>d by ComSignalLength. For ComSignalTypes<br>dy defined by the signal type and therefore may|
|**_Multiplicity_**||0..1||
|**_Type_**||EcucIntegerParamDef||
|**_Range_**||0 .. 64||
|**_Default value_**||--||
|**_Post-Build Variant_**|**_Multipli_**|**_-_**<br>t||
|**_city_**||rue||
|**_Post-Build Variant_**|**_Value_**|true||
|**_Multiplicity_**<br>**_Confi_**|**_guration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**||**_Link time_**|X  VARIANT-LINK-TIME|
|||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Value Configuration_**|**_Class_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|||**_Link time_**|X  VARIANT-LINK-TIME|
|||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependenc_**|**_y_**|scope: local||
|**_SWS Item_**|**ECUC_**|**Com_00314 :**||
|**_Name_**|ComDa|taInvalidAction||
|**_Parent Container_**|ComSig|nal||
|**_Description_**|This pa<br>Relating<br>invalid s<br>If Repla|rameter defines the action<br>to signal groups the actio<br>ignal.<br>ce is used the ComSignalI|performed upon reception of an invalid signal.<br>n in case if one of the included signals is an<br>nitValue will be used for the replacement.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucEn<br>|umerationParamDef<br>||
|**_Range_**|NOTIFY||--|
||<br>REPLA|<br>CE|Literal for DataInvalidAction|
|**_Post-Build Variant_**|<br>|||
|**_Multiplicity_**|false|||
|**_Post-Build Variant_**<br>**_Value_**|<br>false|||
|**_Multiplicity_**<br>**_Confi-_**|**_Pre-co_**|**_mpile time_**|X  VARIANT-PRE-COMPILE|



Document ID 015: AUTOSAR_SWS_COM 

137 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_guration Class_**|**_Link time_**<br>**_Post-build time_**|X  VARIANT-LINK-TIME, VARIANT-<br>POST-BUILD<br>--|
|---|---|---|
|**_Value Configurati-_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link time_**|X  VARIANT-LINK-TIME, VARIANT-<br>POST-BUILD|
||**_Post-build time_**|--|
|**_Scope_**<br>**_/_**<br>**_Depen-_**<br>**_dency_**|scope: local||



|**_SWS Item_**|**ECUC_Com_00499 :**|||
|---|---|---|---|
|**_Name_**|ComErrorNotification|||
|**_Parent Container_**|ComSignal|||
|**_Description_**|Only valid on sender side:<br>called.<br>If thisparameter is omitted|Name<br>no err|of Com_CbkTxErr callback function to be<br>or notification shall takeplace.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucFunctionNameDef|||
|**_Default value_**|--|||
|**_maxLength_**|--|||
|**_minLength_**|--|||
|**_regularExpression_**|--|||
|**_Post-Build Variant Multipli-_**|<br>false|||
|**_city_**||||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00183 :**|||
|**_Name_**|ComFirstTimeout|||
|**_Parent Container_**|ComSignal|||
|**_Description_**|Defines the length of the fi<br>seconds. This timeout is u<br>deadline monitoring servic<br>is configured byECUC_Co|rst dea<br>sed im<br>e. The<br>m_002|dline monitoring timeout period in<br>mediately after start (or restart) of the<br>timeout period of the successive periods<br>63.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucFloatParamDef|||
|**_Range_**|[0 .. 3600]|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**|<br>t|||
|**_city_**|rue|||
|**_Post-Build Variant Value_**|true|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|<br><br>**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|||



Document ID 015: AUTOSAR_SWS_COM 

138 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_SWS Item_**<br>|**ECUC_Com_00165 :**<br>|||
|---|---|---|---|
|**_Name_**|ComHandleId|||
|**_Parent Container_**|ComSignal|||
|**_Description_**|The numerical value used<br>This ID identifies signals a<br>Com_SignalIdType or Com|as the I<br>nd sign<br> _Signa|D.<br>al groups in the COM APIs using<br>lGroupIdTypeparameter respectively.|
|**_Multiplicity_**|0..1|||
|**_Type_**<br>|EcucIntegerParamDef(Sy <br>|mbolic|Namegenerated for thisparameter)|
|**_Range_**|0 .. 65535|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>|<br>false|||
|**_city_**||||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|All Variants|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: ECU|||
|**_SWS Item_**|**ECUC_Com_00811 :**|||
|**_Name_**|ComInitialValueOnly|||
|**_Parent Container_**|ComSignal|||
|**_Description_**<br>|This parameter defines tha<br>into the respective PDU bu<br>through the RTE. Thus the<br>anyAPI calls for this signa<br>|t the re<br>t there<br>Com i<br>l(group|spective signal's initial value shall be put<br>will not be any update of the value<br>mplementation does not need to expect<br>).|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucBooleanParamDef|||
|**_Default value_**|false|||
|**_Post-Build Variant Multili-_**||||
|**_p_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-|
||||BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00315 :**|||
|**_Name_**|ComInvalidNotification|||
|**_Parent Container_**|ComSignal|||
|**_Description_**|Only valid on receiver side<br>called. Name of the functio<br>an invalidated signal/ sign<br>ComDataInvalidAction is c|: Name<br>n which<br>al group<br>onfigur|of Com_CbkInv callback function to be<br>notifies the RTE about the reception of<br>. Only applicable if<br>ed to NOTIFY.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucFunctionNameDef|||
|**_Default value_**|--|||
|**_maxLength_**|--|||



Document ID 015: AUTOSAR_SWS_COM 

139 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_minLength_**<br>||--|||
|---|---|---|---|---|
|**_regularExpression_**||--|||
|**_Post-Build Variant_**|**_Multipli-_**|<br>|||
|<br>**_city_**||<br>false|||
|**_Post-Build Variant_**<br>|**_Value_**<br>|false<br>|||
|**_Multiplicity_**<br>**_Conf_**|**_iguration_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|<br> <br>**_Class_**||<br> <br>**_Link time_**|<br>X|<br>VARIANT-LINK-TIME, VARIANT-POST-|
|||||<br>BUILD|
|||**_Post-build time_**|--||
|**_Value Configuratio_**|**_n Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>|
|||||BUILD|
|||**_Post-build time_**|--||
|**_Scope / Dependen_**|**_cy_**|scope: local|||
|**_SWS Item_**||**ECUC_Com_00498 :**|||
|**_Name_**||ComNotification|||
|**_Parent Container_**||ComSignal|||
|**_Description_**||On sender side: Name of<br>On receiver side: Name o|Com_C<br>f Com_|bkTxAck callback function to be called.<br>CbkRxAck callback function to be called.|
|||If thisparameter is omitte|d no not|ification shall takeplace.|
|**_Multiplicity_**||0..1|||
|**_Type_**||EcucFunctionNameDef|||
|**_Default value_**||--|||
|**_maxLength_**||--|||
|**_minLength_**||--|||
|**_regularExpression_**||--|||
|**_Post-Build Variant_**|**_Multipli-_**|<br>|||
|<br>**_city_**||<br>false|||
|**_Post-Build Variant_**|**_Value_**|false|||
|**_Multiplicity_**<br>**_Conf_**|**_iguration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>|
|||||BUILD|
|||**_Post-build time_**|--||
|**_Value Configuratio_**|**_n Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|||**_Link time_**|X|VARIANT-LINK-TIME VARIANT-POST-|
|||||,<br>BUILD|
|||**_Post-build time_**|--||
|**_Scope / Dependen_**|**_cy_**|scope: local|||
|**_SWS Item_**|**ECUC_C**|**om_00412 :**|||
|**_Name_**|ComRxD|ataTimeoutAction|||
|**_Parent Container_**|ComSign|al|||
|**_Description_**|This para<br>deadline|meter defines the action p<br>monitoringtimer.|erforme|d upon expiration of the reception|
|**_Multiplicity_**|<br>0..1||||
|**_Type_**|<br>EcucEnu|merationParamDef|||
|**_Range_**|NONE||no re|lacement shall takeplace|
||<br>REPLAC|E|<br>signa<br>ComS|<br>ls shall be replaced by their<br>ignalInitValue|
||SUBSTIT|UTE|signa|ls shall be replaced by their|
||||<br>ComT|<br>imeoutSubstitutionValue|
|**_Post-Build Variant_**<br>**_Multiplicity_**|<br>false||||
|**_Post-Build Variant_**|false||||



Document ID 015: AUTOSAR_SWS_COM 

140 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Value_**|||
|---|---|---|
|**_Multiplicity Confi-_**<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_guration Class_**<br>**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
|**_Post-build time_**|--||
|**_Value Configurati-_**<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_on Class_**<br>**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
|**_Post-build time_**|--||
|**_Scope_**<br>**_/_**<br>**_Depen-_**<br>**_dency_**<br>scope: local|||



|**_SWS Item_**|**ECUC_Com_00391 :**|||
|---|---|---|---|
|**_Name_**|ComSignalDataInvalidValu|e||
|**_Parent Container_**|ComSignal|||
|**_Description_**|Defines the data invalid va<br>In case the ComSignalTyp<br>SINT16, SINT32, SINT64<br>chapter Integer Type in th<br>In case the ComSignalTyp<br>interpreted as defined in th<br>specification.<br>In case the ComSignalTyp<br>defined in the chapter Boo<br>In case the ComSignal is a<br>interpreted as a decimal re<br>blanks, e.g. "97 98 100" m<br>0(lowest address), "b" is in<br>address).<br>For the ComSignalType U<br>number of configured char<br>0-sized dynamic signal.|lue of t<br>e is UI<br>the strin<br>e AUTO<br>e is FL<br>e chap<br>e is BO<br>lean Ty<br>UINT8<br>presen<br>eans a<br>byte 1<br>INT8_D<br>acters.|he signal.<br>NT8, UINT16, UINT32, UINT64, SINT8,<br>g shall be interpreted as defined in the<br>SAR EcuC specification.<br>OAT32, FLOAT64 the string shall be<br>ter Float Type in the AUTOSAR EcuC<br>OLEAN the string shall be interpreted as<br>pe in the AUTOSAR EcuC specification.<br>_N, UINT8_DYN the string shall be<br>tation of the characters separated by<br>string "abd", where the char "a" is in byte<br>, and "d" is in byte 2 and (highest<br>YN the dynamic length shall be set to the<br>An empty string "" shall be interpreted as|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucStringParamDef|||
|**_Default value_**|--|||
|**_maxLength_**|--|||
|**_minLength_**|--|||
|**_regularExpression_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local<br>dependency: In case of UI<br>ComSignalDataInvalidValu|NT8_N<br>e has t|the length of<br>o be the same as ComSignalLength.|
|**_SWS Item_**<br>**ECUC_**|**Com_00157 :**|||
|**_Name_**<br>ComSig|nalEndianness|||
|**_Parent Container_**<br>ComSig|nal|||
|**_Description_**<br>Defines|the endianness ofthe sign|al'snet|work representation.|



Document ID 015: AUTOSAR_SWS_COM 

141 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Multiplicity_**|1||
|---|---|---|
|**_Type_**|EcucEnumerationParamDef||
|**_Range_**|BIG_ENDIAN|--|
||LITTLE_ENDIAN|--|
||OPAQUE|--|
|**_Post-Build Variant_**<br>**_Value_**|<br>true||
|**_Value_**<br>**_Configurati-_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope_**<br>**_/_**<br>**_Depen-_**<br>**_dency_**|scope: local||



|**_SWS Item_**|**ECUC_Com_00170 :**|
|---|---|
|**_Name_**|ComSignalInitValue|
|**_Parent Container_**|ComSignal|
|**_Description_**|Initial value for this signal. In case of UINT8_N the default value is a string<br>of length ComSignalLength with all bytes set to 0x00. In case of<br>UINT8_DYN the initial size shall be 0.<br>In case the ComSignalType is UINT8, UINT16, UINT32, UINT64, SINT8,<br>SINT16, SINT32, SINT64 the string shall be interpreted as defined in the<br>chapter Integer Type in the AUTOSAR EcuC specification.<br>In case the ComSignalType is FLOAT32, FLOAT64 the string shall be<br>interpreted as defined in the chapter Float Type in the AUTOSAR EcuC<br>specification.<br>In case the ComSignalType is BOOLEAN the string shall be interpreted as<br>defined in the chapter Boolean Type in the AUTOSAR EcuC specification.<br>In case the ComSignal is a UINT8_N, UINT8_DYN the string shall be<br>interpreted as a decimal representation of the characters separated by<br>blanks, e.g. "97 98 100" means a string "abd", where the char "a" is in byte<br>0(lowest address), "b" is in byte 1, and "d" is in byte 2 and (highest<br>address).<br>For the ComSignalType UINT8_DYN the dynamic length shall be set to the<br>number of configured characters. An empty string "" shall be interpreted as<br>0-sized dynamic signal.|
|**_Multiplicity_**|0..1|
|**_Type_**|EcucStringParamDef|
|**_Default value_**|0|
|**_maxLength_**|--|
|**_minLength_**|--|
|**_regularExpression_**|--|
|**_Post-Build Variant Multipli_**<br>**_city_**|**_-_**<br>true|
|**_Post-Build Variant Value_**|true|
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**<br>X  VARIANT-LINK-TIME|
||**_Post-build time_**<br>X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
||**_Link time_**<br>X  VARIANT-LINK-TIME|
||**_Post-build time_**<br>X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local<br>dependency: In case of UINT8_N the length of ComSignalInitValue has to<br>be the same as ComSignalLength.|
|**_SWS Item_**|**ECUC_Com_00437 :**|
|**_Name_**|ComSignalLength|
|**_Parent Container_**|ComSignal|



Document ID 015: AUTOSAR_SWS_COM 

142 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Description_**|Description:<br>For ComSignalType UINT<br>bytes. For ComSignalType<br>bytes. For all other types t<br>The supported maximum l<br>system. For non TP-PDUs<br>of any included signal, is li<br>example, the limit is 8 byte<br>254 for FlexRay.|8_N thi<br>UINT8<br>his para<br>ength is<br>the ma<br>mited b<br>s for C|s parameter specifies the length n in<br>_DYN it specifies the maximum length in<br>meter shall be ignored.<br>restricted by the used transportation<br>ximum size of a PDU, and therefore also<br>y the concrete bus characteristic. For<br>AN and LIN, 64 bytes for CAN FD and|
|---|---|---|---|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|0 .. 4294967295|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||



|**_SWS Item_**|**ECUC_Com_00127 :**|
|---|---|
|**_Name_**|ComSignalType|
|**_Parent Container_**|ComSignal|
|**_Description_**|The AUTOSAR type of the signal. Whether or not the signal is signed or unsigned<br>can be found by examining the value of this attribute.<br>This type could also be used to reserved appropriate storage in AUTOSAR COM.|
|**_Multiplicity_**|1|
|**_Type_**|EcucEnumerationParamDef|
|**_Range_**|BOOLEAN<br>--|
||FLOAT32<br>--|
||FLOAT64<br>--|
||SINT16<br>--|
||SINT32<br>--|
||SINT64<br>--|
||SINT8<br>--|
||UINT16<br>--|
||UINT32<br>--|
||UINT64<br>--|
||UINT8<br>--|
||UINT8_DYN<br>--|
||UINT8_N<br>--|
|**_Post-Build_**<br>**_Variant_**<br>**_Value_**|<br>false|
|**_Value_**<br>**_Configurati-_**|**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link time_**<br>X  VARIANT-LINK-TIME, VARIANT-<br>POST-BUILD|
||**_Post-build time_**<br>--|
|**_Scope_**<br>**_/_**<br>**_Depen-_**|scope: local|
|**_dency_**||



Document ID 015: AUTOSAR_SWS_COM 

143 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_SWS Item_**|**ECUC_Com_00263 :**||
|---|---|---|
|**_Name_**|ComTimeout||
|**_Parent Container_**|ComSignal||
|**_Description_**|Defines the length of the de<br>The period for the first time<br>ECUC_Com_00183.|adline monitoring timeout period in seconds.<br>out period can be configured separately by|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucFloatParamDef||
|**_Range_**|[0 .. 3600]||
|**_Default value_**|--||
|**_Post-Build Variant Multipli-_**|<br>true||
|**_city_**|||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
||**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local||
|**_SWS Item_**|**ECUC_Com_00552 :**||
|**_Name_**|ComTimeoutNotification||
|**_Parent Container_**|ComSignal||
|**_Description_**|On sender side: Name of C<br>On receiver side: Name of|om_CbkTxTOut callback function to be called.<br>Com_CbkRxTOut callback function to be called.|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucFunctionNameDef||
|**_Default value_**|--||
|**_maxLength_**|--||
|**_minLength_**|--||
|**_regularExpression_**|--||
|**_Post-Build Variant Multipli-_**|<br>fl||
|**_city_**|ase||
|**_Post-Build Variant Value_**|false||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--|
|**_Value Configuration Class_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
||**_Link time_**|X  VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--|
|**_Scope / Dependency_**|scope: local||



|**_SWS Item_**|**ECUC_Com_10006 :**|
|---|---|
|**_Name_**|ComTimeoutSubstitutionValue|
|**_Parent Container_**|ComSignal|
|**_Description_**|The signal substitution value will be used in case of a timeout and<br>ComRxDataTimeoutAction is set to SUBSTITUTE.<br>In case of UINT8_N the default value is a string of length<br>ComSignalLength with all bytes set to 0x00.<br>In case ofUINT8_DYN the initial size shall be 0.|
||In case the ComSignalType is UINT8, UINT16, UINT32, UINT64, SINT8,<br>SINT16, SINT32, SINT64the string shallbeinterpreted as definedinthe|



Document ID 015: AUTOSAR_SWS_COM 

144 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||chapter Integer Type in the<br>In case the ComSignalTyp<br>interpreted as defined in th<br>specification.<br>In case the ComSignalTyp<br>defined in the chapter Boo<br>In case the ComSignal is a<br>interpreted as a decimal re<br>blanks, e.g. "97 98 100" m<br>0(lowest address), "b" is in<br>address). For the ComSig<br>be set to the number of co<br>interpreted as 0-sized dyn|AUTOSAR EcuC specification.<br>e is FLOAT32, FLOAT64 the string shall be<br>e chapter Float Type in the AUTOSAR EcuC<br>e is BOOLEAN the string shall be interpreted as<br>lean Type in the AUTOSAR EcuC specification.<br>UINT8_N, UINT8_DYN the string shall be<br>presentation of the characters separated by<br>eans a string "abd", where the char "a" is in byte<br>byte 1, and "d" is in byte 2 and (highest<br>nalType UINT8_DYN the dynamic length shall<br>nfigured characters. An empty string "" shall be<br>amic signal.|
|---|---|---|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucStringParamDef||
|**_Default value_**|--||
|**_maxLength_**|--||
|**_minLength_**|--||
|**_regularExpression_**|--||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
||**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local||



|**_SWS Item_**|**ECUC_Com_00232 :**||
|---|---|---|
|**_Name_**|ComTransferProperty||
|**_Parent_**<br>**_Cont_**<br>**_ner_**|**_ai-_**<br>ComSignal||
|**_Description_**|Defines if a write access to this signal can trigg<br>corresponding I-PDU. If the I-PDU is triggered,<br>mode of the correspondingI-PDU.|er the transmission of the<br>depends also on the transmission|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucEnumerationParamDef||
|**_Range_**|PENDING|A write access to this<br>signal never triggers the<br>transmission of the<br>correspondingI-PDU.|
||TRIGGERED|Depending on the<br>transmission mode, a write<br>access to this signal can<br>trigger the transmission of<br>the correspondingI-PDU.|
||TRIGGERED_ON_CHANGE|Depending on the<br>transmission mode, a write<br>access to this signal can<br>trigger the transmission of<br>the corresponding I-PDU,<br>but only in case the written<br>value is different to the|



Document ID 015: AUTOSAR_SWS_COM 

145 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|||locally stored (last sent or<br>initial value) in length or<br>value.|
|---|---|---|
||TRIGGERED_ON_CHANGE_WITHOUT_REPETITION|Depending on the<br>transmission mode, a write<br>access to this signal can<br>trigger the transmission of<br>the corresponding I-PDU<br>just once without a<br>repetition, but only in case<br>the written value is<br>different to the locally<br>stored (last sent or initial<br>value)in length or value.|
||TRIGGERED_WITHOUT_REPETITION|Depending on the<br>transmission mode, a write<br>access to this signal can<br>trigger the transmission of<br>the corresponding I-PDU<br>just once without a<br>repetition.|
|**_Post-Build Vari-_**<br>**_ant Multiplicity  _**|<br><sup>true</sup>||
|**_Post-Build Vari-_**<br>**_ant Value_**|<br>true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X VARIANT-PRE-<br>COMPILE|
|**_Class_**|**_Link time_**|X VARIANT-LINK-TIME|
||**_Post-build time_**|X VARIANT-POST-BUILD|
|**_Value_**<br>**_Configu-_**<br>**_ration Class_**|**_Pre-compile time_**|X VARIANT-PRE-<br>COMPILE|
||**_Link time_**|X VARIANT-LINK-TIME|
||**_Post-build time_**|X VARIANT-POST-BUILD|
|**_Scope / Depen-_**<br>**_dency_**|<br>scope: local||



|**_SWS Item_**|**ECUC_Com_00257 :**||
|---|---|---|
|**_Name_**|ComUpdateBitPosition||
|**_Parent Container_**|ComSignal||
|**_Description_**|Bit position of update-bit in<br>If this attribute is omitted th<br>consistently on sender and<br>Range: 0..63 for CAN and<br>0..511 for CAN FD,<br>0..2031 for FlexRay,<br>0..4294967295 for TP.|side I-PDU.<br>en there is no update-bit. This setting must be<br>on receiver side.<br>LIN,|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucIntegerParamDef||
|**_Range_**|0 .. 4294967295||
|**_Default value_**|--||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|



Document ID 015: AUTOSAR_SWS_COM 

146 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||**_Link time_**|X  VARIANT-LINK-TIME|
|---|---|---|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local||
|**_SWS Item_**|**ECUC_Com_00002 :**||
|**_Name_**|ComSystemTemplateSyst|emSignalRef|
|**_Parent Container_**|ComSignal||
|**_Description_**|Reference to the ISignalT<br>ISignal (System Template<br>represents.|oIPduMapping that contains a reference to the<br>) which this ComSignal (or ComGroupSignal)|
|**_Multiplicity_**|0..1||
|**_Type_**|Foreign reference to[I-SI|GNAL-TO-I-PDU-MAPPING]|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
||**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: ECU||



|**_Included Containers_**|||
|---|---|---|
|**_Container Name_**|**_Multiplici_**|**_ty_**<br>**_Scope / Dependency_**|
|ComFilter|0..1|This container contains the configuration parameters of the<br>AUTOSAR COM module's Filters.<br>Note: On sender side the container is used to specify the<br>transmission mode conditions.|



### **10.1.13 ComSignalGroup** 

|**_SWS Item_**|**ECUC_Com_00345 :**||
|---|---|---|
|**_Container Name_**|ComSignalGroup||
|**_Description_**|Contains the configuration<br>signalgroups.|parameters of the AUTOSAR COM module's|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Configuration Parameters_**|||



|**_SWS Item_**|**ECUC_Com_00314 :**|
|---|---|
|**_Name_**|ComDataInvalidAction|
|**_Parent Container_**|ComSignalGroup|
|**_Description_**|This parameter defines the action performed upon reception of an invalid signal.<br>Relating to signal groups the action in case if one of the included signals is an<br>invalid signal.<br>If Replace is used the ComSignalInitValue will be used for the replacement.|
|**_Multiplicity_**|0..1|
|**_Type_**|EcucEnumerationParamDef|
|**_Range_**|NOTIFY<br>--|



Document ID 015: AUTOSAR_SWS_COM 

147 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||REPLACE|Literal for DataInvalidAction|
|---|---|---|
|**_Post-Build Variant_**<br>**_Multiplicity_**|<br>false||
|**_Post-Build Variant_**<br>**_Value_**|<br>false||
|**_Multiplicity_**<br>**_Confi-_**<br>|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_guration Class_**|**_Link time_**|X  VARIANT-LINK-TIME, VARIANT-<br>POST-BUILD|
||**_Post-build time_**|--|
|**_Value Configurati-_**<br>|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link time_**|X  VARIANT-LINK-TIME, VARIANT-<br>POST-BUILD|
||**_Post-build time_**|--|
|**_Scope_**<br>**_/_**<br>**_Depen-_**<br>**_dency_**|scope: local||



|**_SWS Item_**|**ECUC_Com_00499 :**|
|---|---|
|**_Name_**|ComErrorNotification|
|**_Parent Container_**|ComSignalGroup|
|**_Description_**|Only valid on sender side: Name of Com_CbkTxErr callback function to be<br>called.<br>If thisparameter is omitted no error notification shall takeplace.|
|**_Multiplicity_**|0..1|
|**_Type_**|EcucFunctionNameDef|
|**_Default value_**|--|
|**_maxLength_**|--|
|**_minLength_**|--|
|**_regularExpression_**|--|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|
|**_Post-Build Variant Value_**|false|
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**<br>X  VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**<br>--|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
||**_Link time_**<br>X  VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**<br>--|
|**_Scope / Dependency_**|scope: local|
|**_SWS Item_**|**ECUC_Com_00183 :**|
|**_Name_**|ComFirstTimeout|
|**_Parent Container_**|ComSignalGroup|
|**_Description_**|Defines the length of the first deadline monitoring timeout period in<br>seconds. This timeout is used immediately after start (or restart) of the<br>deadline monitoring service. The timeout period of the successive periods<br>is configured byECUC_Com_00263.|
|**_Multiplicity_**|0..1|
|**_Type_**|EcucFloatParamDef|
|**_Range_**|[0 .. 3600]|
|**_Default value_**|--|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true|
|**_Post-Build Variant Value_**|true|
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|



Document ID 015: AUTOSAR_SWS_COM 

148 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Class_**|**_Link time_**<br>|X<br>|VARIANT-LINK-TIME<br>|
|---|---|---|---|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**<br>|**ECUC_Com_00165 :**<br>|||
|**_Name_**<br>|ComHandleId<br>|||
|**_Parent Container_**|ComSignalGroup|||
|**_Description_**|The numerical value used a<br>This ID identifies signals an<br>Com_SignalIdType or Com|s the I<br>d sign<br>_Signa|D.<br>al groups in the COM APIs using<br>lGroupIdTypeparameter respectively.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucIntegerParamDef(Sym|bolic|Namegenerated for thisparameter)|
|**_Range_**|0 .. 65535|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**<br>|**_Pre-compile time_**|X|All Variants|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: ECU|||
|**_SWS Item_**|**ECUC_Com_00811 :**|||
|**_Name_**|ComInitialValueOnly|||
|**_Parent Container_**|ComSignalGroup|||
|**_Description_**|This parameter defines that<br>into the respective PDU but<br>through the RTE. Thus the<br>anyAPI calls for this signal|the re<br>there<br>Com i<br> (group|spective signal's initial value shall be put<br>will not be any update of the value<br>mplementation does not need to expect<br>).|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucBooleanParamDef|||
|**_Default value_**|false|||
|**_Post-Build Variant Multipli-_**|<br>fl|||
|**_city_**|ase|||
|**_Post-Build Variant Value_**<br> <br>|false<br> <br>|||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|<br> <br>**_Class_**|<br><br>**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-|
||||BUILD|
||**_Post-build time_**<br> <br>|--<br>|<br>|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||<br><br>**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-|
||||BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00315 :**|||
|**_Name_**|ComInvalidNotification|||
|**_Parent Container_**|ComSignalGroup|||
|**_Description_**|Only valid on receiver side:|Name|of ComCbkInv callback function to be|
||<br>called. Name of the function|<br>which|_<br>notifies the RTE about the reception of|



Document ID 015: AUTOSAR_SWS_COM 

149 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||an invalidated signal/ signa<br>ComDataInvalidAction is c|l group<br>onfigur|. Only applicable if<br>ed to NOTIFY.|
|---|---|---|---|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucFunctionNameDef|||
|**_Default value_**|--|||
|**_maxLength_**|--|||
|**_minLength_**|--|||
|**_regularExpression_**|--|||
|**_Post-Build Variant Multipli-_**|<br>false|||
|**_city_**||||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00498 :**|||
|**_Name_**|ComNotification|||
|**_Parent Container_**|ComSignalGroup|||
|**_Description_**|On sender side: Name of C<br>On receiver side: Name of<br>If thisparameter is omitted|om_C<br>Com_C<br>no noti|bkTxAck callback function to be called.<br>bkRxAck callback function to be called.<br>fication shall takeplace.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucFunctionNameDef|||
|**_Default value_**|--|||
|**_maxLength_**|--|||
|**_minLength_**|--|||
|**_regularExpression_**|--|||
|**_Post-Build Variant Multipli-_**|<br>fl|||
|**_city_**|ase|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-|
||||BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||



|**_SWS Item_**|**ECUC_Com_00412 :**||
|---|---|---|
|**_Name_**|ComRxDataTimeoutAction||
|**_Parent Container_**|ComSignalGroup||
|**_Description_**|This parameter defines the actio<br>deadline monitoringtimer.|n performed upon expiration of the reception|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucEnumerationParamDef||
|**_Range_**|NONE|no replacement shall takeplace|
||REPLACE|signals shall be replaced bytheir|



Document ID 015: AUTOSAR_SWS_COM 

150 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|||ComSignalInitValue|
|---|---|---|
||SUBSTITUTE|signals shall be replaced by their<br>ComTimeoutSubstitutionValue|
|**_Post-Build Variant_**<br>**_Multiplicity_**|<br>false||
|**_Post-Build Variant_**<br>**_Value_**|<br>false||
|**_Multiplicity Confi-_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_guration Class_**|**_Link time_**|X  VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--|
|**_Value Configurati-_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link time_**|X  VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--|
|**_Scope_**<br>**_/_**<br>**_Depen-_**<br>**_dency_**|scope: local||



|**_SWS Item_**|**ECUC_Com_10003 :**|||
|---|---|---|---|
|**_Name_**|ComSignalGroupArrayAcc|ess||
|**_Parent Container_**|ComSignalGroup|||
|**_Description_**|Defines whether the uint8-<br>ComSignalGroup.|array b|ased access shall be used for this|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucBooleanParamDef|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|All Variants|
|**_Class_**|**_Link time_**|--||
||**_Post-build time_**|--||
|**_Value Configuration Class_**|**_Pre-compile time_**|X|All Variants|
||**_Link time_**|--||
||**_Post-build time_**|--||
|**_Scope / Dependency_**||||



|**_SWS Item_**|**ECUC_Com_00263 :**||
|---|---|---|
|**_Name_**|ComTimeout||
|**_Parent Container_**|ComSignalGroup||
|**_Description_**|Defines the length of the<br>The period for the first tim<br>ECUC_Com_00183.|deadline monitoring timeout period in seconds.<br>eout period can be configured separately by|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucFloatParamDef||
|**_Range_**|[0 .. 3600]||
|**_Default value_**|--||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
||**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|



Document ID 015: AUTOSAR_SWS_COM 

151 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Scope / Dependency_**|scope: local|||
|---|---|---|---|
|**_SWS Item_**|**ECUC_Com_00552 :**|||
|**_Name_**|ComTimeoutNotification|||
|**_Parent Container_**|ComSignalGroup|||
|**_Description_**|On sender side: Name of C<br>On receiver side: Name of|om_C<br>Com_|bkTxTOut callback function to be called.<br>CbkRxTOut callback function to be called.|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucFunctionNameDef|||
|**_Default value_**|--|||
|**_maxLength_**|--|||
|**_minLength_**|--|||
|**_regularExpression_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local|||



|**_SWS Item_**|**ECUC_Com_00232 :**||
|---|---|---|
|**_Name_**|ComTransferProperty||
|**_Parent_**<br>**_Contai-_**<br>**_ner_**|ComSignalGroup||
|**_Description_**|Defines if a write access to this signal can trigger the tran<br>corresponding I-PDU. If the I-PDU is triggered, depends a<br>mode of the correspondingI-PDU.|smission of the<br>lso on the transmission|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucEnumerationParamDef||
|**_Range_**|PENDING|A write access to this<br>signal never triggers the<br>transmission of the<br>correspondingI-PDU.|
||TRIGGERED|Depending on the<br>transmission mode, a write<br>access to this signal can<br>trigger the transmission of<br>the correspondingI-PDU.|
||TRIGGERED_ON_CHANGE|Depending on the<br>transmission mode, a write<br>access to this signal can<br>trigger the transmission of<br>the corresponding I-PDU,<br>but only in case the written<br>value is different to the<br>locally stored (last sent or<br>initial value) in length or<br>value.|
||TRIGGERED_ON_CHANGE_WITHOUT_REPETITION|Depending on the<br>transmission mode, a write<br>access to this signalcan|



Document ID 015: AUTOSAR_SWS_COM 

152 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|||trigger the transmission of<br>the corresponding I-PDU<br>just once without a<br>repetition, but only in case<br>the written value is<br>different to the locally<br>stored (last sent or initial<br>value)in length or value.|
|---|---|---|
||TRIGGERED_WITHOUT_REPETITION|Depending on the<br>transmission mode, a write<br>access to this signal can<br>trigger the transmission of<br>the corresponding I-PDU<br>just once without a<br>repetition.|
|**_Post-Build Vari-_**<br>**_ant Multiplicity  _**|<sup>true</sup>||
|**_Post-Build Vari-_**<br>**_ant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X VARIANT-PRE-<br>COMPILE|
|**_Class_**|**_Link time_**|X VARIANT-LINK-TIME|
||**_Post-build time_**|X VARIANT-POST-BUILD|
|**_Value_**<br>**_Configu-_**<br>**_ration Class_**|**_Pre-compile time_**|X VARIANT-PRE-<br>COMPILE|
||**_Link time_**|X VARIANT-LINK-TIME|
||**_Post-build time_**|X VARIANT-POST-BUILD|
|**_Scope / Depen-_**<br>**_dency_**|scope: local||



|**_SWS Item_**|**ECUC_Com_00257 :**||
|---|---|---|
|**_Name_**|ComUpdateBitPosition||
|**_Parent Container_**|ComSignalGroup||
|**_Description_**|Bit position of update-bit in<br>If this attribute is omitted th<br>consistently on sender and<br>Range: 0..63 for CAN and<br>0..511 for CAN FD,<br>0..2031 for FlexRay,<br>0..4294967295 for TP.|side I-PDU.<br>en there is no update-bit. This setting must be<br>on receiver side.<br>LIN,|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucIntegerParamDef||
|**_Range_**|0 .. 4294967295||
|**_Default value_**|--||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
||**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local||
|**_SWS Item_**|**ECUC_Com_00001 :**||



Document ID 015: AUTOSAR_SWS_COM 

153 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Name_**|ComSystemTemplateSignalGrou|pRef|
|---|---|---|
|**_Parent Container_**|ComSignalGroup||
|**_Description_**|Reference to the ISignalToIPduM<br>ISignalGroup (SystemTemplate)|apping that contains a reference to the<br>which this ComSignalGrouprepresents.|
|**_Multiplicity_**|0..1||
|**_Type_**|Foreign reference to[I-SIGNAL-T|O-I-PDU-MAPPING]|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**<br>X|VARIANT-LINK-TIME|
||**_Post-build time_**<br>X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
||**_Link time_**<br>X|VARIANT-LINK-TIME|
||**_Post-build time_**<br>X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: ECU||
|**_Included Containers_**|||
|**_Container Name_**|**_Multiplicity_**<br>**_Scope / Dependenc_**|**_y_**|
|ComGroupSignal|0..*<br>This container contai<br>signals. I.e. signals th|ns the configuration parameters of group<br>at are included within a signalgroup.|



### **10.1.14 ComGroupSignal** 

|**_SWS Item_**|**ECUC_Com_00520 :**|||
|---|---|---|---|
|**_Container Name_**|ComGroupSignal|||
|**_Description_**|This container contains th<br>signals that are included w|e config<br>ithin a|uration parameters of group signals. I.e.<br>signalgroup.|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Configuration Parameters_**||||
|**_SWS Item_**|**ECUC_Com_00259 :**|||
|**_Name_**|ComBitPosition|||
|**_Parent Container_**|ComGroupSignal|||
|**_Description_**|Starting position within the<br>the I-PDU and not in the s<br>configured to Opaque the<br>of the first byte like in little|I-PDU.<br>hadow<br>parame<br>endian|This parameter refers to the position in<br>buffer. If the endianness conversion is<br>ter ComBitPosition shall define the bit0<br>byte order|
|**_Multiplicity_**|1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|0 .. 4294967295|||
|**_Default value_**|--|||
|**_Post-Build Variant Value_**|true|||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|||
|**_SWS Item_**|**ECUC_Com_00158 :**|||



Document ID 015: AUTOSAR_SWS_COM 

154 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Name_**<br>|ComBitSize<br>||
|---|---|---|
|**_Parent Container_**|ComGroupSignal||
|**_Description_**<br>|Size in bits, for integer signal type<br>UINT8_DYN<br>the size shall be configured by Co<br>FLOAT32 and<br>FLOAT64 the size is already defin<br>be omitted.<br>|s. For ComSignalType UINT8_N and<br>mSignalLength. For ComSignalTypes<br>ed by the signal type and therefore may|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucIntegerParamDef||
|**_Range_**|0 .. 64||
|**_Default value_**|--||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**<br>|<br>**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**<br>X|VARIANT-LINK-TIME|
||**_Post-build time_**<br>X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
||**_Link time_**<br>X|VARIANT-LINK-TIME|
||**_Post-build time_**<br>X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local||
|**_SWS Item_**|**ECUC_Com_00165 :**||
|**_Name_**|ComHandleId||
|**_Parent Container_**|ComGroupSignal||
|**_Description_**<br>|The numerical value used as the I<br>This ID identifies signals and sign<br>Com_SignalIdType or Com_Signa<br>|D.<br>al groups in the COM APIs using<br>lGroupIdTypeparameter respectively.|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucIntegerParamDef(Symbolic|Namegenerated for thisparameter)|
|**_Range_**|0 .. 65535||
|**_Default value_**|--||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false||
|**_Post-Build Variant Value_**|false||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**<br>X|All Variants|
|**_Class_**|**_Link time_**<br>--||
||**_Post-build time_**<br>--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**<br>X|All Variants|
||**_Link time_**<br>--||
||**_Post-build time_**<br>--||
|**_Scope / Dependency_**|scope: ECU||
|**_SWS Item_**|**ECUC_Com_00391 :**||
|**_Name_**|ComSignalDataInvalidValue||
|**_Parent Container_**|ComGroupSignal||
|**_Description_**|Defines the data invalid value of t<br>In case the ComSignalType is UIN<br>SINT16, SINT32, SINT64 the strin<br>chapter Integer Type in the AUTO<br>In case the ComSignalType is FL<br>interpreted as defined in the chap<br>specification.<br>In case the ComSignalType is BO<br>defined in the chapter Boolean Ty<br>Incase the ComSignal is a UINT8|he signal.<br>T8, UINT16, UINT32, UINT64, SINT8,<br>g shall be interpreted as defined in the<br>SAR EcuC specification.<br>OAT32, FLOAT64 the string shall be<br>ter Float Type in the AUTOSAR EcuC<br>OLEAN the string shall be interpreted as<br>pe in the AUTOSAR EcuC specification.<br>_N, UINT8_DYNthe string shallbe|



Document ID 015: AUTOSAR_SWS_COM 

155 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||interpreted as a decimal re<br>blanks, e.g. "97 98 100" m<br>0(lowest address), "b" is in<br>address).<br>For the ComSignalType UI<br>number of configured char<br>0-sized dynamic signal.|presen<br>eans a<br>byte 1<br>NT8_D<br>acters.|tation of the characters separated by<br>string "abd", where the char "a" is in byte<br>, and "d" is in byte 2 and (highest<br>YN the dynamic length shall be set to the<br>An empty string "" shall be interpreted as|
|---|---|---|---|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucStringParamDef|||
|**_Default value_**|--|||
|**_maxLength_**|--|||
|**_minLength_**|--|||
|**_regularExpression_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
||**_Post-build time_**|--||
|**_Scope / Dependency_**|scope: local<br>dependency: In case of UI<br>ComSignalDataInvalidValu|NT8_N<br>e has t|the length of<br>o be the same as ComSignalLength.|



|**_SWS Item_**|**ECUC_Com_00157 :**||
|---|---|---|
|**_Name_**|ComSignalEndianness||
|**_Parent Container_**|ComGroupSignal||
|**_Description_**|Defines the endianness of the signa|l's network representation.|
|**_Multiplicity_**|1||
|**_Type_**|EcucEnumerationParamDef||
|**_Range_**|BIG_ENDIAN|--|
||LITTLE_ENDIAN|--|
||OPAQUE|--|
|**_Post-Build Variant_**<br>**_Value_**<br> <br>|<br>true<br><br>||
|**_Value_**<br>**_Configurati-_**<br>|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope_**<br>**_/_**<br>**_Depen-_**<br>|scope: local||
|**_dency_**|||



|**_SWS Item_**|**ECUC_Com_00170 :**|
|---|---|
|**_Name_**|ComSignalInitValue|
|**_Parent Container_**|ComGroupSignal|
|**_Description_**|Initial value for this signal. In case of UINT8_N the default value is a string<br>of length ComSignalLength with all bytes set to 0x00. In case of<br>UINT8_DYN the initial size shall be 0.<br>In case the ComSignalType is UINT8, UINT16, UINT32, UINT64, SINT8,<br>SINT16, SINT32, SINT64 the string shall be interpreted as defined in the<br>chapter Integer Type in the AUTOSAR EcuC specification.<br>In case the ComSignalType is FLOAT32, FLOAT64 the string shall be<br>interpreted as defined in the chapter Float Type in the AUTOSAR EcuC<br>specification.|



Document ID 015: AUTOSAR_SWS_COM 

156 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||In case the ComSignalTyp<br>defined in the chapter Boo<br>In case the ComSignal is a<br>interpreted as a decimal re<br>blanks, e.g. "97 98 100" m<br>0(lowest address), "b" is in<br>address).<br>For the ComSignalType U<br>number of configured char<br>0-sized dynamic signal.<br>|e is BO<br>lean Ty<br>UINT8<br>presen<br>eans a<br>byte 1,<br>INT8_D<br>acters.|OLEAN the string shall be interpreted as<br>pe in the AUTOSAR EcuC specification.<br>_N, UINT8_DYN the string shall be<br>tation of the characters separated by<br>string "abd", where the char "a" is in byte<br>and "d" is in byte 2 and (highest<br>YN the dynamic length shall be set to the<br>An empty string "" shall be interpreted as|
|---|---|---|---|
|**_Multiplicity_**<br>|0..1<br>|||
|**_Type_**|EcucStringParamDef|||
|**_Default value_**<br>|0|||
|**_maxLength_**<br>|--|||
|**_minLength_**<br>|--|||
|**_regularExpression_**|--|||
|**_Post-Build Variant Multipli-_**|<br>true|||
|**_city_**||||
|**_Post-Build Variant Value_**|true|||
|**_Multiplicity_**<br>**_Configuration_**<br>|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**<br>|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|||
||<br>dependency: In case of UI<br>be the same as ComSigna|NT8_N<br>lLength|the length of ComSignalInitValue has to<br>.|
|**_SWS Item_**<br>|**ECUC_Com_00437 :**<br>|||
|**_Name_**|ComSignalLength|||
|**_Parent Container_**|ComGroupSignal|||
|**_Description_**|Description:<br>|||
||For ComSignalType UINT<br>bytes. For ComSignalType<br>bytes. For all other types t<br>The supported maximum l<br>system. For non TP-PDUs<br>of any included signal, is li<br>example, the limit is 8 byte<br>254 for FlexRay.|8_N this<br>UINT8<br>his para<br>ength is<br>the ma<br>mited b<br>s for C|parameter specifies the length n in<br>_DYN it specifies the maximum length in<br>meter shall be ignored.<br>restricted by the used transportation<br>ximum size of a PDU, and therefore also<br>y the concrete bus characteristic. For<br>AN and LIN, 64 bytes for CAN FD and|
|**_Multiplicity_**<br>|0..1<br>|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|0 .. 4294967295|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>false|||
|**_Post-Build Variant Value_**|false|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|<br><br>**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME, VARIANT-POST-<br>|
||||BUILD|
||**_Post-build time_**|--||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**<br>**_Post-build time_**|X<br>--|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD<br>|



157 of 185 

Document ID 015: AUTOSAR_SWS_COM 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Scope / Dependenc_**|**_y_**<br>scope: local|
|---|---|
|**_SWS Item_**|**ECUC_Com_00127 :**|
|**_Name_**|ComSignalType|
|**_Parent Container_**|ComGroupSignal|
|**_Description_**|The AUTOSAR type of the signal. Whether or not the signal is signed or unsigned<br>can be found by examining the value of this attribute.<br>This type could also be used to reserved appropriate storage in AUTOSAR COM.|
|**_Multiplicity_**|1|
|**_Type_**|EcucEnumerationParamDef|
|**_Range_**|BOOLEAN<br>--|
||FLOAT32<br>--|
||FLOAT64<br>--|
||SINT16<br>--|
||SINT32<br>--|
||SINT64<br>--|
||SINT8<br>--|
||UINT16<br>--|
||UINT32<br>--|
||UINT64<br>--|
||UINT8<br>--|
||UINT8_DYN<br>--|
||UINT8_N<br>--|
|**_Post-Build_**<br>**_Variant_**<br>**_Value_**|<br>false|
|**_Value_**<br>**_Configurati-_**|**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link time_**<br>X  VARIANT-LINK-TIME, VARIANT-<br>POST-BUILD|
||**_Post-build time_**<br>--|
|**_Scope_**<br>**_/_**<br>**_Depen-_**|scope: local|
|**_dency_**||



|**_SWS Item_**|**ECUC_Com_10006 :**|
|---|---|
|**_Name_**|ComTimeoutSubstitutionValue|
|**_Parent Container_**|ComGroupSignal|
|**_Description_**|The signal substitution value will be used in case of a timeout and<br>ComRxDataTimeoutAction is set to SUBSTITUTE.<br>In case of UINT8_N the default value is a string of length<br>ComSignalLength with all bytes set to 0x00.<br>In case ofUINT8_DYN the initial size shall be 0.<br>In case the ComSignalType is UINT8, UINT16, UINT32, UINT64, SINT8,<br>SINT16, SINT32, SINT64 the string shall be interpreted as defined in the<br>chapter Integer Type in the AUTOSAR EcuC specification.<br>In case the ComSignalType is FLOAT32, FLOAT64 the string shall be<br>interpreted as defined in the chapter Float Type in the AUTOSAR EcuC<br>specification.<br>In case the ComSignalType is BOOLEAN the string shall be interpreted as<br>defined in the chapter Boolean Type in the AUTOSAR EcuC specification.<br>In case the ComSignal is a UINT8_N, UINT8_DYN the string shall be<br>interpreted as a decimal representation of the characters separated by<br>blanks, e.g. "97 98 100" means a string "abd", where the char "a" is in byte<br>0(lowest address), "b" is in byte 1, and "d" is in byte 2 and (highest<br>address). For the ComSignalType UINT8_DYN the dynamic length shall|



Document ID 015: AUTOSAR_SWS_COM 

158 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||be set to the number of co<br>interpreted as 0-sized dyn|nfigure<br>amic sig|d characters. An empty string "" shall be<br>nal.|
|---|---|---|---|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucStringParamDef|||
|**_Default value_**|--|||
|**_maxLength_**|--|||
|**_minLength_**|--|||
|**_regularExpression_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true|||
|**_Post-Build Variant Value_**|true|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|||



|**_SWS Item_**|**ECUC_Com_00560 :**|
|---|---|
|**_Name_**|ComTransferProperty|
|**_Parent Container_**|ComGroupSignal|
|**_Description_**|Optionally defines whether this group signal shall contribute to the<br>TRIGGERED_ON_CHANGE transfer property of the signal group. If at least one<br>group signal of a signal group has the "ComTransferProperty" configured all other<br>groupsignals of that signalgroupshall have the attribute configured as well.|
|**_Multiplicity_**|0..1|
|**_Type_**|EcucEnumerationParamDef|
|**_Range_**|PENDING<br>A change of the value of this group<br>signal shall not be considered in the<br>evaluation of the signal groups<br>ComTransferProperty.|
||TRIGGERED_ON_CHANGE<br>A change of the value of this group<br>signal shall be considered in the<br>evaluation of the signal groups<br>ComTransferProperty.|
|**_Post-Build Variant_**<br>**_Multiplicity_**|<br>true|
|**_Post-Build Variant_**<br>**_Value_**|<br>true|
|**_Multiplicity Confi-_**|<br>**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
|**_guration Class_**|**_Link time_**<br>X  VARIANT-LINK-TIME|
||**_Post-build time_**<br>X  VARIANT-POST-BUILD|
|**_Value Configura-_**|<br>**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
|**_tion Class_**|**_Link time_**<br>X  VARIANT-LINK-TIME|
||**_Post-build time_**<br>X  VARIANT-POST-BUILD|
|**_Scope / Depen-_**<br>**_dency_**|<br>scope: local|
|**_SWS Item_**|**ECUC_Com_00002 :**|
|**_Name_**|ComSystemTemplateSystemSignalRef|
|**_Parent Container_**|ComGroupSignal|
|**_Description_**|Reference to the ISignalToIPduMapping that contains a reference to the<br>ISignal (System Template) which this ComSignal (or ComGroupSignal)<br>represents.|
|**_Multiplicity_**|0..1|
|**_Type_**|Foreign reference to [I-SIGNAL-TO-I-PDU-MAPPING ]|



159 of 185 

Document ID 015: AUTOSAR_SWS_COM 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Post-Build Variant Multipli_**<br>**_city_**|**_-_**<br>true||||
|---|---|---|---|---|
|**_Post-Build Variant Value_**|true||||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-comp_**|**_ile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**||X|VARIANT-LINK-TIME|
||**_Post-buil_**|**_d time_**|X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-comp_**|**_ile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**||X|VARIANT-LINK-TIME|
||**_Post-buil_**|**_d time_**|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: EC|U|||
|**_Included Containers_**|||||
|**_Container Name_**|**_Multiplici_**|**_ty_**<br>**_Scope / Dep_**|**_endenc_**|**_y_**|
|ComFilter|0..1|This contain<br>AUTOSAR C<br>Note: On se<br>transmission|er contai<br>OM mod<br>nder side<br>mode co|ns the configuration parameters of the<br>ule's filters.<br>the container is used to specify the<br>nditions.|



### **10.1.15 ComTxMode** 

|**_SWS Item_**||**ECUC_Com_00351 :**|
|---|---|---|
|**_Container N_**|**_ame_**|ComTxMode|
|**_Description_**||This container contains the configuration parameters of the AUTOSAR<br>COM module's transmission modes.|
|**_Configurati_**|**_on Param_**|**_eters_**|
|**_SWS Item_**||**ECUC_Com_00137 :**|
|**_Name_**||ComTxModeMode|
|**_Parent Cont_**|**_ainer_**|ComTxMode|
|**_Description_**||The available transmission modes described in [18] shall be extended by the<br>additional mode None.<br>The transmission mode None shall not have any further sub-attributes in the<br>ComTxMode object.|
|**_Multiplicity_**||1|
|**_Type_**||EcucEnumerationParamDef|
|**_Range_**||DIRECT<br>--|
|||MIXED<br>--|
|||NONE<br>Literal for TxMode|
|||PERIODIC<br>--|
|**_Post-Build_**<br>**_Value_**|**_Variant_**|<br>true|
|**_Value_**<br>**_Con_**|**_figurati-_**|**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
|**_on Class_**||**_Link time_**<br>X  VARIANT-LINK-TIME|
|||**_Post-build time_**<br>X  VARIANT-POST-BUILD|
|**_Scope_**<br>**_/_**<br>**_dency_**|**_Depen-_**|scope: local|
|**_SWS Item_**||**ECUC_Com_00281 :**|
|**_Name_**||ComTxModeNumberOfRepetitions|
|**_Parent Cont_**|**_ainer_**|ComTxMode|
|**_Description_**||Defines the number of repetitions for the transmission mode DIRECT and<br>the event drivenpart of transmission mode MIXED.|
|**_Multiplicity_**||0..1|



Document ID 015: AUTOSAR_SWS_COM 

160 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Type_**<br>**_Range_**|EcucIntegerParamDef<br>0 .. 255||
|---|---|---|
|<br>**_Default value_**|<br>--||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**<br>|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
||<br><br>**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local||
|**_SWS Item_**|**ECUC_Com_00282 :**||
|**_Name_**|ComTxModeRepetitionPer|iod|
|**_Parent Container_**|ComTxMode||
|**_Description_**|Defines the repetition peri<br>case ComTxModeNumber<br>equal to 1 and ComTxMod<br>case of the mixed transmi|od in seconds of the multiple transmissions in<br>OfRepetitions is configured greater than or<br>eMode is configured to DIRECT or MIXED. In<br>ssion mode onlythe event drivenpart is affected.|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucFloatParamDef||
|**_Range_**|[0  3600]||
|<br>**_Default value_**|..<br>--||
|**_Post-Build Variant Multipli-_**<br>**_it_**|<br>true||
|**_cy_**<br>**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
||**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local||
|**_SWS Item_**|**ECUC_Com_00180 :**||
|**_Name_**|ComTxModeTimeOffset||
|**_Parent Container_**|ComTxMode||
|**_Description_**|Defines the period in seco<br>Com_IpduGroupStart and<br>ComTxModeMode is confi<br>mixed transmission mode<br>In case ComTxModeTime<br>periodic transmission shall<br>ComMainFunctionTx.|nds between the start of the I-PDU by<br>the first transmission request in case<br>gured to PERIODIC or MIXED. In case of the<br>only the periodic part is affected.<br>Offset is omitted or configured to 0, the first<br>be transmitted within the next invocation of|
|**_Multiplicity_**|_<br>0..1||
|**_Type_**|EcucFloatParamDef||
|**_Range_**|[0 .. 3600]||
|**_Default value_**|--||
|**_Post-Build Variant Multipli-_**|<br>||
|<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||<br>**_Post-build time_**|<br>X  VARIANT-POST-BUILD|



Document ID 015: AUTOSAR_SWS_COM 

161 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|---|---|---|
||**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local||
|**_SWS Item_**|**ECUC_Com_00178 :**||
|**_Name_**|ComTxModeTimePeriod||
|**_Parent Container_**|ComTxMode||
|**_Description_**|Defines the repetition period<br>requests in case ComTxMo<br>In case of the mixed transm|in seconds of the periodic transmission<br>deMode is configured to PERIODIC or MIXED.<br>ission mode onlytheperiodicpart is affected.|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucFloatParamDef||
|**_Range_**|[0 .. 3600]||
|**_Default value_**|--||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
||**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local||



|**_No Included Containers_**|
|---|



### **10.1.16 ComTxModeTrue** 

|**_SWS Item_**|**ECUC_Com_00455 :**|
|---|---|
|**_Container Name_**|ComTxModeTrue|
|**_Description_**|This container contains the configuration parameters of the AUTOSAR<br>COM module's transmission modes in the case the ComFilter evaluates to<br>true.|
|**_Configuration Parameters_**||



|**_Included Containers_**||
|---|---|
|**_Container Name_**|**_Multiplicity_**<br>**_Scope / Dependency_**|
|ComTxMode|1<br>This container contains the configuration parameters of the<br>AUTOSAR COM module's transmission modes.|



### **10.1.17 ComTxModeFalse** 

|**_SWS Item_**|**ECUC_Com_00454 :**|
|---|---|
|**_Container Name_**|ComTxModeFalse|
|**_Description_**|This container contains the configuration parameters of the AUTOSAR<br>COM module's transmission modes in the case the ComFilter evaluates to<br>false.|
|**_Configuration Parameters_**||



Document ID 015: AUTOSAR_SWS_COM 

162 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Included Containers_**||
|---|---|
|**_Container Name_**|**_Multiplicity_**<br>**_Scope / Dependency_**|
|ComTxMode|1<br>This container contains the configuration parameters of the<br>AUTOSAR COM module's transmission modes.|



### **10.1.18 ComGwMapping** 

|**_SWS Item_**|**ECUC_Com_00544 :**||
|---|---|---|
|**_Container Name_**|ComGwMapping||
|**_Description_**|Each instance of this con<br>Signal Gateway.|tainer defines one mapping of the integrated|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|



|**_Configuration Parameters_**|
|---|



|**_Included Containers_**<br>|||
|---|---|---|
|**_Container Name_**|**_Multiplici_**|**_ty_**<br>**_Scope / Dependency_**|
|ComGwDestination|1..*|Each instance of this choice container allows to define one<br>routing destination either by reference to an already configured<br>COM signal / group signal or by a destination description<br>container.|
|ComGwSource|1|This choice container allows the definition of the gateway<br>source signal either by reference to an already configured<br>COM signal / group signal or by a source description<br>container.|



### **10.1.19 ComGwSource** 

|**_SWS Item_**|**ECUC_Com_00545 :**|
|---|---|
|**_Choice container Name_**|ComGwSource|
|**_Description_**|This choice container allows the definition of the gateway source signal<br>either by reference to an already configured COM signal / group signal or<br>bya source description container.|



|**_Container Choices_**|||
|---|---|---|
|**_Container Name_**|**_Multiplicit_**|**_y_**<br>**_Scope / Dependency_**|
|ComGwSignal|0..1|This container allows specifying a gateway source or<br>destination respectively with a reference to a ComSignal or a<br>ComGroupSignal.|
|ComGwSourceDescription|0..1|Description of a gateway source. This container allows<br>defining a gateway source without the configuration of a<br>complete COM signal. This allows adding / changing gateway<br>relationspost build without the configuration of new signals.|



Document ID 015: AUTOSAR_SWS_COM 

163 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **10.1.20 ComGwSourceDescription** 

|**_SWS Item_**|**ECUC_Com_00548 :**|
|---|---|
|**_Container Name_**|ComGwSourceDescription|
|**_Description_**|Description of a gateway source. This container allows defining a gateway<br>source without the configuration of a complete COM signal. This allows<br>adding / changing gateway relations post build without the configuration of<br>new signals.|
|**_Configuration Parameters_**||



|**_SWS Item_**|**ECUC_Com_00259 :**|||
|---|---|---|---|
|**_Name_**|ComBitPosition|||
|**_Parent Container_**|ComGwSourceDescription|||
|**_Description_**|Starting position within the<br>the I-PDU and not in the sh<br>configured to Opaque the<br>of the first byte like in little|I-PDU<br>adow<br>parame<br>endian|. This parameter refers to the position in<br>buffer. If the endianness conversion is<br>ter ComBitPosition shall define the bit0<br>byte order|
|**_Multiplicity_**|1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|0 .. 4294967295|||
|**_Default value_**|--|||
|**_Post-Build Variant Value_**|true|||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|||



|**_SWS Item_**|**ECUC_Com_00158 :**|||
|---|---|---|---|
|**_Name_**|ComBitSize|||
|**_Parent Container_**|ComGwSourceDescriptio|n||
|**_Description_**|Size in bits, for integer sig<br>UINT8_DYN<br>the size shall be configure<br>FLOAT32 and<br>FLOAT64 the size is alrea<br>be omitted.|nal type<br>d by Co<br>dy defin|s. For ComSignalType UINT8_N and<br>mSignalLength. For ComSignalTypes<br>ed by the signal type and therefore may|
|**_Multiplicity_**|0..1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|0 .. 64|||
|**_Default value_**|--|||
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true|||
|**_Post-Build Variant Value_**|true|||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|||



|**_SWS Item_**|**ECUC_Com_00157 :**|
|---|---|
|**_Name_**|ComSignalEndianness|
|**_Parent Container_**|ComGwSourceDescription|
|**_Description_**|Defines the endianness of the signal's network representation.|
|**_Multiplicity_**|1|



Document ID 015: AUTOSAR_SWS_COM 

164 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_Type_**|EcucEnumerationParamDef||
|---|---|---|
|**_Range_**|BIG_ENDIAN|--|
||LITTLE_ENDIAN|--|
||OPAQUE|--|
|**_Post-Build Variant_**<br>**_Value_**|<br>true||
|**_Value_**<br>**_Configurati-_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope_**<br>**_/_**<br>**_Depen-_**<br>**_dency_**|scope: local||



|**_SWS Item_**||**ECUC_Com_00437 :**||
|---|---|---|---|
|**_Name_**||ComSignalLength||
|**_Parent Container_**||ComGwSourceDescription||
|**_Description_**||Description:<br>For ComSignalType UINT8_N thi<br>bytes. For ComSignalType UINT8<br>bytes. For all other types this para<br>The supported maximum length is<br>system. For non TP-PDUs the ma<br>of any included signal, is limited b<br>example, the limit is 8 bytes for C<br>254 for FlexRay.|s parameter specifies the length n in<br>_DYN it specifies the maximum length in<br>meter shall be ignored.<br>restricted by the used transportation<br>ximum size of a PDU, and therefore also<br>y the concrete bus characteristic. For<br>AN and LIN, 64 bytes for CAN FD and|
|**_Multiplicity_**||0..1||
|**_Type_**||EcucIntegerParamDef||
|**_Range_**||0 .. 4294967295||
|**_Default value_**||--||
|**_Post-Build Variant_**<br>**_city_**|**_Multipli-_**|<br>false||
|**_Post-Build Variant V_**|**_alue_**|false||
|**_Multiplicity_**<br>**_Confi_**|**_guration_**|**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
|**_Class_**||**_Link time_**<br>X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
|||**_Post-build time_**<br>--||
|**_Value Configuration_**|**_Class_**|**_Pre-compile time_**<br>X|VARIANT-PRE-COMPILE|
|||**_Link time_**<br>X|VARIANT-LINK-TIME, VARIANT-POST-<br>BUILD|
|||**_Post-build time_**<br>--||
|**_Scope / Dependenc_**|**_y_**|scope: local||
|**_SWS Item_**|**ECUC_**|**Com_00127 :**||
|**_Name_**|ComSig|nalType||
|**_Parent Container_**|ComGw|SourceDescription||
|**_Description_**|The AU<br>can be f<br>This typ|TOSAR type of the signal. Whethe<br>ound by examining the value of th<br>e could also be used to reserved a|r or not the signal is signed or unsigned<br>is attribute.<br> ppropriate storage in AUTOSAR COM.|
|**_Multiplicity_**|1|||
|**_Type_**|EcucEn|umerationParamDef||
|**_Range_**|BOOLE|AN|--|
||FLOAT|32|--|
||FLOAT|64|--|
||SINT16||--|
||SINT32||--|
||SINT64||--|
||SINT8||--|



Document ID 015: AUTOSAR_SWS_COM 

165 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||UINT16|--|
|---|---|---|
||UINT32|--|
||UINT64|--|
||UINT8|--|
||UINT8_DYN|--|
||UINT8_N|--|
|**_Post-Build_**<br>**_Variant_**<br>**_Value_**|<br>false||
|**_Value_**<br>**_Configurati-_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link time_**|X  VARIANT-LINK-TIME, VARIANT-<br>POST-BUILD|
||**_Post-build time_**|--|
|**_Scope_**<br>**_/_**<br>**_Depen-_**|scope: local||
|**_dency_**|||



|**_SWS Item_**|**ECUC_Com_00257 :**|
|---|---|
|**_Name_**|ComUpdateBitPosition|
|**_Parent Container_**|ComGwSourceDescription|
|**_Description_**|Bit position of update-bit inside I-PDU.<br>If this attribute is omitted then there is no update-bit. This setting must be<br>consistently on sender and on receiver side.<br>Range: 0..63 for CAN and LIN,<br>0..511 for CAN FD,<br>0..2031 for FlexRay,<br>0..4294967295 for TP.|
|**_Multiplicity_**|0..1|
|**_Type_**|EcucIntegerParamDef|
|**_Range_**|0 .. 4294967295|
|**_Default value_**|--|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true|
|**_Post-Build Variant Value_**|true|
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**<br>X  VARIANT-LINK-TIME|
||**_Post-build time_**<br>X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
||**_Link time_**<br>X  VARIANT-LINK-TIME|
||**_Post-build time_**<br>X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|
|**_SWS Item_**|**ECUC_Com_00550 :**|
|**_Name_**|ComGwIPduRef|
|**_Parent Container_**|ComGwSourceDescription|
|**_Description_**|Reference to an I-PDU of a Signal Gateway source or destination<br>description.|
|**_Multiplicity_**|1|
|**_Type_**|Reference to[ComIPdu]|
|**_Post-Build Variant Value_**|true|
|**_Value Configuration Class_**|**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
||**_Link time_**<br>X  VARIANT-LINK-TIME|
||**_Post-build time_**<br>X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**||
|**_No Included Containers_**||



Document ID 015: AUTOSAR_SWS_COM 

166 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **10.1.21 ComGwDestination** 

|**_SWS Item_**|**ECUC_Com_00546 :**||
|---|---|---|
|**_Choice container Name_**|ComGwDestination||
|**_Description_**|Each instance of this choi<br>destination either by refer<br>groupsignal or bya desti|ce container allows to define one routing<br>ence to an already configured COM signal /<br>nation description container.|
|**_Post-Build Variant Multipli-_**<br>**_city_**|true||
|**_Multiplicity_**<br>**_Configuration_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|



|**_Container Choices_**<br>|||
|---|---|---|
|**_Container Name_**|**_Multiplicity_**|**_Scope / Dependency_**|
|ComGwDestinationDescriptio<br>n|0..1|Description of a gateway destination. This container allows<br>defining a gateway destination without the configuration of a<br>complete COM signal. This allows adding / changing gateway<br>relationspost build without the configuration of new signals.|
|ComGwSignal|0..1|This container allows specifying a gateway source or<br>destination respectively with a reference to a ComSignal or a<br>ComGroupSignal.|



### **10.1.22 ComGwDestinationDescription** 

|**_SWS Item_**|**ECUC_Com_00549 :**|
|---|---|
|**_Container Name_**|ComGwDestinationDescription|
|**_Description_**|Description of a gateway destination. This container allows defining a<br>gateway destination without the configuration of a complete COM signal.<br>This allows adding / changing gateway relations post build without the<br>configuration of new signals.|
|**_Configuration Parameters_**||



|**_SWS Item_**|**ECUC_Com_00259 :**|||
|---|---|---|---|
|**_Name_**|ComBitPosition|||
|**_Parent Container_**|ComGwDestinationDescri|ption||
|**_Description_**|Starting position within the<br>the I-PDU and not in the s<br>configured to Opaque the<br>of the first byte like in little|I-PDU<br>hadow<br>parame<br>endian|. This parameter refers to the position in<br>buffer. If the endianness conversion is<br>ter ComBitPosition shall define the bit0<br>byte order|
|**_Multiplicity_**|1|||
|**_Type_**|EcucIntegerParamDef|||
|**_Range_**|0 .. 4294967295|||
|**_Default value_**|--|||
|**_Post-Build Variant Value_**|true|||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X|VARIANT-PRE-COMPILE|
||**_Link time_**|X|VARIANT-LINK-TIME|
||**_Post-build time_**|X|VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|||



Document ID 015: AUTOSAR_SWS_COM 

167 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_SWS Item_**|**ECUC_Com_00157 :**||
|---|---|---|
|**_Name_**|ComSignalEndianness||
|**_Parent Container_**|ComGwDestinationDescription||
|**_Description_**|Defines the endianness of the signal'|s network representation.|
|**_Multiplicity_**|1||
|**_Type_**|EcucEnumerationParamDef||
|**_Range_**|BIG_ENDIAN|--|
||LITTLE_ENDIAN|--|
||OPAQUE|--|
|**_Post-Build Variant_**<br>**_Value_**<br>|<br>true<br> <br>||
|**_Value Configurati-_**<br>|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|**_on Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope_**<br>**_/_**<br>**_Depen-_**<br>|scope: local||
|**_dency_**|||



|**_SWS Item_**|**ECUC_Com_00170 :**||
|---|---|---|
|**_Name_**|ComSignalInitValue||
|**_Parent Container_**|ComGwDestinationDescrip|tion|
|**_Description_**|Initial value for this signal.<br>of length ComSignalLengt<br>UINT8_DYN the initial size<br>In case the ComSignalTyp<br>SINT16, SINT32, SINT64 t<br>chapter Integer Type in the<br>In case the ComSignalTyp<br>interpreted as defined in th<br>specification.<br>In case the ComSignalTyp<br>defined in the chapter Boo<br>In case the ComSignal is a<br>interpreted as a decimal re<br>blanks, e.g. "97 98 100" m<br>0(lowest address), "b" is in<br>address).<br>For the ComSignalType UI<br>number of configured char<br>0-sized dynamic signal.|In case of UINT8_N the default value is a string<br>h with all bytes set to 0x00. In case of<br>shall be 0.<br>e is UINT8, UINT16, UINT32, UINT64, SINT8,<br>he string shall be interpreted as defined in the<br>AUTOSAR EcuC specification.<br>e is FLOAT32, FLOAT64 the string shall be<br>e chapter Float Type in the AUTOSAR EcuC<br>e is BOOLEAN the string shall be interpreted as<br>lean Type in the AUTOSAR EcuC specification.<br>UINT8_N, UINT8_DYN the string shall be<br>presentation of the characters separated by<br>eans a string "abd", where the char "a" is in byte<br>byte 1, and "d" is in byte 2 and (highest<br>NT8_DYN the dynamic length shall be set to the<br>acters. An empty string "" shall be interpreted as|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucStringParamDef||
|**_Default value_**|0||
|**_maxLength_**|--||
|**_minLength_**|--||
|**_regularExpression_**|--||
|**_Post-Build Variant Multipli_**<br>**_city_**|**_-_**<br>true||
|**_Post-Build Variant Value_**|true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
|<br><br>**_Class_**|**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
||<br><br>**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local<br>dependency: In case of UI<br>be the same as ComSigna|NT8_N the length of ComSignalInitValue has to<br>lLength.|



Document ID 015: AUTOSAR_SWS_COM 

168 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_SWS Item_**<br>|**ECUC_Com_00232 :**<br>||
|---|---|---|
|**_Name_**|ComTransferProperty||
|**_Parent_**<br>**_Contai-_**<br>**_ner_**|ComGwDestinationDescription||
|**_Description_**|Defines if a write access to this signal can trigger the trans<br>corresponding I-PDU. If the I-PDU is triggered, depends a<br>mode of the correspondingI-PDU.|mission of the<br>lso on the transmission|
|**_Multiplicity_**|0..1||
|**_Type_**|EcucEnumerationParamDef||
|**_Range_**|PENDING|A write access to this<br>signal never triggers the<br>transmission of the<br>correspondingI-PDU.|
||TRIGGERED|Depending on the<br>transmission mode, a write<br>access to this signal can<br>trigger the transmission of<br>the correspondingI-PDU.|
||TRIGGERED_ON_CHANGE|Depending on the<br>transmission mode, a write<br>access to this signal can<br>trigger the transmission of<br>the corresponding I-PDU,<br>but only in case the written<br>value is different to the<br>locally stored (last sent or<br>initial value) in length or<br>value.|
||TRIGGERED_ON_CHANGE_WITHOUT_REPETITION|Depending on the<br>transmission mode, a write<br>access to this signal can<br>trigger the transmission of<br>the corresponding I-PDU<br>just once without a<br>repetition, but only in case<br>the written value is<br>different to the locally<br>stored (last sent or initial<br>value)in length or value.|
||TRIGGERED_WITHOUT_REPETITION|Depending on the<br>transmission mode, a write<br>access to this signal can<br>trigger the transmission of<br>the corresponding I-PDU<br>just once without a<br>repetition.|
|**_Post-Build Vari-_**<br>**_ant Multiplicity  _**|<br><sup>true</sup>||
|**_Post-Build Vari-_**<br>**_ant Value_**|<br>true||
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**|X VARIANT-PRE-<br>COMPILE|
|<br>**_Class_**|**_Link time_**|X VARIANT-LINK-TIME|
||**_Post-build time_**|X VARIANT-POST-BUILD|
|**_Value_**<br>**_Configu-_**|**_Pre-compile time_**|X VARIANT-PRE-|
|**_ration Class_**||COMPILE|
||**_Link time_**<br>**_Post-build time_**|X VARIANT-LINK-TIME<br>X VARIANT-POST-BUILD|



169 of 185 

Document ID 015: AUTOSAR_SWS_COM 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**_<mark>Scope / Depen-</mark>_** scope: local **_dency_** 

|**_SWS Item_**|**ECUC_Com_00257 :**|
|---|---|
|**_Name_**|ComUpdateBitPosition|
|**_Parent Container_**|ComGwDestinationDescription|
|**_Description_**|Bit position of update-bit inside I-PDU.<br>If this attribute is omitted then there is no update-bit. This setting must be<br>consistently on sender and on receiver side.<br>Range: 0..63 for CAN and LIN,<br>0..511 for CAN FD,<br>0..2031 for FlexRay,<br>0..4294967295 for TP.|
|**_Multiplicity_**|0..1|
|**_Type_**|EcucIntegerParamDef|
|**_Range_**|0 .. 4294967295|
|**_Default value_**|--|
|**_Post-Build Variant Multipli-_**<br>**_city_**|<br>true|
|**_Post-Build Variant Value_**|true|
|**_Multiplicity_**<br>**_Configuration_**|**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
|**_Class_**|**_Link time_**<br>X  VARIANT-LINK-TIME|
||**_Post-build time_**<br>X  VARIANT-POST-BUILD|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
||**_Link time_**<br>X  VARIANT-LINK-TIME|
||**_Post-build time_**<br>X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|scope: local|
|**_SWS Item_**|**ECUC_Com_00550 :**|
|**_Name_**|ComGwIPduRef|
|**_Parent Container_**|ComGwDestinationDescription|
|**_Description_**|Reference to an I-PDU of a Signal Gateway source or destination<br>description.|
|**_Multiplicity_**|1|
|**_Type_**|Reference to[ComIPdu]|
|**_Post-Build Variant Value_**|true|
|**_Value Configuration Class_**|<br>**_Pre-compile time_**<br>X  VARIANT-PRE-COMPILE|
||**_Link time_**<br>X  VARIANT-LINK-TIME|
||**_Post-build time_**<br>X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**||
|**_Included Containers_**||
|**_Container Name_**|**_Multiplicity_**<br>**_Scope / Dependency_**|
|ComFilter|0..1<br>This container contains the configuration parameters of the<br>AUTOSAR COM module's Filters.<br>Note: On sender side the container is used to specify the<br>transmission mode conditions.|



### **10.1.23 ComGwSignal** 

|**_SWS Item_**|**ECUC_Com_00551 :**|
|---|---|
|**_Container Name_**|ComGwSignal|
|**_Description_**|This containerallows specifying a gateway source ordestination|



Document ID 015: AUTOSAR_SWS_COM 

170 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||respectivelywith a referen|ce to a ComSignal or a ComGroupSignal.|
|---|---|---|
|**_Configuration Parameters_**|||
|**_SWS Item_**|**ECUC_Com_00547 :**||
|**_Name_**|ComGwSignalRef||
|**_Parent Container_**|ComGwSignal||
|**_Description_**|Reference to an object of<br>ComGroupSignal.|a gateway relation. Either to a ComSignal or a|
|**_Multiplicity_**|1||
|**_Type_**|Choice reference to[Com|GroupSignal,ComSignal]|
|**_Post-Build Variant Value_**|true||
|**_Value Configuration Class_**|<br>**_Pre-compile time_**|X  VARIANT-PRE-COMPILE|
||**_Link time_**|X  VARIANT-LINK-TIME|
||**_Post-build time_**|X  VARIANT-POST-BUILD|
|**_Scope / Dependency_**|||
|**_No Included Containers_**|||



## **10.2 Configuration Rules** 

### **10.2.1 General Rules** 

**[SWS_Com_00401]** ⌈ It is illegal for any two of the following parameters to have the same value: 

   - shortName of a ComSignal 

   - shortName of a ComSignalGroup 

   - shortName of a ComGroupSignal 

   - shortName of a ComIPdu 

   - shortName of a ComIPduGroup 

- ⌋ (SRS_Com_02067) 

**[SWS_Com_00732]** ⌈ It is illegal for any of the following five parameters: 

- ComNotification 

- ComErrorNotification 

- ComTimeoutNotification 

- ComInvalidNotification 

- ComIPduCallout 

to have the same value as any of the following five parameters 

   - Com_<shortName of a ComSignal> 

   - Com_<shortName of a ComSignalGroup> 

   - Com_<shortName of a ComGroupSignal> 

   - Com_<shortName of a ComIPdu> 

   - Com_<shortName of a ComIPduGroup> 

- ⌋ (SRS_Com_02067) 

**[SWS_Com_00402]** ⌈ It is illegal for any of the following parameters not to be formulated according to C’s identifier rules: 

Document ID 015: AUTOSAR_SWS_COM 

171 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



- shortName of a ComSignal 

- shortName of a ComSignalGroup 

- shortName of a ComGroupSignal 

- shortName of a ComIPdu 

- shortName of a ComIPduGroup 

- ComNotification 

- ComErrorNotification 

- ComTimeoutNotification 

- ComInvalidNotification 

- ComIPduCallout 

⌋ (SRS_Com_02067) 

### **10.2.2 Signal Configuration** 

More than one signal can be packed into an I-PDU as long as the following packing rules are fulfilled: 

**[SWS_Com_00102]** ⌈ ComSignal/ ComGroupSignal are not allowed to overlap each other. ⌋ (SRS_Com_02067) 

It is explicitly allowed that a ComSignal/ ComGroupSignal may have the size 0, see ECUC_Com_00158. 

A signal of size 0 never overlaps other signals. Therefore, it can be configured to an arbitrary position within the I-PDU. The position of a zero sized signal is only relevant in case receiving an I-PDU partially. 

**[SWS_Com_00105]** ⌈ ComSignal/ ComGroupSignal of ComSignalType UINT8_N and UINT8_DYN shall be byte aligned (ComBitPosition is a multiple of 8). ⌋ (SRS_Com_02067) 

**[SWS_Com_00443]** ⌈ A ComSignal/ ComGroupSignal of type uint8[n] shall always be mapped to an n-bytes sized ComSignal/ ComGroupSignal. ⌋ (SRS_Com_02067) 

**[SWS_Com_00553]** ⌈ A ComSignal/ ComGroupSignal of type uint8[n] shall be configured to have OPAQUE endianness. ⌋ (SRS_Com_02067) 

**[SWS_Com_00754]** ⌈ A dynamic length I-PDU shall contain at most one dynamic length signal. ⌋ (SRS_Com_02091, SRS_Com_02092) 

**[SWS_Com_00755]** ⌈ The dynamic length signal shall be placed last in a dynamic length I-PDU. ⌋ (SRS_Com_02091, SRS_Com_02093) 

**[SWS_Com_00756]** ⌈ The ComSignalLength parameter shall be configured to the maximum size/ length for dynamic length signals. ⌋ (SRS_Com_02091, SRS_Com_02097) 

Document ID 015: AUTOSAR_SWS_COM 

172 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00310]** ⌈ For I-PDUs with transmission mode _DIRECT_ or _MIXED_ with ComTxModeNumberOfRepetitions greater or equal 1 no update-bit (ComUpdateBitPosition) shall be configured. ⌋ (SRS_Com_02067, SRS_Com_02030) 

**[SWS_Com_00785]** ⌈ The ComBitSize of a (group) signal shall not extend past the size of its configured ComSignalType. ⌋ (SRS_Com_02067) 

For example, the ComBitSize of a signal with ComSignalType UINT8 shall not exceed 8 bits. 

**[SWS_Com_00790]** ⌈ The configured string of ComSignalInitValues/ ComSignalDataInvalidValue shall be interpreted according to the definitions of [22] for the boolean and all numerical types. ⌋ (SRS_Com_02067) 

**[SWS_Com_00859]** ⌈ In case a ComSignalDataInvalidValue is configured for a ComSignal that is included in a ComIPdu with ComIPduDirection _RECEIVE_ , the ComDataInvalidAction shall also be configured for this ComSignal. ⌋ (SRS_Com_02079, SRS_Com_02087) 

### **10.2.3 Signal Group Configuration** 

**[SWS_Com_00365]** ⌈ It shall not be allowed to configure signal groups for routing with data type differences between receive and transmit signal group. A sub-setting of signal groups (as defined in SWS_Com_00735) shall be supported. ⌋ (SRS_Com_02067) 

How the signals of signal groups are placed within an I-PDU is not restricted. It is allowed to define interlaced signal groups, or to place other signals within the wholes of a signal group. 

**[SWS_Com_00860]** ⌈ In case a ComSignalDataInvalidValue is configured for at least one ComGroupSignal of a ComSignalGroup that is included in a ComIPdu with ComIPduDirection _RECEIVE_ , the ComDataInvalidAction shall also be configured for this ComSignalGroup. ⌋ (SRS_Com_02079, SRS_Com_02087) 

### **10.2.4 Transmission Mode Configuration** 

**[SWS_Com_00465]** ⌈ Every ComTxModeTrue or ComTxModeFalse that is a potential result of the configured/ calculated TMS must be configured. Within the ComTxIPdu, at least one of the containers ComTxModeTrue or ComTxModeFalse has to be included. ⌋ (SRS_Com_02067) 

### **10.2.5 Signal Gateway Configuration** 

**[SWS_Com_00384]** ⌈ The ComBitSize of a received and to be routed ComSignal shall not differ. ⌋ (SRS_Com_02067) 

Document ID 015: AUTOSAR_SWS_COM 

173 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**[SWS_Com_00598]** ⌈ A signal or signal group contained in an I-PDU with ComIPduType configured as TP shall not be configured as source or destination within the ComGwMapping configuration container. ⌋ (SRS_PduR_06055) 

Additionally to reception deadline monitoring of a ComSignal, to be routed by the Signal Gateway, it is possible to configure update-bits via ComUpdateBitPosition, for the transmit signal. In this case, the receiving node can detect if the sender has really updated the signal or it is just repeated by the Signal Gateway. If this is necessary depends on the use-case. 

### **10.2.6 Filter Configuration** 

**[SWS_Com_00535]** ⌈ For the ComFilterAlgorithm _ONE_EVERY_N_ , the ComFilterOffset shall be configured to a value lesser than ComFilterPeriod. ⌋ (SRS_Com_02067) 

### **10.2.7 Post Build Configuration** 

**[SWS_Com_00373]** ⌈ The post-build time configuration part (post-compile and postlink time) can only be updated when it is not in use. ⌋ (SRS_Com_02067, SRS_PduR_06002) 

**[SWS_Com_00487]** ⌈ The complete post-build time configurable configuration shall be identifiable by a unique identifier. ⌋ (SRS_PduR_06097) 

### **10.2.8 Dynamic Length I-PDUs** 

**[SWS_Com_00817]** ⌈ I-PDUs including metadata shall not be configured as dynamic length I-PDUs. ⌋ (SRS_Com_02067) 

The above restriction is necessary, since the length of the dynamic length signal could not be derived correctly, when the I-PDU contains additional metadata. 

Since the FlexRay Interface does only support even values for the I-PDU length, it is not recommend to configure dynamic length I-PDU to be send via FrIf. Instead, the FlexRay TP module should be used to transport dynamic length I-PDUs via FlexRay. 

### **10.2.9 Replicated I-PDUs** 

**[SWS_Com_00834]** ⌈ If an I-PDU is configured for replication (includes a ComIPduReplication), this I-PDU shall also have configured an I-PDU counter (ComIPduCounter) with a counter threshold (ComIPduCounterThreshold) set to 0. ⌋ (SRS_Com_02102) 

For further information on this constraint see 7.10. 

Document ID 015: AUTOSAR_SWS_COM 

174 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



### **10.2.10 I-PDU group** 

**[SWS_Com_00871]** ⌈ All I-PDUs that are contained within one I-PDU group shall have the same ComIPduDirection. ⌋ (SRS_Com_00218) 

Since the nesting of I-PDU groups is only conceptual (see Chapter 7.3.5.1), the above requirements restricts also all nested I-PDU groups to have the same ComIPduDirection. 

Document ID 015: AUTOSAR_SWS_COM 

175 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **11 Not Applicable Requirements** 

**[SWS_Com_00999]** ⌈ These requirements are not applicable to this specification. ⌋ (SRS_BSW_00171, SRS_BSW_00170, SRS_BSW_00383, SRS_BSW_00375, SRS_BSW_00416, SRS_BSW_00437, SRS_BSW_00168, SRS_BSW_00423, SRS_BSW_00424, SRS_BSW_00426, SRS_BSW_00427, SRS_BSW_00428, SRS_BSW_00429, SRS_BSW_00433, SRS_BSW_00417, SRS_BSW_00409, SRS_BSW_00386, SRS_BSW_00161, SRS_BSW_00162, SRS_BSW_00005, SRS_BSW_00164, SRS_BSW_00325, SRS_BSW_00413, SRS_BSW_00347, SRS_BSW_00307, SRS_BSW_00410, SRS_BSW_00314, SRS_BSW_00353, SRS_BSW_00361, SRS_BSW_00302, SRS_BSW_00328, SRS_BSW_00006, SRS_BSW_00378, SRS_BSW_00306, SRS_BSW_00308, SRS_BSW_00309, SRS_BSW_00009, SRS_BSW_00010, SRS_BSW_00333, SRS_BSW_00321, SRS_BSW_00341, SRS_BSW_00334) 

Document ID 015: AUTOSAR_SWS_COM 

176 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



# **12 Appendix A** 

This appendix contains use cases with different transmission modes and the necessary configuration for these. Table 10 shows the notation of the use case diagrams. 

|**_Notation_**|**_Description_**|
|---|---|
|tc, tc1, tc2|cycle times|
|td|cycle time of N-Times sent signals|
|tr|minimum SW reaction time of COM-Layer due to internal main cycle time|
|V|Value:<br>x stands for an arbitrary value/ value range,<br>a…w for specific values / value ranges, defined by the user, with<br>a <> b, _range a_is disjoint from_range b_.|
||request from RTE to the COM-Layer|
||request from COM-Layer to PDU Router|
||potential but skipped request from COM-Layer to PDU Router (e.g. because of a<br>newsendrequest by theRTEordelayed due tominimumdelay time)|
|dt|minimum delay time: minimum distance between two requests to PDU Router|
|without TMS<br>switch|without switching of the TMS (see 7.3.3.2) from_true_to_false_or vice versa|
|with TMS switch|with switching of the TMS (see 7.3.3.2) from_true_to_false_or vice versa (from TM<br>1 to TM 2);one TM is named before the “+” and one behind in the description|



**Table 10: Legend for use case diagrams.** 

**Use case 1** shows an I-PDU that is sent out cyclically with a cycle time tc. This I-PDU consists of signals that all have the ComTransferProperty _PENDING_ . It is configured that the transmission takes place when the TMS evaluates to true. 



<!-- Start of picture text -->
v=x v=x v=x<br>tc tc tc tc tc<br>t<br><!-- End of picture text -->

**Figure 10: Use case 1, TM periodic (without TMS switch, see Chapter 7.3.3.2)** 

|**_ComSignal _**||
|---|---|
|**_ComTransferProperty_**|PENDING or TRIGGERED<br>(TRIGGERED has no influence)|
|**_ComFilter_**||
|**_ComFilterAlgorithm_**|ALWAYS|



Document ID 015: AUTOSAR_SWS_COM 

177 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



|**_ComIPdu_**||
|---|---|
|**_ComIPduDirection _**|SEND|
|**_ComTxModeTrue_**||
|**_ComTxModeTimePeriod_**|tc|
|**_ComTxModeMode_**|PERIODIC|
|**_ComTxIPdu_**||
|**_ComMinimumDelayTime_**|0 or omitted|



**Table 11: Relevant I-PDU transmission configuration for use case 1** 

Because of the configuration of the parameter ComFilterAlgorithm _ALWAYS_ of the ComFilter, there is no need to configure a transmission mode for the case that the TMS evaluates to false. 

It does not make any difference in the behavior whether the ComFilterAlgorithm parameter of the ComFilter is set for all the signals within the I-PDU to _ALWAYS_ or if the ComFilter is not defined (does not contribute to the evaluation of the TMS), see SWS_Com_00255. 

Document ID 015: AUTOSAR_SWS_COM 

178 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**Use case 2** shows an I-PDU which is sent out three times whenever a value is given by the upper (Com_SendSignal or Com_SendSignalGroup). The time between two transmissions is td. This I-PDU consists of signals, which all have the ComTransferProperty _TRIGGERED_ . It is configured that the transmission takes place when the TMS evaluates to true. 



**Figure 11: Use case 2, TM DIRECT  (N-Times) here n = 2 (without TMS switch)** 

|**_ComGeneral_**||
|---|---|
|**_ComEnableMDTForCyclicTransmission_**|true|
|**_ComSignal _**||
|**_ComTransferProperty_**|TRIGGERED|
|**_ComFilter _**||
|**_ComFilterAlgorithm_**|ALWAYS|
|**_ComIPdu_**||
|**_ComIPduDirection_**|SEND|
|**_ComTxModeTrue_**||
|**_ComTxModeMode_**|DIRECT|
|**_ComTxModeNumberOfRepetitions_**|2|
|**_ComTxModeRepetitionPeriod_**|td|
|**_ComTxIPdu_**||
|**_ComMinimumDelayTime_**|dt|



**Table 12: Relevant I-PDU transmission configuration for use case 2** 

If there is a new send request by the RTE before the ongoing repetition cycle is completed, the new repetition cycle is started and the rest of the last one is discarded. 

Document ID 015: AUTOSAR_SWS_COM 

179 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**Use case 3** shows an I-PDU which is send out cyclically with a cycle time tc1 if value v = a (TMS evaluates to true) and with a cycle time tc2 if value v = b (TMS evaluates to false). The I-PDU consists of signals, which all have the ComTransferProperty _PENDING_ . 



**Figure 12: Use case 3, TM periodic + periodic (with TMS switch)** 

|**_ComGeneral _**||
|---|---|
|**_ComEnableMDTForCyclicTransmission_**|true|
|**_ComSignal _**||
|**_ComTransferProperty_**|PENDING or TRIGGERED<br>(TRIGGERED has no influence)|
|**_ComFilter_**||
|**_ComFilterAlgorithm_**|any filter mapping value a to true and value b<br>to false|
|**_ComIPdu_**||
|**_ComIPduDirection _**|SEND|
|**_ComTxModeTrue_**||
|**_ComTxModeMode_**|PERIODIC|
|**_ComTxModeTimePeriod_**|tc1|
|**_ComTxModeFalse_**||
|**_ComTxModeMode_**|PERIODIC|
|**_ComTxModeTimePeriod_**|tc2|
|**_ComTxIPdu_**||
|**_ComMinimumDelayTime_**|dt|



**Table 13: Relevant I-PDU transmission configuration for use case 3** 

The TMS switch caused by the new value v = b, starts a new cycle within the next main function and the new value is sent out. Nevertheless, the minimum delay time dt has to be taken into account, since ComEnableMDTForCyclicTransmission is set to true. 

For the parameter ComFilterAlgorithm, the following filters defined in [17] can be used for this use-case: 

- _MASKED_NEW_EQUALS_X_ 

- _MASKED_NEW_DIFFERS_X_ 

- _MASKED_NEW_DIFFERS_MASKED_OLD_ 

- _NEW_IS_WITHIN_ 

- _NEW_IS_OUTSIDE_ 

Document ID 015: AUTOSAR_SWS_COM 

180 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



**Use case 4** shows an I-PDU which is send out cyclically with a cycle time tc if value v = a (TMS evaluates to true) and if value v = b (TMS evaluates to false) it is sent out three times whenever the value is given by the RTE. The time between two transmissions is td. The I-PDU consists of signals that all have the ComTransferProperty _TRIGGERED_ . 



**Figure 13: Use case 4 scenario a, TM periodic +** **_DIRECT_ /N-Times, here n = 2 (with TMS switch)** 



**Figure 14: Use case 4 scenario b, TM periodic +** **_DIRECT_ /N-Times, here n = 2 (with TMS switch)** 

|**_ComGeneral _**||
|---|---|
|**_ComEnableMDTForCyclicTransmission_**|True|
|**_ComSignal_**||
|**_ComTransferProperty_**|TRIGGERED|
|**_ComFilter_**||
|**_ComFilterAlgorithm_**|any filter mapping value a to true and value b<br>to false|
|**_ComIPdu_**||
|**_ComIPduDirection _**|SEND|
|**_ComTxModeTrue_**||
|**_ComTxModeMode_**|PERIODIC|
|**_ComTxModeTimePeriod_**|tc|
|**_ComTxModeFalse_**||
|**_ComTxModeMode_**|DIRECT|
|**_ComTxModeNumberOfRepetitions_**|2|
|**_ComTxModeRepetitionPeriod_**|td|
|**_ComTxIPdu_**||
|**_ComMinimumDelayTime_**|dt|



**Table 14: Relevant I-PDU transmission configuration for use case 4** 

Document ID 015: AUTOSAR_SWS_COM 

181 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



After the switch from ComTxModeMode _DIRECT_ to _PERIODIC_ the cycle is started within the next main function and the new value a is sent out with respect to ComMinimumDelayTime dt. 

**Use case 5** shows an I-PDU which is send out cyclically with a cycle time tc and if the value (the same or a new one) is given by the RTE it is also sent out directly three times. The time between two of these three transmissions is always td. The I-PDU consists of signals that all have the ComTransferProperty _TRIGGERED_ . 



**Figure 15: Use case 5 scenario a, TM** **_MIXED_ , here n = 2 (without TMS switch)** 



**Figure 16: Use case 5 scenario b, TM** **_MIXED_ , here n = 2 (without TMS switch)** 

|**_ComGeneral _**||
|---|---|
|**_ComEnableMDTForCyclicTransmission_**|true|
|**_ComSignal _**||
|**_ComTransferProperty_**|TRIGGERED|
|**_ComFilter _**||
|**_ComFilterAlgorithm_**|ALWAYS|
|**_ComIPdu_**||
|**_ComIPduDirection _**|SEND|
|**_ComTxModeTrue_**||
|**_ComTxModeMode_**|MIXED|
|**_ComTxModeTimePeriod_**|tc|



Document ID 015: AUTOSAR_SWS_COM 

182 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



||**_ComTxModeNumberOfRepetitions_**|2|
|---|---|---|
||**_ComTxModeRepetitionPeriod_**|td|
|**_ComTxIPdu_**|||
|**_ComM_**|**_inimumDelayTime_**|dt|



**Table 15: Relevant I-PDU transmission configuration for use case 5** 

If the next transmission caused by the periodic part of the ComTxModeMode _MIXED_ should take place within the timeout dt (ComMinimumDelayTime) after a transmission of the _DIRECT_ (N-Times) part, this sent out is delayed until the minimum delay time is elapsed. However, after that the next period of the periodic part is shortened so that there is only an intermediate phase shift of the periodic part but no continuous one. 

**Use case 6** shows an I-PDU which is send out cyclically with a cycle time tc2 if value v = b (TMS evaluates to false). If value v = a (TMS evaluates to true) it is sent out cyclically with a cycle time tc1 and whenever the value v = a is given by the RTE it is also sent out directly three times. The time between two of these three transmissions is always td. The I-PDU consists of signals that all have the ComTransferProperty _TRIGGERED_ . 



**Figure 17: Use Case 6, TM** **_MIXED_ , here n= 2 + periodic (with TMS switch)** 

|**_ComGeneral _**||
|---|---|
|**_ComEnableMDTForCyclicTransmission_**|true|
|**_ComSignal _**||
|**_ComTransferProperty_**|TRIGGERED|
|**_ComFilter _**||
|**_ComFilterAlgorithm_**|any filter mapping value a to true and value b<br>to false|
|**_ComIPdu_**||
|**_ComIPduDirection _**|SEND|
|**_ComTxModeTrue_**||
|**_ComTxModeMode_**|MIXED|
|**_ComTxModeTimePeriod_**|tc1|
|**_ComTxModeNumberOfRepetitions_**|2|
|**_ComTxModeRepetitionPeriod_**|td|
|**_ComTxModeFalse_**||
|**_ComTxModeMode_**|PERIODIC|
|**_ComTxModeTimePeriod_**|tc2|
|**_ComTxIPdu_**||
|**_ComMinimumDelayTime_**|dt|



183 of 185 

Document ID 015: AUTOSAR_SWS_COM 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 



#### **Table 16: Relevant I-PDU transmission configuration for use case 6** 

A usage of this in practice is for example the signal of the button that controls the window-lift motor. If the button is not pressed, there is a long cycle time tc1 with this information. If it is pressed this information is distributed with a short cycle time tc2. If the button is released again, starting with the next main function this information is distributed three times with td and after that, again the long cycle time is used. 

**Use case 7** is similar to use case 5 but with ComEnableMDTForCyclicTransmission disabled and ComTxModeNumberOfRepetitions set to one. 



**Figure 18: Use case 7 scenario a, TM** **_MIXED_ , here n = 1 (without TMS switch)** 



**Figure 19: Use case 7 scenario b, TM** **_MIXED_ , here n = 1 (without TMS switch)** 

Document ID 015: AUTOSAR_SWS_COM 

184 of 185 

– AUTOSAR confidential – 

Specification of Communication AUTOSAR CP Release 4.4.0 





**Figure 20: Use case 7 scenario c, TM** **_MIXED_ , here n = 1 (without TMS switch)** 

|**_ComGeneral _**||
|---|---|
|**_ComEnableMDTForCyclicTransmission_**|False|
|**_ComSignal _**||
|**_ComTransferProperty_**|TRIGGERED|
|**_ComFilter _**||
|**_ComFilterAlgorithm_**|ALWAYS|
|**_ComIPdu_**||
|**_ComIPduDirection_**|SEND|
|**_ComTxModeTrue_**||
|**_ComTxModeMode_**|MIXED|
|**_ComTxModeTimePeriod_**|tc|
|**_ComTxModeNumberOfRepetitions_**|1|
|**_ComTxModeRepetitionPeriod_**|td|
|**_ComTxIPdu_**||
|**_ComMinimumDelayTime_**|dt|



**Table 17: Relevant I-PDU transmission configuration for use case 7** 

In contrary to use case 5, here the minimum delay timer is neither started for the periodic transmissions of the cyclic part nor for the repeated transmissions of the direct part of the Mixed mode. This can result in two consecutive transmissions within the timespan dt as shown in the scenarios b and c. 

Document ID 015: AUTOSAR_SWS_COM 

185 of 185 

– AUTOSAR confidential – 

