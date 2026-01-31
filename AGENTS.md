# AGENTS.md - Kiro CLI Hackathon Template

Welcome to the **Dynamous Kiro Hackathon** project. This repository is a specialized template designed to help you build and document your hackathon submission using the **Kiro CLI**.

## 🚀 Essential Commands

### Project Setup
- `@quickstart` - Run the interactive setup wizard to configure your steering documents and project details. This is the recommended first step for all new projects.
- `kiro-cli login` - Authenticate with your AWS Builder ID or IAM Identity Center.
- `kiro-cli` - Start the Kiro CLI interactive chat session.

### Core Development Workflow
- `@prime` - Load comprehensive project context (run this at the start of every session).
- `@plan-feature` - Create detailed implementation plans for new features.
- `@execute [path-to-plan]` - Systematically implement the tasks defined in a plan.
- `@code-review` - Perform a technical review of your code for bugs and quality.
- `@create-prd` - Generate Product Requirements Documents.
- `@rca` - Perform root cause analysis for issues/bugs.
- `@implement-fix` - Implement fixes based on analysis.

### Quality & Submission
- `@code-review-hackathon` - Evaluate your project against the official hackathon judging rubric.
- `@system-review` - Analyze your implementation against the original plan.
- `@execution-report` - Generate a summary report of your implementation.

## 🏗️ Code Organization

The project follows a specific structure for Kiro-related configurations:

```text
.kiro/
├── steering/          # Persistent project knowledge (product, tech, structure)
├── prompts/           # Custom reusable commands (@prime, @execute, etc.)
├── agents/            # Custom agent configurations (tools, permissions)
├── documentation/     # Local copy of Kiro CLI documentation
└── settings/          # Tool and CLI configuration (MCP, hooks, etc.)
```

### Key Documentation Files
- `README.md` - Your main project documentation and value proposition.
- `DEVLOG.md` - A continuous log of your development process, decisions, and challenges.
- `kiro-guide.md` - A practical guide to Kiro CLI features and concepts.

## 🧠 Development Patterns

### Spec-Driven Development
Kiro emphasizes **Planning before Coding**. 
1. Use `@plan-feature` to generate a plan in `.agents/plans/`.
2. Use `@execute` to implement that plan step-by-step.
3. This ensures high-quality, traceable implementations.

### Persistent Context (Steering)
Update the files in `.kiro/steering/` to keep Kiro informed about your project without repeating yourself:
- `product.md`: The "Why" - business context and user needs.
- `tech.md`: The "What" - tech stack, libraries, and coding standards.
- `structure.md`: The "Where" - file organization and naming conventions.

## ⚠️ Important Gotchas

- **Permissions**: Some tools (write, shell, aws) prompt for permission by default. Use `/tools trust-all` to skip these during active development sessions.
- **Context Limits**: Monitor your context usage with `/context show`. Use `/compact` if the conversation history gets too large.
- **Experimental Features**: Some features like ToDo lists and Checkpointing are experimental and must be enabled via `kiro-cli settings`.

## 🤖 Specialized Agents

This project uses a suite of specialized agents to maintain speed and quality during the sprint:

- **`graph-specialist`**: Use for Neo4j schema design and complex Cypher queries.
- **`eval-specialist`**: Use to create and run evaluation benchmarks for research accuracy.
- **`refactor-specialist`**: Use to audit code for "AI slop" and technical debt.
- **`qa-tester`**: Use to ACTUALLY EXECUTE code and verify end-user UX.
- **`vcs-specialist`**: Use to manage `jj` (Jujutsu) versioning and branching.

To swap to an agent: `/agent swap [agent-name]`

## 🛠️ Tooling & Integration

- **Built-in Tools**: `read`, `write`, `shell`, `glob`, `grep`, `aws`, `web_search`, `web_fetch`.
- **LSP Integration**: Use `/code init` to enable semantic understanding (Go-to-definition, Find-references).
- **Subagents**: Kiro can spawn subagents for parallel processing of complex tasks.

## 🏆 Hackathon Success Tips

1. **Document Everything**: Use `@execution-report` and update `DEVLOG.md` frequently. Process documentation is 20% of your score.
2. **Effective Kiro Usage**: Customize your `.kiro` folder and create custom prompts. This is another 20% of your score.
3. **Judge Yourself**: Run `@code-review-hackathon` early and often to see how your project aligns with the winning criteria.
