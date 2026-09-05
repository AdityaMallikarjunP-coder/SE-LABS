# Inter-City Freight Load Matching Marketplace

**PES University – Department of CSE**  
**Lab 1: Requirements Engineering & UML Use-Case Modelling**  
**Problem Statement #28 – Smart Cities, Transport & Logistics**

## Project Overview
This project is a B2B freight marketplace where shippers post cargo loads and verified trucking carriers submit bids. After a shipment is delivered and the electronic proof of delivery (e-POD) is verified, the milestone payment is released.

## Main Actors
- Shipper
- Freight Carrier
- Payment / Escrow Service
- Notification Service

## Submission Contents
- `Requirements/Requirements_Table.pdf` – 5 Functional Requirements and 2 Non-Functional Requirements.
- `UML/Use_Case_Diagram.png` – UML use-case diagram with include and extend relationships.
- `Use-Case-Flow/Submit_Competitive_Freight_Bid.pdf` – one-page flow specification for submitting a freight bid.

## UML Relationships
- `Post Freight Load` includes `Verify Shipper`.
- `Submit Bid` includes `Verify Carrier`.
- `Release Milestone Payment` includes `Verify e-POD`.
- `Request POD Correction` extends `Submit e-POD`.

## Core Use Case
The selected core use case is **Submit Competitive Freight Bid**. The main flow covers carrier verification, shipment selection, bid submission, bid recording, and shipper notification. An alternate flow is included for an expired auction.
